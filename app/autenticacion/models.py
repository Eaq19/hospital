from werkzeug.security import generate_password_hash, check_password_hash


class DocumentType():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __repr__(self):
        return '<DocumentType {}>'.format(self.name)


class User():
    def __init__(self, id, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, is_active=True, isAuthenticated=False):
        self.id = id
        self.name = name
        self.lastName = lastName
        self.password = generate_password_hash(password)
        self.documentType = documentType
        self.documentNumber = documentNumber
        self.birthDate = birthDate
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.accessDate = accessDate
        self.type = type
        self.is_active = is_active
        self.isAuthenticated = isAuthenticated

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def set_is_authenticated(self, isAuthenticated):
        self.isAuthenticated = isAuthenticated

    def get_is_authenticated(self):
        return self.isAuthenticated

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_documentType(self):
        return self.documentType

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def __repr__(self):
        return '<User {}>'.format(self.name)


""" ========================================================================== """
""" Lista de usuarios para hacer pruebas """
documentTypes = []
users = []

def loadUsers() :
    documentTypes.append(DocumentType(1, 'C.C.'))
    documentTypes.append(DocumentType(2, 'T.I.'))
    documentTypes.append(DocumentType(3, 'Pasaporte'))
    users.append(User(1, 'admin', 'admin', 'admin', documentTypes[0], '12304566', '24/12/1990', '3129989898', 'M', '16/10/2021', 1))
    users.append(User(2, 'medico', 'medico', 'medico', documentTypes[1], '12304566', '24/12/1990', '3129989898', 'M', '16/10/2021', 2))
    users.append(User(3, 'paciente', 'paciente', 'paciente', documentTypes[2], '12304566', '24/12/1990', '3129989898', 'M', '16/10/2021', 3))

def get_user(name):
    for user in users:
        if user.name == name:
            return user
    return None
