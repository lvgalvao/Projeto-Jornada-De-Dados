{{
    config(
        materialized='view',
        schema='bronze',
        tags=['bronze', 'raw', 'vendas']
    )
}}

-- ============================================
-- CAMADA BRONZE: Vendas (Dados Brutos)
-- ============================================
-- Conceito: Primeira camada da arquitetura Medalhão
-- Objetivo: Capturar dados exatamente como vêm da fonte

SELECT
    id,
    cliente_id,
    produto_id,
    quantidade,
    preco_unitario,
    data_venda,
    canal_venda
FROM {{ source('raw', 'vendas') }}

