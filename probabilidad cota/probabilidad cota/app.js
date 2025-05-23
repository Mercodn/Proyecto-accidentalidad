document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const tipo = document.getElementById('tipo').value;
    const dia = document.getElementById('dia').value;
    const hora = document.getElementById('hora').value;
    const vehiculos = parseInt(document.getElementById('vehiculos').value);
    const hipotesis = document.getElementById('hipotesis').value;

    let probabilidad = Math.random() * (0.6 - 0.3) + 0.3; // Valor aleatorio entre 0.3 y 0.6

    if ((hora >= '06:00' && hora <= '09:00') && (tipo === 'Choque' || tipo === 'Volcamiento') && (hipotesis === 'Imprudencia' || hipotesis === 'Exceso de velocidad')) {
        probabilidad = 0.7 + Math.random() * 0.3; // Valor entre 0.7 y 1
    }

    const interpretacion = probabilidad < 0.4 ? 'Riesgo Bajo' : probabilidad < 0.7 ? 'Riesgo Medio' : 'Riesgo Alto';
    const color = probabilidad < 0.4 ? 'green' : probabilidad < 0.7 ? 'yellow' : 'red';

    document.getElementById('probabilidad').textContent = probabilidad.toFixed(2);
    document.getElementById('interpretacion').textContent = interpretacion;
    document.getElementById('interpretacion').style.color = color;
});