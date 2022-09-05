# In this file we define the app views

from flask import Flask, render_template, redirect, url_for, flash, request
from mongoengine import connect

from app.forms import LoginForm, RegisterForm
from app.models import Users, Transactions
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# >>> to get the envirment variable named 'SECRET_KEY' (configuré auparavant sur votre fichier .env)
import os

# Create a flask instance
app = Flask(__name__)

# Load config from a .env file:
load_dotenv()

# >>> To manipulate the sessions with flask we need to configure the secret key
# and to get safe it's used with the csrf_token in forms
# Use the envirement variable with os:
app.secret_key = os.environ['SECRET_KEY']

# Set the Debug mode
app.config['DEBUG'] = os.environ['DEBUG_VALUE']

#Data base config/Cnx
print(os.environ['MONGODB_URI'])
MONGODB_URI = os.environ['MONGODB_URI']
client = connect(MONGODB_URI)

# Flask_login configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.objects(id=user_id).first()

# routes of our app

#start a session when user log in so that when he get to their profile we can output some of his info 
@app.route('/')
@app.route('/login/', methods=['GET', 'POST'])
def login():
    user = None
    form = LoginForm()
    if (form.validate_on_submit()):
        user = Users.objects(email=form.email.data).first()
        if user : 
            if (user.verify_password(form.password_hash.data)):
                # start_session(user)
                # it's a flask_login function that create session and login...
                login_user(user)
                flash('Log in success')
                return redirect('/list-users')
            else:
                flash('wrong password... Try Again')
        else:
            flash("User doesn't exist Try again...")
        
    return render_template('login.html', form=form)

# logout and clean the session
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('you just disconnected')
    return redirect('/login')

# User register will automaticly connect and redirect to his dashboard
@app.route('/registration/', methods=['GET', 'POST'])
def register():
    user = None
    form = RegisterForm()
    if (form.validate_on_submit()):
        user = Users.objects(email=form.email.data).first()
        if user :
            flash('User exist already... Try with an other email')
        else:
            hashed_pwd = generate_password_hash(form.password_hash.data, "sha256")
            user = Users(username=form.username.data, email=form.email.data, name=form.name.data, password_hash=hashed_pwd)
            # user.password = form.password_hash.data
            user.save()
            login_user(user)
            flash('User Sign Up Success')
            return redirect(url_for('dashboard'))

    return render_template('register.html', form=form, user=user)

# Change a user's password
@app.route('/change-password/', methods=['POST'])
def changepwd():
    print(request.form['pwd'])
    current_user.password = request.form['pwd']
    current_user.save()
    flash('User pasword changed Success')
    # we disconnect user so that he connects with the new password
    return redirect('/logout/')

# once we sign up we will automaticly connected and our dashboard/profile will be displayed
@app.route('/profile/')
@login_required
def dashboard():
    return render_template('dashboard.html')

# list-users displayed either for a user log in or for "list-users" button
@app.route('/list-users/')
@login_required
def list_users():
    listUsers = Users.objects()
    return render_template('list-users.html', listUsers=listUsers)

# Display Info for a specific user by clicking on his name in the list users page
@app.route('/show-user-profile/<id>')
def show_profile(id):
    user = Users.objects(id=id).first()
    return render_template('show-user.html', user=user)

@app.route('/send-money/', methods=['GET', 'POST'])
@login_required
# This method is trigged when a user click a "sen money" button 
def send_money():
    if request.method == 'POST':

        # collect the amount of th transaction
        montant = int(request.form['solde'])

        # update the balance of the user receiving the money
        emailreceive = request.form['email']
        userReceive = Users.objects(email=emailreceive).first()
        userReceive.solde = userReceive.solde + montant
        userReceive.save()

        # update the balance of the money sender user
        current_user.solde = current_user.solde - montant
        current_user.save()

        # Save the transaction on the DB table
        transaction = Transactions(user_send=current_user.username, user_receive=userReceive.username, amount=montant)
        transaction.save()

        return redirect('/list-users')

    users = Users.objects()
    return render_template('send-money.html', users=users)

# Customize Error page

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('not-found-404.html'), 404

#Internal Server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('server-error-500.html'), 500