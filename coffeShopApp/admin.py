from django.contrib import admin

# Register your models here.
from .models import *

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'categoria')
    list_display_links = ('id', 'nome_produto')

admin.site.register(Produto, ListandoProdutos)

# admin.site.register(Usuario)
# admin.site.register(Pedido)
# admin.site.register(ProdutoPedido)
