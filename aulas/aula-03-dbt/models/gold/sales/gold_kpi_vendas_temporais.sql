{{
    config(
        materialized='table',
        schema='gold',
        tags=['gold', 'kpi', 'vendas', 'temporal']
    )
}}

-- ============================================
-- CAMADA GOLD: KPI - Vendas Temporais
-- ============================================
-- Conceito: Terceira camada da arquitetura Medalhão
-- Objetivo: Criar métricas de negócio prontas para análise

SELECT
    data_venda_date AS data_venda,
    ano_venda,
    mes_venda,
    dia_venda,
    CASE dia_semana
        WHEN 0 THEN 'Domingo'
        WHEN 1 THEN 'Segunda'
        WHEN 2 THEN 'Terça'
        WHEN 3 THEN 'Quarta'
        WHEN 4 THEN 'Quinta'
        WHEN 5 THEN 'Sexta'
        WHEN 6 THEN 'Sábado'
    END AS dia_semana_nome,
    hora_venda,
    SUM(receita_total) AS receita_total,
    SUM(quantidade) AS quantidade_total,
    COUNT(DISTINCT venda_id) AS total_vendas,
    COUNT(DISTINCT id_cliente) AS total_clientes_unicos,
    AVG(receita_total) AS ticket_medio
FROM {{ ref('silver_vendas_enriquecidas') }}
GROUP BY 1, 2, 3, 4, 5, 6
ORDER BY data_venda DESC, hora_venda

