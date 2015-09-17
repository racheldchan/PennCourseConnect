from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os.path as op
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
#app.config.from_pyfile('../config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI


db = SQLAlchemy(app)
from app.models import Class, User


# Create Database if doesn't already exist
# if not op.isfile(app.config['SQLALCHEMY_DATABASE_NAME'][0]):
#   with app.app_context():
#     db.create_all()

if not op.isfile(app.config['SQLALCHEMY_DATABASE_URI']):
   with app.app_context():
   	print ("creating new db in %s", app.config['SQLALCHEMY_DATABASE_URI'])
   	db.create_all()

import app.views