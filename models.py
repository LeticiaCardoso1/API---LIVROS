from typing import Optional

from pydantic import BaseModel

class Livro (BaseModel):
    id: Optional[int] = None
    nome: str
    autor: str
