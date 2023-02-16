from django.db import models
from django.contrib.auth.models import User
class instalador(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    cep=models.CharField(max_length=255)
    cidade=models.CharField(max_length=255)
    def __str__(self):
        return self.usuario.first_name+' '+self.usuario.last_name
