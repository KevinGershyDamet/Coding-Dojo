from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # establece una clave secreta

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form['email']) 
    session['username'] = request.form['name']
    session['usermail'] = request.form['email']
    # Estas se imprimen en la consola
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)

