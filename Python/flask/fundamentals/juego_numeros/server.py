from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'contraseña segura' # establece una clave secreta

@app.route('/')
def aleatorización(): # Esto permite que no se genere un número nuevo cada que regresemos a la página del juego
    import random
    session['aleatorio'] = random.randint(1,100)
    session['intentos'] = 0
    print(session['aleatorio'])
    return redirect('/juego')

@app.route('/juego')
def juego():
    return render_template('index.html')

@app.route('/procesamiento', methods = ['post'])
def datos():
    session['intentos'] += 1
    session['adivinado'] = int(request.form['adivinado'])
    
    if session['aleatorio'] < int(request.form['adivinado']):
        session['comparación'] = '¡Te excediste!'
        session['color'] = 'red'
    elif session['aleatorio'] > int(request.form['adivinado']):
        session['comparación'] = '¡Lo subestimaste!'
        session['color'] = 'red'
    else:
        session['comparación'] = '¡Acertaste! El número era ' + str(session['aleatorio'])
        session['color'] = 'green'

    if session['intentos'] == 5 and session['color'] == 'red':
        session['comparación'] = '¡Perdiste!'
        
    return redirect('/juego')

@app.route('/procesamiento_2', methods = ['post'])
def procesar():
    session['name'] = request.form['nombre']
    return redirect('registro')

@app.route('/registro')
def resumen():
    return render_template('registro.html')

@app.route('/destroy_session')
def reinicia():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)