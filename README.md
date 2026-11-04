# Analisador de Vendas com Sugestões de Marketing

Aplicação em **Python + Streamlit** para pequenos varejos que já têm as vendas em planilha, mas não têm BI. Você envia um **CSV** e recebe indicadores, rankings e sugestões de marketing.

---

## O que a aplicação entrega

| Análise | Detalhe |
|---------|---------|
| **KPIs** | Faturamento total, itens vendidos, número de vendas, dias analisados, ticket médio e receita por item |
| **Por marca** | Tabela completa, Top 5 marcas, gráfico de barras (faturamento) e de pizza (participação) |
| **Produtos** | Top 10 por faturamento e os 10 de menor saída |
| **Dia da semana** | Vendas por dia, para achar os melhores dias de campanha |
| **Sugestões de marketing** | Recomendações geradas por regras a partir dos números acima |

### Relatório com IA (opcional, ainda não ligado à interface)

O módulo `src/ai_report.py` monta um resumo dos dados e pede à API da OpenAI um relatório com resumo, ações recomendadas, copies prontas para Instagram/WhatsApp e alertas. Ele precisa da variável `OPENAI_API_KEY` em um arquivo `.env` na raiz. **A tela atual usa apenas as sugestões por regras**; a chamada à IA ainda não foi conectada ao app.

---

## Formato do CSV

O arquivo precisa ter as colunas:

| Coluna | Exemplo | Observação |
|--------|---------|------------|
| `data` | `2026-02-01` | Formato `AAAA-MM-DD` |
| `produto` | `Camiseta` | |
| `marca` | `Class` | Usada na análise por marca |
| `quantidade` | `2` | |
| `valor` | `300.00` | **Total da linha** (quantidade × preço) |

Para gerar um arquivo de exemplo com 30 dias de vendas fictícias:

```bash
python gerar_csv.py        # cria vendas_marcas_exemplo.csv
```

---

## Como executar

```bash
# 1. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Inicie o app
streamlit run src/app.py
```

O navegador abre em `http://localhost:8501`. Envie o CSV pelo botão da página.

---

## Tecnologias

Python · Streamlit · Pandas · Plotly · python-dotenv · OpenAI (módulo opcional)

---

## Estrutura

```
src/
├── app.py              # Interface Streamlit
├── data_loader.py      # Leitura e validação do CSV
├── analytics.py        # KPIs, rankings, marcas e dia da semana
├── insights.py         # Sugestões de marketing
├── insights_rules.py   # Regras das sugestões
├── ai_report.py        # Relatório com IA (opcional)
└── formatting.py       # Formatação de valores em reais
gerar_csv.py            # Gera um CSV de exemplo
```
