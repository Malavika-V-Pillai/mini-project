from flask import Flask, render_template, request,session
import sqlite3
app = Flask(__name__)
app.secret_key = 'any random string'

''' welcome link'''
@app.route('/home',defaults={'bookname': ""})

@app.route('/home/<bookname>')
def home(bookname):
	if bookname == "":
		return render_template('home.html')
	else:

		conn = sqlite3.connect('book.db')
		cur = conn.cursor()
		cur.execute("SELECT  * from book where id =?",(bookname))
		ReqBook = cur.fetchall()
		conn.close()
		return render_template("home.html",ReqBook = ReqBook)
''' main page link'''

@app.route("/login")
def signlog():
	return render_template("signlog.html")
@app.route("/addbook", methods =['POST','GET'])
def addbook():
	
	if 'em' in session:
		em = session['em']
		pswd = session['pswd']
		return render_template("profile.html",msg = msg)
		'''profile.html has the information of all our books we need to sell'''
	else:
		try:
			conn = sqlite3.connect('book.db')
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
				session['em'] = em
				pd = request.form['pswd']
				session['pswd'] = pswd
				login_query = cur.execute("SELECT * FROM user WHERE email = ? AND pswd = ?",(em,pd) )
				if not login_query:
					msg = "Invalid User"
					conn.commit()
					return render_template("signlog.html",msg = msg)

				else:
					msg = "login succesful"
					return render_template("profile.html",msg = msg)
			
			return "wrong"		
		except:
			conn.rollback();

		finally:
			
			conn.close()				
@app.route("/book", methods =['POST','GET'])
def book():
	if request.method == "GET":
		try:
			conn = sqlite3.connect('book.db')
			cur = conn.cursor()
			if 'education' in form.request:
				book_name = request.form['book_name']				
				author = request.form['author']
				price = request.form['price']
				description = request.form['description']
				booktype = request.form['booktype']
				cur.execute("INSERT INTO edubook VALUES(?,?,?,?)",(book_name,author,price,description,booktype))
				conn.commit();
				msg = "Book added"
				return render_template('profile.html', msg = msg)

			elif 'fiction' in form.request:
				book_name = request.form['book_name']				
				author = request.form['author']
				price = request.form['price']
				description = request.form['description']
				booktype = request.form['booktype']
				'''fictype for fiction type'''
				cur.execute("INSERT INTO ficbook VALUES(?,?,?,?)",(book_name,author,price,description,booktype))
				conn.commit();
				msg = "Book added"
				return render_template('profile.html', msg = msg)


			else:
				book_name = request.form['book_name']				
				author = request.form['author']
				price = request.form['price']
				description = request.form['description']
				booktype = request.form['booktype']
				'''nfictype for non-fiction type'''
				cur.execute("INSERT INTO nficbook VALUES(?,?,?,?)",(book_name,author,price,description,booktype))
				conn.commit();
				msg = "Book added"
				return render_template('profile.html', msg = msg)
		except:
			conn.rollback()
		finally:
			conn.close()
''' For searching a book in textbox of homepage'''
@app.route('/search', methods = ['POST','GET'])
def search():
	if request.method == "POST":
		searchBook = request.form['searchBook']
		conn = sqlite3.connect('book.db')
		cur = conn.cursor()
		cur.execute("SELECT * FROM edubook WHERE edubook.bookname = ? ",(searchBook,))
		edures= cur.fetchall()
		cur.execute("SELECT * FROM ficbook WHERE ficbook.bookname = ? ",(searchBook,))
		ficres=cur.fetchall()
		cur.execute("SELECT * FROM nficbook WHERE nficbook.bookname = ? ",(searchBook,))
		nficres = cur.fetchall()
		
		if len(edures) == 0 :
			msg = "No results found :("
			return render_template("home.html",msg=msg)
		else:
			listlength = str(len(ficRes)+len(edures)+len(nficres))
			msg = listlength + " books found" 
			return render_template('home.html', msg = msg,edures = edures)

@app.route('/logout')
def logout():
	session.pop('em',none)
	return render_template('home.html')
	
if __name__ == "__main__":
  	app.run(debug = True)
