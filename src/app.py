
import streamlit as st
import plotly.express as px

from data_loader import load_sales_csv
from analytics import compute_kpis, top_products, low_moving_products, sales_by_weekday
from insights_rules import generate_rule_insights      
from ai_report import build_context_payload, generate_ai_report
from formatting import brl
from insights import generate_insights
from analytics import analyze_by_brand



st.set_page_config(page_title="Analisador de Vendas + Marketing", layout="wide")

st.title("📊 Analisador de Vendas com Sugestões de Marketing (Python)")
st.write("Envie um CSV com colunas: **data, produto, quantidade, valor** (valor = total da linha).")

uploaded = st.file_uploader("📎 Envie seu arquivo CSV", type=["csv"])
if uploaded:
    try:
        # 1) Carrega CSV
        df = load_sales_csv(uploaded)
        st.success("✅ CSV carregado com sucesso!")
        # 2) KPIs e análises principais
        kpis = compute_kpis(df)
        top_df = top_products(df, top_n=10)
        low_df = low_moving_products(df, bottom_n=10)
        weekday_df = sales_by_weekday(df)
        st.divider()

        st.subheader("✅ KPIs")
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        c1.metric("Faturamento", f"R$ {kpis['faturamento_total']:,.2f}")
        c2.metric("Itens vendidos", f"{kpis['itens_vendidos']}")
        c3.metric("Nº de vendas", f"{kpis['num_vendas']}")
        c4.metric("Dias analisados", f"{kpis['dias_analisados']}")
        c5.metric("Ticket médio", f"R$ {kpis['ticket_medio']:,.2f}")
        c6.metric("R$/item", f"R$ {kpis['valor_por_item']:,.2f}")

        
        # 3) Análise por Marca
        st.subheader("🏷️ Análise por Marca")
        brand_df = analyze_by_brand(df)
        st.dataframe(brand_df, use_container_width=True)

        

        st.subheader("🏆 Top 5 Marcas")
        top_brands = brand_df.head(5)
        st.dataframe(top_brands, use_container_width=True)
        

        # 📊 Gráfico simples - Faturamento por Marca
        
        fig_bar = px.bar(
            brand_df.sort_values("faturamento_total", ascending=False),
        x="marca",
        y="faturamento_total",
        title="📊 Faturamento por Marca",
        text_auto=True
        
)
        st.plotly_chart(fig_bar, use_container_width=True)

# 🥧 Gráfico simples - Participação por Marca
        fig_pie = px.pie(
        brand_df,
            names="marca",
        values="faturamento_total",
        title="🥧 Participação no Faturamento (%)"
        )
        st.plotly_chart(fig_pie, use_container_width=True)


        st.divider()

        left, right = st.columns(2)

        with left:
            st.subheader("🏆 Top produtos (por faturamento)")
            st.dataframe(top_df, use_container_width=True)

        with right:
            st.subheader("🐢 Produtos com menor saída")
            st.dataframe(low_df, use_container_width=True)

        st.subheader("📅 Vendas por dia da semana")
        st.dataframe(weekday_df, use_container_width=True)

        st.divider()

        # 4) Sugestões
        st.subheader("💡 Sugestões de marketing")
        tips = generate_insights(kpis, top_df, low_df, weekday_df)
        for t in tips:
            st.markdown(f"- {t}")

    except Exception as e:
        st.error(f"Erro ao processar o CSV: {e}")

    else:
        st.info("Envie um CSV para começar.")