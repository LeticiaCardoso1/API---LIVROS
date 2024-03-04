from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

livros = {
    1: {
        "nome": "É assim que acaba",
        "autor": "Colleen Hoover"
    },
    2:{
        "nome": "É assim que comeca",
        "autor": "Colleen Hoover"
    }
}

class Livro(BaseModel):
    nome: str
    autor: str

@app.get('/')
async def mensagem():
    return {'Mensagem': 'Está funcionando, lele'}

@app.get('/livro')
async def get_livros():
    return livros

@app.get('/livro/{livro_id}')
async def get_livro(livro_id: int):
    if livro_id not in livros:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livro não encontrado")
    return livros[livro_id]

@app.post("/livro", status_code=status.HTTP_201_CREATED)
async def post_livro(livro: Livro):
    nextid = len(livros) + 1
    livros[nextid] = livro.dict()
    return livro

@app.put('/livro/{livro_id}')
async def put_livro(livro_id: int, livro: Livro):
    if livro_id in livros:
        livros[livro_id] = livro.dict()
        return livro
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um livro com id {livro_id}.')

@app.delete("/livro/{livro_id}")
async def delete_livro(livro_id: int):
    if livro_id in livros:
        livros.pop(livro_id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um livro com id {livro_id}.')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, log_level='info', reload=True)
