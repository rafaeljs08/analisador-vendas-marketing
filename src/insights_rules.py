import pandas as pd


def generate_rule_insights(kpis: dict, top_df: pd.DataFrame, low_df: pd.DataFrame, weekday_df: pd.DataFrame) -> list[str]:
    insights: list[str] = []

    if not weekday_df.empty:
        best = weekday_df.sort_values("faturamento_total", ascending=False).iloc[0]
        insights.append(
            f"Seu melhor dia foi **{best['dia_semana']}**. Programe post e oferta nesse dia."
        )

    if not top_df.empty:
        top1 = top_df.iloc[0]
        insights.append(
            f"Produto campeão: **{top1['produto']}**. Destaque na vitrine e no WhatsApp/Instagram."
        )

    if not low_df.empty:
        low1 = low_df.iloc[0]
        insights.append(
            f"Produto com menor saída: **{low1['produto']}**. Teste promo leve (10–15%) ou combo com o campeão."
        )

    ticket = float(kpis.get("ticket_medio", 0.0))
    if ticket > 0:
        insights.append(
            f"Ticket médio ~ **R$ {ticket:,.2f}**. Para subir: kits/combos e ofertas de itens complementares no caixa."
        )

    if int(kpis.get("dias_analisados", 0)) < 5:
        insights.append("Poucos dias analisados: se possível, use pelo menos 2–4 semanas para decisões melhores.")

    return insights
