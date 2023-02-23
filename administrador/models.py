from django.db import models
from django.contrib.auth.models import User
class admin(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.first_name+' '+self.usuario.last_name