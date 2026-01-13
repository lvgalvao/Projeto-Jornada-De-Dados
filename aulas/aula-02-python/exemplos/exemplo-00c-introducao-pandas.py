"""
============================================
AQUECIMENTO: Introdução ao Pandas
============================================
Conceito: Entender o que é Pandas e por que é essencial
Pergunta: Por que Pandas é a biblioteca mais usada para dados em Python?

NESTE EXEMPLO VOCÊ APRENDE:
- O que é Pandas
- Por que usar Pandas ao invés de listas/dicionários
- Conceitos básicos: Series e DataFrame
- Operações básicas com Pandas
- Por que Pandas é essencial para trabalhar com dados

CASO DE NEGÓCIO:
Pandas é a ferramenta padrão para trabalhar com dados tabulares
em Python. É essencial para análise, limpeza e transformação de dados.
"""

import pandas as pd

# ============================================
# 1. PANDAS vs LISTAS/DICIONÁRIOS
# ============================================

# SEM PANDAS (usando listas):
vendas = [
    {"produto": "Smartphone", "quantidade": 2, "preco": 1299.90},
    {"produto": "Notebook", "quantidade": 1, "preco": 3499.90},
    {"produto": "Tablet", "quantidade": 3, "preco": 899.90}
]

receita_total = 0
for venda in vendas:
    receita = venda["quantidade"] * venda["preco"]
    receita_total += receita

print(f"Receita total (sem Pandas): R$ {receita_total:,.2f}")

# COM PANDAS (muito mais simples):
df_vendas = pd.DataFrame(vendas)
df_vendas["receita"] = df_vendas["quantidade"] * df_vendas["preco"]
receita_total_pandas = df_vendas["receita"].sum()

print(f"Receita total (com Pandas): R$ {receita_total_pandas:,.2f}")
print(f"\nDataFrame:\n{df_vendas}")


# ============================================
# 2. CONCEITOS BÁSICOS: SERIES E DATAFRAME
# ============================================

# Series = uma coluna de dados
precos = pd.Series([1299.90, 3499.90, 899.90], name="precos")
print(f"\nSeries de preços:\n{precos}")
print(f"Média: R$ {precos.mean():,.2f}, Maior: R$ {precos.max():,.2f}, Menor: R$ {precos.min():,.2f}")

# DataFrame = múltiplas colunas (tabela)
df_produtos = pd.DataFrame({
    "produto": ["Smartphone", "Notebook", "Tablet"],
    "preco": [1299.90, 3499.90, 899.90],
    "quantidade": [10, 5, 15]
})

print(f"\nDataFrame:\n{df_produtos}")
print(f"Formato: {df_produtos.shape} (linhas, colunas)")


# ============================================
# 3. OPERAÇÕES BÁSICAS COM PANDAS
# ============================================

df = pd.DataFrame({
    "produto": ["Smartphone", "Notebook", "Tablet", "Fone"],
    "categoria": ["Eletrônicos", "Informática", "Eletrônicos", "Acessórios"],
    "preco": [1299.90, 3499.90, 899.90, 199.90],
    "quantidade": [10, 5, 15, 20]
})

print(f"\nDataFrame original:\n{df}")

# Filtrar dados
produtos_caros = df[df["preco"] > 1000]
print(f"\nProdutos acima de R$ 1.000:\n{produtos_caros}")

# Agrupar por categoria
receita_por_categoria = df.groupby("categoria")["preco"].sum()
print(f"\nReceita por categoria:\n{receita_por_categoria}")

# Adicionar coluna calculada
df["receita_total"] = df["preco"] * df["quantidade"]
print(f"\nDataFrame com receita total:\n{df}")

