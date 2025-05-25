import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ExcelUploadForm, ColumnSelectionForm
from .utils import process_excel_file, univariate_analysis, bivariate_analysis
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.save(commit=False)
            if request.user.is_authenticated:
                excel_file.user = request.user
            excel_file.save()
            
            file_path = os.path.join(settings.MEDIA_ROOT, excel_file.file.name)
            df = process_excel_file(file_path)
            
            request.session['excel_data'] = df.to_json()
            request.session['excel_filename'] = excel_file.file.name
            
            # Cambia esta línea para incluir el namespace
            return redirect('analyzer_app:select_columns')
    else:
        form = ExcelUploadForm()
    
    return render(request, 'analyzer_app/upload.html', {'form': form})

def select_columns(request):
    if 'excel_data' not in request.session:
        return redirect('upload_file')
    
    # Recuperar datos de la sesión
    df = pd.read_json(request.session['excel_data'])
    columns = df.columns.tolist()
    
    if request.method == 'POST':
        form = ColumnSelectionForm(request.POST, columns=columns)
        if form.is_valid():
            selected_columns = []
            for i, column in enumerate(columns):
                if form.cleaned_data.get(f'column_{i}'):
                    selected_columns.append(column)
            
            if len(selected_columns) == 1 or len(selected_columns) == 2:
                request.session['selected_columns'] = selected_columns
                return redirect('analyzer_app:analyze_data')
            else:
                form.add_error(None, "Debes seleccionar 1 o 2 columnas para analizar")
    else:
        form = ColumnSelectionForm(columns=columns)
    
    # Mostrar las primeras filas del DataFrame
    preview_data = df.head(10).to_dict('records')
    
    return render(request, 'analyzer_app/select_columns.html', {
        'form': form,
        'columns': columns,
        'preview_data': preview_data
    })

def analyze_data(request):
    if 'excel_data' not in request.session or 'selected_columns' not in request.session:
        return redirect('upload_file')
    
    # Recuperar datos de la sesión
    df = pd.read_json(request.session['excel_data'])
    selected_columns = request.session['selected_columns']
    
    # Realizar análisis
    if len(selected_columns) == 1:
        col = selected_columns[0]
        analysis = univariate_analysis(df[col])
        analysis_type = 'univariado'
    else:
        col1, col2 = selected_columns
        analysis = bivariate_analysis(df[col1], df[col2])
        analysis_type = 'bivariado'
    
    return render(request, 'analyzer_app/analyze.html', {
        'analysis': analysis,
        'selected_columns': selected_columns,
        'analysis_type': analysis_type,
        'filename': request.session['excel_filename']
    })