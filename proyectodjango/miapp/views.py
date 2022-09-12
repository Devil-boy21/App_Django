from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def Hola_Mundo (request):
 return HttpResponse("""
                     <h1> Hola mundo Django!!!!!</h1>
                     <h2>Editado por:........</h2>""")
 
def inicio(request):
    return HttpResponse("""<h1>Inicio</h1>
                        <h2>Esta es la ventana de inicio </h2>""") 

