# 🚀 Projeto: AI-Powered Public Feedback Analytics
**LLM + SQL + Power BI + Python**

---

### 🎯 Objetivo
Construir uma solução analítica que utiliza **LLM** para classificar, resumir e gerar insights automáticos a partir de comentários públicos (ex: ouvidoria, pesquisas de satisfação, avaliações), integrando os resultados a um **dashboard executivo no Power BI**.

---

### 🧠 Problema de Negócio
Órgãos públicos e empresas recebem milhares de comentários abertos, enfrentando os seguintes desafios:
* **Análise manual lenta** e custosa.
* **Falta de categorização** padronizada.
* **Atraso na entrega de insights** estratégicos para a gestão.
* **KPIs limitados** apenas a dados estruturados.

---

### 🏗 Arquitetura do Projeto
1.  **Base de dados** com comentários (CSV ou SQL).
2.  **Python** para processamento e orquestração.
3.  **API de LLM** para classificação, análise de sentimento e resumos.
4.  **Armazenamento estruturado** em SQL.
5.  **Dashboard interativo** no Power BI com insights narrativos.

---

### 🔧 Etapas Técnicas

#### **1️⃣ Coleta de Dados**
Utilização de datasets públicos (**Kaggle**) ou simulados contendo:
* **ID, Data e Área**.
* **Comentário** (texto livre) e **Nota**.

#### **2️⃣ Processamento com Python**
Uso das bibliotecas **Pandas**, **Requests** e integração com **APIs de LLM** para:
* **Classificação automática** (Atendimento, Infraestrutura, Sistema, Gestão).
* **Análise de Sentimento** (Positivo, Neutro, Negativo).
* **Extração de tópicos** principais.

#### **3️⃣ Estruturação de Resultados**
Transformação de dados não estruturados em uma tabela analítica:
> `| ID | Categoria | Sentimento | Tema Principal | Score | Resumo |`
* Demonstra competências em **NLP**, **Data Engineering** e **Governança**.
#### **4️⃣ Armazenamento em SQL**
Integração do Python com **SQL Server** ou **PostgreSQL** utilizando modelagem em **estilo Estrela (Star Schema)**.

#### **5️⃣ Dashboard no Power BI**
Criação de indicadores visuais (KPIs) como:
* **% de Sentimento Negativo** por área.
* **Ranking de categorias críticas** e evolução temporal.
* **Resumo Executivo Automático** gerado por IA (Narrativa Inteligente).

---

### 📊 Resultado Esperado
* Identificação de que **37% dos comentários negativos** estão ligados a atrasos.
* Visualização de que **Infraestrutura representa 52%** das reclamações.
* Detecção de **tendências de aumento de críticas** em períodos específicos.

---

### 🧩 Tecnologias Usadas
* **Linguagem:** Python (Pandas).
* **Banco de Dados:** SQL / SQLite.
* **Visualização:** Power BI.
* **IA:** LLM API (OpenAI ou similar).

---

### 💼 Portfolio / Resume Context
**Project: AI-Driven Feedback Intelligence Dashboard**
*Developed an end-to-end analytics solution integrating LLM-based text classification and sentiment analysis with SQL and Power BI. Automated categorization of unstructured feedback data, structured results into analytical models, and built executive dashboards providing real-time strategic insights.*

---

### 🧠 Por que esse projeto é relevante?
Ele demonstra domínio em todo o ciclo de dados:
✔ **Data Science & NLP** | ✔ **Business Intelligence** | ✔ **Data Engineering** | ✔ **IA & Automação**

🔥 **Próximos Passos:** Implementação de **RAG** (Retrieval-Augmented Generation) e documentação técnica da arquitetura.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🇧🇷 Versão em Português

### 📊 Dashboard de Análise de Sentimento com IA
Este projeto automatiza a coleta de feedbacks de clientes (via Kaggle), processa o sentimento e a categoria das mensagens utilizando Inteligência Artificial (LLM) e visualiza os insights em um dashboard executivo no Power BI.

#### **🎯 Objetivo**
Construir uma solução analítica que utiliza IA para classificar, resumir e gerar insights automáticos a partir de comentários públicos, transformando dados não estruturados em indicadores estratégicos.

#### **🧠 Problema de Negócio**
* A análise manual de milhares de comentários é lenta e ineficiente.
* Dificuldade em padronizar categorias e extrair insights em tempo real para a gestão.
* KPIs limitados apenas a dados estruturados.

#### **🏗️ Arquitetura e Etapas Técnicas**
1.  **Coleta de Dados:** Extração automatizada de datasets de feedbacks (Kaggle).
2.  **Processamento com Python:** Pipeline utilizando Pandas para limpeza e integração com APIs de LLM.
3.  **Inteligência Artificial:** Classificação automática por área (Suporte, Infraestrutura, Sistemas) e análise de polaridade (-1 a 1).
4.  **Armazenamento:** Estruturação dos dados processados em SQLite/SQL para consumo analítico.
5.  **Visualização:** Dashboard no Power BI com foco em volume de interações e equilíbrio de sentimento.

#### **🧩 Tecnologias Usadas**
* **Linguagem:** Python (Pandas, SQLite3).
* **IA/ML:** Integração com LLM para NLP (Processamento de Linguagem Natural).
* **BI:** Power BI (DAX, Medidas Dinâmicas, Formatação Condicional).

---

## 🇺🇸 English Version

### 📊 AI-Powered Feedback Analytics Dashboard
This project automates customer feedback collection (via Kaggle), processes message sentiment and categorization using Artificial Intelligence (LLM), and visualizes insights in an interactive executive dashboard.

#### **🎯 Objective**
To build an analytical solution that leverages LLMs to classify, summarize, and generate automatic insights from public comments, transforming unstructured data into strategic KPIs.

#### **🧠 Business Problem**
* Manual analysis of thousands of open comments is slow and lacks standardization.
* Insights take too long to reach management, delaying decision-making.

#### **🚀 Key Features**
* **Automated ETL:** Python pipeline for data extraction, processing, and SQL storage.
* **AI Classification:** Automatic categorization into areas like *Support, Infrastructure, and Systems*.
* **Polarity Analysis:** Sentiment score calculation ranging from -1 (critical) to 1 (excellent).
* **Strategic Visualization:** Dashboard focused on interaction volume versus satisfaction levels by department.

#### **🧩 Tech Stack**
* **Language:** Python (Pandas, SQLite3).
* **AI/ML:** LLM integration for text analysis and NLP.
* **BI:** Power BI (DAX, Dynamic Measures, Conditional Formatting).

---

### 💼 Portfolio / Resume Context
**Project: AI-Driven Feedback Intelligence Dashboard**
Developed an end-to-end analytics solution integrating LLM-based text classification and sentiment analysis with SQL and Power BI. Automated categorization of unstructured feedback data, structured results into analytical models, and built executive dashboards providing real-time strategic insights.