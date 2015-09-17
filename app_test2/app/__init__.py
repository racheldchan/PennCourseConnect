from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os.path as op
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
#app.config.from_pyfile('../config.py')
app.secret_key = '+p_+ Vc23A*b:>nG`{<L=QY7bN+|uM;IP]_<7BwHRP$b;qNwZsw]/yeIl*h?sGy&'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI


db = SQLAlchemy(app)
#version that works on my computer:
from app.models import Class, User
#from models import Class, User

# Create Database if doesn't already exist
# if not op.isfile(app.config['SQLALCHEMY_DATABASE_NAME'][0]):
#   with app.app_context():
#     db.create_all()

if not op.isfile(app.config['SQLALCHEMY_DATABASE_URI']):
   with app.app_context():
   	print("creating new db in %s", app.config['SQLALCHEMY_DATABASE_URI'])
   	db.create_all()

#version that works on my computer:
import app.views
#import views