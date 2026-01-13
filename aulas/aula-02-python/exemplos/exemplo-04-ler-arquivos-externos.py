"""
============================================
EXEMPLO 4: Conectar com DataLake e Ler Parquet
============================================
Conceito: Conectar com DataLake usando boto3 e ler arquivos Parquet
Pergunta: Como ler dados de um DataLake usando a API S3?

NESTE EXEMPLO VOCÊ APRENDE:
- Como conectar com DataLake usando boto3
- Como ler arquivos Parquet de um DataLake
- Por que DataLakes são importantes na indústria
- Como trabalhar com Supabase Storage (compatível com S3)

CASO DE NEGÓCIO:
Ler dados de preços de concorrentes armazenados em um DataLake
para análise competitiva e tomada de decisão
"""

import pandas as pd
import boto3
import io

# ============================================
# POR QUE DATA LAKES SÃO IMPORTANTES?
# ============================================
"""
Data Lakes são repositórios centralizados que armazenam dados em seu formato bruto.
São amplamente utilizados na indústria para:

✅ Armazenar grandes volumes de dados (terabytes/petabytes)
✅ Manter dados em formato original (sem transformação prévia)
✅ Suportar múltiplos formatos (CSV, Parquet, JSON, etc.)
✅ Escalabilidade horizontal (cresce conforme necessidade)
✅ Economia de custos (armazenamento barato)

🌍 AWS S3 É O PADRÃO DA INDÚSTRIA:
- Mais de 50% das empresas usam AWS S3 para Data Lakes
- API padrão que funciona com múltiplas ferramentas
- Compatível com Supabase Storage, MinIO, e outros

📊 CASO DE USO REAL:
Empresas armazenam dados de vendas, produtos, preços de concorrentes
em Data Lakes para análises e machine learning.
"""

# ============================================
# CONFIGURAÇÕES DO DATA LAKE
# ============================================

# Supabase Storage usa API compatível com S3
# Isso permite usar boto3 (biblioteca padrão da AWS)

S3_ENDPOINT_URL = "https://zsutlhnykwxackvunyvr.storage.supabase.co/storage/v1/s3"
AWS_REGION = "us-west-2"

# Credenciais (em produção, use variáveis de ambiente!)
AWS_ACCESS_KEY_ID = "24f38596737f3de9352bdfbb86b2493f"
AWS_SECRET_ACCESS_KEY = "e3f46aac4d7db5d69a173f40d0f65c1457fce3b81d483f0201ec22e63329520e"

BUCKET_NAME = "meu_bucket"
FILE_KEY = "preco_competidores.parquet"  # Arquivo Parquet no bucket

# ============================================
# PASSO 1: Conectar com DataLake
# ============================================

print("=" * 50)
print("PASSO 1: Conectando com DataLake")
print("=" * 50)

print(f"🔗 Conectando ao Data Lake (Supabase Storage)...")
print(f"   Endpoint: {S3_ENDPOINT_URL}")
print(f"   Bucket: {BUCKET_NAME}")
print(f"   Arquivo: {FILE_KEY}")

# Criar cliente S3
# boto3 é a biblioteca padrão da AWS para trabalhar com S3
# Funciona também com Supabase Storage (API compatível)
s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    endpoint_url=S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

print("✅ Cliente S3 criado com sucesso!")

# ============================================
# PASSO 2: Baixar Arquivo Parquet do DataLake
# ============================================

print("\n" + "=" * 50)
print("PASSO 2: Baixando Arquivo Parquet do DataLake")
print("=" * 50)

try:
    # Baixar arquivo do Data Lake
    print(f"📥 Baixando arquivo Parquet do Data Lake...")
    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=FILE_KEY
    )
    
    # Ler bytes do arquivo Parquet
    parquet_bytes = response["Body"].read()
    print(f"✅ Arquivo baixado: {len(parquet_bytes):,} bytes")
    
except Exception as e:
    print(f"❌ Erro ao baixar arquivo: {e}")
    print("\n💡 Verifique:")
    print("   - Se o bucket existe")
    print("   - Se o arquivo está no bucket")
    print("   - Se as credenciais estão corretas")
    exit(1)

# ============================================
# PASSO 3: Converter Parquet para DataFrame
# ============================================

print("\n" + "=" * 50)
print("PASSO 3: Convertendo Parquet para DataFrame")
print("=" * 50)

try:
    # Converter bytes do Parquet para DataFrame
    # Parquet é um formato binário otimizado para Big Data
    df_precos = pd.read_parquet(io.BytesIO(parquet_bytes))
    
    print(f"✅ Parquet convertido para DataFrame com sucesso!")
    print(f"   Linhas x Colunas: {df_precos.shape}")
    
except Exception as e:
    print(f"❌ Erro ao converter Parquet: {e}")
    print("\n💡 Verifique:")
    print("   - Se o arquivo é realmente um Parquet válido")
    print("   - Se o pyarrow está instalado: pip install pyarrow")
    exit(1)

# ============================================
# PASSO 4: Explorar e Analisar Dados
# ============================================

print("\n" + "=" * 50)
print("PASSO 4: Explorando Dados")
print("=" * 50)

# Visualizar primeiras linhas
print(f"\n📊 Primeiras linhas:")
print(df_precos.head())

# Informações do DataFrame
print(f"\n📋 Informações do DataFrame:")
print(df_precos.info())

# Estatísticas descritivas
print(f"\n📈 Estatísticas de preço:")
print(df_precos["preco_concorrente"].describe())

# Análise de concorrentes
print(f"\n🏪 Concorrentes:")
print(df_precos["nome_concorrente"].value_counts())

# Resumo
print(f"\n💡 Resumo dos dados:")
print(f"   - Total de registros: {len(df_precos):,}")
print(f"   - Concorrentes únicos: {df_precos['nome_concorrente'].nunique()}")
print(f"   - Produtos únicos: {df_precos['id_produto'].nunique()}")
print(f"   - Preço médio: R$ {df_precos['preco_concorrente'].mean():.2f}")
print(f"   - Preço mínimo: R$ {df_precos['preco_concorrente'].min():.2f}")
print(f"   - Preço máximo: R$ {df_precos['preco_concorrente'].max():.2f}")

# ============================================
# RESUMO: Por que Parquet?
# ============================================

print("\n" + "=" * 50)
print("💡 POR QUE PARQUET É IDEAL PARA DATA LAKES?")
print("=" * 50)
print("""
✅ Compressão eficiente:
   - Arquivos 50-90% menores que CSV
   - Economia de espaço e custos

✅ Performance superior:
   - Leitura mais rápida, especialmente para grandes volumes
   - Formato columnar otimizado para análises

✅ Schema embutido:
   - Preserva tipos de dados automaticamente
   - Não precisa inferir tipos ao ler

✅ Ideal para Big Data:
   - Suportado por Spark, Pandas, Dask, etc.
   - Otimizado para processamento distribuído

✅ Predicate pushdown:
   - Lê apenas colunas necessárias
   - Reduz I/O e melhora performance
""")

print("=" * 50)
print("✅ Dados do DataLake carregados e prontos para análise!")
print("=" * 50)
