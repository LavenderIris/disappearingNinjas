from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def all_ninjas():
   # redirects back to the '/' route
    return render_template("all_ninjas.html")

@app.route('/ninja/<color>')
def color_ninja(color):
    if color == "blue":
        return render_template("leo.html")
    elif color =="orange":
        return render_template("mickey.html")
    elif color == "red":
        return render_template("raphael.html")
    elif color == "purple":
        return render_template("donnie.html")
    else:
        return render_template("notapril.html")
    

app.run(debug=True)