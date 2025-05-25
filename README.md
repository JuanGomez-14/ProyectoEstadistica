# 📊 Excel Analyzer - Aplicación Django para Análisis de Datos

## 📋 Descripción
Aplicación web que permite cargar archivos Excel (.xlsx, .xls) para visualizar y analizar datos estadísticos. Los usuarios pueden seleccionar columnas específicas y obtener análisis univariados o bivariados con visualizaciones gráficas.

## 🛠️ Requisitos
- Python 3.8+
- pip
- virtualenv (recomendado)

## 🚀 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/excel-analyzer.git
cd excel-analyzer
```

### 2. Crear y activar entorno virtual (recomendado)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/MacOS:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos
```bash
python manage.py migrate
```

## ▶️ Ejecución
```bash
python manage.py runserver
```

Luego abre tu navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔍 Archivo de Prueba
El proyecto incluye un archivo `datosPrueba.xlsx` en la raíz del proyecto que puedes usar para probar la aplicación:

### Cómo usarlo:
1. Ve a la página principal [http://127.0.0.1:8000](http://127.0.0.1:8000)
2. Haz clic en "Seleccionar archivo" y elige `datosPrueba.xlsx`
3. Haz clic en "Subir y Analizar"
4. Selecciona las columnas a analizar

## 🌟 Características Principales
- 📤 Subida de archivos Excel con validación de formato
- 🔍 Visualización de datos en tablas HTML
- 📊 Análisis estadísticos:
  - Univariado: Media, mediana, moda, desviación estándar, etc.
  - Bivariado: Correlación, covarianza, regresión lineal
- 📈 Visualizaciones gráficas: Histogramas, diagramas de dispersión
- 🔄 Navegación intuitiva entre pasos
