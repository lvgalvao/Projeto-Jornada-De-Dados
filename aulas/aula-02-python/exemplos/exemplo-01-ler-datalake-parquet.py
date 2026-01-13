"""
============================================
EXEMPLO 1: Conectar com DataLake e Ler Parquet
============================================
Conceito: Conectar com DataLake usando boto3 e ler arquivos Parquet
Pergunta: Como ler dados de um DataLake usando a API S3?
"""

# Instalar boto3: pip install boto3
import boto3

# Configurações do DataLake
S3_ENDPOINT_URL = "https://XXXX.storage.supabase.co/storage/v1/s3"
AWS_REGION = "us-west-2"
AWS_ACCESS_KEY_ID = "XXXX"
AWS_SECRET_ACCESS_KEY = "XXXXX"
BUCKET_NAME = "XXXX"

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

# Instalar pandas: pip install pandas pyarrow
import pandas as pd
# Trabalha com dados "em memória" transforma um bytes
import io

# Baixar arquivo Parquet
FILE_KEY = "preco_competidores.parquet"
response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
parquet_bytes = response["Body"].read()

# Converter Parquet para DataFrame
df_precos = pd.read_parquet(io.BytesIO(parquet_bytes))

# ============================================
# EXPLORANDO DADOS COM PANDAS
# ============================================

# Visualizar primeiras linhas
df_precos.head()

# Visualizar últimas linhas
df_precos.tail()

# Informações do DataFrame (tipos, memória, etc)
df_precos.info()

# Estatísticas descritivas (média, mediana, desvio padrão, etc)
df_precos.describe()

# Estatísticas de uma coluna específica
df_precos["preco_concorrente"].describe()

# Contar valores únicos
df_precos["nome_concorrente"].value_counts()

# Contar valores únicos com percentual
df_precos["nome_concorrente"].value_counts(normalize=True)

# Agrupar e agregar dados
# Exemplo: Preço médio por concorrente
df_precos.groupby("nome_concorrente")["preco_concorrente"].mean()

# Múltiplas agregações
df_precos.groupby("nome_concorrente")["preco_concorrente"].agg(["mean", "min", "max", "count"])

# Agrupar por múltiplas colunas
df_precos.groupby(["nome_concorrente", "id_produto"])["preco_concorrente"].mean()

# Filtrar dados
# Produtos com preço maior que 100
df_precos[df_precos["preco_concorrente"] > 100]

# Filtrar por múltiplas condições
df_precos[(df_precos["preco_concorrente"] > 100) & (df_precos["nome_concorrente"] == "Amazon")]

# Ordenar dados
df_precos.sort_values("preco_concorrente", ascending=False)

# Ordenar por múltiplas colunas
df_precos.sort_values(["nome_concorrente", "preco_concorrente"], ascending=[True, False])

# Selecionar colunas específicas
df_precos[["id_produto", "nome_concorrente", "preco_concorrente"]]

# Criar nova coluna calculada
df_precos["preco_arredondado"] = df_precos["preco_concorrente"].round(0)

# Contar linhas e colunas
len(df_precos)  # Número de linhas
df_precos.shape  # (linhas, colunas)

# Verificar valores únicos
df_precos["nome_concorrente"].unique()
df_precos["nome_concorrente"].nunique()  # Quantidade de valores únicos

# Verificar valores faltantes
df_precos.isnull().sum()

# Verificar duplicatas
df_precos.duplicated().sum()

# Top N valores
df_precos.nlargest(10, "preco_concorrente")  # Top 10 preços mais altos
df_precos.nsmallest(10, "preco_concorrente")  # Top 10 preços mais baixos

# Converter data_coleta para datetime (se necessário)
df_precos["data_coleta"] = pd.to_datetime(df_precos["data_coleta"])

# Agrupar por data e calcular média
df_precos.groupby(df_precos["data_coleta"].dt.date)["preco_concorrente"].mean()
