from django.db import models
import sys
sys.path.append("accounts/")
from accounts.models import *
class produtos(models.Model):
    nome=models.CharField(max_length=255)
    valor=models.FloatField()
    quantidade=models.IntegerField()
    imagem=models.ImageField(upload_to='falcao/media')
    descricao=models.TextField()
    def __str__(self):
        return self.nome
class vendas(models.Model):
    produtos=models.ForeignKey(produtos,on_delete=models.CASCADE)
    instalador=models.ForeignKey(instalador,on_delete=models.CASCADE)
    quantidade=models.IntegerField()
    data=models.DateField()
    def __str__(self):
        return self.produtos.nome