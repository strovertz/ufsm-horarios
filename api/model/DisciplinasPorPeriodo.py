from pydantic import BaseModel
from typing import List, Optional, Any


class Nivel(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Modalidade(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Funcionamento(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Turno(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Tipo(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Local(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Classificacao(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class AreaConhecimento(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: Any
    descricao: Any


class Secretaria(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: Any
    descricao: Any
    sigla: Any
    url: Any
    endereco: Any
    secretaria: Any
    chefe: Any
    chefeSubstituto: Any
    atividadeChefia: Any
    situacao: Any
    cidade: Any


class Pessoa(BaseModel):
    error: bool | Any
    id: int | Any
    nome: str | Any
    nomeCivil: str | Any
    nomeSocial: Any
    enderecos: Any
    documentos: Any
    vinculos: Any
    usuarios: Any
    biometrias: Any
    biometriasNitgen: Any


class Chefe(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa
    matricula: str | Any
    cargo: Any
    lotacao: Any
    lotacaoOficial: Any
    centro: Any
    situacao: Any
    escolaridade: Any
    regimeJuridico: Any
    jornadaTrabalho: Any


class ChefeSubstituto(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa
    matricula: str | Any
    cargo: Any
    lotacao: Any
    lotacaoOficial: Any
    centro: Any
    situacao: Any
    escolaridade: Any
    regimeJuridico: Any
    jornadaTrabalho: Any


class AtividadeChefia(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Situacao(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Cidade(BaseModel):
    error: bool | Any
    id: int | Any
    nome: Any
    codigoIBGE: Any


class Unidade(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    sigla: str | Any
    url: str | Any
    endereco: Any
    secretaria: Secretaria | Any
    chefe: Chefe | Any
    chefeSubstituto: ChefeSubstituto | Any
    atividadeChefia: AtividadeChefia | Any
    situacao: Situacao | Any
    cidade: Cidade | Any


class Centro(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: Any
    descricao: Any
    sigla: Any
    url: Any
    endereco: Any
    secretaria: Any
    chefe: Any
    chefeSubstituto: Any
    atividadeChefia: Any
    situacao: Any
    cidade: Any


class Cargo(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: Any
    descricao: Any
    grupoCargo: Any
    tipoVinculo: Any


class Lotacao(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: Any
    descricao: Any
    sigla: Any
    url: Any
    endereco: Any
    secretaria: Any
    chefe: Any
    chefeSubstituto: Any
    atividadeChefia: Any
    situacao: Any
    cidade: Any


class LotacaoOficial(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: Any
    descricao: Any
    sigla: Any
    url: Any
    endereco: Any
    secretaria: Any
    chefe: Any
    chefeSubstituto: Any
    atividadeChefia: Any
    situacao: Any
    cidade: Any


class Escolaridade(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class RegimeJuridico(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class JornadaTrabalho(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Coordenador(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Cargo | Any
    lotacao: Lotacao | Any
    lotacaoOficial: LotacaoOficial | Any
    centro: Any
    situacao: Situacao | Any
    escolaridade: Escolaridade | Any
    regimeJuridico: RegimeJuridico | Any
    jornadaTrabalho: JornadaTrabalho | Any


class Curso(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    nivel: Nivel | Any
    modalidade: Modalidade | Any
    funcionamento: Funcionamento | Any
    turno: Turno | Any
    tipo: Tipo | Any
    local: Local | Any
    classificacao: Classificacao | Any
    areaConhecimento: AreaConhecimento | Any
    unidade: Unidade | Any
    centro: Centro | Any
    coordenador: Coordenador | Any
    url: str | Any
    grau: str | Any
    autorizacao: str | Any
    reconhecimento: str | Any
    renovacao: Any
    nome: str | Any
    nomeDiploma: str | Any
    nomeEmec: str | Any
    nomeUnificado: str | Any
    nomeIngles: str | Any
    codigoEmec: str | Any
    codigoUnificado: Any


class Situacao2(BaseModel):
    error: bool | Any
    id: Any
    codigo: str | Any
    descricao: str | Any


class TipoPeriodo(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class VersaoCurso(BaseModel):
    error: bool | Any
    id: int | Any
    curso: Curso
    numero: str | Any
    descricao: str | Any
    situacao: Situacao2
    cargaHorariaExtensao: int | Any
    cargaHorariaTotal: int | Any
    cargaHorariaMinima: int | Any
    cargaHorariaMaxima: int | Any
    totalCreditos: int | Any
    periodoIdeal: int | Any
    periodoMinimo: int | Any
    periodoMaximo: int | Any
    trancamentosTotais: int | Any
    trancamentosParciais: int | Any
    tipoPeriodo: TipoPeriodo | Any


class Estrutura(BaseModel):
    error: bool | Any
    id: int | Any
    versaoCurso: VersaoCurso | Any
    classificacao: Classificacao | Any
    descricao: str | Any
    minimoCreditos: Any
    maximoCreditos: Any
    cargaHorariaMinima: int | Any
    cargaHorariaMaxima: Any
    filhas: Any
    atividades: Any
    disciplinas: Any


class Departamento(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: Any
    descricao: Any
    sigla: Any
    url: Any
    endereco: Any
    secretaria: Any
    chefe: Any
    chefeSubstituto: Any
    atividadeChefia: Any
    situacao: Any
    cidade: Any


class Tipo1(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: str | Any


class TipoDisciplina(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class TipoAula(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: str | Any


class CargasHoraria(BaseModel):
    error: bool | Any
    id: int | Any
    tipoAula: TipoAula | Any
    horasAula: int | Any


class Disciplina1(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    departamento: Departamento | Any
    situacao: Situacao2 | Any
    tipo: Tipo1 | Any
    tipoDisciplina: TipoDisciplina | Any
    creditos: int | Any
    cargaHoraria: int | Any
    encargoDidatico: Optional[int | Any]
    objetivos: Any
    ementa: Any
    documentoPrograma: Any
    cargaHorariaExtensao: Any
    cargasHorarias: List[CargasHoraria] | Any
    programaDisciplina: Any
    turmas: Any


class Tipo2(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class TipoNota(BaseModel):
    error: bool | Any
    id: Any
    codigo: str | Any
    descricao: str | Any


class Disciplina(BaseModel):
    error: bool | Any
    id: int | Any
    estrutura: Estrutura | Any
    disciplina: Disciplina1 | Any
    cargaHorariaEad: Any
    tipo: Tipo2
    tipoNota: TipoNota
    notaMinima: float
    notaMaxima: int | Any
    periodoIdeal: int | Any
    temEquivalencias: Any
    temPreRequisitos: Any


class Chefe1(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Any
    lotacao: Any
    lotacaoOficial: Any
    centro: Any
    situacao: Any
    escolaridade: Any
    regimeJuridico: Any
    jornadaTrabalho: Any


class ChefeSubstituto1(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Any
    lotacao: Any
    lotacaoOficial: Any
    centro: Any
    situacao: Any
    escolaridade: Any
    regimeJuridico: Any
    jornadaTrabalho: Any


class Situacao4(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Unidade1(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    sigla: str | Any
    url: str | Any
    endereco: Any
    secretaria: Secretaria | Any
    chefe: Chefe1 | Any
    chefeSubstituto: ChefeSubstituto1 | Any
    atividadeChefia: AtividadeChefia | Any
    situacao: Situacao4 | Any
    cidade: Cidade | Any


class Coordenador1(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Cargo | Any
    lotacao: Lotacao | Any
    lotacaoOficial: LotacaoOficial | Any
    centro: Any
    situacao: Situacao4 | Any
    escolaridade: Escolaridade | Any
    regimeJuridico: RegimeJuridico | Any
    jornadaTrabalho: JornadaTrabalho | Any


class Curso1(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    nivel: Nivel | Any
    modalidade: Modalidade | Any
    funcionamento: Funcionamento | Any
    turno: Turno | Any
    tipo: Tipo2 | Any
    local: Local | Any
    classificacao: Classificacao | Any
    areaConhecimento: AreaConhecimento | Any
    unidade: Unidade1 | Any
    centro: Centro | Any
    coordenador: Coordenador1 | Any
    url: str | Any
    grau: str | Any
    autorizacao: str | Any
    reconhecimento: str | Any
    renovacao: Any
    nome: str | Any
    nomeDiploma: str | Any
    nomeEmec: str | Any
    nomeUnificado: str | Any
    nomeIngles: str | Any
    codigoEmec: str | Any
    codigoUnificado: Any


class Situacao6(BaseModel):
    error: bool | Any
    id: Any
    codigo: str | Any
    descricao: str | Any


class VersaoCurso1(BaseModel):
    error: bool | Any
    id: int | Any
    curso: Curso1 | Any
    numero: str | Any
    descricao: str | Any
    situacao: Situacao6 | Any
    cargaHorariaExtensao: int | Any
    cargaHorariaTotal: int | Any
    cargaHorariaMinima: int | Any
    cargaHorariaMaxima: int | Any
    totalCreditos: int | Any
    periodoIdeal: int | Any
    periodoMinimo: int | Any
    periodoMaximo: int | Any
    trancamentosTotais: int | Any
    trancamentosParciais: int | Any
    tipoPeriodo: TipoPeriodo | Any


class Estrutura1(BaseModel):
    error: bool | Any
    id: int | Any
    versaoCurso: VersaoCurso1 | Any
    classificacao: Classificacao | Any
    descricao: str | Any
    minimoCreditos: Any
    maximoCreditos: Any
    cargaHorariaMinima: int | Any
    cargaHorariaMaxima: Any
    filhas: Any
    atividades: Any
    disciplinas: Any


class Tipo4(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: str | Any


class CargasHoraria1(BaseModel):
    error: bool | Any
    id: int | Any
    tipoAula: TipoAula | Any
    horasAula: int | Any


class Disciplina2(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    departamento: Departamento | Any
    situacao: Situacao6 | Any
    tipo: Tipo4 | Any
    tipoDisciplina: TipoDisciplina | Any
    creditos: int | Any
    cargaHoraria: int | Any
    encargoDidatico: Optional[int | Any]
    objetivos: Any
    ementa: Any
    documentoPrograma: Any
    cargaHorariaExtensao: Any
    cargasHorarias: List[CargasHoraria1]
    programaDisciplina: Any
    turmas: Any


class Tipo5(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class DisciplinaCurriculo(BaseModel):
    error: bool | Any
    id: int | Any
    estrutura: Estrutura1 | Any
    disciplina: Disciplina2 | Any
    cargaHorariaEad: Any
    tipo: Tipo5 | Any
    tipoNota: TipoNota | Any
    notaMinima: float
    notaMaxima: int | Any
    periodoIdeal: int | Any
    temEquivalencias: Any
    temPreRequisitos: Any


class Tipo6(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: str | Any


class CargasHoraria2(BaseModel):
    error: bool | Any
    id: int | Any
    tipoAula: TipoAula | Any
    horasAula: int | Any


class Disciplina3(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    departamento: Departamento | Any
    situacao: Situacao6 | Any
    tipo: Tipo6 | Any
    tipoDisciplina: TipoDisciplina | Any
    creditos: int | Any
    cargaHoraria: int | Any
    encargoDidatico: Optional[int | Any]
    objetivos: Any
    ementa: Any
    documentoPrograma: Any
    cargaHorariaExtensao: Any
    cargasHorarias: List[CargasHoraria2] | Any
    programaDisciplina: Any
    turmas: Any


class Tipo7(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Chefe2(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Any
    lotacao: Any
    lotacaoOficial: Any
    centro: Any
    situacao: Any
    escolaridade: Any
    regimeJuridico: Any
    jornadaTrabalho: Any


class ChefeSubstituto2(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Any
    lotacao: Any
    lotacaoOficial: Any
    centro: Any
    situacao: Any
    escolaridade: Any
    regimeJuridico: Any
    jornadaTrabalho: Any


class Situacao9(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: Any


class Unidade2(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    sigla: str | Any
    url: str | Any
    endereco: Any
    secretaria: Secretaria | Any
    chefe: Chefe2 | Any
    chefeSubstituto: ChefeSubstituto2 | Any
    atividadeChefia: AtividadeChefia | Any
    situacao: Situacao9 | Any
    cidade: Cidade | Any


class Coordenador2(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Cargo | Any
    lotacao: Lotacao | Any
    lotacaoOficial: LotacaoOficial | Any
    centro: Any
    situacao: Situacao9 | Any
    escolaridade: Escolaridade | Any
    regimeJuridico: RegimeJuridico | Any
    jornadaTrabalho: JornadaTrabalho | Any


class Curso2(BaseModel):
    error: bool | Any
    id: int | Any
    codigo: str | Any
    descricao: str | Any
    nivel: Nivel | Any
    modalidade: Modalidade | Any
    funcionamento: Funcionamento | Any
    turno: Turno | Any
    tipo: Tipo7 | Any
    local: Local | Any
    classificacao: Classificacao | Any
    areaConhecimento: AreaConhecimento | Any
    unidade: Unidade2 | Any
    centro: Centro | Any
    coordenador: Coordenador2 | Any
    url: str | Any
    grau: str | Any
    autorizacao: str | Any
    reconhecimento: str | Any
    renovacao: Any
    nome: str | Any
    nomeDiploma: str | Any
    nomeEmec: str | Any
    nomeUnificado: str | Any
    nomeIngles: str | Any
    codigoEmec: str | Any
    codigoUnificado: Any


class Docente(BaseModel):
    error: bool | Any
    id: int | Any
    pessoa: Pessoa | Any
    matricula: str | Any
    cargo: Cargo | Any
    lotacao: Lotacao | Any
    lotacaoOficial: LotacaoOficial | Any
    centro: Any
    situacao: Situacao9 | Any
    escolaridade: Escolaridade | Any
    regimeJuridico: RegimeJuridico | Any
    jornadaTrabalho: JornadaTrabalho | Any


class Tipo8(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: str | Any


class DiaSemana(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: str | Any
    descricao: str | Any


class HorariosTurmaItem(BaseModel):
    error: bool | Any
    id: int | Any
    horarioInicio: str | Any
    horarioFim: str | Any
    tipo: Tipo8 | Any
    diaSemana: DiaSemana | Any


class Escopo(BaseModel):
    error: bool | Any
    item: int | Any
    sigla: Any
    descricao: str | Any


class Turma(BaseModel):
    error: bool | Any
    id: int | Any
    disciplinaCurriculo: DisciplinaCurriculo | Any
    disciplina: Disciplina3 | Any
    curso: Curso2 | Any
    vagasOferecidas: int | Any
    vagasOcupadas: int | Any
    vagasAumentadas: int | Any
    docentes: List[Docente] | Any
    codigo: str | Any
    cargaHorariaEad: Any
    horariosTurma: List[HorariosTurmaItem] | Any
    escopo: Escopo | Any


class DisciplinaTurma(BaseModel):
    disciplina: Disciplina | Any
    turmas: List[Turma] | Any


class Iten(BaseModel):
    disciplinaTurmas: List[DisciplinaTurma] | Any
    periodo: int | Any


class DisciplinasPorPeriodo(BaseModel):
    error: bool
    itens: List[Iten]
