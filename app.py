# Install the various required library
from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo	

app = Flask(__name__)
	
# Setting up the MONGODB DATABASES to be link up	
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'insurance'
COLLECTION_NAME = 'policyholder'

# set up the connection to MONGO_URI which we set up in bashrc
conn = pymongo.MongoClient(MONGO_URI)
# set 'data' to be the name to represent the database link
data = conn[DATABASE_NAME][COLLECTION_NAME]


@app.route('/') # map the root route to the index function
def index():
    result = data.find({})
    return render_template ("index.html" , data = result)
    
@app.route('/viewlist')
def viewlist():
    policyowner = data.find({})
    return render_template ("viewlist.html", data = policyowner)
    
@app.route('/viewgraph')
def viewgraph():
    return render_template ("viewgraph.html")
    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)