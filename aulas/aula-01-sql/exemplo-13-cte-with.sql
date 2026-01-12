-- ============================================
-- EXEMPLO 13: CTE (WITH) - Common Table Expressions
-- ============================================
-- Conceito: Organizar queries complexas em partes
-- Pergunta: Quais produtos estão mais caros que a média dos concorrentes?

WITH preco_medio_concorrente AS (
    SELECT 
        id_produto,
        AVG(preco_concorrente) AS preco_medio_concorrente,
        MIN(preco_concorrente) AS preco_minimo_concorrente
    FROM 
        preco_competidores
    GROUP BY 
        id_produto
)
SELECT 
    p.nome_produto,
    p.categoria,
    p.preco_atual AS nosso_preco,
    pmc.preco_medio_concorrente,
    pmc.preco_minimo_concorrente,
    (p.preco_atual - pmc.preco_medio_concorrente) AS diferenca_media
FROM 
    produtos p
    INNER JOIN preco_medio_concorrente pmc ON p.id_produto = pmc.id_produto
WHERE 
    p.preco_atual > pmc.preco_medio_concorrente
ORDER BY 
    diferenca_media DESC
LIMIT 20;

