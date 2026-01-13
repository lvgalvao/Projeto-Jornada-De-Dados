"""
Script para converter preco_competidores.csv para Parquet
"""

import pandas as pd
import os

# Caminhos
caminho_csv = "data/preco_competidores.csv"
caminho_parquet = "data/preco_competidores.parquet"

# Ler CSV
print(f"Lendo {caminho_csv}...")
df = pd.read_csv(caminho_csv)
print(f"✅ {len(df):,} linhas carregadas")

# Converter para Parquet
print(f"Convertendo para Parquet...")
df.to_parquet(
    caminho_parquet,
    index=False,
    engine='pyarrow',
    compression='snappy'
)
print(f"✅ Arquivo salvo: {caminho_parquet}")

# Comparar tamanhos
tamanho_csv = os.path.getsize(caminho_csv)
tamanho_parquet = os.path.getsize(caminho_parquet)
reducao = ((tamanho_csv - tamanho_parquet) / tamanho_csv) * 100

print(f"\n📊 Comparação:")
print(f"   CSV:    {tamanho_csv / 1024:.2f} KB")
print(f"   Parquet: {tamanho_parquet / 1024:.2f} KB")
print(f"   Redução: {reducao:.1f}%")

