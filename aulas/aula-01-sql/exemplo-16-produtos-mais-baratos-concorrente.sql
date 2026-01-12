-- ============================================
-- EXEMPLO 16: Comparação de Preços com Concorrentes
-- ============================================
-- Conceito: Comparar nossos preços com os preços dos concorrentes
-- Pergunta: Quais produtos estão mais baratos no concorrente do que na nossa tabela?
--
-- NESTE EXEMPLO VOCÊ APRENDE:
-- - Como comparar preços entre tabelas diferentes
-- - Como usar JOIN para combinar produtos com preços de concorrentes
-- - Como calcular a diferença percentual entre preços
-- - Como identificar oportunidades de ajuste de preço
--
-- CASO DE NEGÓCIO:
-- Identificar produtos onde os concorrentes estão mais baratos
-- Isso ajuda a tomar decisões sobre ajuste de preços ou negociação com fornecedores

SELECT 
    p.id_produto,
    p.nome_produto,
    p.categoria,
    p.marca,
    p.preco_atual AS nosso_preco,
    pc.nome_concorrente,
    pc.preco_concorrente,
    (p.preco_atual - pc.preco_concorrente) AS diferenca_absoluta,
    ROUND(
        ((p.preco_atual - pc.preco_concorrente) / pc.preco_concorrente * 100), 
        2
    ) AS percentual_mais_caro
FROM 
    produtos p
    INNER JOIN preco_competidores pc ON p.id_produto = pc.id_produto
WHERE 
    p.preco_atual > pc.preco_concorrente
ORDER BY 
    percentual_mais_caro DESC
LIMIT 30;

