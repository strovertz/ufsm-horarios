const API_BASE_URL = 'http://localhost:5000/api';

const filterParameters = {
  'campus': null,
  'curso': null,
  'diaSemana': null,
  'horarioInicio': null,
  'horarioFim': null
};

let horariosDisciplinas = [];

const populateCampiSelect = () => {
  const campiSelect = $('#campi-select');

  $.ajax({
    type: 'GET',
    url: `${API_BASE_URL}/campi`,
    success: (data, textStatus, jqXHR) => {
      data.forEach(campus => {
        const campusOption = $('<option>').attr('value', campus.nome_url).text(campus.nome_exibicao);
        campiSelect.append(campusOption);
      });
    },
    dataType: 'json'
  });
};

const populateCursosSelect = () => {
  const cursosSelect = $('#cursos-select');

  $.ajax({
    type: 'GET',
    url: `${API_BASE_URL}/cursos`,
    success: (data, textStatus, jqXHR) => {
      data.forEach(curso => {
        const cursoOption = $('<option>').attr('value', curso.nome_url).text(curso.nome_exibicao);
        cursosSelect.append(cursoOption);
      });
    },
    dataType: 'json'
  });
};

const getCurrentSemester = () => {
  const currentDate = new Date();
  const currentMonth = currentDate.getMonth() + 1;

  return (currentMonth >= 1 && currentMonth <= 6) ? 1 : 2;
};

const renderHeaderTitle = () => {
  const headerTitle = $('#header-title');

  headerTitle.text(`Horários de disciplinas da UFSM (${new Date().getFullYear()}/${getCurrentSemester()})`);
};

const sortHorariosDisciplinasByHorarioInicio = () => {
  if (!horariosDisciplinas || horariosDisciplinas.length === 0) {
    return;
  }

  horariosDisciplinas.sort((a, b) => {
    if (a.horario_inicio === b.horario_inicio) {
      return 0;
    } else if (a.horario_inicio > b.horario_inicio) {
      return 1;
    } else {
      return -1;
    }
  });
};

const renderHorariosDisciplinas = () => {
  if (!horariosDisciplinas) {
    return;
  }
  
  const horariosDisciplinasFiltrados = filterHorariosDisciplinas();

  $('#horarios-disciplinas-spinner-container').attr('hidden', true);
  
  if (horariosDisciplinasFiltrados.length === 0) {
    $('#horarios-disciplinas').attr('hidden', true);
    $('#horarios-disciplinas-not-found').attr('hidden', false);
  } else if (!$('#horarios-disciplinas').is(':visible')) {
    $('#horarios-disciplinas').attr('hidden', false);
    $('#horarios-disciplinas-not-found').attr('hidden', true);
  }

  if ($('#horarios-disciplinas-table-body').length !== 0) {
    $('#horarios-disciplinas-table-body').remove();
  }

  const table = $('#horarios-disciplinas-table');

  const tableBody = $('<tbody>', {'id': 'horarios-disciplinas-table-body'}).appendTo(table);

  sortHorariosDisciplinasByHorarioInicio();

  horariosDisciplinasFiltrados.forEach((horariosDisciplina, index) => {
    const row = $('<tr>', {
      'id': `horarios-disciplinas-table-body-row-${index}`,
      'class': 'horarios-disciplinas-table-body-row'
    }).appendTo(tableBody);

    const nomeExibicaoDisciplina = `${horariosDisciplina.disciplina} (${horariosDisciplina.codigo_disciplina})`;

    $('<td>', {
      'id': `horarios-disciplinas-table-body-row-${index}-cell-0`,
      'class': 'horarios-disciplinas-table-body-disciplina-cell'
    }).append(`<a href="https://ufsm.br/ementario/disciplinas/${horariosDisciplina.codigo_disciplina}" target="_blank" title="${nomeExibicaoDisciplina}">${nomeExibicaoDisciplina}</a>`).appendTo(row);

    $('<td>', {
      'id': `horarios-disciplinas-table-body-row-${index}-cell-1`,
      'class': 'horarios-disciplinas-table-body-docentes-cell'
    }).append(horariosDisciplina.docentes.map((docente, index) => index === horariosDisciplina.docentes.length - 1 ? docente : `${docente}<br>`)).appendTo(row);

    $('<td>', {
      'id': `horarios-disciplinas-table-body-row-${index}-cell-2`,
      'class': 'horarios-disciplinas-table-body-dia-semana-cell'
    }).text(horariosDisciplina.dia_semana).appendTo(row);

    $('<td>', {
      'id': `horarios-disciplinas-table-body-row-${index}-cell-3`,
      'class': 'horarios-disciplinas-table-body-horario-inicio-cell'
    }).text(horariosDisciplina.horario_inicio.slice(0, 5)).appendTo(row);

    $('<td>', {
      'id': `horarios-disciplinas-table-body-row-${index}-cell-4`,
      'class': 'horarios-disciplinas-table-body-horario-fim-cell'
    }).text(horariosDisciplina.horario_fim.slice(0, 5)).appendTo(row);
  });
};

const addSecondsToTimeString = (time) => {
  const hoursAndMinutes = time.split(':');

  const date = new Date();

  date.setHours(parseInt(hoursAndMinutes[0]));
  date.setMinutes(parseInt(hoursAndMinutes[1]));
  date.setSeconds(0);

  return date.toTimeString().slice(0, 8);
};

const compareTimeStrings = (time1, time2) => {
  const [hours1, minutes1, seconds1] = time1.split(':').map(Number);
  const [hours2, minutes2, seconds2] = time2.split(':').map(Number);

  if (hours1 === hours2 && minutes1 === minutes2 && seconds1 === seconds2) {
    return 0;
  } else if (hours1 > hours2 || (hours1 === hours2 && minutes1 > minutes2) || (hours1 === hours2 && minutes1 === minutes2 && seconds1 > seconds2)) {
    return 1;
  } else {
    return -1;
  }
};

const filterHorariosDisciplinas = () => {
  if (!horariosDisciplinas) {
    return [];
  }

  return horariosDisciplinas.filter(horariosDisciplina => {
    if (filterParameters.diaSemana && horariosDisciplina.dia_semana !== $('#dias-semana-select option:selected').text()) {
      return false;
    }

    if (filterParameters.horarioInicio && compareTimeStrings(filterParameters.horarioInicio, horariosDisciplina.horario_inicio) > 0) {
      return false;
    }
    
    if (filterParameters.horarioFim && compareTimeStrings(filterParameters.horarioFim, horariosDisciplina.horario_fim) < 0) {
      return false;
    }

    return true;
  });
};

const getHorariosDisciplinas = () => {
  $('#horarios-disciplinas').attr('hidden', true);
  $('#horarios-disciplinas-not-found').attr('hidden', true);
  $('#horarios-disciplinas-spinner-container').attr('hidden', false);

  const urlSearchParams = new URLSearchParams();

  if (filterParameters.campus) {
    urlSearchParams.append('campus', filterParameters.campus);
  }

  if (filterParameters.curso) {
    urlSearchParams.append('curso', filterParameters.curso);
  }

  $.ajax({
    type: 'GET',
    url: `${API_BASE_URL}/horarios-disciplinas?${urlSearchParams.toString()}`,
    success: (data, textStatus, jqXHR) => {
      horariosDisciplinas = data;
      renderHorariosDisciplinas();
    },
    dataType: 'json'
  });
};

const selectCampus = (value) => {
  filterParameters.campus = value;

  $('#cursos-select').attr('disabled', !value);
  $('#dias-semana-select').attr('disabled', !value);
  $('#horario-inicio-input').attr('disabled', !value);
  $('#horario-fim-input').attr('disabled', !value);

  if (!value) {
    horariosDisciplinas = [];
    renderHorariosDisciplinas();
  } else if (filterParameters.curso) {
    getHorariosDisciplinas();
  }
};

const selectCurso = (value) => {
  filterParameters.curso = value;

  $('#dias-semana-select').attr('disabled', !value);
  $('#horario-inicio-input').attr('disabled', !value);
  $('#horario-fim-input').attr('disabled', !value);

  if (!value) {
    horariosDisciplinas = [];
    renderHorariosDisciplinas();
  } else if (filterParameters.campus) {
    getHorariosDisciplinas();
  }
};

const selectDiaSemana = (value) => {
  filterParameters.diaSemana = value;

  if (!(filterParameters.campus && filterParameters.curso)) {
    return;
  }

  if (horariosDisciplinas && horariosDisciplinas.length > 0) {
    renderHorariosDisciplinas();
  } else {
    getHorariosDisciplinas();
  }
};

const selectHorarioInicio = (value) => {
  filterParameters.horarioInicio = addSecondsToTimeString(value);

  if (!(filterParameters.campus && filterParameters.curso)) {
    return;
  }

  if (horariosDisciplinas && horariosDisciplinas.length > 0) {
    renderHorariosDisciplinas();
  } else {
    getHorariosDisciplinas();
  }
};

const selectHorarioFim = (value) => {
  filterParameters.horarioFim = addSecondsToTimeString(value);

  if (!(filterParameters.campus && filterParameters.curso)) {
    return;
  }

  if (horariosDisciplinas && horariosDisciplinas.length > 0) {
    renderHorariosDisciplinas();
  } else {
    getHorariosDisciplinas();
  }
};

$(document).ready(() => {
  renderHeaderTitle();
  populateCampiSelect();
  populateCursosSelect();
});
