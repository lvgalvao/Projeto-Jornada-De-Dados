"""
Gerador de datasets sintéticos (4 CSVs) para a Aula 01 (SQL & Analytics) com Faker.

Gera:
- produtos.csv
- clientes.csv
- vendas.csv
- preco_competidores.csv

Características (como você pediu):
- 200 produtos
- 50 clientes (10 VIP, 20 TOP_TIER, 20 REGULAR)
- ~100 vendas por dia (por N dias)
- sem distribuição normal (tudo baseado em buckets/ponderações discretas)
- 30 produtos "top sellers" vendem mais (peso maior nas vendas)
- clientes VIP e TOP_TIER compram mais (peso maior nas vendas)
- concorrentes com preços coletados (para comparar com "mercado")

Instalação:
  pip install faker

Execução:
  python generate_datasets.py

Obs:
- Os CSVs são pensados para explicar SELECT/FROM/WHERE/GROUP BY/HAVING/ORDER BY/JOIN/CASE.
"""

from __future__ import annotations

import csv
import os
import random
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, date, time
from typing import Dict, List, Tuple

from faker import Faker


# ----------------------------
# CONFIG
# ----------------------------
SEED = 42
LOCALE = "pt_BR"
OUTPUT_DIR = "data"

N_PRODUCTS = 200
N_CUSTOMERS = 50

# Produtos extras que não serão vendidos (para LEFT JOIN)
N_PRODUCTS_UNSOLD = 15

# Vendas com produtos não cadastrados (para RIGHT JOIN)
N_SALES_UNREGISTERED = 20

DAYS = 30
SALES_PER_DAY = 100

TOP_PRODUCTS = 30
VIP_CUSTOMERS = 10
TOP_TIER_CUSTOMERS = 20  # VIP + TOP_TIER = 30; restante REGULAR = 20

SALES_CHANNEL_WEIGHTS = {
    "ecommerce": 0.72,
    "loja_fisica": 0.28,
}

# quantidades (discreto)
QTY_WEIGHTS: List[Tuple[int, float]] = [
    (1, 0.72),
    (2, 0.18),
    (3, 0.06),
    (4, 0.03),
    (5, 0.01),
]

# preço base do produto (R$) por buckets (discreto)
PRICE_BUCKETS: List[Tuple[float, float, float]] = [
    (29.90, 59.90, 0.18),
    (59.90, 119.90, 0.32),
    (119.90, 249.90, 0.26),
    (249.90, 499.90, 0.16),
    (499.90, 1499.90, 0.08),
]

# horários de venda por janelas (discreto)
PURCHASE_HOUR_WINDOWS: List[Tuple[int, int, float]] = [
    (8, 12, 0.25),
    (12, 15, 0.15),
    (15, 19, 0.30),
    (19, 23, 0.25),
    (23, 24, 0.03),
    (0, 2, 0.02),
]

# pesos por segmento de cliente (quem compra mais)
CUSTOMER_SEGMENT_WEIGHTS = {
    "VIP": 12.0,
    "TOP_TIER": 5.0,
    "REGULAR": 1.0,
}

# 30 produtos vendem mais (peso multiplicador)
TOP_PRODUCT_WEIGHT_MULTIPLIER = 8.0

# promoções na venda (unit_price vs current_price)
# valores discretos (sem normal)
PROMO_FACTORS: List[Tuple[float, float]] = [
    (1.00, 0.55),
    (0.95, 0.15),
    (0.90, 0.15),
    (0.85, 0.10),
    (1.10, 0.05),
]

# concorrentes
COMPETITORS = ["Mercado Livre", "Amazon", "Magalu", "Shopee"]
COMPETITOR_COVERAGE = 0.85  # nem todo concorrente terá preço para todo produto

# variação de preço no concorrente em relação ao nosso current_price (discreto)
# (multiplier, prob)  -> não-normal
COMP_PRICE_FACTORS: List[Tuple[float, float]] = [
    (0.92, 0.10),
    (0.95, 0.18),
    (0.98, 0.22),
    (1.00, 0.20),
    (1.03, 0.15),
    (1.06, 0.10),
    (1.10, 0.05),
]

CATEGORIES = [
    "Eletrônicos", "Casa", "Cozinha", "Moda", "Esporte",
    "Beleza", "Informática", "Acessórios", "Áudio", "Games", "Tênis"
]

BRANDS = [
    "Samsung", "Apple", "LG", "Sony", "Dell", "Lenovo", "Acer", "Asus", "Xiaomi",
    "Motorola", "Philips", "Electrolux", "Brastemp", "Consul", "Arno", "Mondial",
    "Nike", "Adidas", "Puma", "O Boticário"
]

ESTADOS_BRASIL = [
    "SP", "RJ", "MG", "RS", "PR", "SC", "BA", "GO", "PE", "CE",
    "DF", "PA", "ES", "PB", "AM", "RN", "AL", "MT", "PI", "MS",
    "SE", "MA", "RO", "TO", "AC", "AP", "RR"
]

# Nomes de produtos brasileiros reais por categoria
PRODUCT_NAMES_BY_CATEGORY = {
    "Eletrônicos": [
        "Smartphone Galaxy A54", "iPhone 14", "TV LED 50 Polegadas", "Notebook Inspiron 15",
        "Tablet iPad Air", "Smartwatch Galaxy Watch", "Fone Bluetooth JBL", "Caixa de Som JBL",
        "Carregador Wireless", "Cabo USB-C", "Power Bank 20000mAh", "Mouse Gamer Logitech",
        "Teclado Mecânico RGB", "Webcam Full HD", "Microfone USB", "Monitor 24 Polegadas",
        "HD Externo 1TB", "SSD 500GB", "Roteador Wi-Fi 6", "Smart TV 43 Polegadas"
    ],
    "Casa": [
        "Cortina Blackout", "Tapete Persa", "Luminária de Mesa", "Abajur Moderno",
        "Almofada Decorativa", "Quadro Decorativo", "Vaso de Cerâmica", "Cesto de Vime",
        "Organizador de Gaveta", "Porta-retrato", "Espelho de Parede", "Relógio de Parede",
        "Jogo de Toalhas", "Edredom Casal", "Travesseiro Ortopédico", "Cobertor de Lã",
        "Cortina de Rolo", "Persiana Vertical", "Cortina Box", "Tela Mosquiteira"
    ],
    "Cozinha": [
        "Panela de Pressão", "Jogo de Panelas Antiaderente", "Faqueiro Inox 12 Peças",
        "Processador de Alimentos", "Liquidificador Turbo", "Batedeira Planetária",
        "Frigideira Antiaderente", "Assadeira de Vidro", "Forma de Bolo Redonda",
        "Tábua de Corte", "Kit Utensílios de Cozinha", "Espátula de Silicone",
        "Peneira Inox", "Ralador de Queijo", "Descascador de Legumes", "Abre-latas",
        "Garrafa Térmica 1L", "Jarra de Vidro", "Tigela de Vidro", "Porta-temperos"
    ],
    "Moda": [
        "Camiseta Básica", "Calça Jeans Skinny", "Vestido Floral", "Blusa de Manga Longa",
        "Shorts Jeans", "Saia Midi", "Blazer Social", "Jaqueta Jeans", "Cardigan de Lã",
        "Camisa Social", "Polo Masculina", "Bermuda Tactel", "Legging Esportiva",
        "Blusa de Algodão", "Vestido Casual", "Macacão Feminino", "Conjunto de Malha",
        "Casaco de Inverno", "Blusa de Frio", "Regata Básica"
    ],
    "Esporte": [
        "Bicicleta Ergométrica", "Esteira Elétrica", "Halteres Ajustáveis", "Colchonete Yoga",
        "Corda de Pular", "Elástico de Resistência", "Pesos de Pulso", "Faixa Elástica",
        "Bola de Futebol", "Bola de Basquete", "Raquete de Tênis", "Tênis de Corrida",
        "Roupa de Academia", "Garrafa Esportiva", "Mochila Esportiva", "Relógio Esportivo",
        "Protetor Solar FPS 50", "Óculos de Natação", "Boné Esportivo", "Meia Esportiva"
    ],
    "Beleza": [
        "Shampoo Anticaspa", "Condicionador Hidratante", "Sabonete Facial", "Creme Hidratante",
        "Protetor Solar Facial", "Máscara Facial", "Sérum Vitamina C", "Tônico Facial",
        "Esmalte", "Base Líquida", "Batom Matte", "Máscara para Cílios",
        "Pincel de Maquiagem", "Paleta de Sombras", "Blush em Pó", "Iluminador Líquido",
        "Perfume 100ml", "Desodorante Roll-on", "Creme para Mãos", "Hidratante Labial"
    ],
    "Informática": [
        "Mouse Óptico USB", "Teclado Multilaser", "Headset Gamer", "SSD SATA 256GB",
        "Memória RAM 8GB", "HD Externo 2TB", "Webcam 1080p", "Hub USB 4 Portas",
        "Adaptador HDMI-VGA", "Cabo HDMI 2m", "Cooler para Notebook", "Suporte para Monitor",
        "Mesa para Notebook", "Mouse Pad Gamer", "Fonte PC 500W", "Gabinete ATX",
        "Placa de Vídeo GTX", "Processador Intel i5", "Placa Mãe B450", "Fonte ATX 600W"
    ],
    "Acessórios": [
        "Bolsa Feminina", "Mochila Escolar", "Carteira de Couro", "Cinto de Couro",
        "Óculos de Sol", "Relógio Analógico", "Pulseira de Prata", "Colar de Ouro",
        "Brincos de Prata", "Anel de Prata", "Chaveiro Personalizado", "Porta-moedas",
        "Necessaire", "Estojo Escolar", "Agenda 2024", "Caderno Universitário",
        "Caneta Esferográfica", "Marcador de Texto", "Post-it", "Clips de Papel"
    ],
    "Áudio": [
        "Fone de Ouvido Bluetooth", "Caixa de Som Portátil", "Microfone Condensador",
        "Fone de Ouvido com Fio", "Caixa de Som 2.1", "Soundbar TV", "Amplificador de Áudio",
        "Mixer de Áudio", "Interface de Áudio USB", "Fone Gamer RGB", "Headset com Microfone",
        "Caixa de Som Bluetooth", "Fone Intra-auricular", "Alto-falante Bluetooth",
        "Microfone de Lapela", "Gravador de Voz", "Rádio AM/FM", "Toca-discos USB",
        "Caixa de Som 5.1", "Fone de Ouvido Esportivo"
    ],
    "Games": [
        "Controle Xbox", "Controle PlayStation", "Joystick Arcade", "Cadeira Gamer",
        "Mouse Gamer RGB", "Teclado Gamer Mecânico", "Headset Gamer 7.1", "Webcam para Stream",
        "Microfone para Stream", "Iluminador para Stream", "Suporte para Controle",
        "Cabo HDMI 4K", "Adaptador USB-C", "Hub USB Gamer", "Mouse Pad RGB",
        "Teclado Gamer RGB", "Fone Gamer Wireless", "Controle Pro", "Kit Gamer Completo"
    ],
    "Tênis": [
        "Tênis Nike Air Max", "Tênis Adidas Ultraboost", "Tênis Puma Suede",
        "Tênis Nike Dunk", "Tênis Adidas Stan Smith", "Tênis Puma RS-X",
        "Tênis Nike Revolution", "Tênis Adidas Forum", "Tênis Puma Speedcat",
        "Tênis Nike Court", "Tênis Adidas Samba", "Tênis Puma Future",
        "Tênis Nike Blazer", "Tênis Adidas Gazelle", "Tênis Puma Thunder"
    ]
}


# ----------------------------
# MODELS
# ----------------------------
@dataclass
class Product:
    product_id: str
    product_name: str
    category: str
    brand: str
    current_price: float
    created_at: str
    is_top_seller: bool


@dataclass
class Customer:
    customer_id: str
    customer_name: str
    estado: str
    pais: str
    created_at: str


@dataclass
class Sale:
    sale_id: str
    sale_date: str  # timestamp
    customer_id: str
    product_id: str
    sales_channel: str
    quantity: int
    unit_price: float


@dataclass
class CompetitorPrice:
    product_id: str
    competitor_name: str
    competitor_price: float
    collected_at: str  # timestamp


# ----------------------------
# HELPERS
# ----------------------------
def make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def safe_mkdir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def choose_from_dict_weight(d: Dict[str, float]) -> str:
    keys = list(d.keys())
    weights = list(d.values())
    return random.choices(keys, weights=weights, k=1)[0]


def sample_qty() -> int:
    values = [v for v, _p in QTY_WEIGHTS]
    probs = [_p for _v, _p in QTY_WEIGHTS]
    return random.choices(values, weights=probs, k=1)[0]


def sample_bucket_float(buckets: List[Tuple[float, float, float]]) -> float:
    ranges = [(a, b) for a, b, _p in buckets]
    probs = [_p for _a, _b, _p in buckets]
    a, b = random.choices(ranges, weights=probs, k=1)[0]
    raw = random.uniform(a, b)
    # "cara de varejo": centavos discretos
    cents = random.choices([0.90, 0.99, 0.50, 0.00], weights=[0.55, 0.25, 0.10, 0.10], k=1)[0]
    val = float(int(raw)) + cents
    return round(val, 2)


def random_datetime_on_day(d: date) -> datetime:
    windows = [(a, b) for a, b, _p in PURCHASE_HOUR_WINDOWS]
    probs = [_p for _a, _b, _p in PURCHASE_HOUR_WINDOWS]
    start_h, end_h = random.choices(windows, weights=probs, k=1)[0]
    hour = random.randint(start_h, max(start_h, end_h - 1))
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.combine(d, time(hour=hour, minute=minute, second=second))


def sample_discrete_factor(options: List[Tuple[float, float]]) -> float:
    vals = [v for v, _p in options]
    probs = [_p for _v, _p in options]
    return random.choices(vals, weights=probs, k=1)[0]


# ----------------------------
# GENERATORS
# ----------------------------
def generate_products(fake: Faker) -> List[Product]:
    # define ids e top sellers
    # Criamos produtos extras que não serão vendidos (para LEFT JOIN)
    total_products = N_PRODUCTS + N_PRODUCTS_UNSOLD
    product_ids = [make_id("prd") for _ in range(total_products)]
    
    # Definir quantos produtos serão tênis (os menos vendidos)
    # Vamos colocar tênis no final da lista para serem os menos vendidos
    N_TENIS = 15  # Quantidade de produtos de tênis
    tenis_start_idx = total_products - N_TENIS - N_PRODUCTS_UNSOLD
    tenis_end_idx = total_products - N_PRODUCTS_UNSOLD
    tenis_product_ids = set(product_ids[tenis_start_idx:tenis_end_idx])
    
    # Top sellers são os primeiros produtos, mas NÃO podem ser tênis
    # Garantir que top sellers não sejam tênis
    top_seller_candidates = [pid for pid in product_ids[:TOP_PRODUCTS + N_TENIS] if pid not in tenis_product_ids]
    top_seller_set = set(top_seller_candidates[:TOP_PRODUCTS])

    products: List[Product] = []
    for idx, pid in enumerate(product_ids):
        # Produtos de tênis no final (menos vendidos)
        if pid in tenis_product_ids:
            category = "Tênis"
            # Usar marcas de esporte para tênis
            brand = random.choice(["Nike", "Adidas", "Puma"])
            # Nome de tênis real
            product_name = random.choice(PRODUCT_NAMES_BY_CATEGORY["Tênis"])
        else:
            category = random.choice([c for c in CATEGORIES if c != "Tênis"])
            # Selecionar nome real baseado na categoria
            product_name = random.choice(PRODUCT_NAMES_BY_CATEGORY[category])
            # Extrair marca do nome do produto ou usar aleatória
            # Se o nome contém uma marca conhecida, usar ela, senão escolher aleatória
            brand_found = False
            for b in BRANDS:
                if b.lower() in product_name.lower():
                    brand = b
                    brand_found = True
                    break
            if not brand_found:
                brand = random.choice(BRANDS)

        current_price = sample_bucket_float(PRICE_BUCKETS)
        created_at = datetime.now() - timedelta(days=random.randint(10, 1500))

        products.append(
            Product(
                product_id=pid,
                product_name=product_name,
                category=category,
                brand=brand,
                current_price=current_price,
                created_at=iso(created_at),
                is_top_seller=(pid in top_seller_set),
            )
        )
    return products


def generate_customers(fake: Faker) -> List[Customer]:
    customers: List[Customer] = []
    for _ in range(N_CUSTOMERS):
        cid = make_id("cus")
        gender = random.choices(["M", "F"], weights=[0.52, 0.48], k=1)[0]
        name = fake.name_male() if gender == "M" else fake.name_female()
        created_at = datetime.now() - timedelta(days=random.randint(30, 1200), hours=random.randint(0, 23))

        estado = random.choice(ESTADOS_BRASIL)
        
        customers.append(
            Customer(
                customer_id=cid,
                customer_name=name,
                estado=estado,
                pais="Brasil",
                created_at=iso(created_at),
            )
        )
    return customers


def build_weighted_pool_customers(customers: List[Customer]) -> Tuple[List[str], List[float]]:
    ids, weights = [], []
    for c in customers:
        ids.append(c.customer_id)
        # Pesos uniformes - segmentação será criada depois com CASE WHEN baseado em comportamento
        weights.append(1.0)
    return ids, weights


def build_weighted_pool_products(products: List[Product]) -> Tuple[List[str], List[float]]:
    ids, weights = [], []
    for p in products:
        ids.append(p.product_id)
        base = 1.0
        if p.is_top_seller:
            base *= TOP_PRODUCT_WEIGHT_MULTIPLIER
        # Tênis têm peso muito baixo (pouquíssimas vendas)
        if p.category == "Tênis":
            base *= 0.01  # Peso muito baixo para tênis
        else:
            # variação discreta, sem normal
            base *= random.choice([0.8, 1.0, 1.2, 1.5])
        weights.append(base)
    return ids, weights


def generate_sales(customers: List[Customer], products: List[Product]) -> List[Sale]:
    customer_ids, customer_w = build_weighted_pool_customers(customers)
    
    # Separar produtos que serão vendidos dos que não serão
    # Os últimos N_PRODUCTS_UNSOLD produtos não terão vendas (para LEFT JOIN)
    if N_PRODUCTS_UNSOLD > 0:
        products_to_sell = products[:-N_PRODUCTS_UNSOLD]
    else:
        products_to_sell = products
    
    product_ids, product_w = build_weighted_pool_products(products_to_sell)

    # lookup do current_price para gerar unit_price (apenas produtos que serão vendidos)
    price_lookup = {p.product_id: p.current_price for p in products_to_sell}

    start_day = date.today() - timedelta(days=DAYS)

    sales: List[Sale] = []
    
    # Gerar vendas normais (apenas com produtos cadastrados que serão vendidos)
    for i in range(DAYS):
        day = start_day + timedelta(days=i)
        for _ in range(SALES_PER_DAY):
            sale_id = make_id("sal")
            sale_dt = random_datetime_on_day(day)

            customer_id = random.choices(customer_ids, weights=customer_w, k=1)[0]
            product_id = random.choices(product_ids, weights=product_w, k=1)[0]
            sales_channel = choose_from_dict_weight(SALES_CHANNEL_WEIGHTS)

            quantity = sample_qty()

            base_price = price_lookup[product_id]
            factor = sample_discrete_factor(PROMO_FACTORS)
            unit_price = round(base_price * factor, 2)

            sales.append(
                Sale(
                    sale_id=sale_id,
                    sale_date=iso(sale_dt),
                    customer_id=customer_id,
                    product_id=product_id,
                    sales_channel=sales_channel,
                    quantity=quantity,
                    unit_price=unit_price,
                )
            )
    
    # Gerar vendas com produtos NÃO cadastrados (para RIGHT JOIN)
    # Criar IDs de produtos que não existem no catálogo
    registered_product_ids = {p.product_id for p in products}
    for _ in range(N_SALES_UNREGISTERED):
        sale_id = make_id("sal")
        sale_dt = random_datetime_on_day(start_day + timedelta(days=random.randint(0, DAYS-1)))
        
        customer_id = random.choices(customer_ids, weights=customer_w, k=1)[0]
        
        # Criar um product_id que não existe em products
        unregistered_product_id = make_id("prd")
        while unregistered_product_id in registered_product_ids:
            unregistered_product_id = make_id("prd")
        
        sales_channel = choose_from_dict_weight(SALES_CHANNEL_WEIGHTS)
        quantity = sample_qty()
        
        # Preço aleatório para produto não cadastrado
        unit_price = sample_bucket_float(PRICE_BUCKETS)
        factor = sample_discrete_factor(PROMO_FACTORS)
        unit_price = round(unit_price * factor, 2)
        
        sales.append(
            Sale(
                sale_id=sale_id,
                sale_date=iso(sale_dt),
                customer_id=customer_id,
                product_id=unregistered_product_id,
                sales_channel=sales_channel,
                quantity=quantity,
                unit_price=unit_price,
            )
        )
    
    return sales


def generate_competitor_prices(products: List[Product]) -> List[CompetitorPrice]:
    competitor_prices: List[CompetitorPrice] = []
    start_day = date.today() - timedelta(days=1)  # Coleta de 1 dia atrás
    
    # Usar um conjunto para garantir unicidade de (id_produto, nome_concorrente)
    seen_combinations = set()

    for p in products:
        for competitor in COMPETITORS:
            # Verificar se já existe essa combinação
            combination = (p.product_id, competitor)
            if combination in seen_combinations:
                continue
                
            if random.random() > COMPETITOR_COVERAGE:
                continue

            # Apenas 1 coleta por produto/concorrente (único)
            collect_day = start_day
            collected_at = random_datetime_on_day(collect_day)

            # Para tênis: preço do concorrente é metade do nosso (dobro = 2x)
            if p.category == "Tênis":
                factor = 0.5  # Concorrente vende pela metade
            else:
                factor = sample_discrete_factor(COMP_PRICE_FACTORS)
            
            comp_price = round(p.current_price * factor, 2)

            competitor_prices.append(
                CompetitorPrice(
                    product_id=p.product_id,
                    competitor_name=competitor,
                    competitor_price=comp_price,
                    collected_at=iso(collected_at),
                )
            )
            
            # Marcar combinação como vista
            seen_combinations.add(combination)

    return competitor_prices


# ----------------------------
# WRITERS
# ----------------------------
def write_products(path: str, products: List[Product]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_produto", "nome_produto", "categoria", "marca", "preco_atual", "data_criacao"])
        for p in products:
            w.writerow([p.product_id, p.product_name, p.category, p.brand, f"{p.current_price:.2f}", p.created_at])


def write_customers(path: str, customers: List[Customer]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_cliente", "nome_cliente", "estado", "pais", "data_cadastro"])
        for c in customers:
            w.writerow([c.customer_id, c.customer_name, c.estado, c.pais, c.created_at])


def write_sales(path: str, sales: List[Sale]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_venda", "data_venda", "id_cliente", "id_produto", "canal_venda", "quantidade", "preco_unitario"])
        for s in sales:
            w.writerow([s.sale_id, s.sale_date, s.customer_id, s.product_id, s.sales_channel, s.quantity, f"{s.unit_price:.2f}"])


def write_competitor_prices(path: str, comp: List[CompetitorPrice]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id_produto", "nome_concorrente", "preco_concorrente", "data_coleta"])
        for c in comp:
            w.writerow([c.product_id, c.competitor_name, f"{c.competitor_price:.2f}", c.collected_at])


# ----------------------------
# MAIN
# ----------------------------
def main() -> None:
    random.seed(SEED)
    fake = Faker(LOCALE)
    Faker.seed(SEED)

    safe_mkdir(OUTPUT_DIR)

    products = generate_products(fake)
    customers = generate_customers(fake)
    sales = generate_sales(customers, products)
    competitor_prices = generate_competitor_prices(products)

    products_path = os.path.join(OUTPUT_DIR, "produtos.csv")
    customers_path = os.path.join(OUTPUT_DIR, "clientes.csv")
    sales_path = os.path.join(OUTPUT_DIR, "vendas.csv")
    competitor_prices_path = os.path.join(OUTPUT_DIR, "preco_competidores.csv")

    write_products(products_path, products)
    write_customers(customers_path, customers)
    write_sales(sales_path, sales)
    write_competitor_prices(competitor_prices_path, competitor_prices)

    # Resumo rápido (pra você validar)
    top_products_count = sum(1 for p in products if p.is_top_seller)
    
    # Calcular produtos vendidos vs não vendidos
    registered_product_ids = {p.product_id for p in products}
    products_sold = set()
    products_unregistered = set()
    for s in sales:
        if s.product_id in registered_product_ids:
            products_sold.add(s.product_id)
        else:
            products_unregistered.add(s.product_id)
    
    products_unsold = len(products) - len(products_sold)

    print("✅ CSVs gerados com sucesso:")
    print(f"- {products_path}           (products={len(products)} | top_sellers={top_products_count} | não_vendidos={products_unsold})")
    print(f"- {customers_path}          (customers={len(customers)})")
    print(f"- {sales_path}              (sales={len(sales)} | ~{SALES_PER_DAY}/dia por {DAYS} dias | não_cadastrados={len(products_unregistered)})")
    print(f"- {competitor_prices_path}  (rows={len(competitor_prices)} | competitors={len(COMPETITORS)})")
    print("\n💡 Dica: Use LEFT JOIN para encontrar produtos não vendidos e RIGHT JOIN para vendas não cadastradas.")
    print("💡 Dica: Crie a segmentação de clientes usando CASE WHEN baseado no valor de compras (veja exercício-case-when-clientes.sql)")


if __name__ == "__main__":
    main()

