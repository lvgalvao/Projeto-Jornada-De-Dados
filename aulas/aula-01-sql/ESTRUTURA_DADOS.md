# 📊 Estrutura Detalhada dos Datasets

## 🎯 Visão Geral

Este documento descreve em detalhes a estrutura, relacionamentos e características dos 4 datasets do projeto.

---

## 1️⃣ Products (Produtos)

### Estrutura
```sql
CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    brand TEXT,
    current_price REAL,
    created_at TEXT
);
```

### Campos

| Campo | Tipo | Descrição | Exemplo |
|-------|------|-----------|---------|
| `product_id` | TEXT | ID único (formato: `prd_xxxxxxxxxxxx`) | `prd_a1b2c3d4e5f6` |
| `product_name` | TEXT | Nome do produto | `Fone Bluetooth Aura 582` |
| `category` | TEXT | Categoria do produto | `Eletrônicos`, `Casa`, `Cozinha` |
| `brand` | TEXT | Marca do produto | `Samsung`, `Apple`, `LG` |
| `current_price` | REAL | Preço atual (R$) | `299.90` |
| `created_at` | TEXT | Data de criação (ISO) | `2023-05-15 10:30:00` |

### Características
- **Total:** 200 produtos
- **Top Sellers:** 30 produtos (15% do total) vendem muito mais
- **Categorias:** 10 categorias diferentes
- **Marcas:** 20 marcas diferentes
- **Preços:** Distribuídos em 5 faixas:
  - R$ 29,90 - R$ 59,90 (18%)
  - R$ 59,90 - R$ 119,90 (32%)
  - R$ 119,90 - R$ 249,90 (26%)
  - R$ 249,90 - R$ 499,90 (16%)
  - R$ 499,90 - R$ 1.499,90 (8%)

### Relacionamentos
- 1 produto → N vendas (`sales.product_id`)
- 1 produto → N preços de concorrentes (`competitor_prices.product_id`)

---

## 2️⃣ Customers (Clientes)

### Estrutura
```sql
CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    estado TEXT,
    pais TEXT,
    created_at TEXT
);
```

### Campos

| Campo | Tipo | Descrição | Exemplo |
|-------|------|-----------|---------|
| `customer_id` | TEXT | ID único (formato: `cus_xxxxxxxxxxxx`) | `cus_f6e5d4c3b2a1` |
| `customer_name` | TEXT | Nome completo do cliente | `Maria Silva` |
| `estado` | TEXT | Estado (UF) | `SP`, `RJ`, `MG` |
| `pais` | TEXT | País (sempre "Brasil") | `Brasil` |
| `created_at` | TEXT | Data de cadastro (ISO) | `2022-03-20 14:15:00` |

### Características
- **Total:** 50 clientes
- **Distribuição por Estado:** Todos os estados brasileiros representados
- **Nota Importante:** A segmentação de clientes (VIP, TOP_TIER, REGULAR) **não é gerada automaticamente**. Ela deve ser criada usando **CASE WHEN** baseado no comportamento de compra (receita total). Veja o exercício `exercicio-case-when-clientes.sql` para aprender como criar essa segmentação.

### Relacionamentos
- 1 cliente → N vendas (`sales.customer_id`)

---

## 3️⃣ Sales (Vendas)

### Estrutura
```sql
CREATE TABLE sales (
    sale_id TEXT PRIMARY KEY,
    sale_date TEXT,
    customer_id TEXT,
    product_id TEXT,
    sales_channel TEXT,
    quantity INTEGER,
    unit_price REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### Campos

| Campo | Tipo | Descrição | Exemplo |
|-------|------|-----------|---------|
| `sale_id` | TEXT | ID único (formato: `sal_xxxxxxxxxxxx`) | `sal_123456789abc` |
| `sale_date` | TEXT | Data e hora da venda (ISO) | `2024-01-15 18:45:30` |
| `customer_id` | TEXT | ID do cliente | `cus_f6e5d4c3b2a1` |
| `product_id` | TEXT | ID do produto | `prd_a1b2c3d4e5f6` |
| `sales_channel` | TEXT | Canal de venda | `ecommerce`, `loja_fisica` |
| `quantity` | INTEGER | Quantidade vendida | `1`, `2`, `3` |
| `unit_price` | REAL | Preço unitário da venda (R$) | `279.90` |

### Características
- **Total:** ~3.000 vendas
- **Período:** Últimos 30 dias
- **Volume:** ~100 vendas por dia
- **Canais:**
  - Ecommerce: 72% das vendas
  - Loja Física: 28% das vendas
- **Quantidades:**
  - 1 unidade: 72%
  - 2 unidades: 18%
  - 3 unidades: 6%
  - 4 unidades: 3%
  - 5 unidades: 1%
- **Preços:**
  - `unit_price` pode ser diferente de `current_price` (promoções)
  - 55% sem desconto (unit_price = current_price)
  - 30% com desconto de 5-10%
  - 10% com desconto de 15%
  - 5% com aumento de 10% (erro/preço especial)
- **Horários de Venda:**
  - 8h-12h: 25% (manhã)
  - 12h-15h: 15% (almoço)
  - 15h-19h: 30% (tarde - pico)
  - 19h-23h: 25% (noite)
  - 23h-2h: 5% (madrugada)

### Cálculos Importantes
- **Receita da Venda:** `quantity × unit_price`
- **Ticket Médio:** `SUM(quantity × unit_price) / COUNT(sale_id)`

### Relacionamentos
- N vendas → 1 cliente (`customer_id`)
- N vendas → 1 produto (`product_id`)

---

## 4️⃣ Competitor Prices (Preços de Concorrentes)

### Estrutura
```sql
CREATE TABLE competitor_prices (
    product_id TEXT,
    competitor_name TEXT,
    competitor_price REAL,
    collected_at TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

### Campos

| Campo | Tipo | Descrição | Exemplo |
|-------|------|-----------|---------|
| `product_id` | TEXT | ID do produto | `prd_a1b2c3d4e5f6` |
| `competitor_name` | TEXT | Nome do concorrente | `Mercado Livre`, `Amazon` |
| `competitor_price` | REAL | Preço do concorrente (R$) | `289.90` |
| `collected_at` | TEXT | Data da coleta (ISO) | `2024-01-20 09:30:00` |

### Características
- **Total:** ~680 registros
- **Concorrentes:** 4
  - Mercado Livre
  - Amazon
  - Magalu
  - Shopee
- **Cobertura:** 85% dos produtos têm preço de pelo menos 1 concorrente
- **Coletas:** 1-3 coletas por produto/concorrente
- **Período:** Últimos 7 dias (dados recentes)
- **Variação de Preço:**
  - 92% do nosso preço: 10%
  - 95% do nosso preço: 18%
  - 98% do nosso preço: 22%
  - 100% do nosso preço: 20%
  - 103% do nosso preço: 15%
  - 106% do nosso preço: 10%
  - 110% do nosso preço: 5%

### Relacionamentos
- N preços → 1 produto (`product_id`)

---

## 🔗 Diagrama de Relacionamentos

```
┌─────────────┐
│  customers  │
│             │
│ customer_id │◄─────┐
│    ...      │      │
└─────────────┘      │
                     │
┌─────────────┐      │      ┌─────────────┐
│   products  │      │      │    sales    │
│             │      │      │             │
│ product_id  │◄─────┼──────┤ customer_id │
│    ...      │      │      │ product_id  │
└─────────────┘      │      │    ...      │
      │              │      └─────────────┘
      │              │
      │              │
      ▼              │
┌─────────────────┐  │
│competitor_prices │  │
│                 │  │
│   product_id    │──┘
│ competitor_name │
│    ...          │
└─────────────────┘
```

---

## 📈 Padrões e Insights Esperados

### Produtos
- 30 produtos "top sellers" devem aparecer muito mais nas vendas
- Categorias como "Eletrônicos" e "Informática" devem ter preços mais altos
- Marcas premium (Apple, Samsung) devem ter preços mais altos

### Clientes
- Clientes VIP devem gerar muito mais receita que REGULAR
- Clientes VIP devem ter ticket médio maior
- Distribuição de compras deve ser desigual (poucos clientes, muita receita)

### Vendas
- Pico de vendas no período da tarde (15h-19h)
- Ecommerce deve ter mais vendas que loja física
- Maioria das vendas com 1 unidade

### Preços
- Alguns produtos estarão mais caros que concorrentes
- Alguns produtos estarão mais baratos
- Mercado Livre e Shopee tendem a ter preços mais baixos
- Amazon tende a ter preços similares ou mais altos

---

## 💡 Dicas para Análise

1. **Sempre calcule receita:** `quantity × unit_price`
2. **Compare preços:** `current_price` vs `competitor_price`
3. **Use agregações:** SUM, COUNT, AVG são essenciais
4. **Agrupe por dimensões:** categoria, segmento, canal, data
5. **Filtre por período:** últimos 7 dias, último mês, etc.
6. **Identifique outliers:** produtos muito caros, clientes muito ativos

---

## 🎓 Próximos Passos

Com essa estrutura em mente, você está pronto para:
1. Explorar os dados com SQL
2. Responder perguntas de negócio
3. Identificar oportunidades e riscos
4. Comparar com o mercado

**Boa análise! 🚀**

