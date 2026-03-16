🚀 Projeto: AI-Powered Public Feedback Analytics

LLM + SQL + Power BI + Python

🎯 Objetivo

Construir uma solução analítica que utiliza LLM para classificar, resumir e gerar insights automáticos a partir de comentários públicos (ex: ouvidoria, pesquisas de satisfação, avaliações), integrando os resultados a um dashboard executivo no Power BI.

🧠 Problema de Negócio

Órgãos públicos e empresas recebem milhares de comentários abertos, mas:

A análise manual é lenta
Não existe categorização padronizada
Insights demoram a chegar à gestão
KPIs são limitados a dados estruturados
🏗 Arquitetura do Projeto

Base de dados com comentários (CSV ou SQL)
Python para processamento
API de LLM para:
Classificação automática
Análise de sentimento
Extração de temas
Geração de resumo executivo
Armazenamento estruturado em SQL
Dashboard no Power BI
Insight narrativo automático
🔧 Etapas Técnicas 1️⃣ Coleta de Dados Dataset com:

ID
Data
Área
Comentário (texto livre)
Nota (se houver)
Você pode usar:

Dados públicos
Kaggle
Ou simular dataset
2️⃣ Processamento com Python Bibliotecas:

pandas
requests
openai (ou outra API LLM)
Exemplo de aplicação do LLM:

Classificar comentário em categorias:
Atendimento
Infraestrutura
Sistema
Gestão
Outros
Gerar sentimento:
Positivo
Neutro
Negativo
Extrair principais tópicos
3️⃣ Estruturar Resultado

Criar nova tabela: | ID | Categoria | Sentimento | Tema Principal | Score | Resumo | Isso transforma dado não estruturado em estruturado.

Aqui você mostra: ✔ NLP aplicado ✔ Data Engineering ✔ Feature engineering ✔ Governança

4️⃣ Armazenar em SQL

Criar tabela no SQL Server ou PostgreSQL. Você demonstra: ✔ Integração Python + SQL ✔ Modelagem de dados ✔ Estrutura estrela para BI

5️⃣ Criar Dashboard no Power BI

KPIs:

% Sentimento Negativo por Área
Principais temas recorrentes
Evolução temporal
Ranking de categorias críticas
Resumo executivo automático (texto gerado pelo LLM)
Você pode criar um card com: "Resumo Executivo do Período" Gerado pelo LLM. Isso impressiona MUITO recrutador.

📊 Resultado Esperado

Exemplo de insight:

37% dos comentários negativos estão ligados a atraso no atendimento
Infraestrutura representa 52% das reclamações
Tendência de aumento de críticas no último trimestre
🧩 Tecnologias Usadas

Python
SQL
Power BI
LLM API
Pandas
Data Modeling
REST API Integration
💼 Como colocar no currículo Project: AI-Driven Feedback Intelligence Dashboard

Developed an end-to-end analytics solution integrating LLM-based text classification and sentiment analysis with SQL and Power BI. Automated categorization of unstructured feedback data, structured results into analytical models, and built executive dashboards providing real-time strategic insights.

🧠 Por que esse projeto é forte?

Ele mostra: ✔ Data Science ✔ BI ✔ SQL ✔ API Integration ✔ LLM ✔ Automação ✔ Arquitetura analítica ✔ Aplicação real de negócio

🔥 Se quiser deixar ainda mais forte Você pode adicionar:

RAG (Retrieval-Augmented Generation)
Chatbot interno para consulta de feedback
Versionamento GitHub
Documentação técnica
Arquitetura desenhada (diagrama)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🇧🇷 Versão em Português
📊 Dashboard de Análise de Sentimento com IA
Este projeto automatiza a coleta de feedbacks de clientes (via Kaggle), processa o sentimento e a categoria das mensagens utilizando Inteligência Artificial e visualiza os dados em um dashboard interativo no Power BI.

Principais Recursos:
- ETL Automatizado: Pipeline em Python que extrai dados do Kaggle e armazena em SQLite.
- Classificação com IA: Uso de modelos de linguagem para categorizar feedbacks em áreas como Suporte, Infraestrutura e Sistemas.
- Análise de Polaridade: Cálculo de score de sentimento variando de -1 (crítico) a 1 (excelente).
- Visualização Estratégica: Dashboard focado em volume de interações versus nível de satisfação por departamento.

Tecnologias Utilizadas:
- Linguagem: Python (Pandas, SQLite3).
- IA/ML: Integração com LLM para análise de texto.
- BI: Power BI (DAX, Medidas Dinâmicas, Formatação Condicional).

🇺🇸 English Version
📊 AI-Powered Feedback Analytics Dashboard
This project automates customer feedback collection (via Kaggle), processes message sentiment and categorization using Artificial Intelligence, and visualizes the insights in an interactive Power BI dashboard.

Key Features:
- Automated ETL: Python pipeline that extracts data from Kaggle and stores it in SQLite.
- AI Classification: Use of LLMs to categorize feedback into areas such as Support, Infrastructure, and Systems.
- Polarity Analysis: Sentiment score calculation ranging from -1 (critical) to 1 (excellent).
- Strategic Visualization: Dashboard focused on interaction volume versus satisfaction levels by department.

Tech Stack:
- Language: Python (Pandas, SQLite3).
- AI/ML: LLM integration for text analysis.
- BI: Power BI (DAX, Dynamic Measures, Conditional Formatting).
