# Documentação da API

## Execução

Para subir a API, execute o comando `docker compose up -d` no diretório raíz do projeto, que contém o arquivo `compose.yaml`. Após a execução bem-sucedida desse comando, a API estará disponível em `http://localhost:5000`.

## Endpoints

#### Obter horários de disciplinas da UFSM a partir de um filtro de busca

<details>
<summary><code>GET</code> <code><b>/api/horarios-disciplinas?campus={campus}&curso={curso}&diaSemana={diaSemana}&horarioInicio={horarioInicio}&horarioFim={horarioFim}</b></code></summary>

##### Parâmetros

> | Nome            | Tipo     | Obrigatório | Descrição                                      | Valores permitidos                                                                                      |
> | :-------------- | :------- | :---------- | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
> | `campus`        | `string` | `true`      | O nome do campus                               | `santa-maria`, `cachoeira-do-sul`, `frederico-westphalen`, `palmeira-das-missoes`                       |
> | `curso`         | `string` | `true`      | O nome do curso                                | Qualquer curso da UFSM (e.g., `ciencia-da-computacao`, `sistemas-de-informacao`, `engenharia-eletrica`) |
> | `diaSemana`     | `string` | `false`     | O dia da semana em que a disciplina é ofertada | `domingo`, `segunda-feira`, `terca-feira`, `quarta-feira`, `quinta-feira`, `sexta-feira`, `sabado`      |
> | `horarioInicio` | `string` | `false`     | O horário em que a disciplina inicia           | Qualquer horário válido no formato `HH:MM`                                                              |
> | `horarioFim`    | `string` | `false`     | O horário em que a disciplina finaliza         | Qualquer horário válido no formato `HH:MM`                                                              |

##### Respostas

> | Código de status HTTP | Tipo                       | Resposta                                    |
> | :-------------------- | :------------------------- | :------------------------------------------ |
> | `200`                 | `application/json`         | `HorariosDisciplina[]`                      |
> | `400`                 | `application/json`         | `{"code": "400", "message": "Bad request"}` |

##### Exemplo cURL

> ```javascript
>  curl http://localhost:5000/api/horarios-disciplinas?campus=santa-maria&curso=sistemas-de-informacao&diaSemana=quarta-feira&horarioInicio=08:00&horarioFim=14:30
> ```

#### Schemas

<details>
<summary><code>HorariosDisciplina</code></summary>
<br>

> | Campo                      | Tipo       | Exemplo                                                      |
> | :------------------------- | :--------- | :----------------------------------------------------------- |
> | `ano`                      | `number`   | `2023`                                                       |
> | `campus`                   | `string`   | `"Santa Maria"`                                              |
> | `carga_horaria_disciplina` | `number`   | `120`                                                        |
> | `codigo_curso`             | `string`   | `"307"`                                                      |
> | `codigo_disciplina`        | `string`   | `"ELC1074"`                                                  |
> | `creditos_disciplina`      | `number`   | `5`                                                          |
> | `curso`                    | `string`   | `"Ciência da Computação - Bacharelado"`                      |
> | `dia_semana`               | `string`   | `"Terça-feira"`                                              |
> | `disciplina`               | `string`   | `"PROJETO DE SOFTWARE II"`                                   |
> | `docentes`                 | `string[]` | `["ANDREA SCHWERTNER CHARAO", "JOAO VICENTE FERREIRA LIMA"]` |
> | `horario_fim`              | `string`   | `"15:30:00"`                                                 |
> | `horario_inicio`           | `string`   | `"13:30:00"`                                                 |
> | `periodo`                  | `string`   | `"2. Semestre"`                                              |
> | `periodo_disciplina`       | `number`   | `99`                                                         |
> | `tipo_disciplina`          | `string`   | `"Teórica"`                                                  |
> | `vagas_aumentadas`         | `number`   | `0`                                                          |
> | `vagas_ocupadas`           | `number`   | `0`                                                          |
> | `vagas_oferecidas`         | `number`   | `15`                                                         |

</details>

</details>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Obter todos os campi da UFSM

<details>
<summary><code>GET</code> <code><b>/api/campi</b></code></summary>

##### Respostas

> | Código de status HTTP | Tipo                       | Resposta   |
> | :-------------------- | :------------------------- | :--------- |
> | `200`                 | `application/json`         | `Campus[]` |

##### Exemplo cURL

> ```javascript
>  curl http://localhost:5000/api/campi
> ```

##### Schemas

<details>
<summary><code>Campus</code></summary>
<br>

> | Campo           | Tipo     | Exemplo         |
> | :-------------- | :------- | :-------------- |
> | `nome_exibicao` | `string` | `"Santa Maria"` |
> | `nome_url`      | `string` | `"santa-maria"` |

</details>

</details>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Obter todos os cursos da UFSM

<details>
<summary><code>GET</code> <code><b>/api/cursos</b></code></summary>

##### Respostas

> | Código de status HTTP | Tipo                       | Resposta  |
> | :-------------------- | :------------------------- | :-------- |
> | `200`                 | `application/json`         | `Curso[]` |

##### Exemplo cURL

> ```javascript
>  curl http://localhost:5000/api/cursos
> ```

##### Schemas

<details>
<summary><code>Curso</code></summary>
<br>

> | Campo           | Tipo     | Exemplo                 |
> | :-------------- | :------- | :---------------------- |
> | `nome_exibicao` | `string` | `"Engenharia Elétrica"` |
> | `nome_url`      | `string` | `"engenharia-eletrica"` |

</details>

</details>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
