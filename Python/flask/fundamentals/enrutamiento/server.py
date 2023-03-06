from flask import Flask  

app = Flask(__name__)    

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<string:var>')
def hello(var):
    return f'¡Hola, {var}!'

@app.route('/repeat/<int:num>/<string:var>')
def repetir(num, var):
    return f'{var * num}'

@app.route('/<cualquiera>')
def mens_error(cualquiera):
    return f'Error: la ruta deseada no existe'

if __name__=="__main__":
    app.run(debug=True)