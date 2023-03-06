from flask import Flask, render_template, redirect, request

from flask_app import app

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def index():
    dojos_existentes = Dojo.get_all()
    return render_template("dojos.html", dojos_existentes = dojos_existentes)

@app.route('/agregar_dojo', methods=['post'])
def agregar_dojo():
    datos_nuevo_dojo = {'name': request.form['name']}
    Dojo.save(datos_nuevo_dojo)
    return redirect('/dojos')

@app.route('/nuevo_ninja')
def nuevo_ninja():
    dojos_existentes = Dojo.get_all()
    return render_template('nuevo_ninja.html', dojos_existentes = dojos_existentes)

@app.route('/agregar_ninja', methods=['post'])
def agregar_ninja():
    datos_nuevo_ninja = {'first_name': request.form['first_name'],
                        'last_name': request.form['last_name'],
                        'age': request.form['age'],
                        'dojo_id': request.form['seleccion_dojo']}
    Ninja.save(datos_nuevo_ninja)
    return redirect('/lista_ninjas_por_dojo/' + datos_nuevo_ninja['dojo_id'])

@app.route('/lista_ninjas_por_dojo/<int:dojo_id>')
def mostrar_ninjas_por_dojo(dojo_id):
    identificacion = {'dojo_id': dojo_id}
    lista_por_dojo = Dojo.buscar(identificacion)
    dojo_x = Dojo.busqueda_simple(identificacion)
    return render_template('ninjas_dojo.html', lista_por_dojo = lista_por_dojo, dojo_x = dojo_x)
