from django.contrib import admin
from django.urls import path,include
from .views import *
name_app='administrador'

urlpatterns = [
    path('adm/',home_adm,name='admin'),
    path('adm/home-adm/',home_adm, name='home-adm'),
    path('adm/cadastro-form/',form_cadastro, name='cadastro-form'),
    path('adm/cadastro-admin/',cadastra_adm, name='cadastro-adm'),
    path('adm/instaladores',instaladores,name='instaladores'),
    path('adm/altera-senha/',changepass_adm, name='template-altera-adm'),
    path('adm/changepassword/',changePassword_adm, name='/changepassword-adm/'),
    path('adm/perfil-instalador/<int:id>/',perfil_instaladores,name='perfis'),
    path('adm/vender/',template_venda,name='template-venda'),
    path('adm/vender/pronto/',vendendo,name='vendendo'),
    path('adm/filtro-vendas/',vendas_template,name='template_venda'),
    path('adm/busca-vendas/',filtro_vendas,name='vendas')
]