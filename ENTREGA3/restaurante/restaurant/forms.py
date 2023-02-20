from django import forms

class RestauranteFormulario(forms.Form):
    plato=forms.CharField(max_length=40)
    cantidad=forms.CharField(max_length=20)
    bebida=forms.CharField(max_length=40)
    numero_de_mesa=forms.CharField(max_length=5)