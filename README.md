# Horários de Disciplinas - UFSM

## Objetivo

Facilitar a busca por disciplinas que se encaixem apenas no intervalo de horário e dias fornecidos, a ferramenta deve ser capaz de retornar todos os horários de todas as disciplinas de um curso da UFSM utilizando tecnicas de Scrap em Python com Selenium. Os dados são exportados para arquivos CSV e exibidos em um servidor local ```http://localhost:8000/horarios```. 

### Ferramentas

 - Python
 - Selenium
 - HTML

## Execução

Comece instalando as depêndencias do python necessárias. Utilize  ```pip install selenium``` para instalar a biblioteca responsavel pela navegação no chrome. Em seguida realize a instalação do *webdriver chrome*, a instalação deve seguir a seguinte documentação: https://chromedriver.chromium.org/getting-started.

Em seguida, basta clonar o repositório utilizando ```git clone https://github.com/strovertz/ufsm-horarios.git``` navegar até a pasta prd utilizando ```cd ufsm-horarios/prd``` e executar o programa com ```python3 ./scrap.py```.

