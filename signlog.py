from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

''' welcome link'''
@app.route('/')
def signlog():
	return render_template("signlog.html")
''' main page link'''
@app.route("/home")
def home():
	if request.method == 'POST':
		try:
			conn = sqlite3.connection('book.db')
			cur = conn.cursor()
			if 'signup' in request.form.keys():
				name = request.form['name']
				email = request.form['email']
				pswd = request.form['pswd']
				phno = request.form['phno']
				cur.execute("INSERT INTO book VALUES(?,?,?,?)",(name,email,pswd,phno))
				conn.commit();
				msg = "sign up successfull"
				return render_template("home.html", msg = msg)
				'''home.html has the list of categories of books '''
			if 'login' in request.form.keys():
				em = request.form['email']
				pd = request.form['pswd']
				login_query = cur.execute("SELECT * FROM book WHERE EMAIL = ? AND PSWD = ?",(em,pd) )
				if not login_query:
					msg = "Invalid User"
					conn.commit()
					return render_template("signlog.html",msg = msg)

				else:
					msg = "login succesful"
					conn.commit()
					return render_template("home.html")
			
			 		
		except:
			conn.rollback();

		finally:
			conn.close()				
@app.route("/book")
def book():
	if request.method == "GET":
		book_name = request.form[]				
	
if __name__ == "__main__":
  	app.run(host="192.168.43.7",debug = True)