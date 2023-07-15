# Documentação da API

## Execução

Para subir a API, execute o comando `docker compose up -d` no diretório raíz do projeto, que contém o arquivo `compose.yaml`. Após a execução bem-sucedida desse comando, a API estará disponível em `http://localhost:5000`.

## Endpoints

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Obter todos os horários de disciplinas de um curso de um campus

<details>
<summary><code>GET</code> <code><b>/api/campi/{campus}/cursos/{curso}/horarios</b></code></summary>

##### Parâmetros

> | Nome     | Tipo     | Obrigatório | Descrição        | Valores permitidos                                                                                      |
> | :------- | :------- | :---------- | :--------------- | :------------------------------------------------------------------------------------------------------ |
> | `campus` | `string` | `true`      | O nome do campus | `santa-maria`, `cachoeira-do-sul`, `frederico-westphalen`, `palmeira-das-missoes`                       |
> | `curso`  | `string` | `true`      | O nome do curso  | Qualquer curso da UFSM (e.g., `ciencia-da-computacao`, `sistemas-de-informacao`, `engenharia-eletrica`) |

##### Respostas

> | Código de status HTTP | Tipo                       | Resposta                                    |
> | :-------------------- | :------------------------- | :------------------------------------------ |
> | `200`                 | `application/json`         | [`HorariosDisciplina`](#Schemas)            |
> | `400`                 | `application/json`         | `{"code": "400", "message": "Bad request"}` |

##### Exemplo cURL

> ```javascript
>  curl http://localhost:5000/api/campi/santa-maria/cursos/ciencia-da-computacao/horarios
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
