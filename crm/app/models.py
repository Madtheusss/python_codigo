from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    produto = models.CharField(max_length=20)
    valor = models.IntegerField(max_length=6)
