{{
    config(
        materialized='view',
        schema='bronze',
        tags=['bronze', 'raw', 'produtos']
    )
}}

-- ============================================
-- CAMADA BRONZE: Produtos (Dados Brutos)
-- ============================================
-- Conceito: Primeira camada da arquitetura Medalhão
-- Objetivo: Capturar dados exatamente como vêm da fonte
-- 
-- Nesta camada:
-- - Dados são copiados sem transformação
-- - Mantém estrutura original da fonte
-- - Serve como ponto de recuperação (replay)
-- - Permite reprocessamento sem acessar fonte original

SELECT
    id,
    nome_produto,
    categoria,
    marca,
    preco_atual,
    estoque_atual,
    data_cadastro
FROM {{ source('raw', 'produtos') }}

