from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

@app.route('/')
def index():
    if 'contador' in session:
        session['contador'] += 1
    else:
        session['contador'] = 1
    return render_template("index.html")

@app.route('/adicionar', methods = ['post'])
def adicion():
    if 'incremento' in session:
        session['contador'] += int(session['incremento']) -1
    else:
        session['contador'] += 1
    return redirect('/')

@app.route('/modificar', methods = ['post'])
def modificacion():
    session['incremento'] = request.form['incremento']
    return redirect('/')

@app.route('/destroy_session', methods = ['post'])
def reinicia():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)