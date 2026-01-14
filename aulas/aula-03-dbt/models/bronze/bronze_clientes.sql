{{
    config(
        materialized='view',
        schema='bronze',
        tags=['bronze', 'raw', 'clientes']
    )
}}

-- ============================================
-- CAMADA BRONZE: Clientes (Dados Brutos)
-- ============================================
-- Conceito: Primeira camada da arquitetura Medalhão
-- Objetivo: Capturar dados exatamente como vêm da fonte

SELECT
    id_cliente,
    nome_cliente,
    estado,
    pais,
    data_cadastro
FROM {{ source('raw', 'clientes') }}

