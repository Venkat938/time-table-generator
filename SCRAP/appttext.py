from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/jntuk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
#mysql.connector connection code

"""mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="jntuk"
)
"""
#This is the dashboard route where we are going to
@app.route('/')
def dashboard():
    return render_template("dashboard.html")




#Creating Teacheradd table for our jntuk database
class Teacheradd(db.Model):
    __tablename__ = "Teacheradd"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    branch = db.Column(db.String(10))
    def __init__(self, name,branch):
        self.name = name
        self.branch=branch

#query on all our teacher data
@app.route('/teacheradd')
def teacheradd():
    all_data = Teacheradd.query.all()

    for i in all_data:

        print(i)

    return render_template("teacheradd.html", employees = all_data,count=len(all_data))


#this route is for inserting teacher data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
        branch=request.form['branch']
        my_data = Teacheradd(name,branch)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Faculty Inserted Successfully")
 
        return redirect(url_for('teacheradd'))
 
 
#this is our update route where we are going to update our Faculty
@app.route('/updateteacher', methods = ['GET', 'POST'])
def updateteacher():
 
    if request.method == 'POST':
        my_data = Teacheradd.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.branch=request.form['branch']
 
        db.session.commit()
        flash("Employee Updated Successfully")
 
        return redirect(url_for('teacheradd'))
 
 
 
 
#This route is for deleting our faculty
@app.route('/deleteteacher/<id>/', methods = ['GET', 'POST'])
def deleteteacher(id):
    my_data = Teacheradd.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Employee Deleted Successfully")
 
    return redirect(url_for('teacheradd'))


#creating configure teacher/subjects table
class Teacherconfigtable(db.Model):

    __tablename__ = "teacherconfigtable"
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(100))

    subject=db.Column(db.String(100))
 
    def __init__(self, name,subject):
 
        self.name = name

        self.subject=subject


db.create_all()




#This is the class configuration route where we are going to
@app.route('/teacherconfig',methods=["POST", "GET"])
def teacherconfig():

    """mycursor = mydb.cursor()
            
                mycursor.execute("SELECT name from teacheradd")
            
                myresult = mycursor.fetchall()
            
                res=[list(i) for i in myresult]"""

    res2=Teacheradd.query.all()

    """for i in range(len(res)):
                    res2.append(res[i][0])"""

    sub=Subject.query.with_entities(Subject.name).all()

    conf=Teacherconfigtable.query.all()

    for i in sub:
        print(i)

    return render_template("teacherconfigworking.html", teacherlis=res2,sub=sub,conf=conf)



#configuring teachers and subjects
@app.route('/teacherconfigadd',methods=["POST", "GET"])    
def teacherconfigadd():
    if request.method == 'POST':
 

        name = request.form['teachers']
        subject=request.form['subjects']
        my_data = Teacherconfigtable(name,subject)
        db.session.add(my_data)
        db.session.commit()
 
        flash("subject is configured to faculty Successfully")
 
        return redirect(url_for('teacherconfig'))

    



#Creating Classadd table for our jntuk database
class Courseadd(db.Model):
    __tablename__ = "courseadd"
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(100))

    semisters=db.Column(db.Integer)
 
    def __init__(self, coursename,semisters):
 
        self.name = coursename

        self.semisters=semisters


db.create_all()


@app.route('/courseadd')
def courseadd():
    all_data = Courseadd.query.all()
 
    return render_template("courseadd.html", courses= all_data)


#all routes of dropdown CLassadd

@app.route('/insertcourse', methods = ['POST'])
def insertcourse():
 
    if request.method == 'POST':
 
        coursename = request.form['course']
        semisters=request.form['semisters']
 
        my_data = Courseadd(coursename,semisters)
        db.session.add(my_data)
        db.session.commit()
 
        flash("course Inserted Successfully")
 
        return redirect(url_for('courseadd'))
 
 
#this is our update route where we are going to update our Faculty
@app.route('/updatecourse', methods = ['GET', 'POST'])
def updatecourse():
 
    if request.method == 'POST':
        my_data = Courseadd.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']

        my_data.semisters =request.form['semisters']
 
        db.session.commit()
        flash("course Updated Successfully")
 
        return redirect(url_for('courseadd'))
 
 
 
 
#This route is for deleting our employee
@app.route('/deletecourse/<id>/', methods = ['GET', 'POST'])
def deletecourse(id):
    my_data = Courseadd.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("course Deleted Successfully")
 
    return redirect(url_for('classadd'))







#This is the class configuration route where we are going to
@app.route('/classconfig')
def classconfig():
    all_course=Courseadd.query.all()

    all_teacher=Teacheradd.query.all()

    all_subject=Subject.query.all()

    l1,l2=[],[]
    for i in all_course:
              l1.append(i.name)
              l2.append(i.semisters)
              
    pythontojson=dict(zip(l1,l2))



    return render_template("classconfig.html",all_course=all_course,all_teacher=all_teacher,all_subject=all_subject,json_object=pythontojson)




#Creating btechsubject table for our jntuk database
class Subject(db.Model):
    #__tablename__ = "subjectadd"

    id = db.Column(db.Integer, primary_key = True)

    name=  db.Column(db.String(100))

    course= db.Column(db.String(60))


    sem= db.Column(db.String(10))

    subjecttype= db.Column(db.String(20))

 
    def __init__(self,name,sem,subjecttype,course):
 
        self.name = name
        self.course=course
        self.subjecttype=subjecttype
        self.sem=sem


db.create_all()



#route on all our btech subjects list
@app.route('/subject')
def subject():

    print('8')
    all_subjects = Subject.query.all()

    all_course=Courseadd.query.all()

    #print(all_course)

    #mycursor = mydb.cursor()

    #mycursor.execute("SELECT name,semisters from courseadd")

    #all_course = mycursor.fetchall()

    l1,l2=[],[]
    for i in all_course:
              l1.append(i.name)
              l2.append(i.semisters)
              
    pythontojson=dict(zip(l1,l2))

    """for i,j in all_courses.items():
              print(i,j)"""
              
    json_object = json.dumps(pythontojson)
    print(json_object)


    sem=8
    #r=db.engine.execute('SELECT name,semisters from courseadd')


 
    return render_template("subject.html",subjects = all_subjects,all_course=all_course,sem=sem,json_object=pythontojson)



#this route is for inserting btech subjects data to mysql database via html forms
@app.route('/subjectadd', methods = ['POST'])
def subjectadd():
 
    if request.method == 'POST':
 
        name = request.form['name']

        name_list=name.split(",")

        for i in name_list:

            name=i

            course=request.form['course']
            sem=request.form['sem']
            subjecttype=request.form['subjecttype']
            my_data = Subject(name,sem,subjecttype,course)
            db.session.add(my_data)
            db.session.commit()
 
        flash("subject Inserted Successfully")
 
        return redirect(url_for('subject'))


#this is our update route where we are going to update our subject
@app.route('/subjectedit', methods = ['GET', 'POST'])
def subjectedit():
 
    if request.method == 'POST':
        my_data = Subject.query.get(request.form.get('id'))
 
        my_data.name= request.form['name']
        my_data.course=request.form['course']
        my_data.sem= request.form['sem']
        my_data.subjecttype= request.form['subjecttype']
 
        db.session.commit()

        flash("subject Updated Successfully")
 
        return redirect(url_for('subject'))
 

#This route is for deleting our subject
@app.route('/deletesubject/<id>/', methods = ['GET', 'POST'])
def deletesubject(id):
    my_data = Subject.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("subject Deleted Successfully")
 
    return redirect(url_for('subject'))



 
#Creating labadd table for our jntuk database
class Labs(db.Model):
    __tablename__ = "labs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique=True)
    branch = db.Column(db.String(10))

    def __init__(self, name,branch):
        self.name = name
        self.branch=branch

db.create_all();


#query on all our lab data
@app.route('/labpage')
def labpage():
    all_data = Labs.query.all()

    for i in all_data:

        print(i)

    return render_template("labadd.html", labs = all_data,count=len(all_data))


#this route is for inserting teacher data to mysql database via html forms
@app.route('/labadd', methods = ['POST'])
def labadd():
 
    if request.method == 'POST':
 
        name = request.form['name']
        branch=request.form['branch']
        my_data = Labs(name,branch)
        db.session.add(my_data)
        db.session.commit()
 
        flash("Lab  Inserted Successfully")
 
        return redirect(url_for('labpage'))
 
 
#this is our update route where we are going to update our lab
@app.route('/updatelab', methods = ['GET', 'POST'])
def updatelab():
 
    if request.method == 'POST':
        my_data = Labs.query.get(request.form.get('id'))
 
        my_data.name = request.form['name']
        my_data.branch=request.form['branch']
 
        db.session.commit()
        flash("Lab Updated Successfully")
 
        return redirect(url_for('labpage'))
 
 
 
 
#This route is for deleting our lab
@app.route('/deletelab/<id>/', methods = ['GET', 'POST'])
def deletelab(id):
    my_data = Labs.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Lab Deleted Successfully")
 
    return redirect(url_for('labpage'))


if __name__ == "__main__":
    app.run(debug=True)