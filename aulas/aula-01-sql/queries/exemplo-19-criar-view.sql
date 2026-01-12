-- ============================================
-- EXEMPLO 19: Criar VIEW (Visão)
-- ============================================
-- Conceito: Criar uma visão (view) que armazena uma query como se fosse uma tabela
-- Pergunta: Como criar uma visão para produtos com vendas?
--
-- O QUE É UMA VIEW?
-- - Uma VIEW é uma query armazenada que se comporta como uma tabela
-- - Você pode fazer SELECT em uma VIEW como se fosse uma tabela normal
-- - A VIEW não armazena dados, ela executa a query toda vez que é consultada
--
-- VANTAGENS:
-- - Simplifica queries complexas (escreva uma vez, use várias vezes)
-- - Facilita manutenção (mude a VIEW, todos que usam são atualizados)
-- - Controla acesso a dados (usuários veem apenas o que a VIEW permite)
-- - Abstrai complexidade (usuários não precisam saber JOINs complexos)
--
-- QUANDO USAR:
-- - Quando você tem uma query complexa que é usada várias vezes
-- - Quando quer simplificar o acesso a dados para outros usuários
-- - Quando precisa controlar quais dados os usuários podem ver
--
-- DIFERENÇA DE TABELA:
-- - TABELA: armazena dados físicos no disco
-- - VIEW: não armazena dados, apenas a definição da query

-- Criar a VIEW
CREATE VIEW produtos_com_vendas AS
SELECT 
    p.id_produto,
    p.nome_produto,
    p.categoria,
    p.marca,
    p.preco_atual,
    COUNT(v.id_venda) AS total_vendas,
    SUM(v.quantidade * v.preco_unitario) AS receita_total
FROM 
    produtos p
    LEFT JOIN vendas v ON p.id_produto = v.id_produto
GROUP BY 
    p.id_produto, p.nome_produto, p.categoria, p.marca, p.preco_atual;

-- Agora você pode usar a VIEW como se fosse uma tabela:
-- SELECT * FROM produtos_com_vendas WHERE total_vendas > 10;

-- Para ver a VIEW criada:
-- SELECT * FROM produtos_com_vendas LIMIT 10;

-- Para remover a VIEW (se necessário):
-- DROP VIEW produtos_com_vendas;

