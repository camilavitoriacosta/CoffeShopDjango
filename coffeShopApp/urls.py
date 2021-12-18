from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial,name='pagina_inicial'),
    path('catalogo_produtos', views.catalogo_produtos, name='catalogo_produtos')
]