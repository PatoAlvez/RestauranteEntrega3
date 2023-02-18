from django.urls import path, include
from MiRestaurante import views

urlpatterns = [
    path('', views.inicio),
    path("gastronomia", views.gastronomia, name="Gastronomia"),
    path("informacion", views.informacion),
    path("contacto", views.contacto),
    path("RestauranteFormulario", views.RestauranteFormulario, name="RestauranteFormulario"),
]