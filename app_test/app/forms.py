from flask.ext.wtf import Form
from flask.ext.wtf.html5 import EmailField
from flask.ext.wtf.file import FileField, FileRequired, FileAllowed
from wtforms import validators, ValidationError, TextField, RadioField, TextAreaField, SubmitField, PasswordField, SelectMultipleField, FormField, SelectField
from flask import Flask, render_template, redirect, request
from app import db

class RegisterForm(Form):
	firstName = TextField("First name", [validators.Required("Please enter your first name.")])
	lastName = TextField("Last name", [validators.Required("Please enter your last name.")])	
	email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")]))
    major = TextField("Major", [validators.Required("Please enter your email address.")])
	year = TextField("Year", [validators.Required("Please enter your year")])
	gender = RadioField('Gender', choices=[('value1','Male'),('value2','Female')])
	courses = request.form.getList('courseKart')
	bio = TextField("Description", [validators.Required("Please enter in a short bio.")])
  	submit = SubmitField("Let's Study!")

    password = PasswordField('Password', [validators.Required("Please enter a password.")])
    pwdcheck = PasswordField('Password', [validators.Required("Please enter a password.")])

  	def validate(self):
  		if not Form.validate(self):
      		return False
	    if self.pwdcheck.data != self.password.data:
            self.password.errors.append("Please retype your password - they didn't match")
            return False

	    user = Member.query.filter(User.email = self.email.data.lower()).first()
	    if user:
            self.email.errors.append("That email is already taken")
            return False
	    else:
            user = User(firstName, lastName, email, gender, year, major, bio, password)
            classes = self.get_classes()
            user.classes = classes[:]
            return True

    def get_classes(self):
        classes
        for c in self.courses:
            class_to_add = Class.query.filter(Class.class_name==c).first()
            classes.append(class_to_add)
        return classes

    def getuser(self):
        user = User.query.filter(User.email==self.email.data.lower()).first()
        return user.user_id

class SigninForm(Form):	
    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")]))
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
  	submit = SubmitField("Let's Study!")

    def finduser(self):
        user = User.query.filter(User.email==self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
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


