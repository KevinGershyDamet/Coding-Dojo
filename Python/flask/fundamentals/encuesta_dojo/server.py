from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'contraseña segura' # establece una clave secreta

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/procesamiento', methods = ['post'])
def datos():
    session['name'] = request.form['nombre']
    session['email'] = request.form['email']
    session['idioma'] = request.form['idioma']
    session['país'] = request.form['país']
    session['check'] = request.form['verifica'] 
    print(session)
    return redirect('/resumen')

@app.route('/resumen')
def resumen():
    return render_template('resumen.html')

@app.route('/destroy_session')
def reinicia():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)