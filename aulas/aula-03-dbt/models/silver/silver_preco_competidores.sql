{{
    config(
        materialized='table',
        schema='silver',
        tags=['silver', 'cleaned', 'precos', 'competidores']
    )
}}

-- ============================================
-- CAMADA SILVER: Preços de Concorrentes (Dados Limpos)
-- ============================================
-- Conceito: Segunda camada da arquitetura Medalhão
-- Objetivo: Limpar, padronizar e enriquecer dados

SELECT
    id_produto,
    UPPER(TRIM(nome_concorrente)) AS nome_concorrente,
    preco_concorrente,
    data_coleta,
    DATE(data_coleta::timestamp) AS data_coleta_date,
    -- Validações
    CASE 
        WHEN preco_concorrente <= 0 THEN TRUE
        ELSE FALSE
    END AS flag_preco_invalido
FROM {{ ref('bronze_preco_competidores') }}
WHERE id_produto IS NOT NULL
  AND nome_concorrente IS NOT NULL
  AND data_coleta IS NOT NULL

