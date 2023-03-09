from django.shortcuts import render,redirect, get_object_or_404
import sys
sys.path.append("accounts/")
sys.path.append("falcao/")
from falcao.models import *
from accounts.models import *
from administrador.models import *
from django.contrib.auth.decorators import login_required
from .forms import VendaForm
from datetime import date
from django.db.models import Q
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
    return render(request,'../../administrador/templates/cadastro_adm.html',data)
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
    data['instalador']=instalador.objects.all().order_by('usuario')
    data['loja']=admin.objects.all().order_by('nome')
    return render(request,'../../administrador/templates/vender.html',data)
def instaladores(request):
    data={}
    data['instaladores']=instalador.objects.all().order_by("usuario")
    return render(request,'../../administrador/templates/instaladores.html', data)
@login_required(login_url='accounts:login')
def changepass_adm(request):
    user=request.user
    return render(request, '../../administrador/templates/changepassword_adm.html',{'user':user})
@login_required(login_url='accounts:login')
def changePassword_adm(request):
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
def perfil_instaladores(request,id):
    data={}
    data['dados']=get_object_or_404(instalador,pk=id)
    return render(request,'../../administrador/templates/perfis.html', data)
def template_venda(request):
    data={}
    data['form']=VendaForm()
    return render(request,'../../administrador/templates/vender.html',data)
def vendendo(request):
    data={}
    if request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            livro = form.save(commit=False)
            form.save()
            data['msg'] = 'Venda realizada com sucesso!'
            data['class'] = 'alert-success'
        else:
            data['msg'] = 'Falha ao cadastrar a venda!'
            data['class'] = 'alert-danger'
    else:
        form = VendaForm()
    return render(request,'../../administrador/templates/vender.html',data)
def vendas_template(request):
    data={}
    data['anos'] = [i for i in range(date.today().year, 1999, -1)]
    return render(request,'../../administrador/templates/filtro_vendas.html',data)
def filtro_vendas(request):
    mes=request.POST.get('mess')
    ano=request.POST.get('ano')
    data={}
    data['vendas']=vendas.objects.filter(Q(data__year=ano) & Q(data__month=mes))
    return render(request,'../../administrador/templates/vendas.html',data)