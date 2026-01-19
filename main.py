from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI,The Server is Running"}

@app.get("/health")
def health():
    return {"status": "OK"}
