from flask import Flask, render_template, request
from mochila import otimizar_estudos

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/gerar_plano', methods=['POST'])
def gerar_plano():
    try:

        tempo_livre = float(request.form.get('tempo_livre', 0))
        materias = request.form.getlist('materia[]')
        horas = request.form.getlist('horas[]')
        dificuldades = request.form.getlist('dif[]')
        dias_prova = request.form.getlist('dias[]')
        
        disciplinas = []

        for i in range(len(materias)):
            nome = materias[i]

            if nome and nome.strip() != "":
                disciplinas.append({
                    "nome": nome,
                    "horas_necessarias": float(horas[i]),
                    "dificuldade": int(dificuldades[i]),
                    "dias_prova": int(dias_prova[i])
                })

        plano, ganho_total = otimizar_estudos(disciplinas, tempo_livre)

        tempo_gasto = sum(d['horas_necessarias'] for d in plano)

        return render_template(
            'index.html',
            plano=plano,
            ganho=ganho_total,
            tempo_gasto=tempo_gasto,
            tempo_livre_original=tempo_livre
        )
        
    except ValueError:
        return "Erro ao processar os dados. Certifique-se de usar números válidos.", 400

if __name__ == '__main__':
    app.run(debug=True)