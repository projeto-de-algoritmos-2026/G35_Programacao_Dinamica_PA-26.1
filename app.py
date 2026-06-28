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
        nomes = request.form.getlist('nome[]')
        horas = request.form.getlist('horas_necessarias[]')
        dificuldades = request.form.getlist('dificuldade[]')
        dias = request.form.getlist('dias_prova[]')

        disciplinas = []
        for i in range(len(nomes)):
            disciplinas.append({
                'nome': nomes[i],
                'horas_necessarias': float(horas[i]),
                'dificuldade': int(dificuldades[i]),
                'dias_prova': int(dias[i])
            })

        if not disciplinas:
            return render_template('index.html')

        plano, ganho = otimizar_estudos(disciplinas, tempo_livre)

        return render_template('index.html', plano=plano, ganho=ganho, gerou=True)
        
    except Exception as e:

        print(f"Erro no processamento: {e}")
        return f"<h1>Erro interno no Python:</h1><p>{e}</p><a href='/'>Voltar</a>"

if __name__ == '__main__':

    app.run(debug=True)