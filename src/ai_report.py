import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent  # volta de /src para a raiz
load_dotenv(PROJECT_ROOT / ".env")

import os
import json
import pandas as pd
from openai import OpenAI




def _df_to_records(df: pd.DataFrame, max_rows: int = 15) -> list[dict]:
    if df is None or df.empty:
        return []
    return df.head(max_rows).to_dict(orient="records")


def build_context_payload(kpis: dict, top_df: pd.DataFrame, low_df: pd.DataFrame, weekday_df: pd.DataFrame) -> dict:
    return {
        "kpis": kpis,
        "top_produtos": _df_to_records(top_df, 10),
        "produtos_baixa_saida": _df_to_records(low_df, 10),
        "vendas_por_dia_semana": _df_to_records(weekday_df, 7),
    }


def generate_ai_report(payload: dict, business_type: str = "varejo") -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY não encontrado nas variáveis de ambiente.")
    client = OpenAI(api_key=api_key)
    """
    Retorna JSON com:
    - resumo
    - acoes_recomendadas (lista)
    - copies_prontas (lista: legenda + CTA)
    - alertas (lista)
    """
    system = (
        "Você é um consultor de marketing para pequenos varejos no Brasil. "
        "Você analisa métricas de vendas e devolve recomendações práticas e simples. "
        "Seja objetivo, nada de termos técnicos difíceis."
    )

    user = f"""
Negócio: {business_type}

Dados agregados (JSON):
{json.dumps(payload, ensure_ascii=False)}

Tarefa:
1) Crie um RESUMO em até 6 linhas.
2) Gere 6 AÇÕES RECOMENDADAS bem práticas.
3) Gere 3 COPIES PRONTAS para postar (Instagram/WhatsApp): legenda curta + CTA.
4) Gere ALERTAS se notar algo estranho (ex: poucos dias, poucos dados, concentração em 1 produto etc).

Responda OBRIGATORIAMENTE no formato JSON com as chaves:
resumo (string),
acoes_recomendadas (list[string]),
copies_prontas (list[{{"canal": "...", "texto": "..."}}]),
alertas (list[string])
"""

    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.4,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )

    text = resp.choices[0].message.content.strip()

    # Tenta parsear o JSON. Se vier texto extra, tenta achar o bloco JSON.
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(text[start : end + 1])
        raise


