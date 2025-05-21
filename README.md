<div align="center">
  <img src="https://github.com/user-attachments/assets/9e3fbb5b-9eda-4eef-89cf-fc60f7a00e17" width="580"/>
  <br><br>
  <img src="https://github.com/user-attachments/assets/fb78973b-0d60-40ba-acda-c82dd9f86b38" width="300"/>
</div>

(Render)

<p align="center">
  <a href="https://www.apache.org/licenses/LICENSE-2.0">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache-2.0" />
  </a>
  <img src="https://img.shields.io/github/repo-size/SarveshBTelang/True-Notion-AI" alt="Repo Size" />
  <img src="https://img.shields.io/github/last-commit/SarveshBTelang/True-Notion-AI" alt="Last Commit" />
  <img src="https://img.shields.io/github/issues/SarveshBTelang/True-Notion-AI" alt="Issues" />
  <img src="https://img.shields.io/github/issues-pr/SarveshBTelang/True-Notion-AI" alt="Pull Requests" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg" alt="Contributions welcome" />
  <img src="https://img.shields.io/badge/python-3.10.0-blue" alt="Python Version" />
  <img src="https://img.shields.io/badge/pip-25.1-blue" alt="Pip Version" />
  <img src="https://img.shields.io/badge/crewai-0.120.1-blue" alt="CrewAI Version" />
  <img src="https://img.shields.io/badge/fastapi-0.115.12-blue" alt="FastAPI Version" />
  <img src="https://img.shields.io/badge/langchain-0.3.25-blue" alt="LangChain Version" />
  <img src="https://img.shields.io/badge/pydantic-2.11.4-blue" alt="Pydantic Version" />
</p>

> **An open-source AI agent framework combining CrewAI, LangChain, and Agentic RAG, with full control over your data.**

> Ideal template for orchestrating intelligent multi-agent workflows across diverse applications—such as **AI chatbots**, **automated customer support**, **data analysis**, **sales profiling**, **web scraping and crawling bots**, **dynamic report generation**, **business scheduling**, and **financial planning**—powered by **cloud-hosted LLMs** like **Mistral**."

Author: [Sarvesh Telang](https://www.linkedin.com/in/sarvesh-telang-17916448/)

---

## ⭐ Key Features

- **Fully Open Source:** Apache 2.0 licensed and free to extend (**Attribution Required**)
- **Modular Agents:** Easily configurable with CrewAI.
- **Data Ownership:** Full control of models, storage, and flow.
- **Notion Integration:** Use Notion as a structured data backend.
- **Prebuilt AI Assistant:** Plug-and-play example for common use cases.
- **Customize with adding NLP Tools:** Sentiment, semantic analyzers, web crawlers (TextBlob, FASS, Serper etc.).
- **Cloud-Ready Deployment:** Works with Vercel, Render, Railway, etc.

---

## How it Works:

- **Extract insights from Notion notes:** Sync personal or business documents into a Notion database that form the base of your **internal knowledge layer**.
- **Memory Routing via Upstash Redis:** Stores document/task metadata to support fast lookup, secure and persistent data retrieval.
- **Chunking & Embedding (LangChain):** Documents are split into RAG-optimized chunks with configurable top-K, chunk size, and window size.
- **Vectorization & Semantic Retrieval:** Uses local or API-based embeddings (e.g., Mistral) and indexes them into a **Vector Database** like FAISS or Upstash.
- **Tool Creation:** Tools such as VectorStoreTool and SummaryTool are created from the knowledge base and reused across different AI agents.
- **Multi-Agent Orchestration with CrewAI:** Starts with a **Knowledge Analyst** agent and is easily extendable with Web Search Agents (Serper), Sentiment Analyzers, and Domain Experts (e.g., Finance, Sales).
- **Response Generation via LLMs:** Uses **Mistral** or plugin-based LLM APIs with concurrent multi-model support for tailored responses.
- **FastAPI Backend + Optional Frontend:** Backend manages routing and conversations, with a frontend deployable on GitHub Pages, Vercel, or any static host.

---






This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

