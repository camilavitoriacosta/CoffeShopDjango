from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial,name='pagina_inicial'),
    path('catalogo_produtos/coffe', views.catalogo_produtos_coffe, name='catalogo_produtos_coffe'),
    path('catalogo_produtos/tea', views.catalogo_produtos_tea, name='catalogo_produtos_tea'),
    path('catalogo_produtos/smoothie', views.catalogo_produtos_smoothie, name='catalogo_produtos_smoothie'),
    path('buscar_produto', views.buscar_produto, name='buscar_produto'),
    path('/cadastro_produto', views.cadastro_produto, name='cadastro_produto')

]