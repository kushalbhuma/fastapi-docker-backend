from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI, I am running!"}

@app.get("/health")
def health():
    return {"status": "OK"}
