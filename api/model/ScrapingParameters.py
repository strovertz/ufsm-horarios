from pydantic import BaseModel


class ScrapingParameters(BaseModel):
    campus: str
    curso: str
    dia_semana: str | None
    horario_inicio: str | None
    horario_fim: str | None
