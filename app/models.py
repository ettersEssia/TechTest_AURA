from datetime import datetime
from mongoengine import Document, StringField, IntField, ReferenceField, DateTimeField
# For Hashing Passwords 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import uuid

# define my database tables

# user table
# transaction tale
class Transactions(Document):
    user_send = StringField(max_length=15)
    user_receive = StringField(max_length=15)
    amount = IntField(min_value=0)
    date_transaction = DateTimeField(default=datetime.utcnow)

    def __repr__(self):
        return f'<user_send_id="{self.user_send_id}">'

class Users(Document, UserMixin):
    username = StringField(max_length=15, unique=True, required=True)
    email = StringField(unique=True, required=True)
    name = StringField(max_length=50)
    password_hash = StringField()
    solde = IntField(default=100, min_value=0)
# prevent access to the password
    @property
    def password(self):
        raise AttributeError("password is not readbale attribute")
# Set the password user to hash to the entered password
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
# Get the password user to verify whith the entered password
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Users name="{self.name}">'

