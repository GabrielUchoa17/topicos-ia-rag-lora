
# Resumo da Execução em Modo Emergência

Devido às limitações computacionais e ao prazo curto de entrega, foi utilizada uma configuração ultra-leve para validar o pipeline completo.

Configuração:
- MAX_STEPS = 1
- N_TRAIN = 1
- N_EVAL = 1
- MAX_LEN = 32
- LoRA r = 1
- LoRA alpha = 2
- dropout = 0.0

Modelos utilizados:
- Tiny GPT-2
- Tiny Random GPT-2
- Tiny Random T5
- Flan-T5 Small

Artefatos gerados:
- Adaptadores LoRA em models/
- Logs e gráficos de loss em results/loss/
- Tabela de métricas em results/metricas/
- Radar chart em results/metricas/radar_modelos.png
- Amostras qualitativas em results/amostras/
- API FastAPI em main.py
- Frontend em static/index.html

Observação:
A prioridade desta execução foi comprovar a integração do pipeline RAG + LoRA + avaliação + API, e não maximizar a qualidade final dos modelos.

Tempo total aproximado da execução: 0.62 minutos.
