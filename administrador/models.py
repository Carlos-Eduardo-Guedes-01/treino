from django.db import models
from django.contrib.auth.models import User
class admin(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    