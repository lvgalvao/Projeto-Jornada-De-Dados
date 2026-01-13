"""
============================================
EXEMPLO 5: Ler Dados de Banco de Dados
============================================
Conceito: Conectar Python com bancos de dados SQL
Pergunta: Como ler dados diretamente de um banco SQL em Python?

NESTE EXEMPLO VOCÊ APRENDE:
- Como conectar Python com SQLite
- Como conectar Python com PostgreSQL
- Como executar queries SQL e trazer para pandas
- Como trabalhar com diferentes tipos de banco

CASO DE NEGÓCIO:
Ler dados diretamente do banco de dados ao invés de CSVs,
permitindo queries mais complexas e dados atualizados
"""

import pandas as pd
import sqlite3
from typing import Optional
import os

# ============================================
# EXEMPLO 1: SQLite (banco local)
# ============================================
print("=" * 50)
print("EXEMPLO 1: Conectar com SQLite")
print("=" * 50)

def ler_sqlite(query: str, db_path: str) -> pd.DataFrame:
    """
    Executa query SQL em banco SQLite e retorna DataFrame
    
    Args:
        query: Query SQL a ser executada
        db_path: Caminho do arquivo .db
        
    Returns:
        DataFrame com resultados da query
    """
    try:
        # Conectar ao banco
        conn = sqlite3.connect(db_path)
        
        # Executar query e trazer para pandas
        df = pd.read_sql_query(query, conn)
        
        # Fechar conexão
        conn.close()
        
        return df
    
    except Exception as e:
        print(f"❌ Erro ao ler banco: {e}")
        return pd.DataFrame()


# Exemplo: Criar banco SQLite a partir dos CSVs (se não existir)
db_path = "../../data/ecommerce.db"

if not os.path.exists(db_path):
    print("📝 Criando banco SQLite a partir dos CSVs...")
    
    conn = sqlite3.connect(db_path)
    
    # Ler CSVs e salvar como tabelas
    df_produtos = pd.read_csv("../../data/produtos.csv")
    df_clientes = pd.read_csv("../../data/clientes.csv")
    df_vendas = pd.read_csv("../../data/vendas.csv")
    
    df_produtos.to_sql("produtos", conn, if_exists="replace", index=False)
    df_clientes.to_sql("clientes", conn, if_exists="replace", index=False)
    df_vendas.to_sql("vendas", conn, if_exists="replace", index=False)
    
    conn.close()
    print("✅ Banco criado com sucesso!")

# Agora ler dados do banco
query_produtos = "SELECT * FROM produtos LIMIT 5"
df_produtos_db = ler_sqlite(query_produtos, db_path)

print(f"\n✅ {len(df_produtos_db)} produtos carregados do banco")
print(df_produtos_db[["nome_produto", "categoria", "preco_atual"]].head())


# Query mais complexa: Vendas com produtos
print("\n" + "=" * 50)
print("EXEMPLO 2: Query com JOIN")
print("=" * 50)

query_join = """
SELECT 
    v.id_venda,
    p.nome_produto,
    p.categoria,
    v.quantidade,
    v.preco_unitario,
    (v.quantidade * v.preco_unitario) AS receita
FROM vendas v
INNER JOIN produtos p ON v.id_produto = p.id_produto
LIMIT 10
"""

df_vendas_produtos = ler_sqlite(query_join, db_path)
print(f"✅ {len(df_vendas_produtos)} vendas com produtos")
print(df_vendas_produtos.head())


# ============================================
# EXEMPLO 3: PostgreSQL (banco remoto)
# ============================================
print("\n" + "=" * 50)
print("EXEMPLO 3: Conectar com PostgreSQL")
print("=" * 50)

def ler_postgresql(query: str, connection_string: str) -> pd.DataFrame:
    """
    Executa query SQL em PostgreSQL e retorna DataFrame
    
    Args:
        query: Query SQL a ser executada
        connection_string: String de conexão PostgreSQL
                          Ex: "postgresql://user:pass@host:port/dbname"
        
    Returns:
        DataFrame com resultados da query
    """
    try:
        # Usar sqlalchemy para conexão
        from sqlalchemy import create_engine
        
        engine = create_engine(connection_string)
        df = pd.read_sql_query(query, engine)
        engine.dispose()
        
        return df
    
    except ImportError:
        print("⚠️ sqlalchemy não instalado. Instale com: pip install sqlalchemy psycopg2")
        return pd.DataFrame()
    except Exception as e:
        print(f"❌ Erro ao conectar PostgreSQL: {e}")
        return pd.DataFrame()


# Exemplo de uso (comentado pois precisa de banco real)
print("💡 Exemplo de código para PostgreSQL:")
print("""
# String de conexão
conn_string = "postgresql://usuario:senha@localhost:5432/ecommerce"

# Query
query = "SELECT * FROM produtos LIMIT 10"

# Ler dados
df = ler_postgresql(query, conn_string)
""")


print("\n" + "=" * 50)
print("📚 RESUMO:")
print("=" * 50)
print("✅ SQLite: Banco local, arquivo .db")
print("✅ PostgreSQL: Banco remoto, precisa de conexão")
print("✅ pandas.read_sql_query(): Executa SQL e retorna DataFrame")
print("✅ Sempre feche conexões após uso")

