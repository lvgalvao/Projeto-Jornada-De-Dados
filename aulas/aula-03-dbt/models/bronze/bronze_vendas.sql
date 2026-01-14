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
    id_venda,
    data_venda,
    id_cliente,
    id_produto,
    canal_venda,
    quantidade,
    preco_unitario
FROM {{ source('raw', 'vendas') }}

