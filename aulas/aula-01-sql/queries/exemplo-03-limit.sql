-- ============================================
-- EXEMPLO 3: LIMIT
-- ============================================
-- Conceito: Limitar a quantidade de registros retornados
-- Pergunta: Quais são os 10 primeiros produtos mais caros?
--
-- IMPORTANTE:
-- - LIMIT sempre vem no final da query
-- - Geralmente usamos LIMIT junto com ORDER BY para pegar os "top N"
-- - Neste exemplo, combinamos ORDER BY (exemplo 2) com LIMIT

SELECT 
    nome_produto,
    categoria,
    marca,
    preco_atual
FROM 
    produtos
ORDER BY 
    preco_atual DESC
LIMIT 10;

