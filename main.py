from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI backend is running"}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"operation": "add", "result": a + b}


@app.get("/subtract")
def subtract_numbers(a: int, b: int):
    return {"operation": "subtract", "result": a - b}


@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"operation": "multiply", "result": a * b}


@app.get("/divide")
def divide_numbers(a: int, b: int):
    try:
        result = a / b
        return {"operation": "divide", "result": result}
    except ZeroDivisionError:
        raise HTTPException( status_code=400, detail="Division by zero is not allowed")


@app.get("/health")
def health_check():
    return {"status": "ok"}
