"""
============================================
EXEMPLO 6: Tratamento e Limpeza de Dados
============================================
Conceito: Limpar e preparar dados para análise
Pergunta: Como tratar dados inconsistentes e faltantes?

NESTE EXEMPLO VOCÊ APRENDE:
- Como identificar dados faltantes (NaN)
- Como tratar valores duplicados
- Como converter tipos de dados
- Como normalizar e limpar strings
- Como tratar outliers

CASO DE NEGÓCIO:
Preparar dados brutos para análise, garantindo qualidade
e consistência dos dados
"""

import pandas as pd
import numpy as np
import os

# Carregar dados
df_vendas = pd.read_csv("../../data/vendas.csv")

print("=" * 50)
print("EXEMPLO 1: Identificar Dados Faltantes")
print("=" * 50)

# Verificar valores faltantes
print("Valores faltantes por coluna:")
print(df_vendas.isnull().sum())

# Percentual de valores faltantes
print("\nPercentual de valores faltantes:")
print((df_vendas.isnull().sum() / len(df_vendas) * 100).round(2))


print("\n" + "=" * 50)
print("EXEMPLO 2: Tratar Dados Faltantes")
print("=" * 50)

# Criar cópia para não alterar original
df_limpo = df_vendas.copy()

# Opção 1: Remover linhas com valores faltantes
df_sem_nulos = df_limpo.dropna()
print(f"✅ Linhas sem nulos: {len(df_sem_nulos)} (de {len(df_limpo)})")

# Opção 2: Preencher com valor padrão
df_preenchido = df_limpo.copy()
# Exemplo: preencher quantidade faltante com 1
if df_preenchido['quantidade'].isnull().any():
    df_preenchido['quantidade'] = df_preenchido['quantidade'].fillna(1)
    print("✅ Quantidades faltantes preenchidas com 1")

# Opção 3: Preencher com média/mediana
if df_preenchido['preco_unitario'].isnull().any():
    media_preco = df_preenchido['preco_unitario'].mean()
    df_preenchido['preco_unitario'] = df_preenchido['preco_unitario'].fillna(media_preco)
    print(f"✅ Preços faltantes preenchidos com média: R$ {media_preco:.2f}")


print("\n" + "=" * 50)
print("EXEMPLO 3: Remover Duplicatas")
print("=" * 50)

# Verificar duplicatas
duplicatas = df_limpo.duplicated().sum()
print(f"Linhas duplicadas: {duplicatas}")

if duplicatas > 0:
    df_sem_duplicatas = df_limpo.drop_duplicates()
    print(f"✅ Removidas {duplicatas} duplicatas")
    print(f"   Antes: {len(df_limpo)} linhas")
    print(f"   Depois: {len(df_sem_duplicatas)} linhas")


print("\n" + "=" * 50)
print("EXEMPLO 4: Converter Tipos de Dados")
print("=" * 50)

# Verificar tipos atuais
print("Tipos atuais:")
print(df_limpo.dtypes)

# Converter data_venda para datetime
if 'data_venda' in df_limpo.columns:
    df_limpo['data_venda'] = pd.to_datetime(df_limpo['data_venda'], errors='coerce')
    print("✅ data_venda convertida para datetime")

# Converter preco_unitario para float (se necessário)
if df_limpo['preco_unitario'].dtype == 'object':
    df_limpo['preco_unitario'] = pd.to_numeric(
        df_limpo['preco_unitario'], 
        errors='coerce'
    )
    print("✅ preco_unitario convertido para numérico")


print("\n" + "=" * 50)
print("EXEMPLO 5: Normalizar Strings")
print("=" * 50)

# Carregar produtos para exemplo
df_produtos = pd.read_csv("../../data/produtos.csv")

if 'nome_produto' in df_produtos.columns:
    # Remover espaços extras
    df_produtos['nome_produto_limpo'] = df_produtos['nome_produto'].str.strip()
    
    # Converter para minúsculas (opcional)
    # df_produtos['nome_produto_limpo'] = df_produtos['nome_produto_limpo'].str.lower()
    
    print("✅ Nomes de produtos normalizados")
    print("\nExemplo:")
    print(df_produtos[['nome_produto', 'nome_produto_limpo']].head())


print("\n" + "=" * 50)
print("EXEMPLO 6: Tratar Outliers")
print("=" * 50)

# Calcular receita por venda
df_limpo['receita'] = df_limpo['quantidade'] * df_limpo['preco_unitario']

# Identificar outliers usando IQR (Interquartile Range)
Q1 = df_limpo['receita'].quantile(0.25)
Q3 = df_limpo['receita'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df_limpo[(df_limpo['receita'] < limite_inferior) | 
                    (df_limpo['receita'] > limite_superior)]

print(f"✅ Outliers identificados: {len(outliers)} ({len(outliers)/len(df_limpo)*100:.2f}%)")
print(f"   Limite inferior: R$ {limite_inferior:.2f}")
print(f"   Limite superior: R$ {limite_superior:.2f}")

if len(outliers) > 0:
    print("\nTop 5 outliers:")
    print(outliers[['id_venda', 'receita']].nlargest(5, 'receita'))


print("\n" + "=" * 50)
print("📊 RESUMO DO TRATAMENTO:")
print("=" * 50)
print(f"✅ Dados originais: {len(df_vendas)} linhas")
print(f"✅ Dados limpos: {len(df_limpo)} linhas")
print(f"✅ Valores faltantes tratados")
print(f"✅ Tipos de dados corrigidos")
print(f"✅ Outliers identificados")

