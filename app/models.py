<<<<<<< HEAD
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    imagem = models.CharField(max_length=500, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
=======
from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    imagem = models.CharField(max_length=500, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
>>>>>>> b24fc8c7fd829fce604b98f2bb869ff40ed450cb
        return self.nome