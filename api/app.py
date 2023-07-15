from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from service.HorariosDisciplinasScraper import HorariosDisciplinasScraper
from model.HorariosDisciplina import HorariosDisciplina

import sys

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route(rule='/api/campi/<string:campus>/cursos/<string:curso>/horarios', methods=['GET'])
@cross_origin()
def get_horarios_disciplinas(curso: str, campus: str = 'santa-maria'):
    try:
        horarios_disciplinas: list[HorariosDisciplina] = HorariosDisciplinasScraper.scrap(curso, campus)
        return jsonify([horarios_disciplina.model_dump() for horarios_disciplina in horarios_disciplinas]), 200
    except:
        return jsonify({'code': 400, 'message': str(sys.exc_info()[0])}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
