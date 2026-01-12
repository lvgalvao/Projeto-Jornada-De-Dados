-- ============================================
-- EXEMPLO 14: RIGHT JOIN
-- ============================================
-- Conceito: Incluir todos os registros da tabela da direita, mesmo sem match
--
-- COMO FUNCIONA:
-- - RIGHT JOIN retorna TODOS os registros da tabela da direita (vendas)
-- - Adiciona dados da tabela da esquerda (produtos) quando há correspondência
-- - Se não houver match, os valores da esquerda são NULL
--
-- DIFERENÇA DO INNER JOIN:
-- - INNER JOIN: só retorna vendas de produtos cadastrados
-- - RIGHT JOIN: retorna TODAS as vendas, mesmo de produtos não cadastrados
--
-- CASO DE NEGÓCIO:
-- Identificar vendas de produtos que não estão cadastrados no catálogo
-- Isso indica problemas de integridade de dados ou produtos descontinuados

-- ============================================
-- EXEMPLO 14A: Ver todas as vendas com dados do produto (ou NULL)
-- ============================================
-- Pergunta: Quais vendas temos e de quais produtos (incluindo não cadastrados)?

SELECT 
    v.id_venda,
    v.data_venda,
    v.id_produto,
    p.nome_produto,
    p.categoria,
    v.quantidade,
    v.preco_unitario,
    (v.quantidade * v.preco_unitario) AS receita_venda
FROM 
    produtos p
    RIGHT JOIN vendas v ON p.id_produto = v.id_produto
ORDER BY 
    v.data_venda DESC
LIMIT 30;

-- ============================================
-- EXEMPLO 14B: Vendas de produtos NÃO cadastrados
-- ============================================
-- Pergunta: Quais vendas foram feitas de produtos que não estão no catálogo?

SELECT 
    v.id_produto,
    COUNT(v.id_venda) AS total_vendas,
    SUM(v.quantidade) AS total_quantidade,
    SUM(v.quantidade * v.preco_unitario) AS receita_total,
    AVG(v.preco_unitario) AS preco_medio
FROM 
    produtos p
    RIGHT JOIN vendas v ON p.id_produto = v.id_produto
WHERE 
    p.id_produto IS NULL
GROUP BY 
    v.id_produto
ORDER BY 
    receita_total DESC;

