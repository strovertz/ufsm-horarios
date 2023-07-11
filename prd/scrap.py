import csv
from http.server import BaseHTTPRequestHandler, HTTPServer
from string import Template
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="/usr/local/bin/chromedriver")

# Mapeamento dos dias da semana para os índices da tabela
dias_semana = {
    'Segunda-feira': 1,
    'Terça-feira': 2,
    'Quarta-feira': 3,
    'Quinta-feira': 4,
    'Sexta-feira': 5,
    'Sábado': 6
}

# Gerar página HTML com os horários e o filtro
def generate_html(data, materia_selecionada=None):
    table_rows = ""
    for row in data:
        if not materia_selecionada or row['Materia'] == materia_selecionada:
            table_rows += f"<tr><td>{row['Materia']}</td><td>{row['Dia']}</td><td>{row['Horario_inicio']}</td><td>{row['Horario_fim']}</td></tr>"

    html_template = Template('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Horários das Disciplinas</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }

            th, td {
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }

            th {
                background-color: #f2f2f2;
            }

            .filter-container {
                margin-bottom: 16px;
            }

            .filter-label {
                margin-right: 8px;
            }
        </style>
        <script>
            function filterTable() {
                var inputDay = document.getElementById('input-day');
                var inputStartTime = document.getElementById('input-start-time');
                var inputEndTime = document.getElementById('input-end-time');

                var day = inputDay.value;
                var startTime = inputStartTime.value;
                var endTime = inputEndTime.value;

                var table = document.getElementById('table-horarios');
                var rows = table.getElementsByTagName('tr');

                for (var i = 1; i < rows.length; i++) {
                    var row = rows[i];
                    var cells = row.getElementsByTagName('td');
                    var dia = cells[1].innerText;
                    var horarioInicio = cells[2].innerText;
                    var horarioFim = cells[3].innerText;

                    var matchDay = day === 'Todos' || dia === day;
                    var matchTime = startTime === '' && endTime === '' || horarioInicio >= startTime && horarioFim <= endTime;

                    if (matchDay && matchTime) {
                        row.style.display = '';
                    } else {
                        row.style.display = 'none';
                    }
                }
            }
        </script>
    </head>
    <body>
        <h1>Horários das Disciplinas</h1>

        <div class="filter-container">
            <label class="filter-label">Dia:</label>
            <select id="input-day" onchange="filterTable()">
                <option value="Todos">Todos</option>
                <option value="Segunda-feira">Segunda-feira</option>
                <option value="Terça-feira">Terça-feira</option>
                <option value="Quarta-feira">Quarta-feira</option>
                <option value="Quinta-feira">Quinta-feira</option>
                <option value="Sexta-feira">Sexta-feira</option>
                <option value="Sábado">Sábado</option>
            </select>

            <label class="filter-label">Horário Início:</label>
            <input id="input-start-time" type="time" onchange="filterTable()">

            <label class="filter-label">Horário Fim:</label>
            <input id="input-end-time" type="time" onchange="filterTable()">
        </div>

        <table id="table-horarios">
            <tr>
                <th>Materia</th>
                <th>Dia</th>
                <th>Horario Inicio</th>
                <th>Horario Fim</th>
            </tr>
            $table_rows
        </table>
    </body>
    </html>
    ''')

    return html_template.substitute(table_rows=table_rows)

# HTTPRequestHandler personalizado para servir a página HTML
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/horarios':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            data = []
            with open('dados.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                data = [row for row in reader]

            materia_selecionada = self.headers.get('Materia')
            html = generate_html(data, materia_selecionada)
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('Página não encontrada'.encode('utf-8'))

# Inicializar o driver do Chrome
with webdriver.Chrome(service=service) as driver:
    driver.get('https://www.ufsm.br/cursos/graduacao/santa-maria/ciencia-da-computacao/horarios')

    with open('dados.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Materia', 'Dia', 'Horario_inicio', 'Horario_fim'])  # Cabeçalho

        semestre = 1
        while True:
            semestre_xpath = f'/html/body/main/div[2]/div/section/article/div/div[3]/div/div[5]/div[{semestre}]/div[1]/a'
            try:
                semestre_elemento = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, semestre_xpath)))
                print('\nSemestre:', semestre_elemento.text)

                disciplinas_xpath = f'/html/body/main/div[2]/div/section/article/div/div[3]/div/div[5]/div[{semestre}]/div[2]/div/div/div[1]/div'
                disciplinas = driver.find_elements(By.XPATH, disciplinas_xpath)

                if not disciplinas:
                    break

                for materia in disciplinas:
                    elemento_expansivel = materia.find_element(By.TAG_NAME, 'a')
                    print('Materia:', elemento_expansivel.text)
                    # Rolar a página pra pegar a próxima matéria
                    driver.execute_script("arguments[0].scrollIntoView(true);", elemento_expansivel)
                    driver.execute_script("arguments[0].click();", elemento_expansivel)
                    tabela_xpath = './/div[2]/div/div[2]/div/div[2]/table'
                    tabela = WebDriverWait(materia, 10).until(EC.visibility_of_element_located((By.XPATH, tabela_xpath)))
                    linhas = tabela.find_elements(By.TAG_NAME, 'tr')

                    for linha in linhas[1:]:  # Ignorar a primeira linha (cabeçalho da tabela)
                        elementos = linha.find_elements(By.TAG_NAME, 'td')
                        dia_semana = elementos[0].text
                        horario_inicio = elementos[1].text
                        horario_fim = elementos[2].text
                        writer.writerow([elemento_expansivel.text, dia_semana, horario_inicio, horario_fim])

                semestre += 1
            except:
                break

# Função para iniciar o servidor HTTP local
def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Servidor iniciado em http://localhost:8000')
    httpd.serve_forever()

run_server()
