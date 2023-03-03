from django.urls import path
from .views import *


urlpatterns = [
    path('loja',loja, name='loja'),
    path('inventario/<str:nome_personagem>',inventario, name='inventario'),
    path('inventario_update/<str:nome_personagem>',inventario_update, name='inventario_update'),
    path('equipamentos/<str:nome_personagem>',equipamentos, name='equipamentos'),
    path('add_armadura/<str:nome_personagem>',add_armadura, name='add_armadura'),
    path('remover_armadura/<str:nome_personagem>/<int:id>',remover_armadura, name='remover_armadura'),
    path('add_arma/<str:nome_personagem>',add_arma, name='add_arma'),
    path('remover_arma/<str:nome_personagem>/<int:id>',remover_arma, name='remover_arma'),
] 