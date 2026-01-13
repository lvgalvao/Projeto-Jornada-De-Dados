# 🐍 Dia 2: Python & Ingestão de Dados | Jornada de Dados

Bem-vindo ao **segundo dia da imersão Jornada de Dados**! Hoje você vai aprender Python para trabalhar com dados, focando em **ingestão** - o processo de coletar dados de diferentes fontes e prepará-los para análise.

---

## 📖 O que é Python para Dados?

**Python** é uma linguagem de programação versátil e poderosa que se tornou o padrão da indústria para trabalhar com dados. É a ferramenta que permite:

- ✅ **Ingerir dados** - Coletar dados de APIs, web scraping, bancos de dados, arquivos
- ✅ **Processar dados** - Limpar, transformar e preparar dados para análise
- ✅ **Analisar dados** - Fazer análises estatísticas e exploratórias
- ✅ **Automatizar tarefas** - Criar scripts que fazem o trabalho pesado

**Python não é apenas uma linguagem de programação.** É um ecossistema completo com bibliotecas especializadas para cada necessidade de dados.

**Exemplo:**
```python
# Você diz: "Quero ler dados de vendas e calcular receita total"
import pandas as pd

df = pd.read_csv("vendas.csv")
df['receita'] = df['quantidade'] * df['preco_unitario']
receita_total = df['receita'].sum()

print(f"Receita total: R$ {receita_total:,.2f}")
```

---

## 💼 Mercado de Python para Dados

Python é a linguagem mais usada no mercado de dados e ciência de dados:

### 📊 Por que Python é importante?

1. **Ecossistema rico**: Pandas, NumPy, Scikit-learn, TensorFlow, PyTorch
2. **Demanda de mercado**: Habilidade essencial em 90% das vagas de dados
3. **Versatilidade**: Serve para análise, engenharia, machine learning, automação
4. **Comunidade**: Grande comunidade, muitos recursos e bibliotecas open-source
5. **Integração**: Fácil integração com bancos de dados, APIs, sistemas

### 🎯 Onde Python é usado?

- **Data Engineering**: Pipelines de dados, ETL, ingestão
- **Data Analysis**: Análise exploratória, relatórios automatizados
- **Data Science**: Machine Learning, estatística, modelagem
- **Automação**: Scripts para tarefas repetitivas
- **APIs e Integrações**: Conectar diferentes sistemas

### 💰 Salários no Brasil (2024)

- **Analista de Dados com Python**: R$ 4.500 - R$ 8.000
- **Engenheiro de Dados**: R$ 8.000 - R$ 15.000
- **Cientista de Dados**: R$ 10.000 - R$ 20.000+

**Fonte:** Glassdoor, LinkedIn, pesquisas de mercado 2024

---

## 🎯 Foco do Curso

Neste **Dia 2**, vamos focar em:

✅ **Ingestão de Dados** - 70% do tempo  
✅ **Tratamento Básico** - 20% do tempo  
✅ **Exportação** - 10% do tempo  

**Por quê?** Engenheiros e analistas de dados passam a maior parte do tempo coletando e preparando dados. Você vai aprender a **pensar como engenheiro de dados** e **integrar diferentes fontes de dados**.

---

## 🔄 SQL vs Python: Qual a Diferença?

### 📊 SQL (Dia 1)
**Trabalha com dados que JÁ EXISTEM no banco de dados**

- ✅ Dados já estão armazenados
- ✅ Foco em consultar e analisar
- ✅ Linguagem declarativa (diz o que quer)
- ✅ Otimizado para grandes volumes
- ✅ Ideal para análises e relatórios

**Exemplo:**
```sql
-- Os dados JÁ ESTÃO no banco
SELECT * FROM vendas WHERE data_venda > '2024-01-01';
```

### 🐍 Python (Dia 2)
**BUSCA dados de sistemas externos e integra diferentes fontes**

- ✅ Dados vêm de sistemas externos (APIs, web scraping, arquivos)
- ✅ Foco em coletar e integrar
- ✅ Linguagem imperativa (diz como fazer)
- ✅ Ideal para automação e integração
- ✅ Conecta diferentes sistemas

**Exemplo:**
```python
# BUSCA dados de uma API externa
import requests
dados = requests.get("https://api.coinbase.com/v2/prices/spot").json()
```

### 🎯 Resumo

| Aspecto | SQL | Python |
|---------|-----|--------|
| **Dados** | Já existem no banco | Busca de sistemas externos |
| **Foco** | Consultar e analisar | Coletar e integrar |
| **Uso** | Análises e relatórios | APIs, scraping, automação |
| **Quando usar** | Dados já armazenados | Dados externos, integração |

**Python na engenharia de dados = COMUNICAR e INTEGRAR sistemas externos!**

---

## 🎯 Perguntas de Negócio que Vamos Responder

Este **Dia 2** foi criado para resolver problemas reais de ingestão de dados. Abaixo estão todas as perguntas que vamos responder com os exemplos:

### 🔥 Aquecimento (Fundamentos)

1. **Por que preciso saber Python básico para trabalhar com dados?** *(Exemplo 00)*
2. **O que é uma API e como processar dados JSON?** *(Exemplo 00b)*
3. **Por que usar Pandas ao invés de listas/dicionários?** *(Exemplo 00c)*

### 📂 Ingestão de Dados (Exemplos 1-7)

4. **Como carregar dados de CSVs em Python?** *(Exemplo 1)*
5. **Como combinar dados de múltiplos arquivos?** *(Exemplo 2)*
6. **Como buscar dados de uma API REST?** *(Exemplo 3)*
7. **Como fazer web scraping para coletar dados de sites?** *(Exemplo 4)*
8. **Como ler dados diretamente de um banco de dados?** *(Exemplo 5)*
9. **Como limpar e tratar dados inconsistentes?** *(Exemplo 6)*
10. **Como exportar dados processados para diferentes formatos?** *(Exemplo 7)*

---

## 🔥 Aquecimento: Fundamentos de Python

Antes de começar a trabalhar com ingestão de dados, é essencial entender os fundamentos de Python. Estes exemplos de aquecimento vão garantir que você tenha a base necessária.

### 📚 Exemplos de Aquecimento

#### `exemplo-00-aquecimento-fundamentos.py`
**Conceito:** Fundamentos de Python  
**Pergunta de Negócio:** Por que preciso saber Python básico para trabalhar com dados?  
**O que você aprende:**
- Print e Hello World
- Variáveis e tipos básicos (str, int, float)
- Estruturas de dados (lista, dicionário)
- Métodos úteis
- Por que isso é importante para trabalhar com dados

**Conceitos Python:**
- `print()`: exibir informações
- Variáveis: `str`, `int`, `float`
- Listas: `[]` - coleção ordenada
- Dicionários: `{}` - pares chave-valor
- Métodos: funções dos objetos (`.upper()`, `.strip()`, etc.)

**Por que é importante?**
- APIs retornam dados em JSON (que são dicionários em Python)
- Web scraping extrai strings que precisam ser processadas
- Dados de CSVs são lidos como strings e precisam conversão
- Pandas usa esses conceitos por baixo dos panos

---

#### `exemplo-00b-api-json.py`
**Conceito:** APIs e JSON  
**Pergunta de Negócio:** O que é uma API e como processar dados JSON em Python?  
**O que você aprende:**
- O que é uma API
- O que é JSON
- Como JSON se relaciona com dicionários Python
- Como processar dados de APIs
- Por que isso é essencial para ingestão de dados

**Conceitos Python:**
- `json.loads()`: converte JSON string para dicionário Python
- `json.dumps()`: converte dicionário Python para JSON string
- Acessar dados aninhados: `dados["chave"]["subchave"]`
- Processar listas de dicionários

**Casos de uso:**
- Consumir APIs REST
- Processar respostas de APIs
- Converter entre formatos
- Trabalhar com dados estruturados

---

#### `exemplo-00c-introducao-pandas.py`
**Conceito:** Introdução ao Pandas  
**Pergunta de Negócio:** Por que Pandas é a biblioteca mais usada para dados em Python?  
**O que você aprende:**
- O que é Pandas
- Por que usar Pandas ao invés de listas/dicionários
- Conceitos básicos: Series e DataFrame
- Operações básicas com Pandas
- Por que Pandas é essencial para trabalhar com dados

**Conceitos Python:**
- `pd.Series`: uma coluna de dados
- `pd.DataFrame`: tabela de dados
- Operações: filtros, agregações, cálculos
- `df.groupby()`: agrupar dados
- `df.describe()`: estatísticas descritivas

**Vantagens do Pandas:**
- Operações diretas (sem loops)
- Código limpo e legível
- Otimizado para performance
- Funcionalidades prontas (filtros, agregações, joins)
- Integração com Excel, SQL, APIs

---

## 🎯 Progressão de Aprendizado

### 📂 Nível 1: Leitura Básica (Exemplos 1-2)

#### `exemplo-01-ler-csv.py`
**Conceito:** Ler arquivos CSV com Pandas  
**Pergunta de Negócio:** Como carregar os dados da aula 01 em Python?  
**O que você aprende:**
- Como usar pandas para ler arquivos CSV
- Como explorar dados básicos (head, info, describe)
- Como verificar tipos de dados
- Como acessar colunas e linhas

**Conceitos Python:**
- `pandas.read_csv()`: lê arquivo CSV
- `df.head()`: primeiras linhas
- `df.info()`: informações do DataFrame
- `df.describe()`: estatísticas descritivas

**Resultado Esperado:**
- Dados carregados com sucesso
- Informações básicas exibidas (linhas, colunas, tipos)
- Estatísticas descritivas mostradas

---

#### `exemplo-02-ler-multiplos-csv.py`
**Conceito:** Combinar múltiplos arquivos CSV  
**Pergunta de Negócio:** Como combinar dados de produtos, clientes e vendas?  
**O que você aprende:**
- Como ler múltiplos arquivos CSV
- Como fazer merge (equivalente ao JOIN do SQL)
- Como combinar dados de diferentes fontes
- Como validar dados após combinação

**Conceitos Python:**
- `pd.merge()`: combina DataFrames (equivalente ao JOIN)
- `left_on` e `right_on`: especificar colunas de junção
- `how`: tipo de merge (inner, left, right, outer)
- `suffixes`: sufixos para colunas duplicadas

**Resultado Esperado:**
- Dataset combinado com sucesso
- Informações de produtos, clientes e vendas unificadas
- Validação de dados combinados

---

### 🌐 Nível 2: Integração com Sistemas Externos (Exemplos 3-4)

#### `exemplo-03-ler-api-rest.py`
**Conceito:** Consumir APIs REST  
**Pergunta de Negócio:** Como obter dados de uma API externa em Python?  
**O que você aprende:**
- O que é uma API e por que é importante
- Como fazer requisições HTTP com requests
- Como consumir APIs REST
- Como tratar respostas JSON
- Como trabalhar com diferentes tipos de dados (JSON, imagens)

**Conceitos Python:**
- `requests.get()`: faz requisição HTTP GET
- `response.json()`: converte resposta para dicionário Python
- `response.raise_for_status()`: verifica erros HTTP
- Tratamento de exceções com try/except

**Por que APIs são importantes?**
- Python na engenharia de dados = COMUNICAR com sistemas externos
- SQL trabalha com dados que JÁ EXISTEM no banco
- Python BUSCA dados de sistemas externos via APIs
- Permite integrar dados de múltiplas fontes

**Exemplos práticos:**
- API Bitcoin (Coinbase): preços de criptomoedas em tempo real
- API NASA: imagens e dados espaciais

**Resultado Esperado:**
- Dados obtidos de API Bitcoin com sucesso
- Dados obtidos de API NASA com sucesso
- Respostas JSON convertidas para DataFrame
- Tratamento de erros implementado

---

#### `exemplo-04-web-scraping.py`
**Conceito:** Web Scraping com BeautifulSoup  
**Pergunta de Negócio:** Como coletar dados de sites que não têm API?  
**O que você aprende:**
- Como fazer scraping de páginas HTML
- Como usar BeautifulSoup para parsear HTML
- Como extrair dados específicos de elementos
- Como tratar erros e casos especiais
- Exemplo prático: Mercado Livre

**Conceitos Python:**
- `BeautifulSoup`: parseia HTML
- `soup.find()`: encontra elemento único
- `soup.select()`: encontra múltiplos elementos (CSS selector)
- `get_text()`: extrai texto de elementos

**Por que Web Scraping?**
- Nem todos os sites têm API disponível
- Útil para coletar preços de concorrentes
- Acessa dados públicos de sites
- Último recurso quando não há API

**Exemplo prático:**
- Scraping de produto do Mercado Livre
- Extração de nome, preços (antigo, atual, parcelado)

**Boas práticas:**
- Sempre verificar termos de uso do site
- Usar delays entre requisições
- Respeitar robots.txt
- Usar headers apropriados (User-Agent)
- Prefira APIs quando disponíveis

**Resultado Esperado:**
- Dados extraídos de página do Mercado Livre
- HTML parseado corretamente
- Dados convertidos para DataFrame

---

### 💾 Nível 3: Banco de Dados (Exemplo 5)

#### `exemplo-05-ler-banco-dados.py`
**Conceito:** Conectar Python com bancos de dados SQL  
**Pergunta de Negócio:** Como ler dados diretamente de um banco SQL em Python?  
**O que você aprende:**
- Como conectar Python com SQLite
- Como conectar Python com PostgreSQL
- Como executar queries SQL e trazer para pandas
- Como trabalhar com diferentes tipos de banco

**Conceitos Python:**
- `sqlite3.connect()`: conecta com SQLite
- `pd.read_sql_query()`: executa SQL e retorna DataFrame
- `sqlalchemy.create_engine()`: cria engine para PostgreSQL
- `df.to_sql()`: salva DataFrame em tabela SQL

**Vantagens:**
- Dados sempre atualizados (não precisa exportar CSV)
- Queries complexas diretamente no banco
- Performance melhor para grandes volumes
- Integração nativa com SQL

**Resultado Esperado:**
- Conexão com banco estabelecida
- Queries SQL executadas com sucesso
- Dados retornados como DataFrame

---

### 🧹 Nível 4: Tratamento de Dados (Exemplo 6)

#### `exemplo-06-tratar-dados.py`
**Conceito:** Limpar e preparar dados para análise  
**Pergunta de Negócio:** Como tratar dados inconsistentes e faltantes?  
**O que você aprende:**
- Como identificar dados faltantes (NaN)
- Como tratar valores duplicados
- Como converter tipos de dados
- Como normalizar e limpar strings
- Como tratar outliers

**Conceitos Python:**
- `df.isnull()`: identifica valores faltantes
- `df.dropna()`: remove linhas com valores faltantes
- `df.fillna()`: preenche valores faltantes
- `df.drop_duplicates()`: remove duplicatas
- `pd.to_datetime()`: converte para datetime
- `pd.to_numeric()`: converte para numérico

**Estratégias de tratamento:**
- Remover: quando há muitos dados e poucos faltantes
- Preencher: com média, mediana, moda ou valor padrão
- Interpolar: para séries temporais

**Resultado Esperado:**
- Dados limpos e consistentes
- Valores faltantes tratados
- Tipos de dados corrigidos
- Outliers identificados

---

### 📤 Nível 5: Exportação (Exemplo 7)

#### `exemplo-07-exportar-dados.py`
**Conceito:** Salvar dados processados em diferentes formatos  
**Pergunta de Negócio:** Como exportar dados para CSV, JSON, Excel, etc?  
**O que você aprende:**
- Como exportar para CSV
- Como exportar para JSON
- Como exportar para Excel
- Como exportar para banco de dados
- Como escolher o formato adequado

**Conceitos Python:**
- `df.to_csv()`: exporta para CSV
- `df.to_json()`: exporta para JSON
- `df.to_excel()`: exporta para Excel
- `df.to_sql()`: exporta para banco de dados
- `df.to_parquet()`: exporta para Parquet (otimizado)

**Quando usar cada formato:**
- **CSV**: Universal, fácil de abrir em Excel
- **JSON**: Ideal para APIs e integrações
- **Excel**: Bom para relatórios e apresentações
- **SQLite**: Banco de dados local, permite queries
- **Parquet**: Otimizado para big data, compressão eficiente

**Resultado Esperado:**
- Dados exportados em múltiplos formatos
- Formato escolhido baseado no uso
- Dados prontos para consumo

---

## 🎓 Como Usar

### 1. Instalar Dependências

```bash
# Criar ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 2. Executar Exemplos

```bash
# Navegar para diretório de exemplos
cd aulas/aula-02-python/exemplos

# Executar exemplo
python exemplo-01-ler-csv.py
python exemplo-02-ler-multiplos-csv.py
# ... e assim por diante
```

### 3. Modificar e Experimentar

- Altere os caminhos dos arquivos
- Teste com seus próprios dados
- Combine conceitos de diferentes exemplos
- Crie seus próprios scripts

---

## 📝 Checklist de Aprendizado

Após fazer todos os exemplos, você deve ser capaz de:

### 🔥 Aquecimento (Fundamentos)
- [ ] Usar print e f-strings
- [ ] Trabalhar com variáveis (str, int, float)
- [ ] Usar listas e dicionários
- [ ] Aplicar métodos úteis
- [ ] Entender o que é API e JSON
- [ ] Converter entre JSON e dicionários Python
- [ ] Entender o que é Pandas e por que usar
- [ ] Criar Series e DataFrames
- [ ] Fazer operações básicas com Pandas

### 📂 Ingestão de Dados
- [ ] Ler arquivos CSV com pandas
- [ ] Combinar múltiplos arquivos (merge)
- [ ] Fazer requisições HTTP para APIs
- [ ] Fazer web scraping básico
- [ ] Conectar com bancos de dados (SQLite, PostgreSQL)
- [ ] Executar queries SQL e trazer para pandas
- [ ] Identificar e tratar dados faltantes
- [ ] Remover duplicatas
- [ ] Converter tipos de dados
- [ ] Tratar outliers
- [ ] Exportar para CSV, JSON, Excel, banco de dados
- [ ] Escolher o formato adequado para cada caso

---

## 💡 Dicas

- **Execute em ordem:** Cada exemplo introduz um conceito novo
- **Modifique:** Tente adaptar os scripts para seus próprios dados
- **Combine:** Use conceitos de exemplos anteriores em novos contextos
- **Valide:** Sempre verifique se os dados foram carregados corretamente
- **Pratique:** Crie seus próprios scripts de ingestão

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'pandas'"
```bash
pip install pandas
```

### Erro: "FileNotFoundError: vendas.csv"
- Verifique se os arquivos CSV estão na pasta `data/`
- Verifique o caminho relativo no script

### Erro: "ConnectionError" ao fazer scraping
- Verifique sua conexão com internet
- Alguns sites bloqueiam scraping - use com cuidado
- Adicione delays entre requisições

### Erro: "sqlite3.OperationalError: no such table"
- Execute primeiro o exemplo que cria o banco
- Verifique se o banco foi criado corretamente

---

## 🎯 Próximos Passos

Depois de dominar todos os exemplos:

1. Pratique criando seus próprios scripts de ingestão
2. Combine diferentes fontes de dados
3. Automatize processos de coleta de dados
4. Avance para a **Aula 3: Engenharia de Dados**

---

## 📊 Resumo dos Conceitos por Exemplo

| Exemplo | Conceito Principal | Nível |
|---------|-------------------|-------|
| 00 | Fundamentos Python | Básico |
| 00b | APIs e JSON | Básico |
| 00c | Introdução Pandas | Básico |
| 01 | Ler CSV | Básico |
| 02 | Merge de DataFrames | Básico |
| 03 | API REST | Intermediário |
| 04 | Web Scraping | Intermediário |
| 05 | Banco de Dados | Intermediário |
| 06 | Tratamento de Dados | Intermediário |
| 07 | Exportação | Intermediário |

---

**Total: 10 exemplos práticos (3 de aquecimento + 7 de ingestão) cobrindo Python para dados do básico ao intermediário!** 🚀

---

## 🔗 Recursos Adicionais

- [Documentação Pandas](https://pandas.pydata.org/docs/)
- [Documentação Requests](https://requests.readthedocs.io/)
- [Documentação BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)

---

**Boa jornada! 🐍**

