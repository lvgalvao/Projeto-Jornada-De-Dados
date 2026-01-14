{{
    config(
        materialized='view',
        schema='bronze',
        tags=['bronze', 'raw', 'precos', 'competidores']
    )
}}

-- ============================================
-- CAMADA BRONZE: Preços de Concorrentes (Dados Brutos)
-- ============================================
-- Conceito: Primeira camada da arquitetura Medalhão
-- Objetivo: Capturar dados exatamente como vêm da fonte

SELECT
    id_produto,
    nome_concorrente,
    preco_concorrente,
    data_coleta
FROM {{ source('raw', 'preco_competidores') }}

