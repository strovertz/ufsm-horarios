# Horários de Disciplinas - UFSM

## Objetivo

Facilitar a busca por disciplinas que se encaixem apenas no intervalo de horário e dias fornecidos, a ferramenta deve ser capaz de retornar todos os horários de todas as disciplinas de um curso da UFSM utilizando tecnicas de Scrap em Python com Selenium. Os dados são exportados para arquivos CSV e exibidos em um servidor local ```http://localhost:8000/horarios```. 

### Ferramentas

 - Python
 - Selenium
 - HTML
 - xPath Finder (Chrome Extension)

## Execução

Para facilitar o processo de encontrar o path das divs, utilizeo o [xPath Finder](https://chrome.google.com/webstore/detail/xpath-finder/ihnknokegkbpmofmafnkoadfjkhlogph/related?hl=pt-BR) como ferramenta facilitadora, 

Comece instalando as depêndencias do python necessárias. Utilize  ```pip install selenium``` para instalar a biblioteca responsavel pela navegação no chrome. Em seguida realize a instalação do *webdriver chrome*, a instalação deve seguir a seguinte documentação: ```[ChromeDriver doc](https://chromedriver.chromium.org/getting-started)```.

Em seguida, basta clonar o repositório utilizando ```git clone https://github.com/strovertz/ufsm-horarios.git``` navegar até a pasta prd utilizando ```cd ufsm-horarios/prd``` e executar o programa com ```python3 ./scrap.py```.

### OUTPUT

O prompt exibe quais foram as disciplinas encontradas e inicia o servidor local.
![image](https://github.com/strovertz/ufsm-horarios/assets/74078237/194674f7-981a-4e6a-af64-d59c786e0b97)


## Necessidades de atualização: 

- Realizar requisições em tempo real para obter dados de outro curso durante a navegação no servidor;
- Realizar agrupamento por cadeira;
- Exibição de calendário;
- Exibir todas as ocorrências da mesma disciplina, ex: Input = Segunda-Feira, Inicio às 02:30 PM, Fim às 04:30 PM. Como resultado ela deve retornar a outra ocorrência dessa disciplina em outros dias da semana (Caso exista). 

A implantação dessas funcionalidades devem manter a ferramenta como um facilitador para encontrar matérias que se encaixam em um horário *x* para o dia *y* da semana, dessa forma, não podem aproximar ainda mais a ferramenta do site padrão da UFSM.
### Ferramenta
A atual versão esta sendo exibida dessa forma no browser:
![image](https://github.com/strovertz/ufsm-horarios/assets/74078237/024e8df3-81f7-41a0-b55d-c1caf96f0cef)
