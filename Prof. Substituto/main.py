from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI ()

class Aluno (BaseModel):
    nome: str
    idade: int
    turma: str
    dtNascimento: str

@app.get("/")
def read_root ():
    return {"Message": "Hello World"}

@app.get("/buscar-usuarios")
def busca_usuarios():
    return [{"nome": "Guilherme", "idade": 25}, {"nome": "Ederson", "idade": 41}, {"nome": "Mauricio", "idade": 40}]

@app.post ("/cadastrar-aluno")
def cadastrar_aluno (aluno: Aluno):
    return aluno