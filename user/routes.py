from flask import Flask, request, render_template, redirect
#from the file app
from app import app
from .models import User

# In this file we have private routes for user app

# Add a new user
@app.route('/registration/', methods=['POST'])
def signup():
    return User().signup()

# Disconect a user
@app.route('/signout/')
def signout():
    return User().signout()

# Connect a user
@app.route('/login/', methods=['POST'])
def login():
    return User().login()  

# Change a user's password
@app.route('/change-password/', methods=['POST'])
def changepwd():
    return User().changepwd()
   
