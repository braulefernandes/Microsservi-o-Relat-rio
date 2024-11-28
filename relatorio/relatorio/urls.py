from django.urls import path
from relatorioGeral import views
#local em que eu faço os urls

urlpatterns = [
    #rota, view responsavel, nome de referencia
    #usuarios.com
    path('', views.relatorioGeral, name='relatorioGeral'),
    path('relatorioVendas', views.relatorioVendas, name='relatorioVendas'),
    path('relatorioEstoque', views.relatorioEstoque, name='relatorioEstoque'),
]
