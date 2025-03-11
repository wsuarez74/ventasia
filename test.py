from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HumanQuery(BaseModel):
    question: str

@app.post("/human_query")
def handle_query(query: HumanQuery):
    return {"response": f"Recibí tu pregunta: {query.question}"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)