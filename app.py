# Flask is a class inside the flask 
# render.com is used to deploy the website online
from flask import Flask, render_template,jsonify
# creating an app object of the class Flask 
app = Flask(__name__)

jobs = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Bengaluru, India',
        'salary':'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location': 'Delhi, India',
        'salary':'Rs. 15,00,000'
    },
    
        {
        'id':3,
        'title':'Frontend Engineer',
        'location': 'Remote',
        #'salary':'Rs. 12,00,000'
    },
        
        {
        'id':4,
        'title':'Data Analyst',
        'location': 'San Francisco, USA',
        'salary':'120,000 $'
    }

]


# @-is a decorator
@app.route("/")
def hello():
    #return "namaste sai anna"
    return render_template('home.html',
                           jobs=jobs,
                           company_name='Microsoft'
                           )
# registering data from json file so we are registering a new route
# we use api/ something to return a page which is not html. 
@app.route("/api/jobs")
def list_jobs():
    #takes an object and converts it into json object
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    
    