# Create your views here.
from django.shortcuts import render

def inicio(request):
    return render(request, 'blog/inicio.html')

def sobre_mi(request):
    return render(request, 'blog/sobreMi.html')

def publicar(request):
    # publicaciones = [
    #     "Post 1: Django es increíble",
    #     "Post 2: Qué es MVT",
    #     "Post 3: Cómo crear una app"
    # ]
    publicacion = [
         {"titulo": "1", "contenido": "Django es Increible."},
         {"titulo": "2", "contenido": "Que es MVT"},
         {"titulo": "3", "contenido":"¿Cómo Crear esta app?"}
    ]
    context = {"publicacion": publicacion}

    return render(request, 'blog/inicio.html', {'posts': context})