-- ============================================
-- EXERCÍCIO: Categorização de Clientes com CASE WHEN
-- ============================================
-- Objetivo: Praticar CASE WHEN criando categorias baseadas em comportamento de compra
--
-- CONTEXTO:
-- Você já tem a segmentação original dos clientes (VIP, TOP_TIER, REGULAR),
-- mas agora quer criar uma NOVA categorização baseada no valor real de compras (receita total).
--
-- TAREFA:
-- 1. Calcule a receita total de cada cliente (soma de todas as compras)
-- 2. Use CASE WHEN para categorizar os clientes em:
--    - "VIP": receita total >= R$ 10.000
--    - "TOP_TIER": receita total entre R$ 5.000 e R$ 9.999
--    - "REGULAR": receita total < R$ 5.000
-- 3. Mostre: nome do cliente, receita total, segmento criado
-- 4. Ordene por receita total (decrescente)
--
-- CONCEITOS USADOS:
-- - JOIN (clientes com vendas)
-- - GROUP BY (agrupar por cliente)
-- - SUM (calcular receita total)
-- - CASE WHEN (criar categorias)
--
-- DICA:
-- Lembre-se: todas as colunas no SELECT que não são funções de agregação
-- devem estar no GROUP BY.

-- ============================================
-- SOLUÇÃO
-- ============================================

SELECT 
    c.nome_cliente,
    SUM(v.quantidade * v.preco_unitario) AS receita_total,
    CASE 
        WHEN SUM(v.quantidade * v.preco_unitario) >= 10000 THEN 'VIP'
        WHEN SUM(v.quantidade * v.preco_unitario) >= 5000 THEN 'TOP_TIER'
        ELSE 'REGULAR'
    END AS segmento
FROM 
    clientes c
    INNER JOIN vendas v ON c.id_cliente = v.id_cliente
GROUP BY 
    c.id_cliente, c.nome_cliente
ORDER BY 
    receita_total DESC;

-- ============================================
-- DESAFIO EXTRA 1: Distribuição de segmentos criados
-- ============================================
-- Quantos clientes temos em cada segmento criado?
-- Qual é a receita total por segmento?

-- Dica: Use a query acima como CTE e depois agrupe

WITH clientes_categorizados AS (
    SELECT 
        c.nome_cliente,
        SUM(v.quantidade * v.preco_unitario) AS receita_total,
        CASE 
            WHEN SUM(v.quantidade * v.preco_unitario) >= 10000 THEN 'VIP'
            WHEN SUM(v.quantidade * v.preco_unitario) >= 5000 THEN 'TOP_TIER'
            ELSE 'REGULAR'
        END AS segmento
    FROM 
        clientes c
        INNER JOIN vendas v ON c.id_cliente = v.id_cliente
    GROUP BY 
        c.id_cliente, c.nome_cliente
)
SELECT 
    segmento,
    COUNT(*) AS quantidade_clientes,
    SUM(receita_total) AS receita_total_segmento,
    AVG(receita_total) AS receita_media_segmento
FROM 
    clientes_categorizados
GROUP BY 
    segmento
ORDER BY 
    receita_total_segmento DESC;

-- ============================================
-- DESAFIO EXTRA 2: Análise mais detalhada
-- ============================================
-- Mostre também:
-- - Quantidade total de compras
-- - Ticket médio (receita total / quantidade de compras)
-- - Estado do cliente

SELECT 
    c.nome_cliente,
    c.segmento AS segmento_original,
    c.estado,
    COUNT(v.id_venda) AS total_compras,
    SUM(v.quantidade * v.preco_unitario) AS receita_total,
    ROUND(
        SUM(v.quantidade * v.preco_unitario) / COUNT(v.id_venda), 
        2
    ) AS ticket_medio,
    CASE 
        WHEN SUM(v.quantidade * v.preco_unitario) >= 10000 THEN 'Alto Valor'
        WHEN SUM(v.quantidade * v.preco_unitario) >= 5000 THEN 'Médio Valor'
        ELSE 'Baixo Valor'
    END AS categoria_por_valor
FROM 
    clientes c
    INNER JOIN vendas v ON c.id_cliente = v.id_cliente
GROUP BY 
    c.id_cliente, c.nome_cliente, c.segmento, c.estado
ORDER BY 
    receita_total DESC;

