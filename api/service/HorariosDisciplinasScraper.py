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
from model.ScrapingParameters import ScrapingParameters
from exception.CampusInvalidoError import CampusInvalidoError
from exception.CursoInvalidoError import CursoInvalidoError
from util.Util import Util

import json


class HorariosDisciplinasScraper:
    __DIAS_SEMANA: dict = {
        'domingo': 'Domingo',
        'segunda-feira': 'Segunda-feira',
        'terca-feira': 'Terça-feira',
        'quarta-feira': 'Quarta-feira',
        'quinta-feira': 'Quinta-feira',
        'sexta-feira': 'Sexta-feira',
        'sabado': 'Sábado'
    }

    __NOMES_CAMPI_UFSM: dict = Util.load_json('data/nomes-campi-ufsm.json')

    __NOMES_CURSOS_UFSM: dict = Util.load_json('data/nomes-cursos-ufsm.json')

    __REQUEST_URL_TEMPLATE: Template = Template('https://www.ufsm.br/cursos/graduacao/$campus/$curso/horarios')

    __DEFAULT_SLEEP_TIME: int = 10

    @staticmethod
    def __compose_request_url(campus: str, curso: str) -> str:
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
    def __filter(horarios_disciplinas: list[HorariosDisciplina], scraping_parameters: ScrapingParameters) -> list[HorariosDisciplina]:
        horarios_disciplinas_filtrados: list[HorariosDisciplina] = list()

        nome_exibicao_campus: str | None = HorariosDisciplinasScraper.__NOMES_CAMPI_UFSM.get(scraping_parameters.campus)
        nome_exibicao_curso: str | None = HorariosDisciplinasScraper.__NOMES_CURSOS_UFSM.get(scraping_parameters.curso)

        for horarios_disciplina in horarios_disciplinas:
            if not (nome_exibicao_campus and horarios_disciplina.campus.casefold() == nome_exibicao_campus.casefold()):
                continue

            if not (nome_exibicao_curso and horarios_disciplina.curso.casefold().find(nome_exibicao_curso.casefold()) >= 0):
                continue

            if scraping_parameters.dia_semana and horarios_disciplina.dia_semana.casefold() != HorariosDisciplinasScraper.__DIAS_SEMANA.get(scraping_parameters.dia_semana).casefold():
                continue

            if scraping_parameters.horario_inicio and Util.compare_times(scraping_parameters.horario_inicio, horarios_disciplina.horario_inicio) > 0:
                continue

            if scraping_parameters.horario_fim and Util.compare_times(scraping_parameters.horario_fim, horarios_disciplina.horario_fim) < 0:
                continue

            horarios_disciplinas_filtrados.append(horarios_disciplina)

        return horarios_disciplinas_filtrados

    @staticmethod
    def scrap(scraping_parameters: ScrapingParameters) -> list[HorariosDisciplina]:
        chrome_options: Options = HorariosDisciplinasScraper.__get_chrome_options()
        seleniumwire_options: dict = {'disable_encoding': True}

        driver: Chrome = webdriver.Chrome(chrome_options=chrome_options, seleniumwire_options=seleniumwire_options)

        url: str = HorariosDisciplinasScraper.__compose_request_url(scraping_parameters.campus, scraping_parameters.curso)

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

        horarios_disciplinas: list[HorariosDisciplina] = HorariosDisciplinasScraper.__extract_horarios_disciplinas(objects, scraping_parameters.campus)
        horarios_disciplinas_filtrados: list[HorariosDisciplina] = HorariosDisciplinasScraper.__filter(horarios_disciplinas, scraping_parameters)

        return horarios_disciplinas_filtrados
