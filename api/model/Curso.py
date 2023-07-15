from pydantic import BaseModel


class Curso(BaseModel):
    nome_exibicao: str
    nome_url: str
