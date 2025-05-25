from django import forms
from .models import ExcelFile

class ExcelUploadForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': '.xlsx, .xls'})
        }
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            ext = file.name.split('.')[-1].lower()
            if ext not in ['xlsx', 'xls']:
                raise forms.ValidationError("Solo se permiten archivos Excel (.xlsx, .xls)")
        return file

class ColumnSelectionForm(forms.Form):
    def __init__(self, *args, columns=None, **kwargs):
        super().__init__(*args, **kwargs)
        if columns:
            for i, column in enumerate(columns):
                self.fields[f'column_{i}'] = forms.BooleanField(
                    label=column,
                    required=False,
                    widget=forms.CheckboxInput(attrs={'class': 'column-checkbox'})
                )