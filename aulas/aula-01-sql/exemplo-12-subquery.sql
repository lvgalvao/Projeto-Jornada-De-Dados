-- ============================================
-- EXEMPLO 12: Subquery (Query Dentro de Query)
-- ============================================
-- Conceito: Usar resultado de uma query dentro de outra
-- Pergunta: Quais produtos têm preço acima da média geral?

SELECT 
    nome_produto,
    categoria,
    marca,
    preco_atual
FROM 
    produtos
WHERE 
    preco_atual > (
        SELECT AVG(preco_atual) 
        FROM produtos
    )
ORDER BY 
    preco_atual DESC;

