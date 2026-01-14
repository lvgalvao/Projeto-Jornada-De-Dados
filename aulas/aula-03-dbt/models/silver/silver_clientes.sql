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
    id,
    UPPER(TRIM(nome_cliente)) AS nome_cliente,
    LOWER(TRIM(email)) AS email,
    telefone,
    UPPER(TRIM(cidade)) AS cidade,
    UPPER(TRIM(estado)) AS estado,
    data_cadastro,
    -- Validações
    CASE 
        WHEN email LIKE '%@%.%' THEN TRUE
        ELSE FALSE
    END AS flag_email_valido
FROM {{ ref('bronze_clientes') }}
WHERE nome_cliente IS NOT NULL

