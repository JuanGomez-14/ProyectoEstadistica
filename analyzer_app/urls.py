from django.urls import path
from . import views

app_name = 'analyzer_app'  # Este es el namespace de tu aplicación

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('seleccionar/', views.select_columns, name='select_columns'),
    path('analizar/', views.analyze_data, name='analyze_data'),
]