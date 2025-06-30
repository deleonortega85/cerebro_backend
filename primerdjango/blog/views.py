# Create your views here.
from django.shortcuts import render

def inicio(request):
    # publicaciones = [
    #     "Post 1: Django es increíble",
    #     "Post 2: Qué es MVT",
    #     "Post 3: Cómo crear una app"
    # ]
    publicacion = [
         {"titulo": "Post 1", "contenido": "Django es Increible"},
         {"titulo": "Post 2", "contenido": "Que es MVT"},
         {"titulo": "Post 3", "contenido":"¿Cómo Crear esta app?"}
    ]
    context = {"publicacion": publicacion}

    return render(request, 'blog/inicio.html', context)

def sobre_mi(request):
    return render(request, 'blog/sobreMi.html')
