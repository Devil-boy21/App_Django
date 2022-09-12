from django.contrib import admin
from django.urls import path

#importar mis vistas

from miapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('holamundo/', views.Hola_Mundo, name='HOLA MUNDO'),
    path('Inicio/', views.inicio, name='Inicio'),
   
]
