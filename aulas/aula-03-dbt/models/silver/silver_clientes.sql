{{
    config(
        materialized='table',
        schema='silver',
        tags=['silver', 'cleaned', 'clientes']
    )
}}

-- ============================================
-- CAMADA SILVER: Clientes (Dados Limpos)
-- ============================================
-- Conceito: Segunda camada da arquitetura Medalhão
-- Objetivo: Limpar, padronizar e enriquecer dados

SELECT
    id_cliente,
    UPPER(TRIM(nome_cliente)) AS nome_cliente,
    UPPER(TRIM(estado)) AS estado,
    UPPER(TRIM(pais)) AS pais,
    data_cadastro
FROM {{ ref('bronze_clientes') }}
WHERE nome_cliente IS NOT NULL

