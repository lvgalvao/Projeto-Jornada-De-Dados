{{
    config(
        materialized='table',
        schema='gold',
        tags=['gold', 'kpi', 'receita', 'marca']
    )
}}

-- ============================================
-- CAMADA GOLD: KPI - Receita por Marca
-- ============================================
-- Conceito: Terceira camada da arquitetura Medalhão
-- Objetivo: Criar métricas de negócio prontas para análise

SELECT
    marca,
    SUM(receita_total) AS receita_total,
    SUM(quantidade) AS quantidade_total,
    COUNT(DISTINCT venda_id) AS total_vendas,
    COUNT(DISTINCT id_produto) AS total_produtos,
    AVG(receita_total) AS ticket_medio,
    -- Percentual da receita total
    SUM(receita_total) * 100.0 / SUM(SUM(receita_total)) OVER () AS percentual_receita
FROM {{ ref('silver_vendas_enriquecidas') }}
GROUP BY marca
ORDER BY receita_total DESC

