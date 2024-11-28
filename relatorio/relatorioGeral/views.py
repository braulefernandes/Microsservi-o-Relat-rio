from django.shortcuts import render
#local em que eu coloco as coisas para o usuário ver


def home(request):
    return render(request, 'usuarios/relatorioGeral.html')

def relatorio_vendas(request):
    request.GET.get()
