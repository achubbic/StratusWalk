from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # __name __ references this file
#tells app where datadabe is located				       #three slashes: relative path
app.config['SQLALCHEMY_DATABADE_URI'] = 'sqlite"///test.db'#four slashes: absolute path

db = SQLAlchemy(app) #initialize database with settings from our app

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self): #each new element returns task
		return '<Task %r>' %self.id

@app.route('/') #pass in url string of our route
def index():#this function applies specifically to the above route
	return render_template('index.html') #specify which page to read from
										 #note: folder !matter
if __name__ == "__main__":
	app.run(debug=True)
