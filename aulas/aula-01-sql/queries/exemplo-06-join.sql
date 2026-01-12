-- ============================================
-- EXEMPLO 6: JOIN
-- ============================================
-- Conceito: Entender o que é JOIN
-- Pergunta: Como ver o nome do produto junto com a venda?
--
-- ANTES DO JOIN:
-- - Tabela vendas tem: id_venda, id_produto, quantidade
-- - Tabela produtos tem: id_produto, nome_produto, categoria
-- - Não conseguimos ver o nome do produto na venda!
--
-- COM O JOIN:
-- - Juntamos as duas tabelas pelo id_produto
-- - Agora vemos id_venda E nome_produto juntos!
--
-- COMO FUNCIONA:
-- 1. Pegamos uma linha de vendas
-- 2. Procuramos o id_produto correspondente em produtos
-- 3. Combinamos as informações das duas tabelas
-- 4. Resultado: uma linha com dados de ambas as tabelas
--
-- SINTAXE BÁSICA:
--   FROM tabela1 t1
--   INNER JOIN tabela2 t2 ON t1.coluna = t2.coluna
--
-- IMPORTANTE:
-- - INNER JOIN só retorna linhas que têm match em ambas as tabelas
-- - Use aliases (v, p) para encurtar nomes
-- - Sempre especifique a tabela: v.id_venda, p.nome_produto

SELECT 
    v.id_venda,
    v.id_produto,
    p.nome_produto,
    v.quantidade
FROM 
    vendas v
    INNER JOIN produtos p ON v.id_produto = p.id_produto
LIMIT 10;

