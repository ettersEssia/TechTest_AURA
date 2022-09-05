from mongoengine_migrate.actions import *

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
    '0005_auto_20220904_2231'
]

# Action chain
actions = [
    RenameField('Users', 'pwd', new_name='password_hash'),
    AlterField('Users', 'password_hash', db_field='password_hash'),
]