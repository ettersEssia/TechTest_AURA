from mongoengine_migrate.actions import *

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
    '0007_auto_20220905_0008'
]

# Action chain
actions = [
    CreateField('Transactions', 'user_send', choices=None, db_field='user_send',
        default=None, max_length=15, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    CreateField('Transactions', 'user_receive', choices=None, db_field='user_receive',
        default=None, max_length=15, min_length=None, null=False, primary_key=False, regex=None,
        required=False, sparse=False, type_key='StringField', unique=False, unique_with=None),
    DropField('Transactions', 'user_receive_id'),
    DropField('Transactions', 'user_send_id'),
]