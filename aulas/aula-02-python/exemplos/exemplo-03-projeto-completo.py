"""
============================================
EXEMPLO 3: Projeto Completo - DataLake → Banco
============================================
Conceito: Pipeline completo de ingestão de dados
Pergunta: Como fazer um pipeline completo: ler do DataLake e salvar no banco?

NESTE EXEMPLO VOCÊ APRENDE:
- Como combinar todos os conceitos aprendidos
- Pipeline completo: DataLake → PostgreSQL (sem processamento)
- Salvar exatamente o que vem do Parquet
- Por que Python é essencial para engenharia de dados
"""

import io
import pandas as pd
import boto3
from sqlalchemy import create_engine

# ============================================
# PASSO 1: Conectar com DataLake e Ler Parquet
# ============================================

# Instalar boto3: pip install boto3
# Configurações do DataLake
S3_ENDPOINT_URL = "xxxxx"
AWS_REGION = "us-west-2"
AWS_ACCESS_KEY_ID = "xxxxxf"
AWS_SECRET_ACCESS_KEY = "xxxx"
BUCKET_NAME = "meu_bucket"

# Criar cliente S3
s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    endpoint_url=S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

# Listar arquivos no bucket
response = s3.list_objects(Bucket=BUCKET_NAME)
arquivos = [obj["Key"] for obj in response["Contents"]]

# Baixar arquivo Parquet
FILE_KEY = "preco_competidores.parquet"
response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
parquet_bytes = response["Body"].read()

# Converter Parquet para DataFrame
df_precos = pd.read_parquet(io.BytesIO(parquet_bytes))

# ============================================
# PASSO 2: Salvar no PostgreSQL (sem processamento)
# ============================================

# Instalar: pip install sqlalchemy psycopg2-binary
# Configurações do PostgreSQL (Supabase)
DATABASE_URL = "postgresql+psycopg2://postgres.xxx:xxx@aws-0-us-west-2.pooler.suxxx"

# Criar engine de conexão
engine = create_engine(DATABASE_URL)

# Salvar DataFrame exatamente como vem do Parquet
df_precos.to_sql(
    "preco_competidores",  # Nome da tabela
    engine,  # Engine de conexão
    if_exists="replace",  # Substituir se existir
    index=False  # Não salvar índice
)

# Verificar dados salvos
df_verificacao = pd.read_sql_query("SELECT * FROM preco_competidores LIMIT 10", engine)

# Fechar conexão
engine.dispose()

# ============================================
# RESUMO: Pipeline Completo
# ============================================
# 1. ✅ Conectou com DataLake (boto3)
# 2. ✅ Baixou arquivo Parquet
# 3. ✅ Convertou para DataFrame (pandas)
# 4. ✅ Salvou no PostgreSQL (sem processamento)
# 
# Este é o fluxo completo de ingestão de dados:
# EXTRACTION → LOADING (EL)
# Dados salvos exatamente como vêm do Parquet