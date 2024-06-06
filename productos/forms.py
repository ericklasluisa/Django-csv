from django import forms

class SubirCSVForm(forms.Form):
    archivo_csv = forms.FileField(label='Selecciona un archivo CSV')