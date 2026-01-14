{{
    config(
        materialized='table',
        schema='gold',
        tags=['gold', 'kpi', 'clientes', 'top']
    )
}}

-- ============================================
-- CAMADA GOLD: KPI - Top Clientes por Receita
-- ============================================
-- Conceito: Terceira camada da arquitetura Medalhão
-- Objetivo: Criar métricas de negócio prontas para análise

SELECT
    cliente_id,
    nome_cliente,
    estado,
    receita_total,
    total_compras,
    ticket_medio,
    segmento_cliente,
    ranking_receita
FROM {{ ref('gold_kpi_clientes_segmentacao') }}
ORDER BY receita_total DESC
LIMIT {{ var('top_n_clientes', 10) }}

