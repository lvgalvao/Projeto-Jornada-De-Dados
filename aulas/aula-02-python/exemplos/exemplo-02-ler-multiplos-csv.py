"""
============================================
EXEMPLO 2: Ler Múltiplos CSVs e Combinar
============================================
Conceito: Carregar múltiplos arquivos e fazer JOIN
Pergunta: Como combinar dados de produtos, clientes e vendas?

NESTE EXEMPLO VOCÊ APRENDE:
- Como ler múltiplos arquivos CSV
- Como fazer merge (equivalente ao JOIN do SQL)
- Como combinar dados de diferentes fontes
- Como validar dados após combinação

CASO DE NEGÓCIO:
Criar uma visão unificada dos dados de vendas com informações
de produtos e clientes para análise completa
"""

import pandas as pd
import os

# Definir caminho dos dados
DATA_DIR = "../../data"

# Ler todos os CSVs
print("Carregando dados...")
df_produtos = pd.read_csv(os.path.join(DATA_DIR, "produtos.csv"))
df_clientes = pd.read_csv(os.path.join(DATA_DIR, "clientes.csv"))
df_vendas = pd.read_csv(os.path.join(DATA_DIR, "vendas.csv"))

print(f"✅ Produtos: {len(df_produtos)} linhas")
print(f"✅ Clientes: {len(df_clientes)} linhas")
print(f"✅ Vendas: {len(df_vendas)} linhas")

# Fazer merge (equivalente ao JOIN do SQL)
# Primeiro: Vendas + Produtos
df_vendas_produtos = df_vendas.merge(
    df_produtos,
    left_on="id_produto",
    right_on="id_produto",
    how="inner",
    suffixes=("_venda", "_produto")
)

print(f"\n✅ Vendas + Produtos: {len(df_vendas_produtos)} linhas")

# Segundo: Adicionar informações de clientes
df_completo = df_vendas_produtos.merge(
    df_clientes,
    left_on="id_cliente",
    right_on="id_cliente",
    how="inner",
    suffixes=("", "_cliente")
)

print(f"✅ Dataset Completo: {len(df_completo)} linhas")
print(f"✅ Colunas: {len(df_completo.columns)}")

# Mostrar primeiras linhas do dataset combinado
print("\n" + "=" * 50)
print("PRIMEIRAS 3 LINHAS DO DATASET COMBINADO:")
print("=" * 50)
print(df_completo[["id_venda", "nome_produto", "nome_cliente", "quantidade", "preco_unitario"]].head(3))

