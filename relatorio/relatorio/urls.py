from django.urls import path
from relatorioGeral import views
#local em que eu faço os urls

urlpatterns = [
    #rota, view responsavel, nome de referencia
    #usuarios.com
    path('', views.home, name='relatorioGeral'),
    path('relatorio_vendas/', views.relatorio_vendas, name='relatorio_vendas')
]
