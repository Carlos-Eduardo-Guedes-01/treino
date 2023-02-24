from django.contrib import admin
from django.urls import path,include
from .views import *
name_app='accounts'

urlpatterns = [
    path('',inicio,name='inicio'),
    path('cadastro-instalador/',cadastro,name='cadastro'),
    path('cadastrando-instalador/',cadastrando,name='cadastrando'),
    path('login/',login_view,name='login'),
    path('home/',loged,name='loged'),
    path('logouts/',logouts,name='logouts'),
    path('busca-autocomplete/', busca_autocomplete,name='busca-autocomplete'),
    path('altera-senha/',changepass, name='template-altera'),
    path('changepassword/',changePassword, name='/changepassword/'),
]