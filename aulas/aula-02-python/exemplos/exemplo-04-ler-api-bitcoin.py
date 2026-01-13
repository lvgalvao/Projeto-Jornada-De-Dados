"""
============================================
EXEMPLO 4: Ler API e Salvar no Banco
============================================
Conceito: Buscar dados de API e salvar no PostgreSQL
Pergunta: Como obter dados de uma API e salvar no banco de dados?

NESTE EXEMPLO VOCÊ APRENDE:
- O que é uma API e por que usar
- Como usar a biblioteca requests
- Como fazer requisições GET para APIs REST
- Como processar dados JSON
- Como salvar dados de API no PostgreSQL
"""

import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# ============================================
# O QUE É UMA API?
# ============================================
# API (Application Programming Interface) = Interface de Programação de Aplicações
# É uma forma de COMUNICAR com outros sistemas através da internet
# 
# Exemplos de APIs:
# - API do Bitcoin: preços em tempo real
# - API do Twitter: tweets e dados sociais
# - API do Google Maps: localização e rotas
# - API do GitHub: dados de repositórios
#
# Python na Engenharia de Dados = COMUNICAR com sistemas externos
# SQL trabalha com dados que JÁ EXISTEM no banco
# Python BUSCA dados de sistemas externos via APIs

# ============================================
# BIBLIOTECA REQUESTS
# ============================================
# Instalar: pip install requests
# 
# A biblioteca requests é a forma mais simples de fazer requisições HTTP em Python
# Ela permite:
# - GET: buscar dados de uma API
# - POST: enviar dados para uma API
# - PUT: atualizar dados
# - DELETE: deletar dados
#
# Para engenharia de dados, usamos principalmente GET para buscar dados

# ============================================
# PASSO 1: Buscar Dados da API do Bitcoin
# ============================================

# API Coinbase - Preço do Bitcoin em tempo real
url_bitcoin = "https://api.coinbase.com/v2/prices/spot"

# Fazer requisição GET para a API
response = requests.get(url_bitcoin)

# Verificar se a requisição foi bem-sucedida
response.raise_for_status()

# Converter resposta JSON para dicionário Python
dados = response.json()

# Extrair dados do JSON
preco_usd = float(dados["data"]["amount"])
moeda_base = dados["data"]["base"]  # BTC
moeda_quote = dados["data"]["currency"]  # USD

# Adicionar timestamp
timestamp = datetime.now()

# Criar DataFrame com os dados
df_bitcoin = pd.DataFrame([{
    "criptomoeda": moeda_base,
    "preco_usd": preco_usd,
    "moeda_quote": moeda_quote,
    "timestamp": timestamp
}])

# ============================================
# PASSO 2: Processar Dados
# ============================================

# Converter timestamp para formato adequado
df_bitcoin["timestamp"] = pd.to_datetime(df_bitcoin["timestamp"])

# Adicionar coluna calculada (exemplo: preço em BRL - simulado)
taxa_usd_brl = 5.0  # Taxa de conversão (em produção viria de outra API)
df_bitcoin["preco_brl"] = df_bitcoin["preco_usd"] * taxa_usd_brl

# Formatar preço
df_bitcoin["preco_usd_formatado"] = df_bitcoin["preco_usd"].apply(lambda x: f"${x:,.2f}")

# ============================================
# PASSO 3: Salvar no PostgreSQL
# ============================================

# Instalar: pip install sqlalchemy psycopg2-binary
# Configurações do PostgreSQL (Supabase)
DATABASE_URL = "xxxxxx"

# Criar engine de conexão
engine = create_engine(DATABASE_URL)

# Salvar DataFrame em tabela PostgreSQL
# if_exists='append' permite adicionar novos registros sem substituir
df_bitcoin.to_sql(
    "cotacao_bitcoin",  # Nome da tabela
    engine,  # Engine de conexão
    if_exists="append",  # Adicionar ao invés de substituir
    index=False  # Não salvar índice
)

# Verificar dados salvos
df_verificacao = pd.read_sql_query(
    "SELECT * FROM cotacao_bitcoin ORDER BY timestamp DESC LIMIT 10",
    engine
)

# ============================================
# PASSO 4: Análise dos Dados Salvos
# ============================================

# Calcular estatísticas dos dados salvos
query_estatisticas = """
SELECT 
    COUNT(*) as total_registros,
    MIN(preco_usd) as preco_minimo,
    MAX(preco_usd) as preco_maximo,
    AVG(preco_usd) as preco_medio,
    MAX(timestamp) as ultima_atualizacao
FROM cotacao_bitcoin
"""

df_estatisticas = pd.read_sql_query(query_estatisticas, engine)

# Fechar conexão
engine.dispose()

# ============================================
# RESUMO: Pipeline API → Banco
# ============================================
# 1. ✅ Conectou com API do Bitcoin (requests)
# 2. ✅ Buscou dados em tempo real (GET)
# 3. ✅ Processou dados JSON (pandas)
# 4. ✅ Transformou e enriqueceu dados
# 5. ✅ Salvou no PostgreSQL (pandas + sqlalchemy)
# 
# Este é o fluxo completo de ingestão via API:
# API → Processamento → Banco de Dados

