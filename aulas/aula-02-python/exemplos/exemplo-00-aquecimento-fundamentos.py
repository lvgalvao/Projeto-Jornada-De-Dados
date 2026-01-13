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
com APIs, web scraping e processamento de dados
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
nome_produto = "Smartphone Galaxy A54"
categoria = 'Eletrônicos'  # Aspas simples ou duplas funcionam
print(f"Produto: {nome_produto}, Tipo: {type(nome_produto)}")

# Int (int) - Números Inteiros
quantidade = 10
total_produtos = 200
soma = quantidade + 5
multiplicacao = quantidade * 3
print(f"Quantidade: {quantidade}, Soma: {soma}, Multiplicação: {multiplicacao}")

# Float (float) - Números Decimais
preco = 1299.90
desconto = 0.15  # 15%
preco_final = preco * (1 - desconto)
print(f"Preço: R$ {preco}, Preço final: R$ {preco_final:.2f}")


# ============================================
# 3. ESTRUTURAS DE DADOS
# ============================================

# Lista (list) - Coleção Ordenada
produtos = ["Smartphone", "Notebook", "Tablet"]
precos = [1299.90, 3499.90, 899.90]
print(f"Primeiro produto: {produtos[0]}, Último: {produtos[-1]}")

# Adicionar elemento
produtos.append("Fone Bluetooth")
print(f"Produtos: {produtos}")

# Dicionário (dict) - Pares Chave-Valor
produto = {
    "nome": "Smartphone Galaxy A54",
    "categoria": "Eletrônicos",
    "preco": 1299.90,
    "quantidade": 10
}
print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']}")

# Usar get() (mais seguro - retorna None se chave não existir)
print(f"Marca: {produto.get('marca', 'Não informada')}")

# Dicionários aninhados (muito comum em APIs!)
produto_completo = {
    "id": "prd_001",
    "dados": {
        "nome": "Smartphone Galaxy A54",
        "preco": 1299.90
    },
    "estoque": {
        "quantidade": 10,
        "localizacao": "Armazém SP"
    }
}
print(f"Nome (aninhado): {produto_completo['dados']['nome']}")


# ============================================
# 4. MÉTODOS ÚTEIS
# ============================================

# Métodos de string
texto = "  Smartphone Galaxy A54  "
print(f"Original: '{texto}'")
print(f"Maiúsculas: {texto.upper()}")
print(f"Sem espaços: '{texto.strip()}'")

# Métodos de lista
numeros = [10, 5, 20, 15]
print(f"Maior: {max(numeros)}, Menor: {min(numeros)}, Soma: {sum(numeros)}")

# Métodos de dicionário
print(f"Chaves: {list(produto.keys())}")
print(f"Valores: {list(produto.values())}")


# ============================================
# 5. EXEMPLO PRÁTICO: PROCESSAR DADOS DE API
# ============================================

# Simulando dados de uma API (vem como JSON = dicionário Python)
dados_api = {
    "produto": {
        "nome": "Smartphone Galaxy A54",
        "preco": "1299.90",  # Vem como string da API!
        "categoria": "Eletrônicos"
    }
}

# Precisamos converter e processar
nome = dados_api["produto"]["nome"]
preco_str = dados_api["produto"]["preco"]
preco_float = float(preco_str)  # Converter string para float

print(f"\nProduto da API: {nome}")
print(f"Preço formatado: R$ {preco_float:,.2f}")

