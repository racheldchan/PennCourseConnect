from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
#from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db
#from .forms import LoginForm
from app.models import User, Class
from app.forms import SigninForm, RegisterForm
import json

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  login = SigninForm() 
  register = RegisterForm()
  if ('user' in session):
    return redirect(url_for('user_profile')) 
  if login.validate_on_submit(): # means that user is either judge or project member 
    #TODO in login form
    session['user'] = login.finduser()
    return redirect(url_for('user_profile'))
  if register.validate_on_submit():
    print("you have succesfully registered")
    session['user'] = register.getuser()
    flash('you have succesfully registered!')
    return redirect(url_for('user_profile'))
  #flash('Incorrect login details. Please try again or register for a new account.')
  #return redirect(url_for('new_user'))
  return render_template('signIn.html', register=register, login=login)

#unused/unnecessary now (/signin is the landing page w/ both sign up and sign in buttons)
@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
  login = SigninForm()
  register = RegisterForm()
  if register.validate_on_submit():
    print("you have succesfully registered")
    session['user'] = register.getuser()
    flash('you have succesfully registered!')
    return redirect(url_for('signin'))
    
  return render_template('newuser.html', register=register, login=login)

@app.route('/profile', methods=['GET', 'POST'])
def user_profile():
  if ('user' in session):
    user = User.query.filter_by(user_id=session['user']).first()
    thisUser = ''.join(json.dumps(user.serialize))
    usersJSON = [i.serialize for i in User.query.filter_by(curCourse=user.courseOpt)]
    jsonString = ''.join(json.dumps(o) + ";" for o in usersJSON)
    return render_template('profile.html', thisUser=thisUser, usersJSON=jsonString)
  return redirect(url_for('signin'))

@app.route('/test')
def test_index():
    return render_template('test.html')

@app.route('/update', methods=['GET', 'POST'])
def update_cur():
  if ('user' in session):
    course = request.args.get("course")
    room = request.args.get("room")
    assignment = request.args.get("assignment")
    user = User.query.filter_by(user_id=session['user']).first()
    user.curCourse = course
    user.curRoom = room
    user.curAssignment = assignment
    db.session.commit()
    return redirect(url_for('user_profile'))
  return redirect(url_for('signin'))

@app.route('/filter', methods=['GET', 'POST'])
def filter_page():
  if ('user' in session):
    filterOption = request.args.get("course")
    user = User.query.filter_by(user_id=session['user']).first()
    user.courseOpt = filterOption
    db.session.commit()
    return redirect(url_for('user_profile'))
  return redirect(url_for('signin'))
 

@app.route('/logout')
def logged_out():
  user = User.query.filter_by(user_id=session['user']).first()
  user.courseOpt = None
  user.curCourse = None
  user.curRoom = None
  user.curAssignment = None
  db.session.commit()
  del session['user']
  return redirect(url_for('signin'))

app.run(host='192.168.1.14', port=8080, debug=True)
