import os
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from openai import OpenAI



load_dotenv()
SAMBANOVA_API_KEY = os.getenv("SAMBANOVA_API_KEY")

if not SAMBANOVA_API_KEY:
    raise ValueError("SAMBANOVA_API_KEY not found in .env file")



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



user_query = input("\nASK SOMETHING: ")



search_results = vector_db.similarity_search(
    query=user_query,
    k=3
)

if not search_results:
    print("No relevant documents found.")
    exit()



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

You are a helpfull AI Assistant who answers user query based on the available Context retrieved from a PDF 
file along with page_contents and page number. 
You should only answer user based on the following context and navigate the user to open the right page number to know more.

----------------
CONTEXT:
{context}
----------------

User Question:
{user_query}
"""



response = client.chat.completions.create(
    model="Meta-Llama-3.1-8B-Instruct",  
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": final_prompt}
    ],
    temperature=0.2,
)



print("\n\nANSWER:\n")
print(response.choices[0].message.content)
