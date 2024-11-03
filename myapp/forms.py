from django import forms

class ActividadForm(forms.Form):
    archivo_actividad = forms.FileField(label='Archivo de texto (.txt)')
