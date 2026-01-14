{{
    config(
        materialized='table',
        schema='gold',
        tags=['gold', 'kpi', 'produtos', 'precos', 'criticos']
    )
}}

-- ============================================
-- CAMADA GOLD: KPI - Produtos Críticos (Preço)
-- ============================================
-- Conceito: Terceira camada da arquitetura Medalhão
-- Objetivo: Identificar produtos que precisam de ajuste de preço urgente
-- 
-- Produtos críticos:
-- - Top sellers que estão mais caros que o mercado
-- - Produtos com maior diferença de preço vs concorrente mais barato

WITH produtos_top_sellers AS (
    SELECT
        produto_id,
        receita_total,
        quantidade_total
    FROM {{ ref('gold_kpi_produtos_top_receita') }}
    LIMIT {{ var('top_n_produtos', 10) }}
)

SELECT
    pc.produto_id,
    pc.nome_produto,
    pc.categoria,
    pc.marca,
    pc.nosso_preco,
    pc.preco_minimo_concorrentes,
    pc.diferenca_percentual_vs_minimo,
    pc.classificacao_preco,
    pts.receita_total,
    pts.quantidade_total,
    -- Flag de criticidade
    CASE 
        WHEN pc.classificacao_preco IN ('MAIS_CARO_QUE_TODOS', 'ACIMA_DA_MEDIA')
             AND pts.receita_total > 0 THEN TRUE
        ELSE FALSE
    END AS flag_produto_critico
FROM {{ ref('gold_kpi_precos_competitividade') }} pc
INNER JOIN produtos_top_sellers pts
    ON pc.produto_id = pts.produto_id
WHERE pc.classificacao_preco IN ('MAIS_CARO_QUE_TODOS', 'ACIMA_DA_MEDIA')
ORDER BY pc.diferenca_percentual_vs_minimo DESC

