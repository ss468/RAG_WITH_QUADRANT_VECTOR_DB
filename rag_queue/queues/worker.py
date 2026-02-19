from dotenv import load_dotenv
load_dotenv()

from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from openai import OpenAI
import os

SAMBANOVA_API_KEY = os.getenv("SAMBANOVA_API_KEY")

client = OpenAI(
    api_key=SAMBANOVA_API_KEY,
    base_url="https://api.sambanova.ai/v1",
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = QdrantVectorStore.from_existing_collection(
    collection_name="os-module",
    url="http://localhost:6333",
    embedding=embeddings
)

def process_query(query: str):
    print("Searching chunks:", query)

    search_results = vector_db.similarity_search(
        query=query,  # ✅ FIXED
        k=3
    )

    context_blocks = []

    for result in search_results:
        context_blocks.append(
            f"""
Page Number: {result.metadata.get('page', 'N/A')}
Source: {result.metadata.get('source', 'N/A')}
Content:
{result.page_content}
"""
        )

    context = "\n\n----------------\n\n".join(context_blocks)

    final_prompt = f"""
You are a helpful AI assistant.

CONTEXT:
{context}

User Question:
{query}
"""

    response = client.chat.completions.create(
        model="Meta-Llama-3.1-8B-Instruct",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.2,
    )

    answer = response.choices[0].message.content
    print(answer)

    return answer