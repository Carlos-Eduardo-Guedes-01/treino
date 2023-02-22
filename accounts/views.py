from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
def inicio(request):
    data={}
    return render(request,'../../accounts/templates/index.html',data)
def cadastro(request):
    data={}
    return render(request,'../../accounts/templates/cadastro.html',data)
@require_POST
def cadastrando(request):
    data ={}
    print('método cadastrando')
    try:
        usuario_aux = User.objects.get(username=request.POST['user'])
        usuario_aux2= User.objects.filter(password=request.POST['password'])

        if usuario_aux or usuario_aux2:
            data['msg'] = 'Usuario ou Senha já existem!'
            data['class'] = 'alert-danger'
    except User.DoesNotExist:
        user = User.objects.create_user(username=request.POST['user'], first_name=request.POST['first_name'],last_name= request.POST['last_name'], password=request.POST['password'])
        cidade = request.POST['cidade']
        
        query_user=User.objects.get(id=user.id)
        cep=request.POST['cep']
        estado=request.POST.get('UF')
        usu= instalador.objects.create(usuario=query_user,cidade=cidade,cep=cep,uf=estado)
        user.save()
        data['msg'] = 'Instalador Cadastrado com sucesso! Faça Login.'
        data['class'] = 'alert-success'''
    return render(request,'../../accounts/templates/cadastro.html', data)
    #return render(request,'../../accounts/templates/cadastro.html',data)
def login_view(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect("accounts:loged")
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request,'../../accounts/templates/index.html', data)
def loged(request):
    user=request.user
    mode_user=User.objects.get(username=user)
    instalador_=instalador.objects.get(usuario=mode_user.id)
    data={}
    data['nome']=instalador_.usuario.first_name
    return render(request,'../../falcao/templates/home.html',data)
def logouts(request):
    logout(request)
    return redirect('accounts:inicio')
def update(request):
    pass
