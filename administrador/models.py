from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.append("accounts/")
sys.path.append("falcao/")
from accounts.models import *
from falcao.models import *
class admin(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.first_name+' '+self.usuario.last_name
class vendas(models.Model):
    produtos=models.ManyToManyField(produtos)
    instalador=models.ForeignKey(instalador,on_delete=models.CASCADE)
    quantidade=models.IntegerField()
    data=models.DateField()
    def __str__(self):
        return self.produtos.nome
class produto_admin(models.Model):
    nome=models.CharField(max_length=255)
    valor=models.FloatField()
    quantidade=models.IntegerField()
    imagem=models.ImageField(upload_to='falcao/media')
    descricao=models.TextField()
    custo=models.FloatField(default=0)
    def __str__(self):
        return self.nome