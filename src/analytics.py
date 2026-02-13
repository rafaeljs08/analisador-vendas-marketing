import pandas as pd

def analyze_by_brand(df):
    brand_analysis = (
        df.groupby("marca")
        .agg(
            quantidade_total=("quantidade", "sum"),
            faturamento_total=("valor", "sum"),
            num_vendas=("produto", "count")
        )
        .sort_values("faturamento_total", ascending=False)
        .reset_index()
    )

    return brand_analysis
def compute_kpis(df: pd.DataFrame) -> dict:
    faturamento_total = float(df["valor"].sum())
    itens_vendidos = int(df["quantidade"].sum())
    num_vendas = int(len(df))
    dias = int(df["data"].dt.date.nunique())

    ticket_medio = faturamento_total / num_vendas if num_vendas > 0 else 0.0
    valor_por_item = faturamento_total / itens_vendidos if itens_vendidos > 0 else 0.0

    return {
        "Faturamento Total": faturamento_total,
        "Itens Vendidos": itens_vendidos,
        "Numero de Vendas": num_vendas,
        "Dias Analisados": dias,
        "Ticket Medio": ticket_medio,
        "Valor por Item": valor_por_item,
    }


def top_products(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    resumo = (
        df.groupby("produto", as_index=False)
        .agg(
            quantidade_total=("quantidade", "sum"),
            faturamento_total=("valor", "sum"),
            num_vendas=("produto", "count"),
        )
        .sort_values(["faturamento_total", "quantidade_total"], ascending=False)
        .head(top_n)
        .reset_index(drop=True)
    )
    return resumo


def low_moving_products(df: pd.DataFrame, bottom_n: int = 10) -> pd.DataFrame:
    resumo = (
        df.groupby("produto", as_index=False)
        .agg(
            quantidade_total=("quantidade", "sum"),
            faturamento_total=("valor", "sum"),
            num_vendas=("produto", "count"),
        )
        .sort_values(["quantidade_total", "faturamento_total"], ascending=True)
        .head(bottom_n)
        .reset_index(drop=True)
    )
    return resumo


def sales_by_weekday(df: pd.DataFrame) -> pd.DataFrame:
    tmp = df.copy()
    tmp["dia_semana_num"] = tmp["data"].dt.dayofweek  # 0=segunda ... 6=domingo

    mapa = {
        1: "Segunda",
        2: "Terça",
        3: "Quarta",
        4: "Quinta",
        5: "Sexta",
        6: "Sábado",
        7: "Domingo",
    }
    tmp["dia_semana"] = tmp["dia_semana_num"].map(mapa)

    resumo = (
        tmp.groupby(["dia_semana_num", "dia_semana"], as_index=False)
        .agg(
            faturamento_total=("valor", "sum"),
            itens_vendidos=("quantidade", "sum"),
            num_vendas=("dia_semana", "count"),
        )
        .sort_values("dia_semana_num")
        .drop(columns=["dia_semana_num"])
        .reset_index(drop=True)
    )
    return resumo
