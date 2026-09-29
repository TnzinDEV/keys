from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField(default=0)
    imagem = models.CharField(max_length=500, blank=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome