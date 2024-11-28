from django.db import models

class RelatorioVendas(models.Model):
    id_venda = models.AutoField(primary_key=True)  # Chave primária
    nome = models.CharField(max_length=50)        # Nome do produto
    valor_unitario = models.FloatField()          # Valor unitário do produto
    quantidade = models.IntegerField()            # Quantidade vendida
    categoria = models.CharField(max_length=20)   # Categoria do produto
    valor_total = models.FloatField()             # Valor total (calculado depois)

    def save(self, *args, **kwargs):
        # Calcula o valor_total antes de salvar
        self.valor_total = self.valor_unitario * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.categoria}"


class RelatorioEstoque(models.Model):
    nome = models.CharField(max_length=50)        # Nome do produto
    valor_unitario = models.FloatField()          # Valor unitário do produto
    quantidade = models.IntegerField()            # Quantidade em estoque
    categoria = models.CharField(max_length=20)   # Categoria do produto
    valor_total = models.FloatField()             # Valor total (calculado depois)

    def save(self, *args, **kwargs):
        # Calcula o valor_total antes de salvar
        self.valor_total = self.valor_unitario * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.categoria}"
