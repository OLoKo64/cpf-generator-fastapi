from fastapi import FastAPI
from cpf_gen.utils import generate_cpf, validate_cpf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "CPF Generator and Validator API, to see all the endpoints, go to /docs", "source_code": "https://github.com/OLoKo64/cpf-generator-fastapi"}


# Generate random CPF
@app.get("/cpf")
async def cpf_generator(qtd: int = 1):
    return [generate_cpf() for _ in range(qtd)]


# Generate random CPF based on state
@app.get("/cpf/{state_code}")
async def cpf_generator_state(state_code: int = None, qtd: int = 1):
    if state_code < 0 or state_code > 9:
            return { "error": { "message": "Invalid CPF state code, state code must be a number between 0 and 9", "code": 408 } }
    if qtd > 100:
        return { "error": { "message": "Invalid CPF quantity, quantity must be a number between 1 and 100", "code": 410 } }
    return [generate_cpf(state=state_code) for _ in range(qtd)]


# Verify CPF
@app.get("/validate_cpf/{cpf}")
async def cpf_validator(cpf: str):
    result =  validate_cpf(cpf)
    if result:
        return {"is-valid": True, "cpf": result, "message": "Valid CPF"}
    else:
        return { "is_valid": False, "cpf": None, "error": { "message": "Invalid CPF", "code": 406 } }
