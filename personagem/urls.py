from django.urls import path
from .views import *
urlpatterns = [
    path('',index, name='index'),
    path('cria_ficha/', cria_ficha, name='cria_ficha'),
    path('ver_ficha/', ver_ficha, name='ver_ficha'),
    path('editar_ficha/', editar_ficha, name='editar_ficha'),
    path('deletar_ficha/', deletar_ficha, name='deletar_ficha'),
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
]