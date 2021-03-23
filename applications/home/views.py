from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba

class PruebaView (TemplateView): # sireve para mostrar un template al usuario 
    template_name ='prueba.html' 

class PruebaListView (ListView): # sirve para traer un alista de caracteres
    template_name ='home/lista.html'
    context_object_name = 'listaNumeros'# declaro una variable
    queryset=['1','2','3']#lista string

class ListarPrueba (ListView): # enlista lo que tengo en mi base de datos 
    template_name = 'home/lista_prueba.html'
    model = Prueba # Llamo el modelo que quiero en listar 
    context_object_name = 'listarModelo' # declaro una variable para interpolarla en el html 


class PruebaCreateView(CreateView): # crea un nuevo objeto con una respuesta generada por plantilla en el html
    model = Prueba
    template_name = "home/create.html"
    fields = ['titulo','subtitulo','cantidad'] # tengo que llamar los cambos del modelo de mi base de datos





