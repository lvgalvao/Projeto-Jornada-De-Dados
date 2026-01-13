"""
============================================
EXEMPLO 4: Web Scraping com BeautifulSoup
============================================
Conceito: Extrair dados de páginas web
Pergunta: Como coletar dados de sites que não têm API?

NESTE EXEMPLO VOCÊ APRENDE:
- Como fazer scraping de páginas HTML
- Como usar BeautifulSoup para parsear HTML
- Como extrair dados específicos de elementos
- Como tratar erros e casos especiais
- Exemplo prático: Mercado Livre

CASO DE NEGÓCIO:
Coletar preços de produtos de sites de concorrentes
para análise competitiva de preços quando não há API disponível
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ============================================
# POR QUE WEB SCRAPING?
# ============================================
# Nem todos os sites têm API disponível
# Web scraping extrai dados diretamente do HTML
# Útil para: preços de concorrentes, notícias, dados públicos


def fazer_requisicao(url: str) -> str:
    """
    Faz requisição HTTP e retorna HTML como string
    
    Args:
        url: URL da página
        
    Returns:
        HTML da página como string
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    
    except Exception as e:
        print(f"❌ Erro ao fazer requisição: {e}")
        return None


def parsear_produto_mercadolivre(html: str) -> dict:
    """
    Extrai informações de produto do HTML do Mercado Livre
    
    Args:
        html: HTML da página do produto
        
    Returns:
        Dicionário com informações do produto
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extrair nome do produto
        nome_element = soup.find('h1', class_='ui-pdp-title')
        nome = nome_element.get_text(strip=True) if nome_element else "Não encontrado"
        
        # Extrair preços
        preco_elements = soup.find_all('span', class_='andes-money-amount__fraction')
        
        if len(preco_elements) >= 3:
            preco_antigo = int(preco_elements[0].get_text(strip=True).replace('.', ''))
            preco_atual = int(preco_elements[1].get_text(strip=True).replace('.', ''))
            preco_parcela = int(preco_elements[2].get_text(strip=True).replace('.', ''))
        else:
            # Se não encontrar 3 preços, tenta encontrar pelo menos 1
            preco_antigo = None
            preco_atual = int(preco_elements[0].get_text(strip=True).replace('.', '')) if preco_elements else None
            preco_parcela = None
        
        return {
            'nome_produto': nome,
            'preco_antigo': preco_antigo,
            'preco_atual': preco_atual,
            'preco_parcela': preco_parcela,
            'timestamp': pd.Timestamp.now().isoformat()
        }
    
    except Exception as e:
        print(f"❌ Erro ao parsear HTML: {e}")
        return None


# ============================================
# EXEMPLO 1: Scraping Básico
# ============================================

print("=" * 50)
print("EXEMPLO 1: Scraping Básico")
print("=" * 50)

# Página simples de exemplo
url_exemplo = "https://example.com"
html = fazer_requisicao(url_exemplo)

if html:
    soup = BeautifulSoup(html, 'html.parser')
    titulo = soup.find('h1')
    if titulo:
        print(f"✅ Título encontrado: {titulo.get_text()}")


# ============================================
# EXEMPLO 2: Scraping Mercado Livre (Produto)
# ============================================

print("\n" + "=" * 50)
print("EXEMPLO 2: Scraping Mercado Livre - Produto")
print("=" * 50)

# URL de exemplo do Mercado Livre
# NOTA: URLs do Mercado Livre podem mudar, este é um exemplo
url_ml = "https://www.mercadolivre.com.br/apple-iphone-16-pro-1-tb-titnio-preto-distribuidor-autorizado/p/MLB1040287851"

print(f"Buscando dados de: {url_ml}")

# Fazer requisição
html_ml = fazer_requisicao(url_ml)

if html_ml:
    # Parsear dados do produto
    dados_produto = parsear_produto_mercadolivre(html_ml)
    
    if dados_produto:
        print(f"\n✅ Dados extraídos:")
        print(f"   Nome: {dados_produto['nome_produto']}")
        if dados_produto['preco_antigo']:
            print(f"   Preço antigo: R$ {dados_produto['preco_antigo']:,.2f}")
        if dados_produto['preco_atual']:
            print(f"   Preço atual: R$ {dados_produto['preco_atual']:,.2f}")
        if dados_produto['preco_parcela']:
            print(f"   Preço parcelado: R$ {dados_produto['preco_parcela']:,.2f}")
        
        # Converter para DataFrame
        df_produto = pd.DataFrame([dados_produto])
        print(f"\nDataFrame criado:")
        print(df_produto)
    else:
        print("⚠️ Não foi possível extrair dados. A estrutura do site pode ter mudado.")
else:
    print("⚠️ Não foi possível acessar a página. Verifique a URL ou sua conexão.")


# ============================================
# EXEMPLO 3: Scraping com Seletores CSS
# ============================================

print("\n" + "=" * 50)
print("EXEMPLO 3: Usando Seletores CSS")
print("=" * 50)

# Exemplo de como usar seletores CSS
if html_ml:
    soup = BeautifulSoup(html_ml, 'html.parser')
    
    # Buscar elementos usando seletores CSS
    # Exemplo: buscar todos os links
    links = soup.select('a[href]')
    print(f"✅ Encontrados {len(links)} links na página")
    
    # Buscar elementos específicos
    # Exemplo: buscar imagens
    imagens = soup.select('img[src]')
    print(f"✅ Encontradas {len(imagens)} imagens na página")


# ============================================
# BOAS PRÁTICAS
# ============================================

print("\n" + "=" * 50)
print("⚠️ BOAS PRÁTICAS DE WEB SCRAPING")
print("=" * 50)
print("""
1. ✅ Sempre verifique os termos de uso do site
2. ✅ Use delays entre requisições (time.sleep())
3. ✅ Respeite robots.txt
4. ✅ Use headers apropriados (User-Agent)
5. ✅ Implemente tratamento de erros robusto
6. ✅ Prefira APIs quando disponíveis (mais confiável)
7. ✅ Não sobrecarregue o servidor com muitas requisições
8. ✅ Sites podem mudar estrutura - código pode quebrar
""")


# ============================================
# COMPARAÇÃO: API vs WEB SCRAPING
# ============================================

print("\n" + "=" * 50)
print("💡 API vs WEB SCRAPING")
print("=" * 50)
print("""
API (Application Programming Interface):
✅ Forma oficial de acessar dados
✅ Estruturado e confiável
✅ Documentação disponível
✅ Mais rápido e eficiente
✅ Menos chance de quebrar

WEB SCRAPING:
✅ Útil quando não há API
✅ Acessa dados públicos
✅ Pode quebrar se site mudar
✅ Mais lento (precisa parsear HTML)
✅ Pode violar termos de uso

RECOMENDAÇÃO: Use API quando possível, scraping como último recurso.
""")
