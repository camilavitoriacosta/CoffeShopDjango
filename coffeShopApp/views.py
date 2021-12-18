from django.shortcuts import render
from .models import *

def pagina_inicial(requisicao):
    return render(requisicao, 'pagina_inicial.html')


def catalogo_produtos(requisicao):
    #inserir_produto(requisicao)
    
    produtos = Produto.objects.all()
    dados = {
        'produtos': produtos
    }
    
    return render(requisicao, 'catalogo_produtos.html', dados)

def inserir_produto(requisicao):
    produto = Produto(nome_produto="Capuccino", descricao= "Cafe com leite", preco=0.50, categoria="Coffe")
    produto.save()