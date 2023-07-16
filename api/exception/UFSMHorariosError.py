from http import HTTPStatus


class UFSMHorariosError(Exception):
    http_status_code: HTTPStatus
    message: str

    def __init__(self, http_status_code: HTTPStatus, message: str):
        self.http_status_code = http_status_code
        self.message = message

        super().__init__(self.message)
