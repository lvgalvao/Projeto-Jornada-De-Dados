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
# GUARDE BEM ISSO: Lista de dicionários é a estrutura que Pandas usa por baixo!
vendas_tenis = [
    {"tenis": "Tênis Nike Air Max", "quantidade": 2, "preco": 599.90},
    {"tenis": "Tênis Adidas Ultraboost", "quantidade": 1, "preco": 699.90},
    {"tenis": "Tênis Puma RS-X", "quantidade": 3, "preco": 449.90}
]

receita_total = 0
for venda in vendas_tenis:
    receita = venda["quantidade"] * venda["preco"]
    receita_total += receita

print(f"Receita total (sem Pandas): R$ {receita_total:,.2f}")

# COM PANDAS (muito mais simples):
# GUARDE BEM ISSO: Pandas converte lista de dicionários em DataFrame automaticamente!
df_vendas = pd.DataFrame(vendas_tenis)
df_vendas["receita"] = df_vendas["quantidade"] * df_vendas["preco"]
receita_total_pandas = df_vendas["receita"].sum()

print(f"Receita total (com Pandas): R$ {receita_total_pandas:,.2f}")
print(f"\nDataFrame:\n{df_vendas}")


# ============================================
# 2. CONCEITOS BÁSICOS: SERIES E DATAFRAME
# ============================================

# Series = uma coluna de dados
precos_tenis = pd.Series([599.90, 699.90, 449.90, 399.90, 299.90], name="precos")
print(f"\nSeries de preços de tênis:\n{precos_tenis}")
print(f"Média: R$ {precos_tenis.mean():,.2f}, Maior: R$ {precos_tenis.max():,.2f}, Menor: R$ {precos_tenis.min():,.2f}")

# DataFrame = múltiplas colunas (tabela)
# GUARDE BEM ISSO: DataFrame é como uma tabela Excel, mas muito mais poderoso!
df_tenis = pd.DataFrame({
    "tenis": ["Tênis Nike Air Max", "Tênis Adidas Ultraboost", "Tênis Puma RS-X"],
    "marca": ["Nike", "Adidas", "Puma"],
    "preco": [599.90, 699.90, 449.90],
    "quantidade": [10, 5, 15]
})

print(f"\nDataFrame de tênis:\n{df_tenis}")
print(f"Formato: {df_tenis.shape} (linhas, colunas)")


# ============================================
# 3. OPERAÇÕES BÁSICAS COM PANDAS
# ============================================

# GUARDE BEM ISSO: Lista de dicionários vira DataFrame facilmente!
lista_tenis = [
    {"tenis": "Tênis Nike Air Max", "marca": "Nike", "preco": 599.90, "quantidade": 10},
    {"tenis": "Tênis Adidas Ultraboost", "marca": "Adidas", "preco": 699.90, "quantidade": 5},
    {"tenis": "Tênis Puma RS-X", "marca": "Puma", "preco": 449.90, "quantidade": 15},
    {"tenis": "Tênis Vans Old Skool", "marca": "Vans", "preco": 399.90, "quantidade": 20}
]

df = pd.DataFrame(lista_tenis)

print(f"\nDataFrame original:\n{df}")

# Filtrar dados
tenis_caros = df[df["preco"] > 500]
print(f"\nTênis acima de R$ 500:\n{tenis_caros}")

# Agrupar por marca
receita_por_marca = df.groupby("marca")["preco"].sum()
print(f"\nReceita por marca:\n{receita_por_marca}")

# Adicionar coluna calculada
df["receita_total"] = df["preco"] * df["quantidade"]
print(f"\nDataFrame com receita total:\n{df}")

# ============================================
# 4. LISTA DE TÊNIS COMPLETA
# ============================================

# GUARDE BEM ISSO: Esta é a estrutura mais comum que você vai usar!
lista_completa_tenis = [
    {"nome": "Tênis Nike Air Max", "marca": "Nike", "preco": 599.90, "tamanho": 42},
    {"nome": "Tênis Adidas Ultraboost", "marca": "Adidas", "preco": 699.90, "tamanho": 41},
    {"nome": "Tênis Puma RS-X", "marca": "Puma", "preco": 449.90, "tamanho": 40},
    {"nome": "Tênis Vans Old Skool", "marca": "Vans", "preco": 399.90, "tamanho": 39},
    {"nome": "Tênis Converse All Star", "marca": "Converse", "preco": 299.90, "tamanho": 38}
]

# Converter para DataFrame
df_tenis_completo = pd.DataFrame(lista_completa_tenis)

print(f"\n{'='*50}")
print(f"DataFrame completo de {len(df_tenis_completo)} tênis:")
print(f"{'='*50}")
print(df_tenis_completo)

print(f"\n💡 GUARDE BEM ISSO:")
print(f"   - Lista de dicionários → DataFrame (conversão automática!)")
print(f"   - Cada dicionário = uma linha")
print(f"   - Cada chave = uma coluna")
print(f"   - Pandas faz a mágica de organizar tudo!")

