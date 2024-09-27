from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/calc-triangulo')
def calc_triangulo():
    return render_template('calc-triangulo.html')

@app.route('/tipo-triangulo', methods=['GET'])
def tipo_triangulo_get():
    lado1 = float(request.args.get('lado1'))
    lado2 = float(request.args.get('lado2'))
    lado3 = float(request.args.get('lado3'))
    
    if lado1 == lado2 == lado3:
        return render_template('equilatero.html')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return render_template('isosceles.html')
    else:
        return render_template('escaleno.html')
    
@app.route('/media-notas', methods=['GET', 'POST'])
def media_notas():
    if request.method == 'POST':
        nota1 = float(request.form.get('nota1'))
        nota2 = float(request.form.get('nota2'))
        nota3 = float(request.form.get('nota3'))
        nota4 = float(request.form.get('nota4'))
        
        media = (nota1 + nota2 + nota3 + nota4) / 4
        
        if media >= 6:
            return render_template('aprovado.html')
        else:
            return render_template('reprovado.html')
        
    return render_template('media-notas.html')

if __name__ == '__main__':

    app.run(debug=True)