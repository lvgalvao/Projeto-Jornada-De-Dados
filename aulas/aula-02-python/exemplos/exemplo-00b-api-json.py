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
# GUARDE BEM ISSO: JSON = Dicionário Python (fácil conversão!)
# Exemplo de JSON (como string):
json_string = '''
{
    "produto": {
        "id": "ten_001",
        "nome": "Tênis Nike Air Max",
        "preco": 599.90,
        "categoria": "Tênis",
        "marca": "Nike",
        "disponivel": true
    },
    "vendas": [50, 75, 100]
}
'''

# Converter JSON string para dicionário Python
dados_python = json.loads(json_string)

# Acessar dados (igual a dicionário!)
print(f"Nome do tênis: {dados_python['produto']['nome']}")
print(f"Preço: R$ {dados_python['produto']['preco']}")
print(f"Marca: {dados_python['produto']['marca']}")
print(f"Vendas: {dados_python['vendas']}")


# ============================================
# 2. SIMULANDO RESPOSTA DE API
# ============================================

# Simulando uma resposta real de API
# GUARDE BEM ISSO: APIs retornam listas de dicionários (estrutura muito comum!)
resposta_api = {
    "status": "success",
    "data": {
        "tenis": [
            {
                "id": "ten_001",
                "nome": "Tênis Nike Air Max",
                "preco": "599.90",
                "marca": "Nike",
                "categoria": "Tênis"
            },
            {
                "id": "ten_002",
                "nome": "Tênis Adidas Ultraboost",
                "preco": "699.90",
                "marca": "Adidas",
                "categoria": "Tênis"
            },
            {
                "id": "ten_003",
                "nome": "Tênis Puma RS-X",
                "preco": "449.90",
                "marca": "Puma",
                "categoria": "Tênis"
            }
        ],
        "total": 3
    },
    "timestamp": "2024-01-15T10:30:00Z"
}


# ============================================
# 3. PROCESSAR DADOS DA API
# ============================================

# Extrair lista de tênis
lista_tenis = resposta_api["data"]["tenis"]

print(f"\nTotal de tênis: {resposta_api['data']['total']}")

for tenis in lista_tenis:
    nome = tenis["nome"]
    preco_str = tenis["preco"]
    preco_float = float(preco_str)  # Converter string para float
    marca = tenis["marca"]
    
    print(f"  - {nome} ({marca}): R$ {preco_float:,.2f}")


# ============================================
# 4. CONVERTER DICIONÁRIO PARA JSON
# ============================================

# Converter dicionário Python para JSON (string)
# GUARDE BEM ISSO: Você pode converter dicionário Python para JSON quando precisar enviar dados para APIs!
dados_python = {
    "nome": "Tênis Nike Air Max",
    "marca": "Nike",
    "preco": 599.90,
    "disponivel": True
}

json_string = json.dumps(dados_python, indent=2, ensure_ascii=False)
print(f"\nJSON string:\n{json_string}")


# ============================================
# 5. EXEMPLO COMPLETO: PROCESSAR API
# ============================================

def processar_tenis_api(dados_tenis):
    """
    Processa dados de um tênis vindo da API
    """
    nome = dados_tenis["nome"]
    preco = float(dados_tenis["preco"])
    marca = dados_tenis.get("marca", "Não informada")
    categoria = dados_tenis["categoria"]
    
    return {
        "nome_formatado": nome.upper(),
        "preco_formatado": f"R$ {preco:,.2f}",
        "marca": marca,
        "categoria": categoria
    }

# Simular dados de API
tenis_api = {
    "nome": "Tênis Nike Air Max",
    "preco": "599.90",
    "marca": "Nike",
    "categoria": "Tênis"
}

# Processar
tenis_processado = processar_tenis_api(tenis_api)
print(f"\nDados processados: {tenis_processado}")


# ============================================
# 6. LISTA COMPLETA DE TÊNIS (DICIONÁRIOS)
# ============================================

# GUARDE BEM ISSO: Lista de dicionários é a estrutura perfeita para dados tabulares!
# Cada dicionário = uma linha, cada chave = uma coluna
lista_completa_tenis = [
    {
        "id": "ten_001",
        "nome": "Tênis Nike Air Max",
        "marca": "Nike",
        "preco": 599.90,
        "categoria": "Tênis",
        "tamanho": 42,
        "cor": "Preto/Branco"
    },
    {
        "id": "ten_002",
        "nome": "Tênis Adidas Ultraboost",
        "marca": "Adidas",
        "preco": 699.90,
        "categoria": "Tênis",
        "tamanho": 41,
        "cor": "Branco"
    },
    {
        "id": "ten_003",
        "nome": "Tênis Puma RS-X",
        "marca": "Puma",
        "preco": 449.90,
        "categoria": "Tênis",
        "tamanho": 40,
        "cor": "Preto"
    },
    {
        "id": "ten_004",
        "nome": "Tênis Vans Old Skool",
        "marca": "Vans",
        "preco": 399.90,
        "categoria": "Tênis",
        "tamanho": 39,
        "cor": "Preto/Branco"
    },
    {
        "id": "ten_005",
        "nome": "Tênis Converse All Star",
        "marca": "Converse",
        "preco": 299.90,
        "categoria": "Tênis",
        "tamanho": 38,
        "cor": "Branco"
    }
]

print(f"\n{'='*50}")
print(f"Lista completa de {len(lista_completa_tenis)} tênis:")
print(f"{'='*50}")

for tenis in lista_completa_tenis:
    print(f"\n{tenis['nome']} ({tenis['marca']})")
    print(f"  Preço: R$ {tenis['preco']:.2f}")
    print(f"  Tamanho: {tenis['tamanho']}")
    print(f"  Cor: {tenis['cor']}")

print(f"\n💡 GUARDE BEM ISSO:")
print(f"   - Lista de dicionários = estrutura perfeita para dados tabulares")
print(f"   - Cada dicionário = uma linha (registro)")
print(f"   - Cada chave = uma coluna (atributo)")
print(f"   - Pandas converte isso facilmente em DataFrame!")

