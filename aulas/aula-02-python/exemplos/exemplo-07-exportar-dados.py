"""
============================================
EXEMPLO 7: Exportar Dados para Diferentes Formatos
============================================
Conceito: Salvar dados processados em diferentes formatos
Pergunta: Como exportar dados para CSV, JSON, Excel, etc?

NESTE EXEMPLO VOCÊ APRENDE:
- Como exportar para CSV
- Como exportar para JSON
- Como exportar para Excel
- Como exportar para banco de dados
- Como escolher o formato adequado

CASO DE NEGÓCIO:
Salvar dados processados em formatos que outros sistemas
ou pessoas possam consumir facilmente
"""

import pandas as pd
import os

# Carregar e processar dados
df_vendas = pd.read_csv("../../data/vendas.csv")
df_produtos = pd.read_csv("../../data/produtos.csv")

# Fazer merge para criar dataset processado
df_completo = df_vendas.merge(
    df_produtos,
    on="id_produto",
    how="inner"
)

# Adicionar coluna calculada
df_completo['receita'] = df_completo['quantidade'] * df_completo['preco_unitario']

# Criar diretório de saída
output_dir = "../../data/processed"
os.makedirs(output_dir, exist_ok=True)

print("=" * 50)
print("EXEMPLO 1: Exportar para CSV")
print("=" * 50)

# Exportar para CSV
csv_path = os.path.join(output_dir, "vendas_processadas.csv")
df_completo.to_csv(csv_path, index=False, encoding='utf-8')
print(f"✅ Dados exportados para: {csv_path}")
print(f"   Linhas: {len(df_completo)}")
print(f"   Colunas: {len(df_completo.columns)}")


print("\n" + "=" * 50)
print("EXEMPLO 2: Exportar para JSON")
print("=" * 50)

# Exportar para JSON
json_path = os.path.join(output_dir, "vendas_processadas.json")

# Opção 1: JSON orientado por registros (mais comum para APIs)
df_completo.to_json(json_path, orient='records', indent=2, force_ascii=False)
print(f"✅ Dados exportados para JSON: {json_path}")

# Opção 2: JSON orientado por índices
json_index_path = os.path.join(output_dir, "vendas_processadas_index.json")
df_completo.to_json(json_index_path, orient='index', indent=2, force_ascii=False)
print(f"✅ Dados exportados para JSON (index): {json_index_path}")


print("\n" + "=" * 50)
print("EXEMPLO 3: Exportar para Excel")
print("=" * 50)

try:
    excel_path = os.path.join(output_dir, "vendas_processadas.xlsx")
    
    # Exportar para Excel (pode ter múltiplas abas)
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        # Aba 1: Vendas completas
        df_completo.to_excel(writer, sheet_name='Vendas', index=False)
        
        # Aba 2: Resumo por categoria
        resumo_categoria = df_completo.groupby('categoria').agg({
            'receita': 'sum',
            'quantidade': 'sum',
            'id_venda': 'count'
        }).reset_index()
        resumo_categoria.columns = ['Categoria', 'Receita Total', 'Quantidade Total', 'Total Vendas']
        resumo_categoria.to_excel(writer, sheet_name='Resumo por Categoria', index=False)
    
    print(f"✅ Dados exportados para Excel: {excel_path}")
    print(f"   Abas criadas: Vendas, Resumo por Categoria")

except ImportError:
    print("⚠️ openpyxl não instalado. Instale com: pip install openpyxl")


print("\n" + "=" * 50)
print("EXEMPLO 4: Exportar para Banco de Dados")
print("=" * 50)

try:
    import sqlite3
    
    db_path = os.path.join(output_dir, "vendas_processadas.db")
    conn = sqlite3.connect(db_path)
    
    # Exportar DataFrame para tabela SQL
    df_completo.to_sql('vendas_processadas', conn, if_exists='replace', index=False)
    
    # Exportar resumo também
    resumo_categoria.to_sql('resumo_categoria', conn, if_exists='replace', index=False)
    
    conn.close()
    print(f"✅ Dados exportados para SQLite: {db_path}")
    print(f"   Tabelas criadas: vendas_processadas, resumo_categoria")

except Exception as e:
    print(f"⚠️ Erro ao exportar para banco: {e}")


print("\n" + "=" * 50)
print("EXEMPLO 5: Exportar para Parquet (formato otimizado)")
print("=" * 50)

try:
    parquet_path = os.path.join(output_dir, "vendas_processadas.parquet")
    df_completo.to_parquet(parquet_path, index=False, compression='snappy')
    print(f"✅ Dados exportados para Parquet: {parquet_path}")
    print("   💡 Parquet é otimizado para análise de dados grandes")

except ImportError:
    print("⚠️ pyarrow não instalado. Instale com: pip install pyarrow")


print("\n" + "=" * 50)
print("📊 RESUMO DOS FORMATOS:")
print("=" * 50)
print("✅ CSV: Universal, fácil de abrir em Excel")
print("✅ JSON: Ideal para APIs e integrações")
print("✅ Excel: Bom para relatórios e apresentações")
print("✅ SQLite: Banco de dados local, permite queries")
print("✅ Parquet: Otimizado para big data, compressão eficiente")

print("\n💡 DICA: Escolha o formato baseado no uso:")
print("   - Análise: CSV, Parquet")
print("   - API/Integração: JSON")
print("   - Relatório: Excel")
print("   - Banco de dados: SQL, Parquet")

