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
    pub = [
        {"1": "Django es Increible.",
         "2": "Que es MVT",
         "3": "¿Cómo Crear esta app?"
         }
    ]

    return render(request, 'blog/inicio.html', {'posts': pub})