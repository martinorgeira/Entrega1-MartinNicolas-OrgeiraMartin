from django import forms

class HumanoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)
    
    
class BuscarHumano(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)