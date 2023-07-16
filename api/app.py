from flask import Flask, jsonify, Response
from flask_cors import CORS, cross_origin
from redis.client import Redis
from http import HTTPStatus, HTTPMethod

from model.Campus import Campus
from model.Curso import Curso
from service.HorariosDisciplinasScraper import HorariosDisciplinasScraper
from model.HorariosDisciplina import HorariosDisciplina
from exception.UFSMHorariosError import UFSMHorariosError
from util.Util import Util

import json

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

redis_connection: Redis = Redis(host='ufsm-horarios-api-cache', port=6379, db=0, decode_responses=True)


@app.route(rule='/api/campi/<string:campus>/cursos/<string:curso>/horarios', methods=[HTTPMethod.GET])
@cross_origin()
def get_horarios_disciplinas(campus: str, curso: str) -> tuple[Response, HTTPStatus]:
    name: str = f'horarios-disciplinas:{curso}:{campus}'

    try:
        if not redis_connection.get(name=name):
            horarios_disciplinas: list[HorariosDisciplina] = HorariosDisciplinasScraper.scrap(curso, campus)
            redis_connection.set(name=name, value=json.dumps(horarios_disciplinas, default=lambda x: x.model_dump()), ex=86400)

        return jsonify(json.loads(redis_connection.get(name=name))), HTTPStatus.OK
    except UFSMHorariosError as error:
        return jsonify({'code': error.http_status_code, 'message': error.message}), error.http_status_code


@app.route(rule='/api/campi', methods=[HTTPMethod.GET])
@cross_origin()
def get_campi() -> tuple[Response, HTTPStatus]:
    name: str = 'campi'

    if not redis_connection.get(name=name):
        nomes_campi_ufsm: dict = Util.load_json('data/nomes-campi-ufsm.json')
        campi: list[Campus] = list()

        for nome_url, nome_exibicao in nomes_campi_ufsm.items():
            campi.append(Campus(**{'nome_exibicao': nome_exibicao, 'nome_url': nome_url}))

        redis_connection.set(name=name, value=json.dumps(campi, default=lambda x: x.model_dump()), ex=86400)

    return jsonify(json.loads(redis_connection.get(name=name))), HTTPStatus.OK


@app.route(rule='/api/cursos', methods=[HTTPMethod.GET])
@cross_origin()
def get_cursos() -> tuple[Response, HTTPStatus]:
    name: str = 'cursos'

    if not redis_connection.get(name=name):
        nomes_cursos_ufsm: dict = Util.load_json('data/nomes-cursos-ufsm.json')
        cursos: list[Curso] = list()

        for nome_url, nome_exibicao in nomes_cursos_ufsm.items():
            cursos.append(Curso(**{'nome_exibicao': nome_exibicao, 'nome_url': nome_url}))

        redis_connection.set(name=name, value=json.dumps(cursos, default=lambda x: x.model_dump()), ex=86400)

    return jsonify(json.loads(redis_connection.get(name=name))), HTTPStatus.OK


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
