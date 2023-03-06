
from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self ,data):
        self.id = data['id']
        self.name = data['name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('usuarios').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def buscar(cls, identificacion):
        query = "select * from users where id = %(id)s;"
        return connectToMySQL('usuarios').query_db(query, identificacion)
    
    @classmethod
    def quitar(clas, identificacion):
        query = 'delete from users where id = %(id)s;'
        return connectToMySQL('usuarios').query_db(query, identificacion)
    
    @classmethod
    def modificar(clas, datos_nuevos):
        query = 'update users set name=%(nombre)s, occupation=%(ocupación)s, updated_at=now() where id = %(id)s;'
        return connectToMySQL('usuarios').query_db(query, datos_nuevos)
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( name , occupation , created_at, updated_at ) VALUES ( %(nombre)s , %(ocupación)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('usuarios').query_db(query, data)