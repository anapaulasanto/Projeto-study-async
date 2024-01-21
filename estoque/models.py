from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    validade = models.CharField(max_length=10)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome