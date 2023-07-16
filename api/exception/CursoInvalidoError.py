from http import HTTPStatus

from exception.UFSMHorariosError import UFSMHorariosError


class CursoInvalidoError(UFSMHorariosError):
    http_status_code: HTTPStatus
    message: str
    nome_curso: str
    nome_campus: str | None

    def __init__(self, nome_curso: str, nome_campus: str | None):
        self.http_status_code = HTTPStatus.NOT_FOUND
        self.nome_curso = nome_curso

        if nome_campus:
            self.message = f'A UFSM não oferta o curso "{nome_curso}" em "{nome_campus}"'
        else:
            self.message = f'A UFSM não oferta o curso "{nome_curso}"'

        super().__init__(self.http_status_code, self.message)
