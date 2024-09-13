from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/menu')
def menu():
    return render_template ('menu.html')

@app.route('/reservations')
def reservations():
    return render_template ('reservation.html')

@app.route('/special-dishes')
def special():
    return render_template ('special-dishes.html')

@app.route('/team')
def team():
    return render_template ('team.html')

app.run(debug=True)