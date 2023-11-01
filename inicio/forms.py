from django import forms

class CrearCelularFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=100)
    anio = forms.IntegerField()
    
class CrearTabletFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=100)
    anio = forms.IntegerField()

class CrearAccesorioFormulario(forms.Form):
    tipo_producto = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=100)
    
class BusquedaCelularFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)



