-- ============================================
-- EXEMPLO 5: Funções de Agregação
-- ============================================
-- Conceito: Calcular totais, médias, contagens, máximos e mínimos
--
-- FUNÇÕES DE AGREGAÇÃO DISPONÍVEIS:
-- - COUNT: Conta registros
-- - SUM: Soma valores
-- - AVG: Calcula média
-- - MAX: Encontra o maior valor
-- - MIN: Encontra o menor valor
--
-- IMPORTANTE:
-- - COUNT(*) conta todas as linhas (inclui NULLs)
-- - COUNT(coluna) conta apenas valores não-nulos
-- - COUNT(DISTINCT coluna) conta valores únicos

-- ============================================
-- EXEMPLO 5A: COUNT, SUM e AVG
-- ============================================
-- Pergunta: Qual é o total de vendas, receita total e ticket médio?

SELECT 
    COUNT(*) AS total_vendas,
    SUM(quantidade) AS total_unidades_vendidas,
    SUM(quantidade * preco_unitario) AS receita_total,
    AVG(quantidade * preco_unitario) AS ticket_medio
FROM 
    vendas;

-- ============================================
-- EXEMPLO 5B: MAX e MIN
-- ============================================
-- Pergunta: Qual é a maior e menor venda? Qual o produto mais caro?

SELECT 
    MAX(quantidade * preco_unitario) AS maior_venda,
    MIN(quantidade * preco_unitario) AS menor_venda,
    MAX(preco_unitario) AS maior_preco_unitario,
    MIN(preco_unitario) AS menor_preco_unitario
FROM 
    vendas;

-- ============================================
-- EXEMPLO 5C: COUNT com DISTINCT
-- ============================================
-- Pergunta: Quantos produtos diferentes foram vendidos? Quantos clientes únicos compraram?

SELECT 
    COUNT(DISTINCT id_produto) AS produtos_diferentes_vendidos,
    COUNT(DISTINCT id_cliente) AS clientes_unicos,
    COUNT(*) AS total_vendas
FROM 
    vendas;

-- ============================================
-- EXEMPLO 5D: Todas as funções juntas
-- ============================================
-- Pergunta: Resumo completo das vendas

SELECT 
    COUNT(*) AS total_vendas,
    COUNT(DISTINCT id_produto) AS produtos_unicos,
    COUNT(DISTINCT id_cliente) AS clientes_unicos,
    SUM(quantidade) AS total_unidades,
    SUM(quantidade * preco_unitario) AS receita_total,
    AVG(quantidade * preco_unitario) AS ticket_medio,
    MAX(quantidade * preco_unitario) AS maior_venda,
    MIN(quantidade * preco_unitario) AS menor_venda
FROM 
    vendas;

