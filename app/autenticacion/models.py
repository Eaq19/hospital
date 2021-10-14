from werkzeug.security import generate_password_hash, check_password_hash


class User():
    def __init__(self, id, nombre, apellido, password, is_admin=False):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.nombre)
    
""" ========================================================================== """
""" Lista de usuaruios para hacer pruebas """
users = []
def get_user(nombre):
    for user in users:
        if user.nombre == nombre:
            return user
    return None
