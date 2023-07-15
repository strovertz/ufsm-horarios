from pydantic import BaseModel
from typing import Any


class Periodo(BaseModel):
    id: int | None
    itemId: int
    item: int
    descricao: str
    sigla: str
    padrao: Any
    ativo: Any
    idTabelaSup: Any
    filhos: Any
    tipoPeriodo: Any


class Matricula(BaseModel):
    id: int | None
    ano: int
    periodo: Periodo | Any


class Oferta(BaseModel):
    id: int | None
    ano: int
    periodo: Periodo | Any


class Itens(BaseModel):
    matricula: Matricula | Any
    oferta: Oferta | Any


class AnoPeriodoAtual(BaseModel):
    error: bool
    itens: Itens
