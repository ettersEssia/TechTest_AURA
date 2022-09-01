from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

# In this file we will create ou collection for th DB
class User:

    #start a session when user signs up so that when he get to their profile we can output some of his info 
    def start_session(self, user):
        # We don't send the password to the frontend we must delete it
        del user['pwd']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200
    def signup(self):

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name" : request.form['name'],
            "email" : request.form['email'],
            "pwd": request.form['pwd']
        }

        #encrypt the pwd
        user['pwd'] = pbkdf2_sha256.encrypt(user['pwd'])

        #get sure to not have an existing email adress for another user
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email adress already in use"}), 400
        
        #add user to our users collection 
        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}),400

    def signout(self):
        session.clear()
        return redirect('/')