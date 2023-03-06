from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def tablero_1():
    return render_template('index.html', x = 8, y = 8, color1 = 'white', color2 = 'black')

@app.route('/<int:num>')
def tablero_2(num):
    return render_template('index.html', x = 8, y = num, color1 = 'white', color2 = 'black')

@app.route('/<int:numx>/<int:numy>')
def tablero_3(numx, numy):
    return render_template('index.html', x = numx, y = numy, color1 = 'white', color2 = 'black')

@app.route('/<string:color1>/<int:numx>/<string:color2>/<int:numy>')
def tablero_4(color1, numx, color2, numy):
    return render_template('index.html', x = numx, y = numy, color1 = color1, color2 = color2)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
