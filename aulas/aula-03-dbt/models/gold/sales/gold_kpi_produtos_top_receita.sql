{{
    config(
        materialized='table',
        schema='gold',
        tags=['gold', 'kpi', 'produtos', 'receita']
    )
}}

-- ============================================
-- CAMADA GOLD: KPI - Top Produtos por Receita
-- ============================================
-- Conceito: Terceira camada da arquitetura Medalhão
-- Objetivo: Criar métricas de negócio prontas para análise
-- 
-- Nesta camada:
-- - KPIs e métricas de negócio
-- - Agregações complexas
-- - Rankings e segmentações
-- - Dados prontos para dashboards

WITH vendas_por_produto AS (
    SELECT
        id_produto,
        nome_produto,
        categoria,
        marca,
        SUM(receita_total) AS receita_total,
        SUM(quantidade) AS quantidade_total,
        COUNT(DISTINCT venda_id) AS total_vendas,
        AVG(preco_unitario) AS preco_medio_vendido,
        AVG(receita_total) AS ticket_medio
    FROM {{ ref('silver_vendas_enriquecidas') }}
    GROUP BY 1, 2, 3, 4
)

SELECT
    id_produto AS produto_id,
    nome_produto,
    categoria,
    marca,
    receita_total,
    quantidade_total,
    total_vendas,
    preco_medio_vendido,
    ticket_medio,
    -- Ranking
    ROW_NUMBER() OVER (ORDER BY receita_total DESC) AS ranking_receita,
    ROW_NUMBER() OVER (PARTITION BY categoria ORDER BY receita_total DESC) AS ranking_receita_categoria
FROM vendas_por_produto
ORDER BY receita_total DESC
LIMIT {{ var('top_n_produtos', 10) }}

