from django.urls import path, include
from MiRestaurante import views

urlpatterns = [
    path('', views.inicio),
    path("MiRestaurante/", include("MiRestaurante.urls")),
    path("gastronomia", views.gastronomia, name="Gastronomia"),
    path("informacion", views.informacion),
    path("contacto", views.contacto),
]