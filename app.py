from flask import Flask, render_template, request
from mochila import otimizar_estudos

app = Flask(__name__)

@app.route('/gerar_plano', methods=['POST'])
def gerar_plano():

    horas_disponiveis = float(request.form.get('tempo_livre'))
    plano, ganho_total = otimizar_estudos(disciplinas, horas_disponiveis)
    
    return render_template('resultado.html', plano=plano, ganho=ganho_total)