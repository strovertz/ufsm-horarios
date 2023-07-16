from seleniumwire import webdriver
from seleniumwire.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from pydantic_core import ValidationError
from string import Template
from datetime import datetime
from time import sleep

from model.AnoPeriodoAtual import AnoPeriodoAtual
from model.DisciplinasPorPeriodo import DisciplinasPorPeriodo
from model.HorariosDisciplina import HorariosDisciplina
from exception.CampusInvalidoError import CampusInvalidoError
from exception.CursoInvalidoError import CursoInvalidoError
from util.Util import Util

import json


class HorariosDisciplinasScraper:
    __NOMES_CAMPI_UFSM: dict = Util.load_json('data/nomes-campi-ufsm.json')

    __NOMES_CURSOS_UFSM: dict = Util.load_json('data/nomes-cursos-ufsm.json')

    __REQUEST_URL_TEMPLATE: Template = Template('https://www.ufsm.br/cursos/graduacao/$campus/$curso/horarios')

    __DEFAULT_SLEEP_TIME: int = 2

    @staticmethod
    def __compose_request_url(curso: str, campus: str = 'santa-maria') -> str:
        if campus.casefold() not in HorariosDisciplinasScraper.__NOMES_CAMPI_UFSM:
            raise CampusInvalidoError(campus)

        if curso.casefold() not in HorariosDisciplinasScraper.__NOMES_CURSOS_UFSM:
            raise CursoInvalidoError(curso, HorariosDisciplinasScraper.__NOMES_CAMPI_UFSM.get(campus))

        return HorariosDisciplinasScraper.__REQUEST_URL_TEMPLATE.substitute(campus=campus, curso=curso)

    @staticmethod
    def __convert_to_object(data: dict) -> AnoPeriodoAtual | DisciplinasPorPeriodo | None:
        try:
            return AnoPeriodoAtual(**data)
        except ValidationError:
            try:
                return DisciplinasPorPeriodo(**data)
            except ValidationError:
                return None

    @staticmethod
    def __extract_horarios_disciplinas(
        objects: list[AnoPeriodoAtual | DisciplinasPorPeriodo],
        campus: str
    ) -> list[HorariosDisciplina]:
        ano = datetime.today().year
        periodo = Util.get_current_semester()

        horarios_disciplinas: list[HorariosDisciplina] = list()

        for object in objects:
            if isinstance(object, AnoPeriodoAtual):
                ano = object.itens.oferta.ano
                periodo = object.itens.oferta.periodo.descricao
            elif isinstance(object, DisciplinasPorPeriodo):
                for item in object.itens:
                    for disciplina_turma in item.disciplinaTurmas:
                        for turma in disciplina_turma.turmas:
                            for horario_turma in turma.horariosTurma:
                                horarios_disciplinas.append(
                                    HorariosDisciplina(**{
                                        'ano': ano,
                                        'periodo': periodo,
                                        'campus': HorariosDisciplinasScraper.__NOMES_CAMPI_UFSM.get(campus),
                                        'codigo_curso': turma.curso.codigo,
                                        'curso': turma.curso.descricao,
                                        'codigo_disciplina': disciplina_turma.disciplina.disciplina.codigo,
                                        'disciplina': disciplina_turma.disciplina.disciplina.descricao,
                                        'periodo_disciplina': item.periodo,
                                        'tipo_disciplina': horario_turma.tipo.descricao,
                                        'carga_horaria_disciplina': disciplina_turma.disciplina.disciplina.cargaHoraria,
                                        'creditos_disciplina': disciplina_turma.disciplina.disciplina.creditos,
                                        'vagas_oferecidas': turma.vagasOferecidas,
                                        'vagas_ocupadas': turma.vagasOcupadas,
                                        'vagas_aumentadas': turma.vagasAumentadas,
                                        'docentes': [docente.pessoa.nome for docente in turma.docentes],
                                        'dia_semana': horario_turma.diaSemana.descricao,
                                        'horario_inicio': horario_turma.horarioInicio,
                                        'horario_fim': horario_turma.horarioFim
                                    })
                                )

        return horarios_disciplinas

    @staticmethod
    def __get_chrome_options() -> Options:
        chrome_options: Options = webdriver.ChromeOptions()

        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        return chrome_options

    @staticmethod
    def scrap(curso: str, campus: str = 'santa-maria') -> list[HorariosDisciplina]:
        chrome_options: Options = HorariosDisciplinasScraper.__get_chrome_options()
        seleniumwire_options: dict = {'disable_encoding': True}

        driver: Chrome = webdriver.Chrome(chrome_options=chrome_options, seleniumwire_options=seleniumwire_options)

        url: str = HorariosDisciplinasScraper.__compose_request_url(curso, campus)

        driver.get(url)

        sleep(HorariosDisciplinasScraper.__DEFAULT_SLEEP_TIME)

        objects: list[AnoPeriodoAtual | DisciplinasPorPeriodo] = list()

        for request in driver.requests:
            if request.url and request.url.endswith('.json') and request.response:
                try:
                    body: dict = json.loads(request.response.body)
                    object: AnoPeriodoAtual | DisciplinasPorPeriodo = HorariosDisciplinasScraper.__convert_to_object(body)
                    objects.append(object)
                except ValueError:
                    pass

        driver.quit()

        return HorariosDisciplinasScraper.__extract_horarios_disciplinas(objects, campus)
