{{
    config(
        materialized='table',
        schema='silver',
        tags=['silver', 'cleaned', 'vendas']
    )
}}

-- ============================================
-- CAMADA SILVER: Vendas (Dados Limpos e Enriquecidos)
-- ============================================
-- Conceito: Segunda camada da arquitetura Medalhão
-- Objetivo: Limpar, padronizar e enriquecer dados

SELECT
    v.id,
    v.cliente_id,
    v.produto_id,
    v.quantidade,
    v.preco_unitario,
    v.data_venda,
    UPPER(TRIM(v.canal_venda)) AS canal_venda,
    -- Colunas calculadas
    v.quantidade * v.preco_unitario AS receita_total,
    -- Dimensões temporais
    DATE(v.data_venda) AS data_venda_date,
    EXTRACT(YEAR FROM v.data_venda) AS ano_venda,
    EXTRACT(MONTH FROM v.data_venda) AS mes_venda,
    EXTRACT(DAY FROM v.data_venda) AS dia_venda,
    EXTRACT(DOW FROM v.data_venda) AS dia_semana, -- 0 = Domingo, 6 = Sábado
    EXTRACT(HOUR FROM v.data_venda) AS hora_venda,
    -- Validações
    CASE 
        WHEN v.quantidade <= 0 THEN TRUE
        ELSE FALSE
    END AS flag_quantidade_invalida,
    CASE 
        WHEN v.preco_unitario <= 0 THEN TRUE
        ELSE FALSE
    END AS flag_preco_invalido
FROM {{ ref('bronze_vendas') }} v
WHERE v.cliente_id IS NOT NULL
  AND v.produto_id IS NOT NULL
  AND v.data_venda IS NOT NULL

