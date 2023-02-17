from django.shortcuts import render
from django.http import HttpResponse
from django.template import *
# Create your views here.
def inicio(request):
    return render(request, "MiRestaurante/inicio.html")
    

def gastronomia(request):
    return render(request, "MiRestaurante/gastronomia.html")
    

def informacion(request):
    return render(request, "MiRestaurante/informacion.html")
    

def contacto(request):
    return render(request, "MiRestaurante/contacto.html")
    
        

def padre(self):
    mihtml=open("C:/Users/LTA/Desktop/ENTREGA3/restaurante/restaurant/plantillas/padre.html")
    plantilla=padre(mihtml.read())
    mihtml.close()
    micontexto=context()
    documento=plantilla.render(micontexto)
    return HttpResponse(documento)
