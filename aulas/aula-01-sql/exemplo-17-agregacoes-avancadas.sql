-- ============================================
-- EXEMPLO 17: Agregações Avançadas (ROUND, Percentuais)
-- ============================================
-- Conceito: Calcular percentuais e formatar números
-- Pergunta: Qual é a distribuição percentual de receita por canal?

SELECT 
    canal_venda,
    COUNT(*) AS total_vendas,
    SUM(quantidade * preco_unitario) AS receita_total,
    ROUND(
        SUM(quantidade * preco_unitario) * 100.0 / (
            SELECT SUM(quantidade * preco_unitario) 
            FROM vendas
        ), 
        2
    ) AS percentual_receita
FROM 
    vendas
GROUP BY 
    canal_venda
ORDER BY 
    receita_total DESC;

