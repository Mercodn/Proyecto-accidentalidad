from flask import Flask, render_template, request, jsonify
import random
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    tipo = request.form.get('tipo')
    dia = request.form.get('dia')
    hora = request.form.get('hora')
    vehiculos = request.form.get('vehiculos')
    hipotesis = request.form.get('hipotesis')

    # Lógica de simulación
    if (hora >= '06:00' and hora <= '09:00') and (tipo in ['Choque', 'Volcamiento']) and (hipotesis in ['Imprudencia', 'Exceso de velocidad']):
        riesgo = 0.75
    else:
        riesgo = random.uniform(0.3, 0.6)

    interpretacion = 'Riesgo Bajo' if riesgo < 0.4 else 'Riesgo Medio' if riesgo < 0.7 else 'Riesgo Alto'

    # Guardar en log
    with open('log.csv', 'a', newline='') as csvfile:
        logwriter = csv.writer(csvfile)
        logwriter.writerow([datetime.now(), tipo, dia, hora, vehiculos, hipotesis, riesgo, interpretacion])

    return jsonify({'riesgo': riesgo, 'interpretacion': interpretacion})

@app.route('/prediccion')
def prediccion():
    return render_template('prediccion.html')

@app.route('/metodologia')
def metodologia():
    return render_template('metodologia.html')

@app.route('/datos-historicos')
def datos_historicos():
    return render_template('datos_historicos.html')

if __name__ == '__main__':
    app.run(debug=True)