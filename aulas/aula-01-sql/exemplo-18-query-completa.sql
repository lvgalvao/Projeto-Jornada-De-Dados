-- ============================================
-- EXEMPLO 18: Query Completa (Todos os Conceitos)
-- ============================================
-- Conceito: Combinar múltiplos conceitos em uma análise complexa
-- Pergunta: Quais produtos top sellers estão mais caros que todos os concorrentes?

WITH produtos_top_vendas AS (
    SELECT 
        p.id_produto,
        p.nome_produto,
        p.categoria,
        p.preco_atual,
        SUM(v.quantidade * v.preco_unitario) AS receita_total
    FROM 
        produtos p
        INNER JOIN vendas v ON p.id_produto = v.id_produto
    GROUP BY 
        p.id_produto, p.nome_produto, p.categoria, p.preco_atual
    ORDER BY 
        receita_total DESC
    LIMIT 30
),
precos_concorrentes AS (
    SELECT 
        id_produto,
        MIN(preco_concorrente) AS preco_minimo_concorrente,
        AVG(preco_concorrente) AS preco_medio_concorrente
    FROM 
        preco_competidores
    GROUP BY 
        id_produto
)
SELECT 
    ptv.nome_produto,
    ptv.categoria,
    ptv.preco_atual AS nosso_preco,
    pc.preco_minimo_concorrente,
    pc.preco_medio_concorrente,
    ptv.receita_total,
    CASE 
        WHEN ptv.preco_atual > pc.preco_minimo_concorrente THEN 'Acima do mercado'
        ELSE 'Competitivo'
    END AS status_preco,
    ROUND(
        ((ptv.preco_atual - pc.preco_minimo_concorrente) / pc.preco_minimo_concorrente * 100), 
        2
    ) AS percentual_diferenca
FROM 
    produtos_top_vendas ptv
    INNER JOIN precos_concorrentes pc ON ptv.id_produto = pc.id_produto
WHERE 
    ptv.preco_atual > pc.preco_minimo_concorrente
ORDER BY 
    percentual_diferenca DESC;

