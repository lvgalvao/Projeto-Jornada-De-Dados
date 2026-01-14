{{
    config(
        materialized='table',
        schema='silver',
        tags=['silver', 'enriched', 'vendas']
    )
}}

-- ============================================
-- CAMADA SILVER: Vendas Enriquecidas (JOIN com dimensões)
-- ============================================
-- Conceito: Segunda camada da arquitetura Medalhão
-- Objetivo: Enriquecer vendas com dados de produtos e clientes
-- 
-- Este modelo combina dados de múltiplas fontes (vendas, produtos, clientes)
-- para criar uma visão completa e pronta para análise

SELECT
    v.id AS venda_id,
    v.cliente_id,
    v.produto_id,
    v.quantidade,
    v.preco_unitario,
    v.receita_total,
    v.data_venda,
    v.canal_venda,
    v.ano_venda,
    v.mes_venda,
    v.dia_venda,
    v.dia_semana,
    v.hora_venda,
    -- Dados do produto
    p.nome_produto,
    p.categoria,
    p.marca,
    p.preco_atual AS preco_atual_produto,
    p.faixa_preco,
    -- Dados do cliente
    c.nome_cliente,
    c.cidade,
    c.estado
FROM {{ ref('silver_vendas') }} v
LEFT JOIN {{ ref('silver_produtos') }} p
    ON v.produto_id = p.id
LEFT JOIN {{ ref('silver_clientes') }} c
    ON v.cliente_id = c.id
WHERE v.flag_quantidade_invalida = FALSE
  AND v.flag_preco_invalido = FALSE

