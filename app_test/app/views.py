from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
#from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
#from .forms import LoginForm
from app.models import User, Class
import json


@app.route('/signin', methods=['GET', 'POST'])
def signin():
  login = SigninForm() 
  if ('user' in session):
    return redirect(url_for('profile')) 
  if login.validate_on_submit(): # means that user is either judge or project member 
    #TODO in login form
    session['user'] = login.finduser()
    return redirect(url_for('profile'))
  flash('Incorrect login details. Please try again or register for a new account.')
  return redirect(url_for('signin')) 


@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
  register = RegisterForm()
  if register.validate_on_submit():
    session['user'] = register.getuser()
    flash('you have succesfully registered!')
    return redirect(url_for('profile'))
  return render_template('newuser.html', register=register)

@app.route('/profile')
def user_profile():
    return

@app.route('/test')
def test_index():
    return render_template('test.html')
