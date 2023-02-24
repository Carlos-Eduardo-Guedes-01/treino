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
    custo=models.FloatField(default=0)
    def __str__(self):
        return self.nome
