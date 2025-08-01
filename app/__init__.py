from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from random import randint

#Create the app
app = Flask(__name__)


# Home Page - loading a static page
@app.get("/")
def home ():
     return render_template('pages/home.jinja')

# About Page - loading a static page
@app.get("/about/")
def about():
     return render_template('pages/about.jinja')

# Random Number Page - passing a value into template
@app.get("/random/")
def random():
     randNum = str(randint(1,1000))
     return render_template('pages/random.jinja', number = randNum) #number = str(randint(1,1000)) would also work, the two lines are just to be ultra-clear.

# Number Page - getting a value from the route and passing it into template
@app.get("/number/<int:num>")
def analyseNumber(num):
     return render_template('pages/number.jinja', number = num)

# Form Page - static page with a form
@app.get("/form/")
def form():
     return render_template('pages/form.jinja')

# Form Response Page - handle data posted from the form
@app.post("/processForm")
def processForm():
     print(f"Form Data: ${request.form}")
     return render_template(
          "pages/formData.jinja", 
          name = request.form["name"],
          age = request.form["age"]
     )

# Handle any missing page requests
@app.errorhandler(404)
def notFound(e):
     return render_template('pages/404.jinja')