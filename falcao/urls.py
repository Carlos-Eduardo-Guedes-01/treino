from django.contrib import admin
from django.urls import path,include
from .views import *
name_app='accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name='inicio'),
    path('produtos/',lista_precos,name='produtos'),
    path('cadastrando-produto',cadastra_produto,name='cadastra-produto'),
    path('processado/',cadastrando_produto,name='cadastrando'),
    path('perfil/',perfil,name='perfil'),
    path('lista-vendas/',listar_vendas,name='lista-vendas'),

]