from werkzeug.security import generate_password_hash, check_password_hash
from ..__init__ import db

class DocumentType(db.Model):

    __tablename__ = 'document_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return DocumentType.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return DocumentType.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return DocumentType.query.all()

    def __repr__(self):
        return '<DocumentType {}>'.format(self.name)

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lastName = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    documentType = db.Column(db.Integer, db.ForeignKey('document_type.id', ondelete='CASCADE'), nullable=False)
    documentNumber = db.Column(db.String(256), unique=True, nullable=False)
    birthDate = db.Column(db.Date, nullable=False)
    phoneNumber = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    accessDate = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=False)
    isAuthenticated = db.Column(db.Boolean, default=False)

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

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return User.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return User.query.all()

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
    loadUsers()
    for user in users:
        if user.name == name and user.is_active == True :
            return user
    return None

"""
class DocumentType(db.Model):

    __tablename__ = 'document_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return DocumentType.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return DocumentType.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return DocumentType.query.all()

    def __repr__(self):
        return '<DocumentType {}>'.format(self.name)


class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lastName = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    documentType = db.Column(db.Integer, db.ForeignKey('document_type.id', ondelete='CASCADE'), nullable=False)
    documentNumber = db.Column(db.String(256), unique=True, nullable=False)
    birthDate = db.Column(db.Date, nullable=False)
    phoneNumber = db.Column(db.String(128), nullable=False)
    gender = db.Column(db.String(128), nullable=False)
    accessDate = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=False)
    isAuthenticated = db.Column(db.Boolean, default=False)

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

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return User.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return User.query.all()

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Admin(User) :

    def __init__(self, id, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, level, is_active=False, isAuthenticated=False):
        super().__init__(id, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, is_active, isAuthenticated)
        self.level = level

    def __repr__(self):
        return '<Admin {}>'.format(self.name)

class Doctor(User) :

    def __init__(self, id, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, specialty, is_active=False, isAuthenticated=False):
        super().__init__(id, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, is_active, isAuthenticated)
        self.specialty = specialty

    def __repr__(self):
        return '<Doctor {}>'.format(self.name)

class Patient(User) :

    def __init__(self, id, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, listAppointment, is_active=False, isAuthenticated=False):
        super().__init__(id, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, is_active, isAuthenticated)
        self.listAppointment = listAppointment

    def __repr__(self):
        return '<Patient {}>'.format(self.name)

class Comment():
    def __init__(self, id, date, doctor:Doctor, txt):
        self.id = id
        self.date = date
        self.doctor = doctor
        self.txt = txt

    def __repr__(self):
        return '<Comment {}>'.format(self.id)

class AppointmentType():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<AppointmentType {}>'.format(self.id)

class Appointment():
    def __init__(self, id, doctor:Doctor, date, creationDate, patient:Patient, comments:Comment, appointmentType:AppointmentType, phoneNumber, is_active=True):
        self.id = id
        self.doctor = doctor
        self.date = date
        self.creationDate = creationDate
        self.idPatient = patient
        self.comments = comments
        self.appointmentType = appointmentType
        self.phoneNumber = phoneNumber
        self.is_active = is_active

    def __repr__(self):
        return '<Appointment {}>'.format(self.id)

documentTypes = []
users = []

def loadUsers() :
    documentTypes.append(DocumentType(1, 'C.C.'))
    documentTypes.append(DocumentType(2, 'T.I.'))
    documentTypes.append(DocumentType(3, 'Pasaporte'))
    users.append(Admin(1, 'admin', 'admin', 'admin', documentTypes[0], '12304566', '24/12/1990', '3129989898', 'M', '16/10/2021', 1, 'Total', True))
    users.append(Doctor(2, 'medico', 'medico', 'medico', documentTypes[1], '12304566', '24/12/1990', '3129989898', 'M', '16/10/2021', 2, 'General', True))
    users.append(Patient(3, 'paciente', 'paciente', 'paciente', documentTypes[2], '12304566', '24/12/1990', '3129989898', 'M', '16/10/2021', 3, [], True))

def get_user(name):
    loadUsers()
    for user in users:
        if user.name == name and user.is_active == True :
            return user
    return None
"""