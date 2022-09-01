import imp
from flask import Flask, request, render_template, redirect
#from the file app
from app import app
from .models import User

#routes for my user app
@app.route('/registration/', methods=['POST', 'GET'])
def signup():
    return User().signup()

@app.route('/signout/')
def signout():
    return User().signout()

@app.route('/login/', methods=['POST'])
def login():
    return User().login()    
