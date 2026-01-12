-- ============================================
-- EXEMPLO 7: CASE WHEN (Lógica Condicional)
-- ============================================
-- Conceito: Criar classificações e categorizações
-- Pergunta: Classifique os produtos por faixa de preço

SELECT 
    nome_produto,
    preco_atual,
    CASE 
        WHEN preco_atual < 100 THEN 'Econômico'
        WHEN preco_atual < 300 THEN 'Médio'
        WHEN preco_atual < 600 THEN 'Alto'
        ELSE 'Premium'
    END AS faixa_preco
FROM 
    produtos
ORDER BY 
    preco_atual DESC;

