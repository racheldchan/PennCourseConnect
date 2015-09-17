from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from app import db
from werkzeug import generate_password_hash, check_password_hash
 
#Base = declarative_base()

#for many-to-many relationship
# association_table = Table('association', Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.user_id')),
#     Column('class_id', Integer, ForeignKey('classes.class_id'))
# )

association_table = db.Table('association',
    Column('user_id', Integer, ForeignKey('users.user_id')),
    Column('class_id', Integer, ForeignKey('classes.class_id'))
)


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    gender = db.Column(db.String(1))
    year = db.Column(db.String(4))
    major = db.Column(db.String(120))
    bio = db.Column(db.String(1000))
    #classes = relationship("Class", secondary=association_table, backref="users")
    courses = db.Column(db.String(50))
    location = db.Column(db.String(40))
    pwdhash = db.Column(db.String(100))
    curCourse = db.Column(db.String(10))
    curRoom = db.Column(db.String(10))
    curAssignment = db.Column(db.String(10))
    courseOpt = db.Column(db.String(10))


    def __init__(self, firstname, lastname, email, gender, year, major, bio, courses, location, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.gender = gender
        self.year = year
        self.major = major
        self.bio = bio
        self.courses = courses
        self.location = location
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    @property
    def serialize(self):
        return {
            'id' : self.user_id,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'gender' : self.gender,
            'year' : self.year,
            'major' : self.major,
            'bio' : self.bio,
            'location' : self.location,
            'curCourse' : self.curCourse,
            'curRoom' : self.curRoom,
            'curAssignment' : self.curAssignment
        }

    def __repr__(self):
        return '<User %r, %r, %r, %r, %r, %r, %r, %r, %r>' % (self.email, self.firstname, self.lastname, self.gender, self.year, self.major, self.courses, self.bio, self.location)
  # python 3

class Class(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(10), unique=True)

    def __init__(self, class_name):
        self.class_name = class_name

    def get_id(self):
        try:
            return unicode(self.class_id)  # python 2
        except NameError:
            return str(self.class_id)

    def __repr__(self):
        return '<Class %r>' % self.class_name
  #python 3

