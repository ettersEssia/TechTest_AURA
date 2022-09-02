from flask import Flask, render_template, session, redirect, request
from functools import wraps
import pymongo

from dotenv import load_dotenv

# >>> to get the envirment variable named 'SECRET_KEY' (configuré auparavant sur votre fichier .env)
import os

# Load config from a .env file:
load_dotenv()

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=(os.environ['DEBUG'] == 'True'))

# >>> To manipulate the sessions with flask we need to configure the secret key
# Use the envirement variable with os:
app.secret_key = os.environ['SECRET_KEY']


# >>> DB configuration/connection
MONGODB_URI = os.environ['MONGODB_URI']
client = pymongo.MongoClient(MONGODB_URI)
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

# Since home page we can sign up or log in 
@app.route('/')
def home ():
    return render_template('home.html')

# once we sign up and this new user is connected and his dashboard/profile will be displayed
@app.route('/profile/')
@login_required
def dashboard ():
    return render_template('dashboard.html')

# Display Info for a specific user by clicking on his name in the list users page
@app.route("/show-user-profile/<id>")
def show_profile(id):
    user = db.users.find_one({"_id": id})
    return render_template("show-user.html", user=user)

# list-users displayed either for a user log in or for "list-users" button
@app.route('/list-users/', methods=['GET'])
@login_required
def list_users():
    users = db.users.find({})
    return render_template('list-users.html', users=users)

@app.route('/send-money/', methods=['GET', 'POST'])
@login_required
# this method is trigged when a user click a "sen money" button 
def send_money():
    users = db.users.find({})
    message = ""
    if request.method == 'GET':
        return render_template('send-money.html', users=users)
    elif request.method == 'POST':
        # get user from DB to whom we will send money
        user = db.users.find_one({"email": request.form['email']})
        
        # Ubdate his balance
        solde = user['solde'] + int(request.form['solde'])
        db.users.update_one({"_id": user['_id']},{"$set":{"solde":solde}})
        
        # Ubdate the balance of the user who sent the money
        solde = session['user']['solde'] - int(request.form['solde'])
        db.users.update_one({"_id": session['user']['_id']},{"$set":{"solde":solde}})

    return render_template('send-money.html', users=users) 

