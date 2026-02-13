import io
import pandas as pd


REQUIRED_COLUMNS = {"data", "produto", "marca", "quantidade", "valor"}

def load_sales_csv(uploaded_file) -> pd.DataFrame:
    """
    Lê CSV enviado via Streamlit (compatível com UploadedFile / proxies).
    Tenta separador ',' e ';'. Faz validações básicas.
    """

    # Garante que a leitura comece do início
    try:
        uploaded_file.seek(0)
    except Exception:
        pass

    # Tenta ler com vírgula
    try:
        df = pd.read_csv(uploaded_file, sep=",", encoding="utf-8-sig")
        if df.shape[1] == 1:
            # talvez seja ';'
            try:
                uploaded_file.seek(0)
            except Exception:
                pass
            df = pd.read_csv(uploaded_file, sep=";", encoding="utf-8-sig")
    except pd.errors.EmptyDataError:
        raise ValueError("CSV vazio ou sem cabeçalho. Verifique o arquivo.")
    except Exception as e:
        raise ValueError(f"Erro ao ler o CSV: {e}")

    # Normaliza nomes de colunas
    df.columns = [c.strip().lower() for c in df.columns]

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV faltando colunas obrigatórias: {sorted(list(missing))}")

    # Limpeza
    df["produto"] = df["produto"].astype(str).str.strip()
    df["marca"] = df["marca"].astype(str).str.strip()

    # Conversões
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    if df["data"].isna().any():
        raise ValueError("Algumas datas estão inválidas na coluna 'data'.")

    df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

    if df[["quantidade", "valor"]].isna().any().any():
        raise ValueError("Existem valores inválidos em 'quantidade' ou 'valor'.")

    df["quantidade"] = df["quantidade"].astype(int)

    return df
