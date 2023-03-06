from flask import Flask, render_template, redirect, request

from flask_app import app

from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    users = Usuario.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/procesar', methods = ['post'])
def procesar():
    datos_nuevos = {'nombre': request.form['nombre'],
                    'ocupación': request.form['ocupación']
                    }
    Usuario.save(datos_nuevos)
    return redirect('/')

@app.route('/mostrar/<string:id>')
def mostrar(id):
    identificacion = {'id': int(id)}
    hallado = Usuario.buscar(identificacion)
    return render_template('mostrar.html', hallado = hallado)

@app.route('/eliminar/<string:id>')
def eliminar(id):
    identificacion = {'id':int(id)}
    Usuario.quitar(identificacion)
    return redirect('/')

@app.route('/editar/<string:id>')
def editar(id):
    identificacion = {'id': int(id)}
    hallado = Usuario.buscar(identificacion)
    return render_template('editar.html', hallado = hallado)

@app.route('/modificar/<int:id>', methods = ['post'])
def cambiar(id):
    datos_nuevos = {'id':id,
                    'nombre': request.form['nombre'],
                    'ocupación': request.form['ocupación']
                    }
    Usuario.modificar(datos_nuevos)
    return redirect('/')