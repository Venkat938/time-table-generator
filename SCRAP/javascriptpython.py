from appy import *
"""from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

 
app = Flask(__name__)
app.secret_key = "Secret Key javascript"
 
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/jntuk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
#mysql.connector connection code

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="jntuk"
)
"""
all_course=Classadd.query.all()
print(all_course)
"""if __name__ == "__main__":
    app.run(debug=True)"""