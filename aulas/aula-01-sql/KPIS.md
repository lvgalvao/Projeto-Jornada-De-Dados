# 📊 KPIs da Aula 1 - SQL & Analytics

## 🎯 Objetivos de Negócio

### 1. **Análise Interna (Vendas e Clientes)**

#### 1.1 Produtos Mais Vendidos
- **KPI**: Top 10 produtos por quantidade vendida
- **KPI**: Top 10 produtos por receita (quantity × unit_price)
- **KPI**: Produtos com maior ticket médio
- **Pergunta de negócio**: Quais produtos devemos priorizar no estoque?

#### 1.2 Análise de Clientes
- **KPI**: Top 10 clientes por receita total
- **KPI**: Criar segmentação de clientes usando CASE WHEN (VIP, TOP_TIER, REGULAR) baseado em receita total
- **KPI**: Distribuição de clientes por segmento criado
- **KPI**: Ticket médio por segmento de cliente
- **KPI**: Frequência de compra por segmento
- **Pergunta de negócio**: Quem são nossos melhores clientes? Como tratá-los?
- **Nota**: A segmentação deve ser criada usando CASE WHEN baseado no comportamento de compra (veja exercício-case-when-clientes.sql)

#### 1.3 Análise de Receita
- **KPI**: Receita total por dia
- **KPI**: Receita total por canal (ecommerce vs loja_fisica)
- **KPI**: Receita total por categoria de produto
- **KPI**: Receita total por marca
- **Pergunta de negócio**: Onde está concentrada nossa receita?

#### 1.4 Análise Temporal
- **KPI**: Vendas por dia da semana
- **KPI**: Vendas por horário do dia
- **KPI**: Tendência de vendas (últimos 7 dias vs últimos 30 dias)
- **Pergunta de negócio**: Quando nossos clientes compram mais?

---

### 2. **Análise de Mercado (Preços e Concorrência)**

#### 2.1 Comparação de Preços
- **KPI**: Produtos mais caros que a concorrência
- **KPI**: Produtos mais baratos que a concorrência
- **KPI**: Diferença percentual média de preço vs concorrentes
- **KPI**: Produtos com maior variação de preço entre concorrentes
- **Pergunta de negócio**: Estamos competitivos no mercado?

#### 2.2 Análise por Concorrente
- **KPI**: Qual concorrente tem os preços mais baixos (por produto)
- **KPI**: Qual concorrente tem os preços mais altos (por produto)
- **KPI**: Média de preços por concorrente
- **Pergunta de negócio**: Quem é nossa maior ameaça de preço?

#### 2.3 Produtos Críticos (Preço)
- **KPI**: Produtos top sellers que estão mais caros que o mercado
- **KPI**: Produtos com maior diferença de preço vs concorrente mais barato
- **Pergunta de negócio**: Quais produtos precisam de ajuste de preço urgente?

---

## 🔍 Queries SQL que Resolvem Esses KPIs

### Conceitos SQL Utilizados:

1. **SELECT / FROM** - Seleção básica
2. **WHERE** - Filtros
3. **GROUP BY** - Agregações
4. **HAVING** - Filtros em agregações
5. **ORDER BY** - Ordenação
6. **JOIN** - Relacionamento entre tabelas
7. **CASE WHEN** - Lógica condicional
8. **Funções de agregação**: SUM, COUNT, AVG, MAX, MIN
9. **Funções de data**: DATE(), EXTRACT(), DATE_TRUNC()
10. **CTEs (Common Table Expressions)** - Organização de queries complexas

---

## 📈 Estrutura de Análise Sugerida

### Fase 1: Exploração Básica
- Contar registros em cada tabela
- Entender a estrutura dos dados
- Identificar valores nulos ou inconsistentes

### Fase 2: Análise Descritiva
- Top produtos, clientes, categorias
- Distribuições e médias
- Padrões temporais

### Fase 3: Análise Comparativa
- Comparação interna (segmentos, canais, categorias)
- Comparação externa (preços vs concorrentes)

### Fase 4: Insights para Decisão
- Identificar oportunidades
- Alertar sobre riscos
- Priorizar ações

---

## 💡 Exemplos de Perguntas que os Alunos Vão Responder

1. **Qual produto gerou mais receita no último mês?**
2. **Quantos clientes VIP temos e quanto eles representam em receita?** (criar segmentação primeiro com CASE WHEN)
3. **Qual canal de venda (ecommerce vs loja física) é mais lucrativo?**
4. **Em que horário do dia acontecem mais vendas?**
5. **Quais produtos estão mais caros que todos os concorrentes?**
6. **Qual é a diferença média de preço entre nós e o Mercado Livre?**
7. **Quais são os top 5 produtos que vendem bem mas estão com preço acima do mercado?**
8. **Qual categoria de produto tem o maior ticket médio?**
9. **Como criar a segmentação de clientes baseada no valor de compras?** (usando CASE WHEN)

