from django.shortcuts import render

def pagina_inicial(requisicao):
    return render(requisicao, 'pagina_inicial.html')

