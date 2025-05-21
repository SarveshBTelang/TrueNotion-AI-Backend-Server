<div align="center">
  <img src="logo_blue.png" width="580"/>
</div>

* Demonstration website backend code (Without transformers or langchains) for memory optimized open source frontend deployment
* Implements RAG using glove-gigaword-50 vector embeddings instead of high memory transformer models or paid serverless API services
* Great for initial learning and experimentation with vector embedding models

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
</p>

> **Backend code for a demo website built without transformers or LangChain — optimized for lightweight, open-source frontend deployments.**

> Implements Retrieval-Augmented Generation (RAG) using GloVe (gigaword-50) embeddings, avoiding memory-heavy transformer models and paid serverless APIs.

> Useful for learning and experimenting with vector embedding-based retrieval in a low-resource setup.

> Support with star ⭐ if you find this useful..

Author: [Sarvesh Telang](https://www.linkedin.com/in/sarvesh-telang-17916448/)

---
Refer main repo -->

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

