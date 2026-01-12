-- ============================================
-- EXEMPLO 9: HAVING com JOIN
-- ============================================
-- Conceito: Filtrar resultados após agrupamento
-- Pergunta: Quais categorias geram mais de R$ 50.000 em receita?

SELECT 
    p.categoria,
    COUNT(*) AS total_vendas,
    SUM(v.quantidade * v.preco_unitario) AS receita_total
FROM 
    vendas v
    INNER JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY 
    p.categoria
HAVING 
    SUM(v.quantidade * v.preco_unitario) > 50000
ORDER BY 
    receita_total DESC;

