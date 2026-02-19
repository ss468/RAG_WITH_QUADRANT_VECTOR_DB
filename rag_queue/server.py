from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Query
from .client.rq_client import queue
from .queues.worker import process_query

app = FastAPI()

@app.get('/')
def root():
    return {"status": "Server is up and running"}

@app.post('/chat')
def chat(
    query: str = Query(..., description="User query")
):
    job = queue.enqueue(process_query, query)
    return {
        "message": "Query received",
        "job_id": job.get_id()
    }

@app.get('/result')
def get_result(
        job_id:str=Query(..., description="Job ID to fetch the result for")

):
    job=queue.fetch_job(job_id)
    result=job.return_value()

    return {"result": result}