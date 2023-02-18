from django import forms

class RestauranteFormulario(forms.Form):
    Plato=forms.CharField(max_length=30)
    N_Mesa= forms.IntegerField()