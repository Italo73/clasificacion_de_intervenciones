# myapp/views.py
import torch
import torch.nn as nn
import pandas as pd
from django.shortcuts import render


class SimpleModel(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_classes):
        super(SimpleModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, num_classes)

    def forward(self, x):
        x = self.embedding(x)
        x = torch.mean(x, dim=1)
        x = self.fc(x)
        return x


def index(request):
    # Ruta del archivo HTML generado en el Jupyter Notebook
    plotly_figure_paths = [
        r'C:\Users\italo\OneDrive\Escritorio\djangoproject\myapp\plotly_figure.html',
        r'C:\Users\italo\OneDrive\Escritorio\djangoproject\myapp\plotly_figure2.html',
        r'C:\Users\italo\OneDrive\Escritorio\djangoproject\myapp\plotly_figure3.html',
    ]

    plotly_divs = []
    for path in plotly_figure_paths:
        with open(path, 'r', encoding='utf-8') as f:
            plotly_div = f.read()
            plotly_div = plotly_div.replace('width="100%"', 'width="900px"')
            plotly_div = plotly_div.replace('height="100%"', 'height="500px"')
            plotly_divs.append(plotly_div)

    resumen_datos = cargar_resumen_csv()

    context = {
        'plotly_div': plotly_divs[0],
        'plotly_div2': plotly_divs[1],
        'plotly_div3': plotly_divs[2],
        'resumen': resumen_datos,
    }
    return render(request, 'myapp/templates/index.html', context)

def reuniones(request):
    return render(request, 'myapp/templates/reuniones.html')

def nuevo_reporte(request):
    return render(request, 'myapp/templates/nuevo_reporte.html')

def cargar_resumen_csv():
    # Ruta al archivo CSV
    csv_file_path = r'C:\Users\italo\OneDrive\Escritorio\djangoproject\myapp\resumen_intervenciones.csv'
    
    # Leer el archivo CSV
    df = pd.read_csv(csv_file_path)
    
    # Convertir el DataFrame a un diccionario
    return df.to_dict(orient='records')
