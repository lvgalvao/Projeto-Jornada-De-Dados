# 📚 Dia 1 - SQL & Analytics | Jornada de Dados

## 🎯 Bem-vindo ao Primeiro Dia da Imersão!

Este é o **primeiro dia da sua Jornada de Dados**. Aqui você vai aprender a usar **SQL** para responder perguntas reais de negócio, analisando dados de um e-commerce.

**Não é uma aula teórica de SQL. É uma imersão prática em como dados resolvem problemas reais.**

---

## 🎯 Objetivo do Dia 1

Ao final deste dia, você será capaz de:

- ✅ **Escrever queries SQL** para responder perguntas de negócio
- ✅ **Entender relacionamentos** entre tabelas (JOINs)
- ✅ **Calcular KPIs** básicos (receita, top produtos, ticket médio)
- ✅ **Comparar preços** com concorrentes
- ✅ **Criar segmentações** de clientes usando lógica condicional
- ✅ **Pensar como um analista de dados**

---

## 📊 O Cenário do Projeto

Você está trabalhando com uma **empresa de e-commerce** que precisa usar dados para tomar decisões melhores. A empresa tem:

- **200 produtos** no catálogo
- **50 clientes** cadastrados
- **~3.000 vendas** nos últimos 30 dias
- **Preços de concorrentes** coletados para comparação

**Sua missão:** Usar SQL para descobrir insights que ajudem a empresa a vender mais e melhor.

---

## 📦 Os 4 Datasets que Vamos Usar

### 1. `produtos.csv` - Catálogo de Produtos
Informações sobre todos os produtos da empresa.

**Colunas:**
- `id_produto` - ID único do produto
- `nome_produto` - Nome do produto (ex: "Smartphone Galaxy A54", "Panela de Pressão")
- `categoria` - Categoria (Eletrônicos, Casa, Cozinha, Moda, Esporte, etc.)
- `marca` - Marca (Samsung, Apple, Nike, Adidas, etc.)
- `preco_atual` - Preço atual do produto (R$)
- `data_criacao` - Data de criação do produto

**Total:** 200 produtos (30 são "top sellers")

---

### 2. `clientes.csv` - Base de Clientes
Informações sobre os clientes da empresa.

**Colunas:**
- `id_cliente` - ID único do cliente
- `nome_cliente` - Nome completo do cliente
- `estado` - Estado (UF) onde o cliente está localizado
- `pais` - País (sempre "Brasil")
- `data_cadastro` - Data de cadastro do cliente

**Total:** 50 clientes

**💡 Importante:** A segmentação de clientes (VIP, TOP_TIER, REGULAR) **não vem pronta**. Você vai criar usando **CASE WHEN** baseado no comportamento de compra (receita total). Isso é parte do aprendizado!

---

### 3. `vendas.csv` - Histórico de Vendas
Registro de todas as vendas realizadas.

**Colunas:**
- `id_venda` - ID único da venda
- `data_venda` - Data e hora da venda (timestamp)
- `id_cliente` - ID do cliente que fez a compra
- `id_produto` - ID do produto vendido
- `canal_venda` - Canal de venda (`ecommerce` ou `loja_fisica`)
- `quantidade` - Quantidade vendida
- `preco_unitario` - Preço unitário da venda (pode ter desconto/promoção)

**Total:** ~3.000 vendas (últimos 30 dias, ~100 vendas/dia)

**Cálculo importante:**
- **Receita da venda** = `quantidade × preco_unitario`
- `preco_unitario` pode ser diferente de `preco_atual` (produtos podem ter promoção)

---

### 4. `preco_competidores.csv` - Preços dos Concorrentes
Preços coletados dos principais concorrentes para comparação.

**Colunas:**
- `id_produto` - ID do produto
- `nome_concorrente` - Nome do concorrente (Mercado Livre, Amazon, Magalu, Shopee)
- `preco_concorrente` - Preço do concorrente (R$)
- `data_coleta` - Data e hora da coleta do preço

**Total:** ~680 registros (não todos os produtos têm preço de todos os concorrentes)

**Concorrentes monitorados:**
- Mercado Livre
- Amazon
- Magalu
- Shopee

---

## 🔗 Como as Tabelas se Relacionam

```
┌─────────────┐
│  clientes   │
│             │
│ id_cliente  │◄─────┐
│    ...      │      │
└─────────────┘      │
                     │
┌─────────────┐      │      ┌─────────────┐
│  produtos   │      │      │   vendas    │
│             │      │      │             │
│ id_produto  │◄─────┼──────┤ id_cliente  │
│    ...      │      │      │ id_produto  │
└─────────────┘      │      │    ...      │
      │              │      └─────────────┘
      │              │
      │              │
      ▼              │
┌─────────────────┐  │
│preco_competidores│ │
│                 │  │
│   id_produto    │──┘
│ nome_concorrente│
│    ...          │
└─────────────────┘
```

**Relacionamentos:**
- 1 cliente → N vendas (um cliente pode fazer várias compras)
- 1 produto → N vendas (um produto pode ser vendido várias vezes)
- 1 produto → N preços de concorrentes (um produto pode ter preços de vários concorrentes)

---

## 🛠️ Comandos SQL que Você Vai Aprender Hoje

### 📊 Nível 1: Fundamentos (Exemplos 1-4)
- **`SELECT`** - Selecionar colunas de uma tabela
- **`FROM`** - Especificar a tabela de origem
- **`WHERE`** - Filtrar registros com condições
- **`ORDER BY`** - Ordenar resultados (crescente/decrescente)
- **`LIMIT`** - Limitar quantidade de resultados

**Exemplo prático:**
```sql
SELECT nome_produto, preco_atual
FROM produtos
WHERE preco_atual > 500
ORDER BY preco_atual DESC
LIMIT 10;
```

---

### 📈 Nível 2: Agregações (Exemplo 5)
- **`COUNT()`** - Contar registros
- **`SUM()`** - Somar valores
- **`AVG()`** - Calcular média
- **`MAX()`** - Maior valor
- **`MIN()`** - Menor valor
- **`COUNT(DISTINCT)`** - Contar valores únicos

**Exemplo prático:**
```sql
SELECT 
    COUNT(*) AS total_vendas,
    SUM(quantidade * preco_unitario) AS receita_total,
    AVG(quantidade * preco_unitario) AS ticket_medio
FROM vendas;
```

---

### 🔗 Nível 3: Relacionamentos (Exemplos 6, 8, 9)
- **`INNER JOIN`** - Juntar tabelas (apenas matches)
- **`LEFT JOIN`** - Incluir todos da esquerda
- **`RIGHT JOIN`** - Incluir todos da direita
- **`GROUP BY`** - Agrupar dados
- **`HAVING`** - Filtrar grupos

**Exemplo prático:**
```sql
SELECT 
    p.categoria,
    COUNT(v.id_venda) AS total_vendas,
    SUM(v.quantidade * v.preco_unitario) AS receita_total
FROM vendas v
INNER JOIN produtos p ON v.id_produto = p.id_produto
GROUP BY p.categoria
HAVING receita_total > 50000
ORDER BY receita_total DESC;
```

---

### 🧠 Nível 4: Lógica Condicional (Exemplo 7)
- **`CASE WHEN`** - Criar classificações e categorizações

**Exemplo prático:**
```sql
SELECT 
    nome_produto,
    preco_atual,
    CASE 
        WHEN preco_atual < 100 THEN 'Econômico'
        WHEN preco_atual < 300 THEN 'Médio'
        WHEN preco_atual < 600 THEN 'Alto'
        ELSE 'Premium'
    END AS faixa_preco
FROM produtos;
```

---

### 🚀 Nível 5: Queries Avançadas (Exemplos 12-15)
- **Subquery** - Query dentro de query
- **CTE (WITH)** - Organizar queries complexas em partes
- **LEFT JOIN / RIGHT JOIN** - Incluir todos os registros mesmo sem match

**Exemplo prático (CTE):**
```sql
WITH receita_por_cliente AS (
    SELECT 
        id_cliente,
        SUM(quantidade * preco_unitario) AS receita_total
    FROM vendas
    GROUP BY id_cliente
)
SELECT 
    c.nome_cliente,
    rpc.receita_total,
    CASE 
        WHEN rpc.receita_total >= 10000 THEN 'VIP'
        WHEN rpc.receita_total >= 5000 THEN 'TOP_TIER'
        ELSE 'REGULAR'
    END AS segmento
FROM clientes c
INNER JOIN receita_por_cliente rpc ON c.id_cliente = rpc.id_cliente;
```

---

### 💰 Nível 6: Análises de Negócio (Exemplos 16-18)
- Comparação de preços com concorrentes
- Cálculo de percentuais
- Queries complexas combinando todos os conceitos

---

### 🏗️ Nível 7: Estruturas de Dados (Exemplos 19-21)
- **`CREATE VIEW`** - Criar visão (query armazenada)
- **`CREATE TABLE`** - Criar tabela física
- **`CREATE TEMP VIEW`** - Criar visão temporária

---

## 🚀 Como Começar

### Passo 1: Gerar os Datasets

```bash
# Na raiz do projeto
python generate_datasets.py
```

Os CSVs serão gerados na pasta `data/`:
- `produtos.csv`
- `clientes.csv`
- `vendas.csv`
- `preco_competidores.csv`

---

### Passo 2: Importar os Dados no Banco

#### Opção A: SQLite (Recomendado para iniciantes)

```bash
# Criar banco de dados
sqlite3 ecommerce.db

# Configurar modo CSV
.mode csv

# Importar os arquivos
.import data/produtos.csv produtos
.import data/clientes.csv clientes
.import data/vendas.csv vendas
.import data/preco_competidores.csv preco_competidores

# Verificar se importou corretamente
SELECT COUNT(*) FROM produtos;
SELECT COUNT(*) FROM clientes;
SELECT COUNT(*) FROM vendas;
SELECT COUNT(*) FROM preco_competidores;
```

#### Opção B: PostgreSQL

```sql
-- Criar tabelas
CREATE TABLE produtos (
    id_produto TEXT,
    nome_produto TEXT,
    categoria TEXT,
    marca TEXT,
    preco_atual REAL,
    data_criacao TEXT
);

CREATE TABLE clientes (
    id_cliente TEXT,
    nome_cliente TEXT,
    estado TEXT,
    pais TEXT,
    data_cadastro TEXT
);

CREATE TABLE vendas (
    id_venda TEXT,
    data_venda TEXT,
    id_cliente TEXT,
    id_produto TEXT,
    canal_venda TEXT,
    quantidade INTEGER,
    preco_unitario REAL
);

CREATE TABLE preco_competidores (
    id_produto TEXT,
    nome_concorrente TEXT,
    preco_concorrente REAL,
    data_coleta TEXT
);

-- Importar CSVs
COPY produtos FROM 'data/produtos.csv' WITH CSV HEADER;
COPY clientes FROM 'data/clientes.csv' WITH CSV HEADER;
COPY vendas FROM 'data/vendas.csv' WITH CSV HEADER;
COPY preco_competidores FROM 'data/preco_competidores.csv' WITH CSV HEADER;
```

---

### Passo 3: Executar os Exemplos em Ordem

Vá para a pasta `queries/` e execute os exemplos em ordem:

```bash
# SQLite
sqlite3 ecommerce.db < queries/exemplo-01-select-basico.sql
sqlite3 ecommerce.db < queries/exemplo-02-order-by.sql
# ... e assim por diante
```

Ou copie e cole cada query no seu cliente SQL.

---

## 📚 Estrutura dos Exemplos

Temos **21 exemplos SQL** organizados em progressão didática:

1. **Exemplos 1-4:** Fundamentos (SELECT, WHERE, ORDER BY, LIMIT)
2. **Exemplo 5:** Funções de Agregação (COUNT, SUM, AVG, MAX, MIN)
3. **Exemplos 6, 8, 9:** JOINs e Agrupamentos
4. **Exemplo 7:** CASE WHEN (Lógica Condicional)
5. **Exemplos 12-13:** Subquery e CTE
6. **Exemplos 14-15:** LEFT JOIN e RIGHT JOIN
7. **Exemplos 16-18:** Análises de Negócio
8. **Exemplos 19-21:** VIEW, TABLE, TEMP VIEW

**Cada exemplo:**
- Introduz um novo conceito SQL
- Responde uma pergunta de negócio real
- Tem comentários explicativos
- Constrói sobre os exemplos anteriores

---

## 🎯 Perguntas de Negócio que Vamos Responder

### Análise Interna
1. Quais são os 10 produtos que mais vendem?
2. Quem são os clientes que mais compram?
3. Qual canal de venda gera mais receita?
4. Qual categoria de produto é mais lucrativa?
5. Quais produtos nunca foram vendidos?

### Análise de Mercado
1. Quais produtos estão mais caros que a concorrência?
2. Qual concorrente tem os preços mais baixos?
3. Quais produtos top sellers estão com preço acima do mercado?
4. Qual é a diferença média de preço entre nós e os concorrentes?

### Segmentação de Clientes
1. Como criar segmentação de clientes (VIP, TOP_TIER, REGULAR) usando CASE WHEN?
2. Qual segmento gera mais receita?
3. Qual é o ticket médio por segmento?

---

## 📝 Checklist de Aprendizado

Após fazer todos os exemplos, você deve ser capaz de:

- [ ] Selecionar e filtrar dados (SELECT, WHERE)
- [ ] Ordenar e limitar resultados (ORDER BY, LIMIT)
- [ ] Calcular agregações (COUNT, SUM, AVG, MAX, MIN)
- [ ] Agrupar dados (GROUP BY)
- [ ] Filtrar grupos (HAVING)
- [ ] Juntar tabelas (JOIN, LEFT JOIN, RIGHT JOIN)
- [ ] Criar lógica condicional (CASE WHEN)
- [ ] Organizar queries complexas (CTEs, Subqueries)
- [ ] Calcular percentuais e diferenças
- [ ] Comparar dados entre tabelas
- [ ] Criar views e tabelas

---

## 💡 Dicas Importantes

### Durante a Aula
- **Execute em ordem:** Cada exemplo introduz um conceito novo
- **Modifique:** Tente adaptar as queries para responder outras perguntas
- **Valide:** Sempre verifique se os resultados fazem sentido
- **Pergunte:** "Por que isso importa para o negócio?"

### Comandos Úteis

**SQLite:**
```bash
# Ver estrutura de uma tabela
.schema produtos

# Ver primeiras linhas
SELECT * FROM produtos LIMIT 10;

# Verificar quantos registros
SELECT COUNT(*) FROM produtos;

# Sair do SQLite
.quit
```

**PostgreSQL:**
```sql
-- Ver estrutura de uma tabela
\d produtos

-- Ver primeiras linhas
SELECT * FROM produtos LIMIT 10;

-- Verificar quantos registros
SELECT COUNT(*) FROM produtos;
```

---

## 🐛 Troubleshooting

### Erro: "no such table: produtos"
**Solução:** Verifique se importou os CSVs corretamente. Use `.tables` (SQLite) ou `\dt` (PostgreSQL) para listar tabelas.

### Erro: "ambiguous column name"
**Solução:** Especifique a tabela: `produtos.nome_produto` ao invés de apenas `nome_produto` quando há JOIN.

### Erro: "column must appear in GROUP BY"
**Solução:** Todas as colunas no SELECT que não são funções de agregação devem estar no GROUP BY.

---

## 📚 Material Complementar

- **[Queries de Exemplo](./queries/README.md)** - Guia completo com todos os 21 exemplos
- **[KPIs da Aula 1](./KPIS.md)** - Lista completa de KPIs e perguntas de negócio
- **[Estrutura dos Dados](./ESTRUTURA_DADOS.md)** - Documentação detalhada dos datasets
- **[Exercícios](./exercicios/)** - Exercícios práticos para fixar o aprendizado

---

## 🎯 Resultado Esperado

Ao final do **Dia 1**, você terá:

✅ **Conhecimento prático de SQL** aplicado a negócios reais  
✅ **21 exemplos funcionais** que você pode adaptar  
✅ **Capacidade de responder perguntas de negócio** usando dados  
✅ **Base sólida** para os próximos dias da imersão  

---

## 💡 Frase de Ouro

> **"Você não está aprendendo SQL. Você está aprendendo como dados resolvem problemas reais."**

Cada query que você escrever deve responder uma pergunta de negócio. Sempre pergunte: **"Por que isso importa?"**

---

## 🚀 Próximo Passo

Depois de dominar o **Dia 1 (SQL & Analytics)**, você estará pronto para:

- **Dia 2:** Python & Ingestão de Dados
- **Dia 3:** Engenharia de Dados
- **Dia 4:** Inteligência Artificial

**Boa jornada! 🚀**
