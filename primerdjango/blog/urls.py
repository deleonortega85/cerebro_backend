from django.urls import path
from . import views

urlpatterns = [
    path('blog/inicio', views.inicio, name='inicio'),
]