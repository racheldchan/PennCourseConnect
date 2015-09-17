from flask import *
import sqlite3
import json

DATABASE = 'studentInfo.db'


# adds a student to the db
@debug
def add_student_info(form):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    studentName = form['name']
    gender = form['gender']
    year = form['year']
    major = form['major']
    bio = form['bio']

    courses = []

    course1 = form['class1']
    course2 = form['class2']
    course3 = form['class3']
    course4 = form['class4']
    course5 = form['class5']
    course6 = form['class6']
    course7 = form['class7']

    allCourses = [course1, course2, course3, course4, course5, course6, course7]

    for course in allCourses:
        if course is not null:
            courses.append(course)

    c.execute('insert into students (name, gender, year, major, bio, courses) \
                values (?, ?, ?, ?, ?, ?)', (studentName, gender, year, major, bio, courses))
    conn.commit()
    conn.close()
    return name + " successfully added to the students database!"
