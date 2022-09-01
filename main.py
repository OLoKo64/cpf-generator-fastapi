from fastapi import FastAPI, HTTPException
from re import search
from cpf_gen.utils import generate_cpf

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Generate random CPF
@app.get("/cpf")
async def cpf(qtd: int = 1):
    return [generate_cpf() for _ in range(qtd)]


# Generate random CPF based on state
@app.get("/cpf/{state_code}")
async def cpf(state_code: int = None, qtd: int = 1):
    return [generate_cpf(state_code) for _ in range(qtd)]


# Verify CPF
@app.get("/verify_cpf/{cpf}")
async def cpf(cpf: str):
    if len(cpf) == 11 and search(r'\d{11}', cpf):
        return {"message": "cpf", "cpf": cpf}
    else:
        raise HTTPException(status_code=406, detail="Invalid CPF")
