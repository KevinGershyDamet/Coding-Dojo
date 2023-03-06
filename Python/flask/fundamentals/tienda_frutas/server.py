from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def bienvenida():
    return render_template('index.html', rep = 3, color = 'lightblue')

@app.route('/play/<int:num>')
def mostrar_cajas(num):
    return render_template('index.html', rep = num, color = 'lightblue')

@app.route('/play/<int:num>/<string:color>')
def cambiar_color(num, color):
    return render_template('index.html', rep = num, color = color)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración