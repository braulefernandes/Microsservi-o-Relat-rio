from django.shortcuts import render
from .models import RelatorioVendas
#local em que eu coloco as coisas para o usuário ver


def relatorioGeral(request):
    return render (request, 'relatorioGeral/templates/relatorioGeral.html')

def relatorioVendas(request):
    return render (request, '/relatorioVendas.html')

def relatorioEstoque(request):
    return render (request, '/relatorioEstoque.html')


def relatorio_vendas_json(request):
    # Consultando todos os registros de RelatorioVendas
    vendas = RelatorioVendas.objects.all()

    # Convertendo os registros para um formato de lista de dicionários
    vendas_data = list(vendas.values())

    # Retornando a resposta em formato JSON
    return JsonResponse(vendas_data, safe=False)

def relatorio_estoque_json(request):
    # Consultando todos os registros de RelatorioVendas
    estoque = RelatorioEstoque.objects.all()

    # Convertendo os registros para um formato de lista de dicionários
    estoque_data = list(estoque.values())

    # Retornando a resposta em formato JSON
    return JsonResponse(estoque_data, safe=False)