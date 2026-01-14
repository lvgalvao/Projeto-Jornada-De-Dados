{{
    config(
        materialized='table',
        schema='silver',
        tags=['silver', 'cleaned', 'produtos']
    )
}}

-- ============================================
-- CAMADA SILVER: Produtos (Dados Limpos)
-- ============================================
-- Conceito: Segunda camada da arquitetura Medalhão
-- Objetivo: Limpar, padronizar e enriquecer dados
-- 
-- Nesta camada:
-- - Remove duplicatas
-- - Padroniza formatos (texto, datas, números)
-- - Trata valores nulos
-- - Adiciona colunas calculadas básicas
-- - Valida integridade dos dados

SELECT
    id_produto,
    UPPER(TRIM(nome_produto)) AS nome_produto,
    UPPER(TRIM(categoria)) AS categoria,
    UPPER(TRIM(marca)) AS marca,
    preco_atual,
    data_criacao,
    -- Colunas calculadas
    CASE 
        WHEN preco_atual > 1000 THEN 'PREMIUM'
        WHEN preco_atual > 500 THEN 'MEDIO'
        ELSE 'BASICO'
    END AS faixa_preco,
    -- Validações
    CASE 
        WHEN preco_atual < 0 THEN TRUE
        ELSE FALSE
    END AS flag_preco_invalido
FROM {{ ref('bronze_produtos') }}
WHERE nome_produto IS NOT NULL
  AND categoria IS NOT NULL

