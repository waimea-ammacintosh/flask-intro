from flask import Flask
from flask import render_template
from random import randint

#Create the app
app = Flask(__name__)



@app.get("/")
def home ():
     return render_template('pages/home.jinja')

@app.get("/random/")
def random():
     randNum = str(randint(1,1000))
     return render_template('pages/random.jinja', number = randNum) #number = str(randint(1,1000)) would also work, the two lines are just to be ultra-clear.

@app.get("/about/")
def about():
     return render_template('pages/about.jinja')