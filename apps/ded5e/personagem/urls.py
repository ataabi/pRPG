from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('cria_ficha/', cria_ficha, name='cria_ficha'),
    path('ver_ficha/', ver_ficha, name='ver_ficha'),
    path('ver_magias/<str:nome_personagem>', ver_magias, name='ver_magias'),
    path('adicionar_magia/<str:nome_personagem>', adicionar_magia, name='adicionar_magia'),
    path('remover_magia/<str:nome_personagem>/<int:id>', remover_magia, name='remover_magia'),
    path('editar_ficha/', editar_ficha, name='editar_ficha'),
    path('deletar_ficha/', deletar_ficha, name='deletar_ficha'),
]