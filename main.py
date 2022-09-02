from fastapi import FastAPI
from cpf_gen.utils import generate_cpf, validate_cpf

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "CPF Generator and Validator API, to see all the endpoints, go to /docs"}


# Generate random CPF
@app.get("/cpf")
async def cpf(qtd: int = 1):
    return [generate_cpf() for _ in range(qtd)]


# Generate random CPF based on state
@app.get("/cpf/{state_code}")
async def cpf(state_code: int = None, qtd: int = 1):
    if state_code < 0 or state_code > 9:
            return { "error": { "message": "Invalid CPF state code, state code must be a number between 0 and 9", "code": 408 } }
    if qtd > 100:
        return { "error": { "message": "Invalid CPF quantity, quantity must be a number between 1 and 100", "code": 410 } }
    return [generate_cpf(state=state_code) for _ in range(qtd)]


# Verify CPF
@app.get("/verify_cpf/{cpf}")
async def cpf(cpf: str):
    result =  validate_cpf(cpf)
    if result:
        return {"is-valid": True, "cpf": result, "message": "Valid CPF"}
    else:
        return { "is_valid": False, "cpf": None, "error": { "message": "Invalid CPF", "code": 406 } }
