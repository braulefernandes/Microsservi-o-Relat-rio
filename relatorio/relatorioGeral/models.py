from django.db import models


class Relatorioestoque(models.Model):
    id_produto = models.IntegerField()
    nome = models.CharField(max_length=50)
    valor_unitario = models.FloatField()
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=200, blank=True, null=True)
    categoria = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RelatorioEstoque'


class Relatoriovendas(models.Model):
    id_vendas = models.IntegerField()
    id_produto = models.IntegerField()
    data_venda = models.DateTimeField()
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RelatorioVendas'
