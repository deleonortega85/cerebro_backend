from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobreMi/', views.sobre_mi, name='sobreMi'),
]