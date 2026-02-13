import pandas as pd
import random
from datetime import datetime, timedelta

# Lista de produtos e marcas
produtos = [
    "Camiseta", "Calça", "Boné", "Moletom",
    "Regata", "Bermuda", "Casaco", "Meias"
]

marcas = ["Class", "Suf Gang", "New Era", "Tears", "Sopro", "Baw Clothing", "Nike"]

# Preço base estimado por produto por marca (em R$)
precos = {
    "Camiseta": {"Nike": 129.99, "Suf Gang": 199.00, "Class": 150.00, "Baw Clothing": 180.00, "Sopro": 160.00, "Tears": 170.00, "New Era": 140.00},
    "Calça": {"Nike": 299.90, "Suf Gang": 249.00, "Class": 230.00, "Baw Clothing": 260.00, "Sopro": 240.00, "Tears": 220.00, "New Era": 210.00},
    "Boné": {"Nike": 139.90, "New Era": 49.99, "Suf Gang": 79.00, "Class": 80.00, "Baw Clothing": 85.00, "Sopro": 75.00, "Tears": 78.00},
    "Moletom": {"Nike": 359.90, "Suf Gang": 299.00, "Class": 280.00, "Baw Clothing": 320.00, "Sopro": 270.00, "Tears": 290.00, "New Era": 250.00},
    "Regata": {"Nike": 99.90, "Suf Gang": 89.00, "Class": 95.00, "Baw Clothing": 110.00, "Sopro": 90.00, "Tears": 100.00, "New Era": 85.00},
    "Bermuda": {"Nike": 189.99, "Suf Gang": 170.00, "Class": 160.00, "Baw Clothing": 180.00, "Sopro": 165.00, "Tears": 175.00, "New Era": 150.00},
    "Casaco": {"Nike": 399.90, "Suf Gang": 350.00, "Class": 330.00, "Baw Clothing": 360.00, "Sopro": 340.00, "Tears": 345.00, "New Era": 300.00},
    "Meias": {"Nike": 49.99, "Suf Gang": 35.00, "Class": 40.00, "Baw Clothing": 45.00, "Sopro": 38.00, "Tears": 42.00, "New Era": 30.00},
}

# Gera período de 30 dias de vendas
data_inicio = datetime(2026, 2, 1)
dias = 30

registros = []
for i in range(dias):
    data_atual = (data_inicio + timedelta(days=i)).strftime("%Y-%m-%d")

    num_vendas = random.randint(5, 10)
    for _ in range(num_vendas):
        produto = random.choice(produtos)
        marca = random.choice(marcas)

        # Se não tiver preço específico, pegar o genérico da Nike
        if produto not in precos or marca not in precos[produto]:
            marca = "Nike"
        preco_unitario = precos[produto][marca]

        quantidade = random.randint(1, 3)
        valor = round(preco_unitario * quantidade, 2)

        registros.append({
            "data": data_atual,
            "produto": produto,
            "marca": marca,
            "quantidade": quantidade,
            "valor": valor
        })


df = pd.DataFrame(registros)
df.to_csv("vendas_marcas_exemplo.csv", index=False)
print("Arquivo vendas_marcas_exemplo.csv gerado com sucesso!")