"""
============================================
EXEMPLO 3: Consumir API REST
============================================
Conceito: Buscar dados de uma API externa
Pergunta: Como obter dados de uma API REST em Python?

NESTE EXEMPLO VOCÊ APRENDE:
- O que é uma API e por que é importante
- Como fazer requisições HTTP com requests
- Como consumir APIs REST
- Como tratar respostas JSON
- Como trabalhar com diferentes tipos de dados (JSON, imagens)

CASO DE NEGÓCIO:
Python na engenharia de dados é usado principalmente para se comunicar
e integrar outros sistemas. APIs são a forma moderna de sistemas se comunicarem.
Quando falamos de SQL, já tínhamos os dados. Python busca dados de sistemas externos.
"""

import requests
import pandas as pd
import json
from datetime import datetime

# ============================================
# O QUE É UMA API?
# ============================================
# API = Application Programming Interface
# É uma forma de sistemas diferentes se comunicarem e compartilharem dados.
# 
# Python na engenharia de dados:
# - SQL: trabalha com dados que JÁ EXISTEM no banco
# - Python: BUSCA dados de sistemas externos via APIs
# 
# Exemplos de APIs:
# - API Bitcoin: preços de criptomoedas
# - API NASA: imagens e dados espaciais
# - API Mercado Livre: produtos e preços
# - API bancária: saldos e transações


# ============================================
# EXEMPLO 1: API Bitcoin (Coinbase)
# ============================================

def buscar_preco_bitcoin():
    """
    Busca o preço atual do Bitcoin da API Coinbase
    """
    url = "https://api.coinbase.com/v2/prices/spot"
    params = {"currency": "USD"}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        dados = response.json()
        
        # Extrair dados
        preco_usd = float(dados["data"]["amount"])
        moeda = dados["data"]["currency"]
        
        return {
            "criptomoeda": "Bitcoin",
            "preco_usd": preco_usd,
            "moeda": moeda,
            "timestamp": datetime.now().isoformat()
        }
    
    except Exception as e:
        print(f"❌ Erro ao buscar preço Bitcoin: {e}")
        return None


# Buscar preço do Bitcoin
print("=" * 50)
print("EXEMPLO 1: API Bitcoin (Coinbase)")
print("=" * 50)

dados_bitcoin = buscar_preco_bitcoin()

if dados_bitcoin:
    print(f"✅ Preço do Bitcoin: ${dados_bitcoin['preco_usd']:,.2f} {dados_bitcoin['moeda']}")
    print(f"   Timestamp: {dados_bitcoin['timestamp']}")
    
    # Converter para DataFrame
    df_bitcoin = pd.DataFrame([dados_bitcoin])
    print(f"\nDataFrame criado:")
    print(df_bitcoin)


# ============================================
# EXEMPLO 2: API NASA - Imagem do Dia
# ============================================

def buscar_imagem_nasa(api_key: str = "DEMO_KEY"):
    """
    Busca a imagem astronômica do dia da API NASA
    
    Args:
        api_key: Chave da API NASA (DEMO_KEY funciona para testes)
    """
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": api_key}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        dados = response.json()
        
        return {
            "titulo": dados.get("title", ""),
            "data": dados.get("date", ""),
            "explicacao": dados.get("explanation", "")[:200] + "...",  # Primeiros 200 chars
            "url_imagem": dados.get("url", ""),
            "tipo_midia": dados.get("media_type", "")
        }
    
    except Exception as e:
        print(f"❌ Erro ao buscar imagem NASA: {e}")
        return None


print("\n" + "=" * 50)
print("EXEMPLO 2: API NASA - Imagem do Dia")
print("=" * 50)

# Buscar imagem do dia (usa DEMO_KEY que funciona para testes)
dados_nasa = buscar_imagem_nasa()

if dados_nasa:
    print(f"✅ Título: {dados_nasa['titulo']}")
    print(f"   Data: {dados_nasa['data']}")
    print(f"   Tipo: {dados_nasa['tipo_midia']}")
    print(f"   URL: {dados_nasa['url_imagem']}")
    print(f"   Explicação: {dados_nasa['explicacao']}")


# ============================================
# EXEMPLO 3: Processar Múltiplas APIs
# ============================================

print("\n" + "=" * 50)
print("EXEMPLO 3: Integrar Dados de Múltiplas APIs")
print("=" * 50)

# Buscar dados de múltiplas fontes
dados_apis = []

# Bitcoin
bitcoin = buscar_preco_bitcoin()
if bitcoin:
    dados_apis.append(bitcoin)

# NASA
nasa = buscar_imagem_nasa()
if nasa:
    # Adicionar apenas metadados (não a imagem em si)
    dados_apis.append({
        "fonte": "NASA",
        "titulo": nasa["titulo"],
        "data": nasa["data"],
        "tipo": nasa["tipo_midia"]
    })

# Criar DataFrame com dados de múltiplas APIs
if dados_apis:
    df_apis = pd.DataFrame(dados_apis)
    print(f"✅ {len(df_apis)} registros de diferentes APIs")
    print(f"\nDados integrados:")
    print(df_apis)


# ============================================
# RESUMO: Por que APIs são importantes?
# ============================================

print("\n" + "=" * 50)
print("💡 POR QUE APIS SÃO IMPORTANTES?")
print("=" * 50)
print("""
✅ Python na engenharia de dados = COMUNICAR com sistemas externos
✅ SQL trabalha com dados que JÁ EXISTEM no banco
✅ Python BUSCA dados de sistemas externos via APIs
✅ APIs retornam dados em JSON (fácil de processar)
✅ Permite integrar dados de múltiplas fontes
✅ Dados em tempo real (Bitcoin, preços, etc.)
✅ Automatizar coleta de informações
""")
