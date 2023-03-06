
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self ,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas').query_db(query)
        dojos_existentes = []
        for dojo in results:
            dojos_existentes.append(cls(dojo))
        return dojos_existentes
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s , NOW());"
        print(query)
        return connectToMySQL('dojos_ninjas').query_db(query, data)
    
    @classmethod
    def buscar(cls, identificacion):
        query = "SELECT first_name, last_name, age, dojos.name AS nombre_dojo FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, identificacion)
        return results
    
    @classmethod
    def busqueda_simple(cls, identificacion):
        query = "SELECT name FROM dojos WHERE id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas').query_db(query, identificacion)
        return results