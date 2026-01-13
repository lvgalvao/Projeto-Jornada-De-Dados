"""
============================================
EXEMPLO 2: Salvar Dados no Banco de Dados PostgreSQL
============================================
Conceito: Salvar dados processados no PostgreSQL usando pandas
Pergunta: Como salvar dados processados em um banco PostgreSQL?

NESTE EXEMPLO VOCÊ APRENDE:
- Como conectar com PostgreSQL usando pandas
- Como salvar DataFrame em tabela SQL
- Por que pandas serve para ler, processar E salvar dados
"""

import pandas as pd
from sqlalchemy import create_engine

# Instalar: pip install sqlalchemy psycopg2-binary

# Configurações do PostgreSQL (Supabase)
# Usar postgresql+psycopg2:// ao invés de postgresql://
DATABASE_URL = "postgresql+psycopg2://xxxx"

# Criar engine de conexão
engine = create_engine(DATABASE_URL)

# Exemplo: Dados processados do exemplo anterior (DataLake)
# Continuando do exemplo 01, vamos salvar os dados processados no banco
# Simulando dados processados (em produção viriam do exemplo 01)
dados_processados = {
    "id_produto": ["prd_001", "prd_002", "prd_003"],
    "nome_produto": ["Tênis Nike Air Max", "Tênis Adidas Ultraboost", "Tênis Puma RS-X"],
    "preco_medio": [550.00, 650.00, 400.00],
    "total_concorrentes": [4, 3, 2]
}

df_processado = pd.DataFrame(dados_processados)

# Salvar DataFrame em tabela PostgreSQL
# if_exists: 'replace' (substitui), 'append' (adiciona), 'fail' (erro se existir)
df_processado.to_sql(
    "precos_processados",  # Nome da tabela
    engine,  # Engine de conexão
    if_exists="replace",  # Substituir se existir
    index=False  # Não salvar índice
)

# Ler dados salvos para verificar
df_verificacao = pd.read_sql_query("SELECT * FROM precos_processados", engine)

# ============================================
# OUTRAS OPERAÇÕES COM PANDAS E SQL
# ============================================

# Ler dados de uma tabela existente
df_produtos = pd.read_sql_query("SELECT * FROM produtos LIMIT 10", engine)

# Executar query complexa e trazer para pandas
query = """
SELECT 
    nome_concorrente,
    COUNT(*) as total_produtos,
    AVG(preco_concorrente) as preco_medio
FROM precos_processados
GROUP BY nome_concorrente
"""
df_agregado = pd.read_sql_query(query, engine)

# Salvar resultado de query em nova tabela
df_agregado.to_sql("resumo_precos", engine, if_exists="replace", index=False)

# Atualizar tabela existente (append)
novos_dados = pd.DataFrame({
    "id_produto": ["prd_004"],
    "nome_produto": ["Tênis Vans Old Skool"],
    "preco_medio": [350.00],
    "total_concorrentes": [2]
})
novos_dados.to_sql("precos_processados", engine, if_exists="append", index=False)

# Fechar conexão
engine.dispose()
