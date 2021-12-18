from django.shortcuts import render
from .models import *

def pagina_inicial(requisicao):
    return render(requisicao, 'pagina_inicial.html')


def catalogo_produtos_coffe(requisicao):
    produtos = filtrar_produto_por_categoria("coffe")    
    dados = {
        'produtos': produtos
    }
    
    return render(requisicao, 'catalogo_produtos.html', dados)

def catalogo_produtos_tea(requisicao):
    produtos = filtrar_produto_por_categoria("tea")    
    dados = {
        'produtos': produtos
    }
    
    return render(requisicao, 'catalogo_produtos.html', dados)

def catalogo_produtos_smoothie(requisicao):
    produtos = filtrar_produto_por_categoria("smoothie")    
    dados = {
        'produtos': produtos
    }
    return render(requisicao, 'catalogo_produtos.html', dados)

def filtrar_produto_por_categoria(categoria_produto):
    return Produto.objects.filter(categoria=categoria_produto)
    
def inserir_produto(requisicao):
    produto = Produto(nome_produto="Capuccino", descricao= "Cafe com leite", preco=0.50, categoria="Coffe")
    produto.save()