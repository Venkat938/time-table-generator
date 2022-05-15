from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


import mysql.connector as myconn
mydb = myconn.connect(
  host="localhost",
  user="root",
  password="",
  database="jntuk"
)

#print(mydb)
obj= mydb.cursor();
#print(obj) 
obj.execute("CREATE TABLE IF NOT EXISTS teacheradd(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), branch VARCHAR(10))")

 
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"
 
#SqlAlchemy Database Configuration With Mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/jntuk'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
#db = SQLAlchemy(app)
 
 
#Creating Teacheradd table for our jntuk database
"""class Teacheradd(db.Model):
    __tablename__ = "Teacheradd"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    branch = db.Column(db.String(10))
 
    def __init__(self, name,branch):
        name = name


#Creating Classadd table for our jntuk database
class Classadd(db.Model):
    __tablename__ = "Classadd"
    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(100))
 
    def __init__(self, classname):
 
        self.name = classname

db.create_all()"""




#This is the dashboard route where we are going to
@app.route('/')
def dashboard():
    return render_template("dashboard.html")


#query on all our teacher data
@app.route('/teacheradd')
def teacheradd():
    all_data = Teacheradd.query.all()
 
    return render_template("teacheradd.html", employees = all_data)


#query on all our class data
@app.route('/classadd')
def classadd():
    all_data = Classadd.query.all()
 
    return render_template("classadd.html", classes = all_data)

#This is the class configuration route where we are going to
@app.route('/classconfig')
def classconfig():
    return render_template("classconfig.html")
 
 
 
#this route is for inserting teacher data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        name = request.form['name']
 
        my_data = Teacheradd(name)
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


 
#all routes of dropdown CLassadd

@app.route('/insertclass', methods = ['POST'])
def insertclass():
 
    if request.method == 'POST':
 
        classname = request.form['class']
 
        my_data = Classadd(classname)
        db.session.add(my_data)
        db.session.commit()
 
        flash("class Inserted Successfully")
 
        return redirect(url_for('classadd'))
 
 
#this is our update route where we are going to update our Faculty
@app.route('/updateclass', methods = ['GET', 'POST'])
def updateclass():
 
    if request.method == 'POST':
        my_data = Classadd.query.get(request.form.get('id'))
 
        my_data.classname = request.form['name']
 
        db.session.commit()
        flash("class Updated Successfully")
 
        return redirect(url_for('classadd'))
 
 
 
 
#This route is for deleting our employee
@app.route('/deleteclass/<id>/', methods = ['GET', 'POST'])
def deleteclass(id):
    my_data = Classadd.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("class Deleted Successfully")
 
    return redirect(url_for('classadd'))



 
if __name__ == "__main__":
    app.run(debug=True)