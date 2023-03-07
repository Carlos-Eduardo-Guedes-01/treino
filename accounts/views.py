from django.shortcuts import render,redirect
from .models import *
import sys
sys.path.append("administrador/")
sys.path.append("falcao/")
from falcao.models import *
from administrador.models import *
from django.http import HttpResponse, JsonResponse
import json as simplejson
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
        usu= instalador.objects.create(usuario=query_user,cidade=cidade,cep=cep,uf=estado,total_av=0)
        user.save()
        data['msg'] = 'Instalador Cadastrado com sucesso! Faça Login.'
        data['class'] = 'alert-success'''
    return render(request,'../../accounts/templates/cadastro.html', data)
    #return render(request,'../../accounts/templates/cadastro.html',data)
def login_view(request):
    data = {}
    if request.POST:
        user = authenticate(username=request.POST['user'], password=request.POST['password'])
        if user is not None:
            query=instalador.objects.filter(usuario=user.pk)
            query2=admin.objects.filter(usuario=user.pk)
            if(query):
                login(request, user)
                return redirect("accounts:loged")
            elif(query2):
                login(request, user)
                return redirect("administrador:home-adm")
            elif(query is False):
                login(request,user)
                return
        else:
            data['msg'] = 'Usuário ou Senha inválidos!'
            data['class'] = 'alert-danger'
    else:
        data['msg'] = 'Campos Inválidos!'
        data['class'] = 'alert-danger'
    return render(request,'../../accounts/templates/index.html', data)

@login_required(login_url='accounts:login')
def loged(request):
    user=request.user
    if user is None:
        return redirect('accounts:login')
    data={}
    return render(request,'../../falcao/templates/home.html',data)
@login_required(login_url='accounts:login')
def logouts(request):
    logout(request)
    return redirect('accounts:inicio')
@login_required(login_url='accounts:login')
def changepass(request):
    user=request.user
    return render(request, '../../accounts/templates/changepassword.html',{'user':user})
@login_required(login_url='accounts:login')
def changePassword(request):
    senha=request.POST.get("senha_atual")
    user=request.POST.get("usu")
    u = User.objects.get(username=user)
    data=[]
    context={}
    if(u is not None):
        u.set_password(request.POST.get('nova_senha'))
        u.save()
        context={
            'msg':"Senha Alterada com Sucesso!",
            'class':"alert-success",
            'user':user

        }
    else:
        context={
            'msg':"Senha Antiga inválida!",
            'class':"alert-danger"
        }
    if(user is None):
        return redirect('accounts:inicio')
    return render(request, '../../accounts/templates/index.html',context)
def busca_autocomplete(request):
    if 'term' in request.GET:
        prod = produtos.objects.filter(nome__contains=request.GET.get('term'))
        nomes=list()
        for produto in prod:
            nomes.append(produto.nome)
        return JsonResponse(nomes, safe=False)
    return HttpResponse(prod)