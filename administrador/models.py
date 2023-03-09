from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.append("accounts/")
sys.path.append("falcao/")
from accounts.models import *
from falcao.models import *
class admin(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    valor_vendas=models.FloatField(default=0)
    def __str__(self):
        return self.usuario.first_name+' '+self.usuario.last_name
class vendas(models.Model):
    produtos=models.ForeignKey(produtos,on_delete=models.CASCADE)
    instalador=models.ForeignKey(instalador,on_delete=models.CASCADE)
    quantidade=models.IntegerField()
    data=models.DateField()
    valor_venda=models.FloatField(default=0.0)
    def __str__(self):
        return self.produtos.nome