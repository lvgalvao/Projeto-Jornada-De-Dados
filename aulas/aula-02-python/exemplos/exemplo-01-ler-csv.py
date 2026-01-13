"""
============================================
EXEMPLO 1: Ler CSV com Pandas
============================================
Conceito: Ler arquivos CSV e explorar dados
Pergunta: Como carregar os dados da aula 01 em Python?

NESTE EXEMPLO VOCÊ APRENDE:
- Como usar pandas para ler arquivos CSV
- Como explorar dados básicos (head, info, describe)
- Como verificar tipos de dados
- Como acessar colunas e linhas

CASO DE NEGÓCIO:
Carregar os dados de vendas gerados na aula 01 para análise em Python
"""

import pandas as pd
import os

# Definir caminho dos dados
DATA_DIR = "../../data"

# Ler arquivo CSV
df_vendas = pd.read_csv(os.path.join(DATA_DIR, "vendas.csv"))

# Explorar dados básicos
print("=" * 50)
print("PRIMEIRAS 5 LINHAS:")
print("=" * 50)
print(df_vendas.head())

print("\n" + "=" * 50)
print("INFORMAÇÕES DO DATAFRAME:")
print("=" * 50)
print(df_vendas.info())

print("\n" + "=" * 50)
print("ESTATÍSTICAS DESCRITIVAS:")
print("=" * 50)
print(df_vendas.describe())

print("\n" + "=" * 50)
print("FORMATO DO DATAFRAME:")
print("=" * 50)
print(f"Linhas: {len(df_vendas)}")
print(f"Colunas: {len(df_vendas.columns)}")
print(f"Colunas: {list(df_vendas.columns)}")

