from django.shortcuts import render,redirect
import sys
sys.path.append("accounts/")
sys.path.append("falcao/")
from falcao.models import *
from accounts.models import *
from administrador.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:login')
def home_adm(request):
    user=request.user
    if(user is None):
        return redirect('accounts:inicio')
    mode_user=User.objects.get(username=user)
    admini=admin.objects.get(usuario=mode_user.id)
    data={}
    data['nome']=admini.usuario.first_name
    return render(request,'../../administrador/templates/home_adm.html',data)
def form_cadastro(request):
    data={}
    return render(request,'../../administrador/templates/cadastro.html',data)
def cadastra_adm(request):
    data ={}
    try:
        usuario_aux = User.objects.get(username=request.POST['user'])
        usuario_aux2= User.objects.filter(password=request.POST['password'])

        if usuario_aux or usuario_aux2:
            data['msg'] = 'Usuario ou Senha já existem!'
            data['class'] = 'alert-danger'
    except User.DoesNotExist:
        user = User.objects.create_user(username=request.POST['user'], first_name=request.POST['first_name'],last_name= request.POST['last_name'], password=request.POST['password'])
        query_user=User.objects.get(id=user.id)
        usu= admin.objects.create(usuario=query_user)
        user.save()
        data['msg'] = 'Instalador Cadastrado com sucesso! Faça Login.'
        data['class'] = 'alert-success'''
    return render(request,'../../accounts/templates/cadastro.html', data)
def loged_adm(request):
    return render(request,'../../administrador/home.html')
def template_vender(request):
    data={}
    data['produtos']=produtos.objects.all().order_by('nome')
    data['instalador']=instalador.objects.all().order_by('nome')
    data['loja']=admin.objects.all().order_by('nome')
    return render(request,'../../administrador/templates/vender.html',data)