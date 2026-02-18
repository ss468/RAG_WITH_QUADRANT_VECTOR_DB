# 🧠 RAG System with Qdrant vector DB and HuggingFace Embeddings

This project implements a Retrieval-Augmented Generation (RAG) system using:

- 🔎 Qdrant Vector Database
- 🤗 HuggingFace Embeddings
- ⚡ SambaNova LLM
- 🔗 LangChain
- 🐳 Docker (for Qdrant)

---

## 🏗️ Architecture

User Query  
→ Embedding (HuggingFace)  
→ Qdrant Vector Search  
→ Top-K Context Retrieval  
→ SambaNova LLM  
→ Context-Aware Answer  

---
