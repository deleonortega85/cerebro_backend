from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobreMi/', views.sobre_mi, name='sobreMi'),
    path('lista_post/', views.lista_posts, name='lista_post'),
]