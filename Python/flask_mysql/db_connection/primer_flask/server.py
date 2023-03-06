from flask import Flask, render_template, redirect, request
# importar la clase de friend.py
from friend import Friend
app = Flask(__name__)

@app.route("/")
def index():
    friends = Friend.get_all()
    return render_template("index.html", friends = friends)

@app.route('/create_friend', methods = ['post'])
def crear_amigo():
    data = {'fname': request.form['fname'],
            'lname': request.form['lname'],
            'occ': request.form['occ']}
    Friend.save(data)
    return redirect('/')
            
if __name__ == "__main__":
    app.run(debug=True)

