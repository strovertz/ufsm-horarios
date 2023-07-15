from pydantic import BaseModel


class HorariosDisciplina(BaseModel):
    ano: int
    periodo: str
    campus: str
    codigo_curso: str
    curso: str
    codigo_disciplina: str
    disciplina: str
    periodo_disciplina: int
    tipo_disciplina: str
    carga_horaria_disciplina: int
    creditos_disciplina: int
    vagas_oferecidas: int
    vagas_ocupadas: int
    vagas_aumentadas: int
    docentes: list[str]
    dia_semana: str
    horario_inicio: str
    horario_fim: str
