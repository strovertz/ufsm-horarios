from pydantic import BaseModel


class Campus(BaseModel):
    nome_exibicao: str
    nome_url: str
