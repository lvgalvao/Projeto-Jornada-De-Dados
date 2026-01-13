"""
============================================
AQUECIMENTO: Fundamentos de Python
============================================
Conceito: Revisar conceitos fundamentais antes de trabalhar com dados
Pergunta: Por que preciso saber Python básico para trabalhar com dados?

NESTE EXEMPLO VOCÊ APRENDE:
- Print e Hello World
- Variáveis e tipos básicos (str, int, float)
- Estruturas de dados (lista, dicionário)
- Métodos úteis
- Por que isso é importante para trabalhar com dados

CASO DE NEGÓCIO:
Entender os fundamentos de Python é essencial antes de trabalhar
com APIs, arquivos externos e processamento de dados
"""

# ============================================
# 1. PRINT - Hello World!
# ============================================

# Print simples
print("Hello World!")

# Print com variáveis
nome = "Jornada de Dados"
print("Olá,", nome)

# Print com formatação (f-strings) - RECOMENDADO!
idade = 2024
print(f"Ano: {idade}")
print(f"Bem-vindo ao {nome} em {idade}!")


# ============================================
# 2. VARIÁVEIS - Tipos Básicos
# ============================================

# String (str) - Texto
nome_produto = "Tênis Nike Air Max"
categoria = 'Tênis'  # Aspas simples ou duplas funcionam
print(f"Produto: {nome_produto}, Tipo: {type(nome_produto)}")

# Int (int) - Números Inteiros
quantidade = 10
total_produtos = 200
soma = quantidade + 5
multiplicacao = quantidade * 3
print(f"Quantidade: {quantidade}, Soma: {soma}, Multiplicação: {multiplicacao}")


# ============================================
# 3. ESTRUTURAS DE DADOS
# ============================================

# Lista (list) - Coleção Ordenada
# Lista de tênis
tenis = ["Tênis Nike Air Max", "Tênis Adidas Ultraboost", "Tênis Puma RS-X"]
precos = [599.90, 699.90, 449.90]
print(f"Primeiro tênis: {tenis[0]}, Último: {tenis[-1]}")

# Adicionar elemento
tenis.append("Tênis Vans Old Skool")
print(f"Tênis: {tenis}")

# Dicionário (dict) - Pares Chave-Valor
# GUARDE BEM ISSO: Dicionários são perfeitos para armazenar conjuntos de dados!
tenis_nike = {
    "nome": "Tênis Nike Air Max",
    "marca": "Nike",
    "categoria": "Tênis",
    "preco": 599.90,
    "quantidade": 10,
    "tamanho": 42
}
print(f"Nome: {tenis_nike['nome']}, Preço: R$ {tenis_nike['preco']}")

# Usar get() (mais seguro - retorna None se chave não existir)
print(f"Cor: {tenis_nike.get('cor', 'Não informada')}")

# Dicionários aninhados (muito comum em APIs!)
# GUARDE BEM ISSO: Dicionários aninhados permitem estruturar dados complexos!
tenis_completo = {
    "id": "ten_001",
    "dados": {
        "nome": "Tênis Nike Air Max",
        "marca": "Nike",
        "preco": 599.90
    },
    "estoque": {
        "quantidade": 10,
        "localizacao": "Armazém SP",
        "tamanhos_disponiveis": [38, 39, 40, 41, 42, 43]
    }
}
print(f"Nome (aninhado): {tenis_completo['dados']['nome']}")
print(f"Tamanhos disponíveis: {tenis_completo['estoque']['tamanhos_disponiveis']}")


# ============================================
# 4. EXEMPLO PRÁTICO: PROCESSAR DADOS DE API
# ============================================

# Simulando dados de uma API (vem como JSON = dicionário Python)
# GUARDE BEM ISSO: APIs retornam dados em JSON, que são dicionários em Python!
dados_api = {
    "produto": {
        "nome": "Tênis Nike Air Max",
        "preco": "599.90",  # Vem como string da API!
        "categoria": "Tênis",
        "marca": "Nike"
    }
}

# Precisamos converter e processar
nome = dados_api["produto"]["nome"]
preco_str = dados_api["produto"]["preco"]
preco_float = float(preco_str)  # Converter string para float

print(f"\nTênis da API: {nome}")
print(f"Preço formatado: R$ {preco_float:,.2f}")


# ============================================
# 5. LISTA DE TÊNIS COM DICIONÁRIOS
# ============================================

# GUARDE BEM ISSO: Lista de dicionários é a estrutura mais comum para dados tabulares!
lista_tenis = [
    {
        "nome": "Tênis Nike Air Max",
        "marca": "Nike",
        "preco": 599.90,
        "tamanho": 42
    },
    {
        "nome": "Tênis Adidas Ultraboost",
        "marca": "Adidas",
        "preco": 699.90,
        "tamanho": 41
    },
    {
        "nome": "Tênis Puma RS-X",
        "marca": "Puma",
        "preco": 449.90,
        "tamanho": 40
    },
    {
        "nome": "Tênis Vans Old Skool",
        "marca": "Vans",
        "preco": 399.90,
        "tamanho": 39
    },
    {
        "nome": "Tênis Converse All Star",
        "marca": "Converse",
        "preco": 299.90,
        "tamanho": 38
    }
]

print(f"\nLista de {len(lista_tenis)} tênis:")
for tenis in lista_tenis:
    print(f"  - {tenis['nome']}: R$ {tenis['preco']:.2f} (Tamanho {tenis['tamanho']})")

