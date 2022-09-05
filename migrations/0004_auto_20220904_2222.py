from mongoengine_migrate.actions import *
import pymongo

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
    '0003_auto_20220904_2221'
]

# Action chain
actions = [
    DropField('Users', 'username'),
    DropIndex('Users', 'username_1', fields=[('username', pymongo.ASCENDING)], sparse=False,
        unique=True),
]