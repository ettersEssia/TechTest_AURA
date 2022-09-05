from mongoengine_migrate.actions import *
import pymongo

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
]

# Action chain
actions = [
    CreateDocument('Users', collection='users'),
    CreateDocument('Transactions', collection='transactions'),
    CreateField('Users', 'email', choices=None, db_field='email', default=None,
        max_length=None, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=True, unique_with=None),
    CreateField('Users', 'name', choices=None, db_field='name', default=None, max_length=50,
        min_length=None, null=False, primary_key=False, regex=None, required=False,
        sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('Users', 'auto_id_0', choices=None, db_field='_auto_id_0', default=None,
        null=False, primary_key=False, required=False, sparse=False, type_key='ObjectIdField',
        unique=False, unique_with=None),
    CreateField('Users', 'pwd', choices=None, db_field='pwd', default=None, max_length=None,
        min_length=None, null=False, primary_key=False, regex=None, required=False,
        sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('Users', 'solde', choices=None, db_field='solde', default=100,
        max_value=None, min_value=0, null=False, primary_key=False, required=False,
        sparse=False, type_key='IntField', unique=False, unique_with=None),
    CreateField('Users', 'username', choices=None, db_field='username', default=None,
        max_length=15, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=True, unique_with=None),
    CreateField('Transactions', 'amount', choices=None, db_field='amount', default=None,
        max_value=None, min_value=0, null=False, primary_key=False, required=False,
        sparse=False, type_key='IntField', unique=False, unique_with=None),
    CreateField('Transactions', 'user_send_id', choices=None, db_field='user_send_id',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=False, sparse=False, type_key='StringField', unique=False,
        unique_with=None),
    CreateField('Transactions', 'date_transaction', choices=None,
        db_field='date_transaction', default=None, null=False, primary_key=False,
        required=False, sparse=False, type_key='DateTimeField', unique=False, unique_with=None),
    CreateField('Transactions', 'user_receive_id', choices=None, db_field='user_receive_id',
        default=None, max_length=None, min_length=None, null=False, primary_key=False,
        regex=None, required=False, sparse=False, type_key='StringField', unique=False,
        unique_with=None),
    CreateIndex('Users', 'email_1', fields=[('email', pymongo.ASCENDING)], sparse=False,
        unique=True),
    CreateIndex('Users', 'username_1', fields=[('username', pymongo.ASCENDING)],
        sparse=False, unique=True),
]