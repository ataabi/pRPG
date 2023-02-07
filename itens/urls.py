from django.urls import path
from .views import *


urlpatterns = [
    path('loja',loja, name='loja'),
    path('inventario',inventario, name='inventario'),
    path('inventario_update',inventario_update, name='inventario_update'),
] 