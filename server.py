from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")

@app.route('/color', methods = ['POST'])   
def color():
    red =  request.form['r']
    green = request.form['g']
    blue = request.form['b']
    print red, green, blue
    return render_template("form.html", r=red,g=green, b=blue)


app.run(debug=True)