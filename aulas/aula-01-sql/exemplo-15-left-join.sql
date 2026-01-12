-- ============================================
-- EXEMPLO 15: LEFT JOIN
-- ============================================
-- Conceito: Incluir todos os registros da tabela da esquerda, mesmo sem match
--
-- COMO FUNCIONA:
-- - LEFT JOIN retorna TODOS os registros da tabela da esquerda (produtos)
-- - Adiciona dados da tabela da direita (vendas) quando há correspondência
-- - Se não houver match, os valores da direita são NULL
--
-- DIFERENÇA DO INNER JOIN:
-- - INNER JOIN: só retorna produtos que têm vendas
-- - LEFT JOIN: retorna TODOS os produtos, mesmo sem vendas
--
-- CASO DE NEGÓCIO:
-- Identificar produtos cadastrados que nunca geraram venda
-- Isso ajuda a identificar itens que precisam de atenção em marketing

-- ============================================
-- EXEMPLO 15A: Ver todos os produtos com suas vendas (ou NULL)
-- ============================================
-- Pergunta: Quais produtos temos e quantas vendas cada um teve?

SELECT 
    p.id_produto,
    p.nome_produto,
    p.categoria,
    p.preco_atual,
    COUNT(v.id_venda) AS total_vendas
FROM 
    produtos p
    LEFT JOIN vendas v ON p.id_produto = v.id_produto
GROUP BY 
    p.id_produto, p.nome_produto, p.categoria, p.preco_atual
ORDER BY 
    total_vendas ASC, p.preco_atual DESC;

-- ============================================
-- EXEMPLO 15B: Produtos que NUNCA foram vendidos
-- ============================================
-- Pergunta: Quais produtos nunca foram vendidos?

SELECT 
    p.id_produto,
    p.nome_produto,
    p.categoria,
    p.preco_atual,
    COUNT(v.id_venda) AS total_vendas
FROM 
    produtos p
    LEFT JOIN vendas v ON p.id_produto = v.id_produto
GROUP BY 
    p.id_produto, p.nome_produto, p.categoria, p.preco_atual
HAVING 
    COUNT(v.id_venda) = 0
ORDER BY 
    p.preco_atual DESC;

