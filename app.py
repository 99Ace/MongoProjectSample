# Install the various required library
from flask import Flask, render_template, request, redirect, url_for
import os
import pymongo	

app = Flask(__name__)
	
# Setting up the MONGODB DATABASES to be link up	
MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = 'cars_listing'
COLLECTION_NAME = 'car_plate'

# set up the connection to MONGO_URI which we set up in bashrc
conn = pymongo.MongoClient(MONGO_URI)
# set 'data' to be the name to represent the database link
data = conn[DATABASE_NAME][COLLECTION_NAME]


@app.route('/') # map the root route to the index function
def index():
    return "hello world" # Testing to make sure the route is working, run 'python3 app.py' on terminal 
                         # to test for 'hello world' to be displayed 
    

    
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)