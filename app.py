from flask import Flask, render_template, session, redirect, request, url_for
from functools import wraps
import pymongo

from dotenv import load_dotenv

# >>> to get the envirment variable named 'SECRET_KEY' (configuré auparavant sur votre fichier .env)
import os

# Load config from a .env file:
load_dotenv()

app = Flask(__name__)

# >>> To manipulate the sessions with flask we need to configure the secret key
# Use the envirement variable with os:
app.secret_key = os.environ['SECRET_KEY']


# >>> DB configuration/connection
MONGODB_URI = os.environ['MONGODB_URI']
# client = pymongo.MongoClient(MONGODB_URI)
try:
    client = pymongo.MongoClient(MONGODB_URI)
    dataBase = client.SmoneyDB
except:
    print('Failed to connect to the data base')

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
    # A user who is already logged in cannot create an account or log in to another account unless he logs out.
    # il faut verifié si session est cré ou pas encore
    if session.get('logged_in') == None:
        return render_template('home.html')
    elif not session['logged_in']  :
        return render_template('home.html')
    else:
        return redirect(url_for('dashboard'))
   

# once we sign up and this new user is connected and his dashboard/profile will be displayed
@app.route('/profile/')
@login_required
def dashboard ():
    return render_template('dashboard.html')

# Display Info for a specific user by clicking on his name in the list users page
@app.route("/show-user-profile/<id>")
def show_profile(id):
    user = dataBase.users.find_one({"_id": id})
    return render_template("show-user.html", user=user)

# list-users displayed either for a user log in or for "list-users" button
@app.route('/list-users/', methods=['GET'])
@login_required
def list_users():
    users = dataBase.users.find({})
    return render_template('list-users.html', users=users)

@app.route('/send-money/', methods=['GET', 'POST'])
@login_required
# This method is trigged when a user click a "sen money" button 
def send_money():
    users = dataBase.users.find({})
    
    if request.method == 'POST':
        # get user from DB to whom we will send money
        user = dataBase.users.find_one({"email": request.form['email']})
        
        # updated the balance of the user receiving the money
        solde = user['solde'] + int(request.form['solde'])
        dataBase.users.update_one({"_id": user['_id']},{"$set":{"solde":solde}})
        
        # Ubdate the balance of the user who sent the money
        solde = session['user']['solde'] - int(request.form['solde'])
        dataBase.users.update_one({"_id": session['user']['_id']},{"$set":{"solde":solde}})

        # Ubdate the user session
        session['user'] = dataBase.users.find_one({"email": session['user']['email']})

        return redirect('/profile')

    return render_template('send-money.html', users=users) 

# app running with python app.py
# but in our case we run our application by setting the FLASK_APP in cmd, then we execute the command 'flask run'
# if __name__ == "__main__":
#     app.run(debug=True)