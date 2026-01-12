-- ============================================
-- EXEMPLO 1: SELECT Básico
-- ============================================
-- Conceito: Selecionar colunas de uma tabela
-- Pergunta: Quais produtos temos no catálogo?

SELECT 
    id_produto,
    nome_produto,
    categoria,
    marca,
    preco_atual
FROM 
    produtos;

