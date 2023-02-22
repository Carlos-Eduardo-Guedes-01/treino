from django.shortcuts import render
import sys
sys.path.append("accounts/")
from falcao.models import *
from accounts.models import *
def inicio(request):
    return render(request,'../../falcao/templates/index.html')
def lista_precos(request):
    if request.POST:
        search=request.POST.get('search')
        itens=produtos.objects.filter(nome__contains=search)
        data={}
        data['produtos']=itens
    else: 
        itens=produtos.objects.order_by('nome')
        data={}
        data['produtos']=itens
    return render(request,'../../falcao/templates/produtos.html',data)
def cadastra_produto(request):
    return render(request,'../../falcao/templates/cadastro_produtos.html')
def cadastrando_produto(request):
    nome=request.POST.get('nome')
    quant=request.POST.get('quantidade')
    valor=request.POST.get('valor')
    img=request.FILES.get('img')
    desc=request.POST.get('descricao')
    prod=produtos(nome=nome, quantidade=quant, valor=valor, imagem=img,descricao=desc)
    prod.save()
    data={}
    data['msg'] = 'Produto Cadastrado com sucesso!'
    data['class'] = 'alert-success'
    return render(request,'../../falcao/templates/cadastro_produtos.html',data)
def perfil(request):
    user=request.user
    data={}
    data['dados']=instalador.objects.get(usuario=user)
    return render(request,'../../accounts/templates/perfil.html', data)
def listar_vendas(request):
    pass