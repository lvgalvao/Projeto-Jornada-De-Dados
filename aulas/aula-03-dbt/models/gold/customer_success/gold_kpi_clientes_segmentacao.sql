{{
    config(
        materialized='table',
        schema='gold',
        tags=['gold', 'kpi', 'clientes', 'segmentacao']
    )
}}

-- ============================================
-- CAMADA GOLD: KPI - Segmentação de Clientes
-- ============================================
-- Conceito: Terceira camada da arquitetura Medalhão
-- Objetivo: Criar segmentação de clientes baseada em receita
-- 
-- Segmentação:
-- - VIP: Receita >= R$ 10.000
-- - TOP_TIER: Receita >= R$ 5.000 e < R$ 10.000
-- - REGULAR: Receita < R$ 5.000

WITH receita_por_cliente AS (
    SELECT
        id_cliente,
        nome_cliente,
        estado,
        SUM(receita_total) AS receita_total,
        COUNT(DISTINCT venda_id) AS total_compras,
        AVG(receita_total) AS ticket_medio,
        MIN(data_venda_date) AS primeira_compra,
        MAX(data_venda_date) AS ultima_compra
    FROM {{ ref('silver_vendas_enriquecidas') }}
    GROUP BY 1, 2, 3
)

SELECT
    id_cliente AS cliente_id,
    nome_cliente,
    estado,
    receita_total,
    total_compras,
    ticket_medio,
    primeira_compra,
    ultima_compra,
    -- Segmentação usando CASE WHEN
    CASE 
        WHEN receita_total >= {{ var('segmentacao_vip_threshold', 10000) }} THEN 'VIP'
        WHEN receita_total >= {{ var('segmentacao_top_tier_threshold', 5000) }} THEN 'TOP_TIER'
        ELSE 'REGULAR'
    END AS segmento_cliente,
    -- Ranking
    ROW_NUMBER() OVER (ORDER BY receita_total DESC) AS ranking_receita
FROM receita_por_cliente
ORDER BY receita_total DESC

