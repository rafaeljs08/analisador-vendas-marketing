import pandas as pd


def generate_insights(
    kpis: dict,
    top_df: pd.DataFrame,
    low_df: pd.DataFrame,
    weekday_df: pd.DataFrame,
) -> list[str]:
    insights = []

    # 1) Melhor dia
    if not weekday_df.empty:
        best = weekday_df.sort_values("faturamento_total", ascending=False).iloc[0]
        insights.append(
            f"Seu melhor dia foi **{best['dia_semana']}**. Tente fazer post/oferta nesse dia para aproveitar o movimento."
        )

    # 2) Produto campeão
    if not top_df.empty:
        top1 = top_df.iloc[0]
        insights.append(
            f"O produto que mais trouxe faturamento foi **{top1['produto']}**. Faça destaque dele (vitrine, stories, status do WhatsApp)."
        )

    # 3) Produto parado
    if not low_df.empty:
        low1 = low_df.iloc[0]
        insights.append(
            f"O produto com menor saída foi **{low1['produto']}**. Sugestão: promo leve (ex: 10–15%) ou combo com um produto campeão."
        )

    # 4) Ticket médio
    ticket = kpis.get("ticket_medio", 0.0)
    if ticket > 0:
        insights.append(
            f"Seu **ticket médio** está em aproximadamente **R$ {ticket:,.2f}**. Para aumentar, crie kits (ex: 'leve 2 e ganhe desconto') ou produtos complementares no caixa."
        )

    # 5) Dica geral de consistência
    insights.append(
        "Faça uma rotina simples: **3 posts/semana** (1 produto campeão, 1 promoção, 1 prova social). Consistência costuma gerar mais resultado do que postar muito uma vez só."
    )

    return insights
