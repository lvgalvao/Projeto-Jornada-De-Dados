-- ============================================
-- EXEMPLO 4: WHERE (Filtros)
-- ============================================
-- Conceito: Filtrar registros com condições
-- Pergunta: Quais produtos custam mais de R$ 500?

SELECT 
    nome_produto,
    categoria,
    marca,
    preco_atual
FROM 
    produtos
WHERE 
    preco_atual > 500;

