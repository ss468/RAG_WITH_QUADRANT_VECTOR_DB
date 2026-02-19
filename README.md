🧠 RAG System with Qdrant Vector DB+ HuggingFace Embeddings + Async Redis Queue

This project implements a production-style Retrieval-Augmented Generation (RAG) system with asynchronous processing using Redis and RQ.

🚀 Tech Stack

🔎 Qdrant – Vector Database

🤗 HuggingFace Embeddings – Text embeddings

⚡ SambaNova LLM – Large Language Model

🔗 LangChain – Retrieval pipeline

⚡ FastAPI – API layer

🔁 Redis (Valkey) – Message broker

🧵 RQ (Redis Queue) – Background worker system

🐳 Docker – Containerized services

🏗️ Updated Architecture (Asynchronous)

User Query
→ FastAPI
→ Redis Queue (RQ)
→ Background Worker
→ Embedding (HuggingFace)
→ Qdrant Vector Search
→ Top-K Context Retrieval
→ SambaNova LLM
→ Context-Aware Answer

⚡ Why Async Architecture?

Previously, the RAG pipeline ran synchronously inside the API.

Now:

✅ Non-blocking API responses

✅ Parallel query processing

✅ Scalable worker system

✅ Production-ready architecture

FastAPI immediately enqueues jobs, and workers process heavy RAG tasks in the background.
