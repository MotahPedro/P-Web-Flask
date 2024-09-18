from flask import Flask, render_template, request 

# Flask é a base para a aplicação
# render_template habilida a  renderização pelas rotas
# request puxa o dado da rota de acordo com o nome do input do form

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('imc.html')

@app.route('/calcular_imc_post', methods=['POST']) # Rota para o método POST do formulário corresponde a action="calcular_imc_post"
def calcular_imc():
    altura = float(request.form['txt_altura'])
    peso = float(request.form['txt_peso'])
    imc = peso/(altura*altura)
    # Usar uma f-string, você pode incluir expressões Python dentro de chaves {} dentro da string. Essas expressões serão avaliadas e seus resultados serão incorporados na string final.
    return render_template('imc.html', result_imc =  imc)

app.run(debug=True)