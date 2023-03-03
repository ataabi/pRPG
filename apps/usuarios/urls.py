from django.urls import path
from .views import *

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('altera_senha/', altera_senha, name='altera_senha'),
]