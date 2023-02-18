from django.db import models
class produtos(models.Model):
    nome=models.CharField(max_length=255)
    valor=models.FloatField()
    quantidade=models.IntegerField()
    imagem=models.ImageField()
    descricao=models.TextField()
    def __str__(self):
        return self.nome
class vendas(models.Model):
    produtos=models.ForeignKey(produtos,on_delete=models.CASCADE)
    quantidade=models.IntegerField()
    data=models.DateField()
    def __str__(self):
        return self.produtos.nome