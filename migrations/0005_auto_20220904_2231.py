from mongoengine_migrate.actions import *
import pymongo

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
    '0004_auto_20220904_2222'
]

# Action chain
actions = [
    CreateField('Users', 'username', choices=None, db_field='username', default=None,
        max_length=15, min_length=None, null=False, primary_key=False, regex=None,
        required=True, sparse=False, type_key='StringField', unique=True, unique_with=None),
    CreateIndex('Users', 'username_1', fields=[('username', pymongo.ASCENDING)],
        sparse=False, unique=True),
]