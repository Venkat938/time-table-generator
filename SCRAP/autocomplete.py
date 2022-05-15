from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="jntuk"
)


@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "GET":

		mycursor = mydb.cursor()

		mycursor.execute("SELECT name from teacheradd")

		myresult = mycursor.fetchall()

		res=[list(i) for i in myresult]

		res2=[]
		for i in range(len(res)):
			res2.append(res[i][0])
		
		return render_template("autocomplete.html", lis=res2)


if __name__ == '__main__':
	app.run(debug=True)



