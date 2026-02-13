# 📊 Analisador de Vendas com Sugestões de Marketing (Python + IA)


Este projeto permite que pequenos varejos (mercado, loja de roupas etc.) enviem um CSV de vendas e recebam:

- KPIs (faturamento, ticket médio, etc.)
- Ranking de produtos
- Vendas por dia da semana
- Sugestões automáticas (regras)
- Relatório e copies prontos com IA (GPT)

📁 A empresa envia um CSV de vendas
📊 O sistema analisa automaticamente
💡 E entrega KPIs + insights estratégicos de marketing


# 🎯 Objetivo

- Criar uma ferramenta prática que:
- Analisa faturamento total
- Identifica produtos mais e menos vendidos
- Calcula ticket médio
- Mostra desempenho por marca
- Analisa vendas por dia da semana
- Gera sugestões estratégicas de marketing

Pensado especialmente para pequenos varejistas que não possuem BI estruturado, mas já possuem dados em planilha.

#   ✅ KPIs Estratégicos 📊 Funcionalidades

- Faturamento total
- Itens vendidos
- Número de vendas
- Dias analisados
- Ticket médio
- Receita por item

#   🏷️ Análise por Marca

- Quantidade total vendida por marca
- Faturamento total por marca
- Número de vendas por marca
- Ranking das Top 5 marcas

📈 Gráfico de barras — Faturamento por Marca
🥧 Gráfico de pizza — Participação percentual no faturamento

#   🏆 Produtos

- Top produtos por faturamento
- Produtos com menor saída

#   📅 Vendas por Dia da Semana

- Permite identificar:
- Dia com maior faturamento
- Padrões de comportamento do cliente
- Oportunidades de campanhas específicas


# 💡 Sugestões de Marketing

- O sistema gera recomendações automáticas como:
- Aproveitar o melhor dia da semana
- Criar destaque para o produto campeão
- Estratégias para produtos com baixa saída
- Ideias de promoção e combos
- Sugestão de rotina de postagens


## ✅ Requisitos do CSV
O arquivo deve conter as colunas:
- `data` (ex: 2026-02-01)
- `produto` (ex: Camisa)
- `marca` (ex: Class)
- `quantidade` (ex: 2)
- `valor` (float) -> valor TOTAL da linha (quantidade * preço)

## 🚀 Como rodar

### 1) Criar ambiente e instalar dependências
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
# source .venv/bin/activate

pip install -r requirements.txt
