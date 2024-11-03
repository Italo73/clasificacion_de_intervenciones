# Clasificación Automática de Intervenciones en Reuniones Ágiles

Este proyecto implementa un sistema de clasificación de intervenciones en reuniones ágiles mediante técnicas de Procesamiento de Lenguaje Natural (NLP). El objetivo es analizar las intervenciones realizadas durante estas reuniones y clasificarlas de acuerdo con su propósito, mejorando la estructura de la comunicación en entornos de trabajo colaborativo.

## Descripción del Proyecto

En el contexto de las metodologías ágiles, la comunicación efectiva es fundamental. Este proyecto está diseñado para clasificar automáticamente las intervenciones en reuniones ágiles (preguntas, respuestas, sugerencias, retroalimentación, comentario) para optimizar el flujo de información y facilitar la revisión de las reuniones.

El sistema utiliza modelos de aprendizaje automático entrenados con un dataset artificial para identificar la naturaleza de cada intervención, aportando una estructura clara a la comunicación en los equipos ágiles.

En la carpeta myapp/ se encuentra el Jupyter notebook "Entrenamiento.ipynb". Al ejecutarlo, se crearán las visualizaciones correspondientes de los gráficos, para luego ser mostradas en la interfaz gráfica desarrollada con Django.

## Instalación

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/djangoproject_github.git
   cd djangoproject_github

2. Crea un entorno virtual y actívalo:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

3. Instala las dependencias:
   
   ```bash
   pip install -r requerimientos.txt

5. Realiza las migraciones de la base de datos:
   
   ```bash
   python manage.py migrate

5. Inicia el servidor de desarrollo:

   ```bash
   python manage.py runserver

6. Abre tu navegador y accede a http://127.0.0.1:8000 para ver la aplicación en funcionamiento.
