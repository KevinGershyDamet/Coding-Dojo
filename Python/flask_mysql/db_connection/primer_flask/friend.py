# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Friend:
    def __init__(self ,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('mydb').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append( cls(friend) )
        return friends
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO friends ( first_name , last_name , occupation , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(occ)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('mydb').query_db(query, data)
    

    # query = "SELECT * FROM users WHERE email = %(email)s;"
    
    # # la variable de marcador de posición se llama email
    # # debe coincidir con el nombre de la clave en el diccionario de datos
    # data = { 
    #     # esta clave de 'email' en los datos debe tener un nombre que coincida con el marcador en la consulta
    #     'email' : request.form['email'] 
    # }
    # result = mysql.query_db(query, data)


