-- ============================================
-- EXEMPLO 8: GROUP BY com JOIN
-- ============================================
-- Conceito: Agrupar dados de tabelas juntadas
--
-- COMO FUNCIONA:
-- 1. Fazemos JOIN para juntar vendas com produtos
-- 2. Agrupamos por categoria (GROUP BY)
-- 3. Calculamos métricas para cada grupo
--
-- IMPORTANTE:
-- - Todas as colunas no SELECT devem estar no GROUP BY ou serem funções de agregação
-- - GROUP BY sempre vem depois do JOIN e antes do ORDER BY

-- ============================================
-- EXEMPLO 8A: Primeiro passo - Categoria e Total de Vendas
-- ============================================
-- Pergunta: Quantas vendas foram feitas por categoria?

SELECT 
    p.categoria,
    COUNT(*) AS total_vendas
FROM 
    vendas v
    INNER JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY 
    p.categoria
ORDER BY 
    total_vendas DESC;

-- ============================================
-- EXEMPLO 8B: Adicionando Receita Total
-- ============================================
-- Pergunta: Qual é a receita total por categoria?

SELECT 
    p.categoria,
    COUNT(*) AS total_vendas,
    SUM(v.quantidade * v.preco_unitario) AS receita_total
FROM 
    vendas v
    INNER JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY 
    p.categoria
ORDER BY 
    receita_total DESC;

-- ============================================
-- EXEMPLO 8C: Análise Completa por Categoria
-- ============================================
-- Pergunta: Qual é a receita total, preço médio e total de vendas por categoria?

SELECT 
    p.categoria,
    COUNT(*) AS total_vendas,
    SUM(v.quantidade * v.preco_unitario) AS receita_total,
    AVG(v.preco_unitario) AS preco_medio
FROM 
    vendas v
    INNER JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY 
    p.categoria
ORDER BY 
    receita_total DESC;

