from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def signlog():
	
	return render_template("signlog.html")
@app.route("/home")
def home():
	return render_template("home.html")	

if __name__ == "__main__":
  	app.run(host="192.168.56.1",debug = True)