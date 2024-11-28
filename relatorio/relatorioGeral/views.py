from django.shortcuts import render
#local em que eu coloco as coisas para o usuário ver


def relatorioGeral(request):
    return render (request, 'usuarios/relatorioGeral.html')

def relatorioVendas(request):
    return render (request, 'relatorioVendas.html')

def relatorioEstoque(request):
    return render (request, 'relatorioEstoque.html')
