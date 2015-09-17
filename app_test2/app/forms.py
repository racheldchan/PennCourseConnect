from flask.ext.wtf import Form
from flask.ext.wtf.html5 import EmailField
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms import validators, ValidationError, TextField, RadioField, TextAreaField, SubmitField, PasswordField, SelectMultipleField, FormField, SelectField
from flask import Flask, render_template, redirect, request, session
from app import db
from app.models import User, Class

class RegisterForm(Form):
    firstName = TextField("First name", [validators.Required("Please enter your first name.")])
    lastName = TextField("Last name", [validators.Required("Please enter your last name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    major = TextField("Major", [validators.Required("Please enter your email address.")])
    year = TextField("Year", [validators.Required("Please enter your year")])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female')])
    courses = TextField("Courses", [validators.Required("Please enter your classes separated by semicolons.")])
    bio = TextField("Description", [validators.Required("Please enter in a short bio.")])
    upLocation = TextField("Location", [validators.Required("Please submit your location")])
    submit = SubmitField("Let's Study!!")

    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    pwdcheck = PasswordField('Password', [validators.Required("Please enter a password.")])

    def validate(self):
        if not Form.validate(self):
            print("not valid")
            return False
        if self.pwdcheck.data != self.password.data:
            self.password.errors.append("Please retype your password - they didn't match")
            return False

        user = User.query.filter(User.email == self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            user = User(self.firstName.data, self.lastName.data, self.email.data, self.gender.data,
                self.year.data, self.major.data, self.bio.data, self.courses.data, self.upLocation.data, self.password.data)
            #classes = self.get_classes()
            #user.classes = classes[:]
            db.session.add(user)
            db.session.commit()
            return True

    def get_classes(self):
        classes = self.courses.data.split(";")
        for c in classes:
            print(c)
            #class_to_add = Class.query.filter(Class.class_name==c).first()
            #classes.append(class_to_add)
        return classes

    def getuser(self):
        user = User.query.filter(User.email==self.email.data.lower()).first()
        return user.user_id

    def printData():
        print("validating register form")
        print (self.firstName.data)
        print (self.lastName.data)
        print (self.email.data)
        print (self.major.data)
        print (self.year.data)
        print (self.gender.data)
        print (self.bio.data)
        print (self.password.data)
        print (self.pwdcheck.data)

class SigninForm(Form): 
    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    inLocation = TextField("Location", [validators.Required("Please submit your location.")])
    submit = SubmitField("Let's Study!")

    def finduser(self):
        user = User.query.filter(User.email==self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            user.location = self.inLocation
            db.session.commit()
            return user.user_id
        return None

    def validate(self):
        if not Form.validate(self):
            return False
        if self.finduser():
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False

