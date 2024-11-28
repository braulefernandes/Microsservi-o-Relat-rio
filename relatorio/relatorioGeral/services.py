#cuidar da comunicação e alimentação do banco

import requests
from .models import RelatorioVendas, RelatorioEstoque

def fetch_vendas_from_gabriel():
    url = "https://gabriel-server.com/api/vendas/"  # URL do servidor do Gabriel
    try:
        response = requests.get(url)
        response.raise_for_status()
        vendas_data = response.json()

        # Inserir dados no banco
        for venda in vendas_data:
            RelatorioVendas.objects.create(
                id_venda=venda["id_venda"],
                nome=venda["nome"],
                valor_unitario=venda["valor_unitario"],
                quantidade=venda["quantidade"],
                categoria=venda["categoria"]
            )
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados de vendas: {e}")


import requests
from .models import RelatorioEstoque

def fetch_estoque_from_arthur():
    # Substitua pela URL real do servidor do Arthur
    url = "https://arthur-server.com/api/estoque/"
    try:
        # Faz a requisição para o servidor do Arthur
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção se a resposta tiver erro (ex.: 404 ou 500)
        estoque_data = response.json()  # Converte os dados recebidos em JSON

        # Insere os dados no banco de dados local
        for item in estoque_data:
            RelatorioEstoque.objects.create(
                nome=item["nome"],
                valor_unitario=item["valor_unitario"],
                quantidade=item["quantidade"],
                categoria=item["categoria"]
            )
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados de estoque do Arthur: {e}")
