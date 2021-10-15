from werkzeug.security import generate_password_hash, check_password_hash

class DocumentType():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def __repr__(self):
        return '<DocumentType {}>'.format(self.name)

class User():
    def __init__(self, id, name, lastName, password, documentType, is_admin=False):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.documentType = documentType
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def getDocumentType(self):
        return self.documentType
    
    def __repr__(self):
        return '<User {}>'.format(self.name)
    
""" ========================================================================== """
""" Lista de usuaruios para hacer pruebas """
users = []
documentTypes = []
def get_user(name):
    documentTypes.append(DocumentType(1, 'admin'))
    documentTypes.append(DocumentType(2, 'paciente'))
    documentTypes.append(DocumentType(3, 'medico'))
    users.append( User(1, 'admin', 'admin', 'admin', documentTypes[0]) )
    users.append( User(2, 'paciente', 'paciente', 'paciente', documentTypes[1]) )
    users.append( User(3, 'medico', 'medico', 'medico', documentTypes[2]) )
    for user in users:
        if user.name == name:
            return user
    return None

