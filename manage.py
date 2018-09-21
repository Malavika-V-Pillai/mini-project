from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

''' welcome link'''
@app.route('/login')
def home():
	
	return render_template("home.html")
''' main page link'''
@app.route("/addbook")
def addbook():
	if em in session:
		em = session['em']
		pswd = session['pswd']
		return render_template("profile.html",msg = msg)
		'''profile.html has the information of all our books we need to sell'''
	else:
		try:
			conn = sqlite3.connection('book.db')
			cur = conn.cursor()
			if 'signup' in request.form.keys():
				name = request.form['name']  
				''' html form should contain the same name as "name,email,pswd,phno '''
				email = request.form['email']
				pswd = request.form['pswd']
				phno = request.form['phno']
				location = request.form['location']
				cur.execute("INSERT INTO user VALUES(?,?,?,?,?)",(name,email,pswd,phno,location))
				conn.commit();
				msg = "sign up successfull"
				return render_template("profile.html", msg = msg, name = name)
				'''msg to be flashed in the html document'''
				
			if 'login' in request.form.keys():
				em = request.form['email']
				session.em = em
				pd = request.form['pswd']
				session.pswd = pswd
				login_query = cur.execute("SELECT * FROM user WHERE EMAIL = ? AND PSWD = ?",(em,pd) )
				if not login_query:
					msg = "Invalid User"
					conn.commit()
					return render_template("login.html",msg = msg)

				else:
					msg = "login succesful"
					return render_template("profile.html",msg = msg)
			
			 		
		except:
			conn.rollback();

		finally:
			
			conn.close()				
@app.route("/book")
def book():
	if request.method == "GET":
		try:
			conn = sqlite3.connection('book.db')
			cur = conn.cursor()
			if 'education' in form.request:
				book_name = request.form['book_name']				
				author = request.form['author']
				price = request.form['price']
				description = request.form['description']
				edu_type = request.form['edutype']
				cur.execute("INSERT INTO edubook VALUES(?,?,?,?)",(book_name,author,price,description,edu_type))
				conn.commit();
				msg = "Book added"
				return render_template('profile.html', msg = msg)

			elif 'fiction' in form.request:
				book_name = request.form['book_name']				
				author = request.form['author']
				price = request.form['price']
				description = request.form['description']
				edu_type = request.form['fictype']
				'''fictype for fiction type'''
				cur.execute("INSERT INTO ficbook VALUES(?,?,?,?)",(book_name,author,price,description,fic_type))
				conn.commit();
				msg = "Book added"
				return render_template('profile.html', msg = msg)


			else
				book_name = request.form['book_name']				
				author = request.form['author']
				price = request.form['price']
				description = request.form['description']
				edu_type = request.form['nfictype']
				'''nfictype for non-fiction type'''
				cur.execute("INSERT INTO ficbook VALUES(?,?,?,?)",(book_name,author,price,description,nfic_type))
				conn.commit();
				msg = "Book added"
				return render_template('profile.html', msg = msg)
		except:
			conn.rollback()
		finally:
			conn.close()

@app.route('/logout')
def logout():
	session.pop('em',none)
	return render_template('home.html')
	
if __name__ == "__main__":
  	app.run(host="192.168.43.7",debug = True)