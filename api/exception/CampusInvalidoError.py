from http import HTTPStatus

from exception.UFSMHorariosError import UFSMHorariosError


class CampusInvalidoError(UFSMHorariosError):
    http_status_code: HTTPStatus
    message: str
    nome_campus: str

    def __init__(self, nome_campus: str):
        self.http_status_code = HTTPStatus.NOT_FOUND
        self.message = f'A UFSM não possui campus em "{nome_campus}"'
        self.nome_campus = nome_campus

        super().__init__(self.http_status_code, self.message)
