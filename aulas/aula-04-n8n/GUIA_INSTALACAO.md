# 🚀 Guia Rápido de Instalação - n8n

Este guia te ajuda a instalar e configurar o n8n rapidamente para começar a usar os workflows da Aula 4.

---

## 📋 Opção 1: n8n Cloud (Mais Fácil - Recomendado para Iniciantes)

### Passo 1: Criar Conta
1. Acesse [n8n.io](https://n8n.io)
2. Clique em **"Sign Up"** ou **"Get Started"**
3. Crie sua conta (pode usar GitHub, Google ou email)
4. Plano gratuito permite workflows limitados (suficiente para aprender)

### Passo 2: Acessar Dashboard
1. Após criar conta, você será redirecionado para o dashboard
2. Pronto! Você já pode começar a criar workflows

**Vantagens:**
- ✅ Não precisa instalar nada
- ✅ Acesso de qualquer lugar
- ✅ Atualizações automáticas
- ✅ Sem configuração de servidor

**Desvantagens:**
- ❌ Limite de execuções no plano gratuito
- ❌ Dados ficam na nuvem

---

## 📋 Opção 2: n8n Self-Hosted (Recomendado para Produção)

### Via Docker (Recomendado)

#### Pré-requisitos
- Docker instalado ([Download Docker](https://www.docker.com/get-started))

#### Instalação
```bash
# Criar diretório para dados do n8n
mkdir -p ~/.n8n

# Executar n8n via Docker
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  n8nio/n8n
```

#### Acessar
- Abra o navegador em: `http://localhost:5678`
- Crie sua conta de administrador na primeira vez

#### Parar o Container
```bash
docker stop n8n
```

#### Iniciar Novamente
```bash
docker start n8n
```

---

### Via npm (Node.js)

#### Pré-requisitos
- Node.js 18+ instalado ([Download Node.js](https://nodejs.org/))

#### Instalação
```bash
# Instalar n8n globalmente
npm install n8n -g

# Iniciar n8n
n8n start
```

#### Acessar
- Abra o navegador em: `http://localhost:5678`
- Crie sua conta de administrador na primeira vez

---

## 🔧 Configuração Inicial

### 1. Criar Credenciais do Supabase

#### Passo 1: Obter Credenciais do Supabase Dashboard

**Para conexão PostgreSQL (usado nesta aula):**

1. Acesse o [Supabase Dashboard](https://app.supabase.com)
2. Faça login e selecione seu projeto
3. Vá em **Settings** (ícone de engrenagem no menu lateral)
4. Clique em **Database**

**Opção A: Connection String Direta**
- Na seção **Connection string**, você verá:
  - **Host**: `db.xxxxx.supabase.co` (exemplo: `db.zsutlhnykwxackvunyvr.supabase.co`)
  - **Port**: `5432`
  - **Database**: `postgres`
  - **User**: `postgres.xxxxx` (exemplo: `postgres.zsutlhnykwxackvunyvr`)
  - **Password**: A senha que você definiu ao criar o projeto

**Opção B: Connection Pooler (Recomendado para produção)**
- Na mesma página, procure por **Connection Pooling**
- Use a URL do pooler (exemplo: `aws-0-us-west-2.pooler.supabase.com`)
- A porta geralmente é `5432`
- User e Password são os mesmos da Connection String

**Para usar a Data API (REST API) do Supabase:**

1. No Supabase Dashboard, vá em **Settings** → **API**
2. Na seção **Project API keys**, você encontrará:
   - **URL**: `https://xxxxx.supabase.co` (sua URL do projeto - ex: `https://zsutlhnykwxackvunyvr.supabase.co`)
   - **anon/public key**: Para uso público (com Row Level Security)
   - **service_role key**: Para uso administrativo (⚠️ NUNCA exponha publicamente)

3. **⚠️ IMPORTANTE: Configurar Exposed Schemas**
   
   Para fazer queries nas tabelas via Data API, você precisa expor os schemas:
   
   - Na mesma página **Settings** → **API**, procure pela seção **"Exposed schemas"**
   - Esta seção mostra quais schemas estão expostos na API
   - **Adicione os schemas que você quer acessar**:
     - Se suas tabelas estão em `public`, adicione `public`
     - Se suas tabelas estão em `gold` (como na Aula 3), adicione `gold`
     - Se suas tabelas estão em `silver`, adicione `silver`
     - Se suas tabelas estão em `bronze`, adicione `bronze`
   - Você pode adicionar múltiplos schemas separados por vírgula
   - Clique em **Save** para salvar as alterações
   
   **O que são Exposed Schemas?**
   > "The schemas to expose in your API. Tables, views and stored procedures in these schemas will get API endpoints."
   
   - Tabelas, views e stored procedures nos schemas expostos terão endpoints REST automáticos
   - Sem expor o schema, você **não conseguirá** acessar as tabelas via Data API REST
   - Exemplo: Se você quer acessar `gold.gold_kpi_produtos_top_receita`, precisa expor o schema `gold`

4. Para agentes de IA que precisam acessar dados via API REST, use:
   - **URL**: A URL do projeto (ex: `https://xxxxx.supabase.co`)
   - **service_role key**: A chave service_role (tem acesso total ao banco)
   - **Schemas expostos**: Certifique-se de que os schemas necessários estão configurados em "Exposed schemas"

**📝 Resumo:**
- **PostgreSQL direto**: Use credenciais de **Settings → Database** (Host, User, Password)
- **Data API REST**: Use **URL** e **service_role key** de **Settings → API**
- **⚠️ IMPORTANTE para Data API**: Configure **Exposed schemas** em **Settings → API** para liberar acesso às tabelas

#### Passo 2: Configurar no n8n

1. No n8n, clique no ícone de **chave** (Credentials) no menu lateral
2. Clique em **"Add Credential"**
3. Procure por **"Postgres"** e selecione
4. Preencha os dados obtidos do Supabase:

```
Host: [do Supabase Dashboard - ex: aws-0-us-west-2.pooler.supabase.com]
Port: 5432
Database: postgres
User: [do Supabase Dashboard - ex: postgres.zsutlhnykwxackvunyvr]
Password: [sua senha do projeto Supabase]
SSL: Enable SSL
```

5. Clique em **"Test"** para verificar conexão
6. Clique em **"Save"** e dê um nome: **"Supabase Jornada"**

**⚠️ Importante:**
- Mantenha suas credenciais seguras
- Nunca compartilhe a **service_role key** publicamente
- Use **Connection Pooler** em produção para melhor performance
- Para esta aula, usamos **PostgreSQL direto** (não a Data API)
- Se precisar usar a Data API REST:
  - Você precisará da **URL** e **service_role key** de **Settings → API**
  - **OBRIGATÓRIO**: Configure os **Exposed schemas** em **Settings → API** para liberar acesso às tabelas
  - Sem expor o schema, as tabelas não estarão acessíveis via Data API REST

---

### 2. Criar Bot no Telegram

#### Passo 1: Criar Bot com BotFather
1. Abra o Telegram
2. Procure por **@BotFather**
3. Envie `/newbot`
4. Escolha um nome: `Jornada Dados Bot`
5. Escolha um username: `jornada_dados_bot` (deve terminar com `_bot`)
6. **Copie o Token** que o BotFather fornecer

**Exemplo de Token:**
```
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

#### Passo 2: Configurar no n8n
1. No n8n, vá em **Credentials**
2. Clique em **"Add Credential"**
3. Procure por **"Telegram"** e selecione
4. Cole o **Token** do bot
5. Clique em **"Save"** e dê um nome: **"Telegram Bot Jornada"**

---

### 3. Configurar OpenAI (para Agentes de IA)

#### Passo 1: Criar Conta OpenAI
1. Acesse [OpenAI Platform](https://platform.openai.com)
2. Crie uma conta ou faça login
3. Vá em **API Keys** no menu lateral
4. Clique em **"Create new secret key"**
5. **Copie a API Key** (você só verá ela uma vez!)

**Exemplo de API Key:**
```
sk-1234567890abcdefghijklmnopqrstuvwxyz
```

#### Passo 2: Configurar no n8n
1. No n8n, vá em **Credentials**
2. Clique em **"Add Credential"**
3. Procure por **"OpenAI"** e selecione
4. Cole a **API Key**
5. Clique em **"Save"** e dê um nome: **"OpenAI API"**

**Nota:** O uso da API OpenAI tem custos. O modelo `gpt-4o-mini` é mais barato e suficiente para aprender.

---

### 4. Testar o Bot

#### Esquenta: Hello World
1. Abra o Telegram
2. Procure pelo seu bot
3. Envie qualquer pergunta: "Olá, como você está?"
4. O bot deve responder de forma amigável

#### Etapa 1: Agente de Turismo
1. Envie: "O que fazer em Salvador?"
2. O bot deve responder com um roteiro completo
3. Envie: "Qual é a capital do Brasil?" (fora do tema)
4. O bot deve responder educadamente que só ajuda com turismo

#### Etapa 2: Memória
1. Envie: "Eu sou o Luciano, o que fazer no Rio de Janeiro?"
2. O bot responde sobre Rio
3. Envie: "Qual é o meu nome?"
4. O bot deve lembrar: "Seu nome é Luciano!"

#### Etapa 3: Tool + Supabase
1. Envie: "Quais são os top 5 produtos mais vendidos?"
2. O bot deve consultar o banco e responder com dados reais
3. Envie: "Quanto foi a receita total?"
4. O bot deve consultar e responder com valor real

---

## 📥 Importar Workflows

### Passo 1: Baixar Workflow
1. Abra o arquivo JSON do workflow (ex: `exemplo-01-query-supabase-telegram.json`)
2. Copie todo o conteúdo

### Passo 2: Importar no n8n
1. No n8n, clique em **"Workflows"** no menu lateral
2. Clique no botão **"+"** (Add Workflow)
3. Clique nos **três pontos** (menu) no canto superior direito
4. Selecione **"Import from File"** ou **"Import from URL"**
5. Cole o conteúdo do JSON ou selecione o arquivo
6. Clique em **"Import"**

### Passo 3: Configurar Credenciais
1. Após importar, você verá os nós do workflow
2. Clique nos nós que têm ícone de **chave** (precisam de credenciais)
3. Selecione as credenciais que você criou:
   - **PostgreSQL**: Selecione "Supabase Jornada" (apenas para Etapa 3)
   - **Telegram**: Selecione "Telegram Bot Jornada"
   - **OpenAI**: Selecione "OpenAI API" (para todos os workflows de agente)

### Passo 4: Ativar Workflow
1. No canto superior direito, há um **toggle** (switch)
2. Ative o workflow clicando no toggle
3. O workflow agora está ativo e funcionando!

---

## ✅ Verificar se Está Funcionando

### Testar Workflow Manualmente
1. No workflow, clique no botão **"Execute Workflow"** (play)
2. Veja a execução em tempo real
3. Verifique se cada nó executa com sucesso (ícone verde)

### Testar Bot no Telegram
1. Abra o Telegram
2. Procure pelo seu bot
3. Envie `/start` - deve responder com mensagem de boas-vindas
4. Envie `/help` - deve listar comandos disponíveis
5. Envie `/top_produtos` - deve retornar top produtos

---

## 🐛 Troubleshooting

### Bot não responde
- ✅ Verifique se o workflow está **ativo** (toggle no canto superior direito)
- ✅ Verifique se as **credentials** do Telegram estão corretas
- ✅ Verifique se o **token** do bot está correto
- ✅ Veja os **logs** do workflow (clique em "Executions" no menu lateral)

### Erro de conexão com Supabase
- ✅ Verifique se as **credentials** do PostgreSQL estão corretas
- ✅ Verifique se o **host** e **port** estão corretos
- ✅ Verifique se o **SSL** está habilitado
- ✅ Teste a conexão clicando em **"Test"** nas credentials

### Workflow não executa
- ✅ Verifique se o workflow está **ativo**
- ✅ Verifique se há **erros** nos nós (ícones vermelhos)
- ✅ Veja os **logs** de execução para identificar o problema

---

## 📚 Próximos Passos

Agora que você tem o n8n configurado:

1. ✅ Importe os workflows da pasta `workflows/`
2. ✅ Configure as credenciais (Supabase e Telegram)
3. ✅ Teste cada workflow
4. ✅ Explore os exemplos e adapte para suas necessidades

**Boa sorte! 🚀**

