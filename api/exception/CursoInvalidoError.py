from http import HTTPStatus

from exception.UFSMHorariosError import UFSMHorariosError


class CursoInvalidoError(UFSMHorariosError):
    nome_curso: str
    nome_campus: str | None

    def __init__(self, nome_curso: str, nome_campus: str | None):
        self.nome_curso = nome_curso

        if nome_campus:
            message = f'A UFSM não oferta o curso "{nome_curso}" em "{nome_campus}"'
            self.nome_campus = nome_campus
        else:
            message = f'A UFSM não oferta o curso "{nome_curso}"'

        super().__init__(HTTPStatus.NOT_FOUND, message)
