{{
    config(
        materialized='table',
        schema='gold',
        tags=['gold', 'kpi', 'produtos', 'quantidade']
    )
}}

-- ============================================
-- CAMADA GOLD: KPI - Top Produtos por Quantidade
-- ============================================
-- Conceito: Terceira camada da arquitetura Medalhão
-- Objetivo: Criar métricas de negócio prontas para análise

WITH vendas_por_produto AS (
    SELECT
        id_produto,
        nome_produto,
        categoria,
        marca,
        SUM(quantidade) AS quantidade_total,
        SUM(receita_total) AS receita_total,
        COUNT(DISTINCT venda_id) AS total_vendas
    FROM {{ ref('silver_vendas_enriquecidas') }}
    GROUP BY 1, 2, 3, 4
)

SELECT
    id_produto AS produto_id,
    nome_produto,
    categoria,
    marca,
    quantidade_total,
    receita_total,
    total_vendas,
    -- Ranking
    ROW_NUMBER() OVER (ORDER BY quantidade_total DESC) AS ranking_quantidade
FROM vendas_por_produto
ORDER BY quantidade_total DESC
LIMIT {{ var('top_n_produtos', 10) }}

