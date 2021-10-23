from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class DocumentType(db.Model):

    __tablename__ = 'document_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
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
    type = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    isAuthenticated = db.Column(db.Boolean, default=False)
    level = db.Column(db.Integer, nullable=True)
    specialty = db.Column(db.String(128), nullable=True)

    def __init__(self, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, level:int, specialty, is_active=True, isAuthenticated=False):
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
        self.level = level
        self.specialty = specialty

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

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

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

    def __init__(self, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, level:int, is_active=True, isAuthenticated=False):
        super().__init__(name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, level, None, is_active, isAuthenticated)

    def __repr__(self):
        return '<Admin {}>'.format(self.name)

class Doctor(User) :

    def __init__(self, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, specialty, is_active=True, isAuthenticated=False):
        super().__init__(name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, None, specialty, is_active, isAuthenticated)

    def __repr__(self):
        return '<Doctor {}>'.format(self.name)

class Patient(User) :

    def __init__(self, name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, is_active=True, isAuthenticated=False):
        super().__init__(name, lastName, password, documentType, documentNumber, birthDate, phoneNumber, gender, accessDate, type, None, None, is_active, isAuthenticated)

    def __repr__(self):
        return '<Patient {}>'.format(self.name)

class Comment(db.Model):

    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    doctor = db.Column('doctor', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    txt = db.Column(db.Text, nullable=False)

    def __init__(self, date, doctor:Doctor, txt):
        self.date = date
        self.doctor = doctor
        self.txt = txt

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
        return Comment.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Comment.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return Comment.query.all()

    def __repr__(self):
        return '<Comment {}>'.format(self.id)

class AppointmentType(db.Model):

    __tablename__ = 'appointment_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
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
        return AppointmentType.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return AppointmentType.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return AppointmentType.query.all()

    def __repr__(self):
        return '<AppointmentType {}>'.format(self.id)

class Appointment(db.Model):

    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    doctor = db.Column('doctor', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    creationDate = db.Column(db.Date, nullable=False)
    appointmentType = db.Column('appointment_type', db.Integer, db.ForeignKey('appointment_type.id', ondelete='CASCADE'), nullable=False)

    def __init__(self, doctor:Doctor, date, creationDate, patient:Patient, comments:Comment, appointmentType:AppointmentType):
        self.doctor = doctor
        self.date = date
        self.creationDate = creationDate
        self.idPatient = patient
        self.comments = comments
        self.appointmentType = appointmentType
    
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
        return Appointment.query.get(id)
    
    @staticmethod
    def get_by_name(name):
        return Appointment.query.filter_by(name=name).first()

    @staticmethod
    def get_all():
        return Appointment.query.all()

    def __repr__(self):
        return '<Appointment {}>'.format(self.id)

""" ========================================================================== """
""" Lista de usuarios para hacer pruebas """
def loadDocumentType() :
    documentTypes = DocumentType.get_all()
    if not documentTypes :
        DocumentType('C.C.').save()
        DocumentType('T.I.').save()
        DocumentType('Pasaporte').save()
        documentTypes = DocumentType.get_all()
    return documentTypes

def loadData():
    loadUsers(loadDocumentType())

def loadUsers(documentTypes) :
    if not User.get_all() :
        Admin('admin', 'admin', 'admin', documentTypes[0].get_id(), '12304566', '24/12/1990', '3129989898', 'M', '16/10/2021', 1, 1).save()
        Doctor('medico', 'medico', 'medico', documentTypes[1].get_id(), '12304576', '24/12/1990', '3129989898', 'M', '16/10/2021', 2, "General").save()
        Patient('paciente', 'paciente', 'paciente', documentTypes[2].get_id(), '12304586', '24/12/1990', '3129989898', 'M', '16/10/2021', 3).save()
    

def get_user(name):
    for user in User.get_all():
        if user.name == name and user.is_active == True :
            return user
    return None