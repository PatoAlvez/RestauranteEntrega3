from django.urls import path, include
from MiRestaurante import views

urlpatterns = [
    path('', views.inicio),
    path("gastronomia", views.gastronomia, name="Gastronomia"),
    path("informacion", views.informacion, name="Informacion"),
    path("contacto", views.contacto, name="Contacto"),
    path("inicio", views.inicio, name="Inicio"),
    path("RestauranteFormulario", views.RestauranteFormulario, name="RestauranteFormulario"),
    path("BaseDeDatos", views.BaseDeDatos, name="BaseDeDatos"),
    path("busquedaformulario", views.busquedaFormulario, name="BusquedaFormulario"),
    path("buscar", views.buscar, name="Buscar"),
]