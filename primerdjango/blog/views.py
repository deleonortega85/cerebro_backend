# Create your views here.
from django.shortcuts import render

def inicio(request):
    return render(request, 'blog/inicio.html')

def sobre_mi(request):
    return render(request, 'blog/sobre_mi.html')