from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from forms import *
from MiRestaurante.models import *
# Create your views here.
def inicio(request):
    mihtml= open("C:/Users/LTA/Desktop/ENTREGA3/restaurante/restaurant/MiRestaurante/template/MiRestaurante/inicio.html")
    plantilla= Template(mihtml.read())
    mihtml.close()
    miContexto= Context()
    documento= plantilla.render(miContexto)
    return HttpResponse(documento)
    
def gastronomia(request):
    return render(request, "MiRestaurante/gastronomia.html")
    

def informacion(request):
    return render(request, "MiRestaurante/informacion.html")
    
def contacto(request):
    return render(request, "MiRestaurante/contacto.html")
    
def restauranteFormulario(request):

    if request.method == "POST":
        MiFormulario= RestauranteFormulario(request.POST)
        print(MiFormulario)
        if MiFormulario.is_valid:
            Informacion= MiFormulario.cleaned_data
            restaurante= inicio (request.POST["Plato"], request.POST ["N_Mesa"])
            restaurante.save()
            return render(request,"MiRestaurante/inicio.html")
    else:
        MiFormulario= RestauranteFormulario()
    return render (request, "MiRestaurante/RestauranteFormulario.html")

def busquedaFormulario(request):
    return render (request,"MiRestaurante/busquedaFormulario.html")

def buscar(request):
    if request.GET["N_mesa"]:
        plato= request.GET["Plato"]
        n_mesa= PlatoPrincipal.objects.filter(plato__icontains=plato)
        return render(request, "MiRestaurante/resultadosbusqueda.html", {"plato": plato, "n_mesa":n_mesa})

    else:
        respuesta= "No enviaste datos"
    return HttpResponse(respuesta)

def leerdatos(request):
    plato= Entrada.objects.all()
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/leerdatos.html", contexto)

def eliminardatos(request, datos__nombre):
    plato= Entrada.objects.get(nombre=datos__nombre)
    plato.delete()

    plato= Entrada.objects.all()
    contexto= {"Entrada:":plato}
    return render(request, "MiRestaurante/leerdatos.html", contexto)