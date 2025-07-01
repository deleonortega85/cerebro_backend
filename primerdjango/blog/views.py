# Create your views here.
from django.shortcuts import render
from .models import Post
def inicio(request):
    publicacion = [
         {"titulo": "Post 1", "contenido": "Django es Increible"},
         {"titulo": "Post 2", "contenido": "Que es MVT"},
         {"titulo": "Post 3", "contenido": "¿Cómo Crear esta app?"}
    ]
    context = {"publicacion": publicacion}

    return render(request, 'blog/inicio.html', context)

def sobre_mi(request):
    return render(request, 'blog/sobreMi.html')

def lista_posts(request):
    posts = Post.objects.filter(publicado=True).order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'posts': posts})