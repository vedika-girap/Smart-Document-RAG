from fastapi import FastAPI

app = FastAPI(
    title = "Smart Document RAG",
    description= "An end to end Retrieval Augmented Generation system.",
    version = "0.1.0",
)

@app.get("/")
def root():
    return{
        "message": "Welcome to Smart Document RAG."
    }