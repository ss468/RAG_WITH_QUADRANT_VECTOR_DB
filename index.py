import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings


load_dotenv()


pdf_path = Path(__file__).parent / "OS Module 1.pdf"

loader = PyPDFLoader(str(pdf_path))
docs = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(docs)

print("Number of chunks:", len(chunks))


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


print("Embedding size:", len(embeddings.embed_query("hello world")))


vector_store = QdrantVectorStore.from_documents(
    chunks,
    embedding=embeddings,
    collection_name="os-module",
    url="http://localhost:6333"
)

print("✅ Data stored successfully in Qdrant!")
