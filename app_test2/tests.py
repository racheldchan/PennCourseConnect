from app import app, db
from app.models import User, Class

def printTables():
	print("Students---------------------")
	students = User.query.filter()
	classes = Class.query.filter()

	for student in students:
		print('%p', student)

	for class_ in classes:
		print('%p', class_)

	# for student in students:
	# 	print '%s | %s | %s | %s | %s | %s | %s | %s | %s | %p', (student.firstname, student.lastname, 
	# 															student.username, student.email, student.gender, student.year
	# 															student.major, student.bio, student.classes)

	# print "Classes---------------------"
	# classes = Class.query.filter()
	# for class_ in classes:
	# 	print '%s | ', class_.class_name



#sahil = User('Sahil', 'Shah', 'deltaspin@gmail.com', 'male', '2016', 'CMPE', 'I love computer science', 'pwd1')
#nickhil = User('Nickhil', 'Nabar', 'nick@gmail.com', 'male', '2017', 'CIS', 'I dont love computer science', 'pwd1')
#murray = User('Eric', 'Murray','murr@gmail.com', 'male', '2017', 'CIS', 'I love CIS110', 'pwd3')


#cis350 = Class('CIS 350')
#cis455 = Class('CIS 455')
#cis120 = Class('CIS 120')
#cis121 = Class('CIS 121')

#Add classes
#db.session.add(cis350)
#db.session.add(cis455)
#db.session.add(cis120)
#db.session.add(cis121)
#db.session.commit()

#Add users
#db.session.add(sahil)
#db.session.add(nickhil)
#db.session.add(murray)
#db.session.commit()
#printTables()

#Check if updating a user and then committing again works
#user = User.query.filter(User.firstname=='Sahil').first()
#user.bio = 'I wanted to change my bio a little'
#db.session.commit()

#Add class to a user
#class_to_add = Class.query.filter(Class.class_name=='CIS 120').first()
#user = User.query.filter(User.firstname=='Eric').filter(User.lastname=='Murray').first()
#user.classes.append(class_to_add)
#nics = User.query.filter(User.username=='nickhil').first()
#nics.classes.append(class_to_add)

#db.session.commit()

printTables()
