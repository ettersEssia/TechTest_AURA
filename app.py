from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
# >>> to get the envirment variable named 'SECRET_KEY' (configuré auparavant sur votre pc)
import os

app = Flask(__name__)
# >>> To manipulate the sessions with flask we need to configure the secret key
app.secret_key = os.environ.get('SECRET_KEY')

# >>> DB configuration
client = pymongo.MongoClient('localhost', 27017)
db = client.SmoneyDB

# >>> include routes of our user app 
from user import routes

# Create decorate to limit access to users not logged in
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

@app.route('/')
def home ():
    return render_template('home.html')

@app.route('/profile/')
@login_required
def dashboard ():
    # >>> need cnx with DB to get all registered user
    return render_template('dashboard.html')