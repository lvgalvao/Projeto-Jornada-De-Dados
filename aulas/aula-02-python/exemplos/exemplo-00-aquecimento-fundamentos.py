"""
============================================
AQUECIMENTO: Fundamentos de Python
============================================
Conceito: Revisar conceitos fundamentais antes de trabalhar com dados
Pergunta: Por que preciso saber Python básico para trabalhar com dados?
"""

# Print simples
print("Hello World!")

# Print com variáveis
nome = "Jornada de Dados"
print(f"Olá, {nome}")

# Variáveis - String (str)
nome_produto = "Tênis Nike Air Max"
categoria = 'Tênis'

# Variáveis - Int (int)
quantidade = 10
total_produtos = 200

# Lista (list) - Coleção Ordenada
tenis = ["Tênis Nike Air Max", "Tênis Adidas Ultraboost", "Tênis Puma RS-X"]
precos = [599.90, 699.90, 449.90]

# Dicionário (dict) - Pares Chave-Valor
# GUARDE BEM ISSO: Dicionários são perfeitos para armazenar conjuntos de dados!
tenis_nike = {
    "nome": "Tênis Nike Air Max",
    "marca": "Nike",
    "categoria": "Tênis",
    "preco": 599.90,
    "quantidade": 10
}

# Lista de dicionários - Estrutura mais comum para dados tabulares!
lista_tenis = [
    {"nome": "Tênis Nike Air Max", "marca": "Nike", "preco": 599.90},
    {"nome": "Tênis Adidas Ultraboost", "marca": "Adidas", "preco": 699.90},
    {"nome": "Tênis Puma RS-X", "marca": "Puma", "preco": 449.90},
    {"nome": "Tênis Vans Old Skool", "marca": "Vans", "preco": 399.90},
    {"nome": "Tênis Converse Chuck", "marca": "Converse", "preco": 349.90}
]

# Simulando dados de uma API (vem como JSON = dicionário Python)
# GUARDE BEM ISSO: APIs retornam dados em JSON, que são dicionários em Python!
dados_api = {
    "produto": {
        "nome": "Tênis Nike Air Max",
        "preco": "599.90",  # Vem como string da API!
        "categoria": "Tênis"
    }
}

# Processar dados da API
nome = dados_api["produto"]["nome"]
preco_str = dados_api["produto"]["preco"]
preco_float = float(preco_str)  # Converter string para float
