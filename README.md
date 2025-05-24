<div align="center">
  <img src="logo_blue.png" width="580"/>
</div>

* Backend code for the Demonstration website (Without transformers or langchains) for memory optimized open source frontend deployment
* Implements RAG using GloVe (gigaword-50) vector embeddings, avoiding memory-heavy transformer models and paid serverless APIs.
* Great for initial learning and experimentating with vector embedding-based retrieval in a low-resource setup.

<p align="center">
  <a href="https://www.apache.org/licenses/LICENSE-2.0">
    <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache-2.0" />
  </a>
  <img src="https://img.shields.io/github/repo-size/SarveshBTelang/True-Notion-AI-Backend-Server" alt="Repo Size" />
  <img src="https://img.shields.io/github/last-commit/SarveshBTelang/True-Notion-AI-Backend-Server" alt="Last Commit" />
  <img src="https://img.shields.io/github/issues/SarveshBTelang/True-Notion-AI-Backend-Server" alt="Issues" />
  <img src="https://img.shields.io/github/issues-pr/SarveshBTelang/True-Notion-AI-Backend-Server" alt="Pull Requests" />
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg" alt="Contributions welcome" />
  <img src="https://img.shields.io/badge/python-3.10.0-blue" alt="Python Version" />
  <img src="https://img.shields.io/badge/pip-25.1-blue" alt="Pip Version" />
  <img src="https://img.shields.io/badge/crewai-0.120.1-blue" alt="CrewAI Version" />
  <img src="https://img.shields.io/badge/fastapi-0.115.12-blue" alt="FastAPI Version" />
</p>

> Support with star ⭐.. It helps more than you think!
---
* Standalone Python app
```bash
python main.py
```
* Standalone Fast API python app
```bash
uvicorn app:app --reload
```
* Docker 
```bash
docker build -t true-notion-ai . 

docker run --env-file .env -d -p 9000:9000 true-notion-ai
--> Any custom <LOCAL_PORT>:<CONTAINER_PORT>
--> or through adding PORT variable in .env
```

Author: [Sarvesh Telang](https://www.linkedin.com/in/sarvesh-telang-17916448/)

---
---
tags:
- glove
- gensim
- fse
---
# Glove Twitter 

Pre-trained glove vectors based on 2B tweets, 27B tokens, 1.2M vocab, uncased.

Read more:
* https://nlp.stanford.edu/projects/glove/
* https://nlp.stanford.edu/pubs/glove.pdf

Author: Jeffrey Pennington, Richard Socher and Christopher D. Manning

---

## Frontend Deployment Solution for Open Source RAG Projects
#### Sarvesh Telang

Note:
This project can be implemented and extended with any advanced LLM and vector embedding models. However, free frontend deployment platforms such as Render, Fly.io, Railway, Koyeb, and others typically impose strict resource limits — usually around 512 MB RAM and 1 GB storage.

These constraints necessitate completely isolating the app from outbound HTTP calls, which makes running large transformer models with high parameter counts impractical unless you chose paid services or rely on serverless APIs.

Proposed Approach:
To address this, you can use a lightweight embedding model that balances moderate accuracy with efficient similarity search.

For fully offline vector embedding generation, download the pre-trained GloVe embeddings file:

glove.6B.50d.txt
Available on Kaggle:
https://www.kaggle.com/datasets/watts2/glove6b50dtxt (Author: Ashish Lal)

⚠️ **Important**: Before running docker, convert GloVe file into the Word2Vec format using the glove2word2vec tool (saved in tools folder). Then, save it under path "models/glove-wiki-gigaword-50" and load it with the python KeyedVectors library.

You can explore a lot more and accurate vector embedding models with txt files, however looking at the currently available sources (May 2025) this Glove-50 model turns out to be having the lowest size (167 mb).

To improve accuracy in vector-based retrieval, consider the following strategies:

* Adjust RAG parameters: Tune top_k, chunk_size, and memory to improve retrieval relevance (can be modified remotely through upstash).
* Tune chunk overlap: Increase overlap to preserve context across chunks (larger memory footprint and slower processing).
* Data duplication: Re-emphasize important content by repeating it (can introduce bias or redundancy).
* Preprocessing: Clean and normalize text for better embeddings (may risk over-cleaning and data loss).
* Use transformer-based embeddings: Leverage models like Sentence-BERT for semantic accuracy (high memory and compute usage; may exceed free-tier limits).
* Deploy domain-specific models: Fine-tune embeddings for your use case (requires labeled data and training time).
* Utilize caching: Store computed embeddings to reduce latency (increases storage and complexity).
* Use vector quantization: Apply techniques like FAISS PQ/HNSW for scalable search (may reduce embedding precision slightly).
* Use serverless APIs: Services like Cohere or DeepInfra offer scalable embedding generation (paid services; may have latency limits).
* Deploy on-premise or hybrid models: Ensure data privacy and control (requires infrastructure and maintenance).
* Use custom LLMs for embeddings: Possible but inefficient compared to dedicated embedding models (Less Effective, resource-heavy, minimal gains).

Alternatively if your server platform allows more storage you can experiment with other embedding models listed in following sources:

https://www.kaggle.com/datasets/reppy4620/embeddings

https://www.edenai.co/post/top-free-embedding-tools-apis-and-open-source-models

https://www.kaggle.com/code/vikas15/word-embeddings

---
Refer main repo --> [True-Notion-AI](https://github.com/SarveshBTelang/True-Notion-AI)

## ⭐ Key Features

- **Fully Open Source:** Apache 2.0 licensed and free to extend (**Attribution Required**)
- **Modular Agents:** Easily configurable with CrewAI.
- **Data Ownership:** Full control of models, storage, and flow.
- **Notion Integration:** Use Notion as a structured data backend.
- **Prebuilt AI Assistant:** Plug-and-play example for common use cases.
- **Customize with adding NLP Tools:** Sentiment, semantic analyzers, web crawlers (TextBlob, FASS, Serper etc.).
- **Cloud-Ready Deployment:** Works with Vercel, Render, Railway, etc.

---

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
© Copyright 2025 Sarvesh Telang

