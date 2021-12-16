from django.db import models
from django.conf import settings
from django.utils import timezone

class Usuario(models.Model):
    email = models.EmailField()
    senha = models.CharField(max_length=50)

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)
    tamanho = models.IntegerField()
    preco = models.FloatField()

class Pedido(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    quantidade_itens = models.IntegerField()
    total = models.FloatField()
    nome_cliente = models.CharField(max_length=50)
    mesa = models.IntegerField()


class ProdutoPedido(models.Model):
    id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade_produto = models.IntegerField()

