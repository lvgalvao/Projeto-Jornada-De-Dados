-- ============================================
-- EXEMPLO 21: Criar TEMP VIEW (Visão Temporária)
-- ============================================
-- Conceito: Criar uma visão temporária que existe apenas durante a sessão
-- Pergunta: Como criar uma visão temporária para análise rápida?
--
-- O QUE É UMA TEMP VIEW?
-- - Uma TEMP VIEW é uma view que existe apenas durante a sessão atual
-- - Ela é automaticamente removida quando você desconecta do banco
-- - Útil para análises temporárias ou testes
--
-- VANTAGENS:
-- - Não polui o banco de dados (é removida automaticamente)
-- - Útil para testes e análises exploratórias
-- - Não precisa se preocupar em limpar depois
-- - Cada sessão pode ter sua própria TEMP VIEW com o mesmo nome
--
-- QUANDO USAR:
-- - Para análises temporárias durante uma sessão
-- - Para testes de queries antes de criar uma VIEW permanente
-- - Quando você não quer deixar "lixo" no banco
-- - Para análises exploratórias que não serão reutilizadas
--
-- DIFERENÇA DE VIEW E TABELA:
-- - VIEW: permanente, precisa DROP VIEW para remover
-- - TEMP VIEW: temporária, removida automaticamente ao desconectar
-- - TABELA: permanente, armazena dados físicos

-- Criar a TEMP VIEW
CREATE TEMP VIEW produtos_mais_vendidos_temp AS
SELECT 
    p.id_produto,
    p.nome_produto,
    p.categoria,
    COUNT(v.id_venda) AS total_vendas,
    SUM(v.quantidade * v.preco_unitario) AS receita_total
FROM 
    produtos p
    INNER JOIN vendas v ON p.id_produto = v.id_produto
GROUP BY 
    p.id_produto, p.nome_produto, p.categoria
HAVING 
    COUNT(v.id_venda) > 10
ORDER BY 
    receita_total DESC;

-- Usar a TEMP VIEW como uma tabela normal
-- SELECT * FROM produtos_mais_vendidos_temp LIMIT 20;

-- A TEMP VIEW será automaticamente removida quando você:
-- - Desconectar do banco de dados
-- - Fechar a sessão
-- - Executar: DROP VIEW produtos_mais_vendidos_temp;

-- Para remover manualmente (opcional):
-- DROP VIEW produtos_mais_vendidos_temp;

