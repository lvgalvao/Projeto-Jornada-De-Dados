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
    id,
    nome_cliente,
    email,
    telefone,
    cidade,
    estado,
    data_cadastro
FROM {{ source('raw', 'clientes') }}

