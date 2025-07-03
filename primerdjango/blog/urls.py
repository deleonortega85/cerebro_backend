from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobreMi/', views.sobre_mi, name='sobreMi'),
    path('blog', views.lista_posts, name='lista_posts'),
    path('post/<int:id>/', views.detalle_post, name='detalle_post'),
]