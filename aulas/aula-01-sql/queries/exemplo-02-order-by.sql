-- ============================================
-- EXEMPLO 2: ORDER BY
-- ============================================
-- Conceito: Ordenar resultados por uma ou mais colunas
-- Pergunta: Quais são os produtos ordenados por preço (do mais caro para o mais barato)?

SELECT 
    nome_produto,
    categoria,
    marca,
    preco_atual
FROM 
    produtos
ORDER BY 
    preco_atual DESC;

