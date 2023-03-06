from django.contrib import admin
from django.urls import path,include
from .views import *
name_app='administrador'

urlpatterns = [
    path('adm/',home_adm,name='admin'),
    path('home-adm/',home_adm, name='home-adm'),
    path('cadastro-form/',form_cadastro, name='cadastro-form'),
    path('cadastro-admin/',cadastra_adm, name='cadastro-adm'),
    path('home-adm/instaladores',instaladores,name='instaladores'),
    path('adm/altera-senha/',changepass_adm, name='template-altera-adm'),
    path('adm/changepassword/',changePassword_adm, name='/changepassword-adm/'),
    path('adm/perfil-instalador/<int:id>/',perfil_instaladores,name='perfis'),
    path('adm/vender/',template_venda,name='template-venda'),
]