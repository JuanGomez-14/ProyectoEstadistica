import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def process_excel_file(file_path):
    """Lee el archivo Excel y devuelve un DataFrame"""
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Error al procesar el archivo Excel: {str(e)}")

def generate_histogram(series):
    """Genera un histograma y lo devuelve como imagen base64"""
    plt.figure(figsize=(8, 4))
    series.hist()
    plt.title(f'Histograma de {series.name}')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    return base64.b64encode(image_png).decode('utf-8')

def generate_scatter_plot(series1, series2):
    """Genera un diagrama de dispersión con línea de regresión"""
    plt.figure(figsize=(8, 4))
    plt.scatter(series1, series2, alpha=0.5)
    
    # Calcular regresión lineal
    slope, intercept, r_value, p_value, std_err = stats.linregress(series1, series2)
    line = slope * series1 + intercept
    plt.plot(series1, line, 'r', label=f'y={slope:.2f}x+{intercept:.2f}')
    
    plt.title(f'Diagrama de dispersión: {series1.name} vs {series2.name}')
    plt.xlabel(series1.name)
    plt.ylabel(series2.name)
    plt.legend()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    return base64.b64encode(image_png).decode('utf-8'), slope, intercept, r_value

def univariate_analysis(series):
    """Realiza análisis univariado sobre una serie de datos"""
    analysis = {
        'media': series.mean(),
        'mediana': series.median(),
        'moda': series.mode().tolist(),
        'desviacion_estandar': series.std(),
        'varianza': series.var(),
        'maximo': series.max(),
        'minimo': series.min(),
        'rango': series.max() - series.min(),
        'coeficiente_variacion': (series.std() / series.mean()) * 100 if series.mean() != 0 else np.nan,
        'percentiles': {
            '25': series.quantile(0.25),
            '50': series.quantile(0.50),
            '75': series.quantile(0.75)
        },
        'asimetria': series.skew(),
        'curtosis': series.kurtosis(),
        'conteo': series.count(),
        'valores_unicos': series.nunique(),
        'histograma': generate_histogram(series)
    }
    return analysis

def bivariate_analysis(series1, series2):
    """Realiza análisis bivariado entre dos series de datos"""
    scatter_plot, slope, intercept, r_value = generate_scatter_plot(series1, series2)
    analysis = {
        'correlacion_pearson': series1.corr(series2),
        'covarianza': series1.cov(series2),
        'resumen_col1': univariate_analysis(series1),
        'resumen_col2': univariate_analysis(series2),
        'scatter_plot': scatter_plot,
        'regresion': {
            'pendiente': slope,
            'intercepto': intercept,
            'r_cuadrado': r_value**2
        }
    }
    return analysis