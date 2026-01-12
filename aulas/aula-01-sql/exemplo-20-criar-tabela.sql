-- ============================================
-- EXEMPLO 20: Criar TABELA
-- ============================================
-- Conceito: Criar uma tabela física para armazenar dados
-- Pergunta: Como criar uma tabela para armazenar resumo de vendas por categoria?
--
-- O QUE É UMA TABELA?
-- - Uma TABELA é uma estrutura física que armazena dados no banco
-- - Os dados são persistidos no disco e permanecem mesmo após desconectar
-- - Você pode inserir, atualizar, deletar e consultar dados em uma tabela
--
-- VANTAGENS:
-- - Dados são armazenados fisicamente (mais rápido para consultas frequentes)
-- - Pode ser indexada para melhor performance
-- - Pode ter constraints (validações, chaves primárias, etc.)
-- - Dados persistem mesmo após reiniciar o banco
--
-- QUANDO USAR:
-- - Quando precisa armazenar dados que serão consultados muitas vezes
-- - Quando quer melhorar performance de queries complexas
-- - Quando precisa de dados históricos ou agregados
-- - Quando quer garantir integridade com constraints
--
-- DIFERENÇA DE VIEW:
-- - TABELA: armazena dados físicos (mais rápido, ocupa espaço)
-- - VIEW: não armazena dados, apenas a query (mais lento, não ocupa espaço)

-- Criar a tabela
CREATE TABLE resumo_vendas_categoria (
    categoria TEXT NOT NULL,
    total_vendas INTEGER NOT NULL,
    receita_total REAL NOT NULL,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (categoria)
);

-- Inserir dados na tabela usando uma query
INSERT INTO resumo_vendas_categoria (categoria, total_vendas, receita_total)
SELECT 
    p.categoria,
    COUNT(v.id_venda) AS total_vendas,
    SUM(v.quantidade * v.preco_unitario) AS receita_total
FROM 
    produtos p
    LEFT JOIN vendas v ON p.id_produto = v.id_produto
GROUP BY 
    p.categoria;

-- Consultar a tabela criada
-- SELECT * FROM resumo_vendas_categoria ORDER BY receita_total DESC;

-- Para atualizar dados na tabela:
-- UPDATE resumo_vendas_categoria 
-- SET total_vendas = 100, receita_total = 50000.00 
-- WHERE categoria = 'Eletrônicos';

-- Para remover a tabela (se necessário):
-- DROP TABLE resumo_vendas_categoria;

