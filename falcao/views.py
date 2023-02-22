from django.shortcuts import render
from .models import *
def inicio(request):
    return render(request,'../../falcao/templates/index.html')
def lista_precos(request):
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
