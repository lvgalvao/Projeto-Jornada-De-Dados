"""
============================================
AQUECIMENTO: APIs e JSON
============================================
Conceito: Entender como APIs funcionam e como trabalhar com JSON
Pergunta: O que é uma API e como processar dados JSON em Python?

NESTE EXEMPLO VOCÊ APRENDE:
- O que é uma API
- O que é JSON
- Como JSON se relaciona com dicionários Python
- Como processar dados de APIs
- Por que isso é essencial para ingestão de dados

CASO DE NEGÓCIO:
APIs são a principal forma de obter dados de sistemas externos.
Entender JSON é fundamental para trabalhar com dados modernos.
"""

import json

# ============================================
# 1. JSON vs DICIONÁRIO PYTHON
# ============================================

# JSON é muito similar a dicionários Python!
# Exemplo de JSON (como string):
json_string = '''
{
    "produto": {
        "id": "prd_001",
        "nome": "Smartphone Galaxy A54",
        "preco": 1299.90,
        "categoria": "Eletrônicos",
        "disponivel": true
    },
    "vendas": [100, 150, 200]
}
'''

# Converter JSON string para dicionário Python
dados_python = json.loads(json_string)

# Acessar dados (igual a dicionário!)
print(f"Nome do produto: {dados_python['produto']['nome']}")
print(f"Preço: R$ {dados_python['produto']['preco']}")
print(f"Vendas: {dados_python['vendas']}")


# ============================================
# 2. SIMULANDO RESPOSTA DE API
# ============================================

# Simulando uma resposta real de API
resposta_api = {
    "status": "success",
    "data": {
        "produtos": [
            {
                "id": "prd_001",
                "nome": "Smartphone Galaxy A54",
                "preco": "1299.90",
                "categoria": "Eletrônicos"
            },
            {
                "id": "prd_002",
                "nome": "Notebook Dell Inspiron",
                "preco": "3499.90",
                "categoria": "Informática"
            }
        ],
        "total": 2
    },
    "timestamp": "2024-01-15T10:30:00Z"
}


# ============================================
# 3. PROCESSAR DADOS DA API
# ============================================

# Extrair produtos
produtos = resposta_api["data"]["produtos"]

print(f"\nTotal de produtos: {resposta_api['data']['total']}")

for produto in produtos:
    nome = produto["nome"]
    preco_str = produto["preco"]
    preco_float = float(preco_str)  # Converter string para float
    categoria = produto["categoria"]
    
    print(f"  - {nome}: R$ {preco_float:,.2f} ({categoria})")


# ============================================
# 4. CONVERTER DICIONÁRIO PARA JSON
# ============================================

# Converter dicionário Python para JSON (string)
dados_python = {
    "nome": "Smartphone",
    "preco": 1299.90,
    "disponivel": True
}

json_string = json.dumps(dados_python, indent=2, ensure_ascii=False)
print(f"\nJSON string:\n{json_string}")


# ============================================
# 5. EXEMPLO COMPLETO: PROCESSAR API
# ============================================

def processar_produto_api(dados_produto):
    """
    Processa dados de um produto vindo da API
    """
    nome = dados_produto["nome"]
    preco = float(dados_produto["preco"])
    categoria = dados_produto["categoria"]
    
    return {
        "nome_formatado": nome.upper(),
        "preco_formatado": f"R$ {preco:,.2f}",
        "categoria": categoria
    }

# Simular dados de API
produto_api = {
    "nome": "Smartphone Galaxy A54",
    "preco": "1299.90",
    "categoria": "Eletrônicos"
}

# Processar
produto_processado = processar_produto_api(produto_api)
print(f"\nDados processados: {produto_processado}")

