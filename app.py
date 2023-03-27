# Flask is a class inside the flask 
from flask import Flask, render_template
# creating an app object of the class Flask 
app = Flask(__name__)
# @-is a decorator
@app.route("/")
def hello():
    #return "namaste sai anna"
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
    