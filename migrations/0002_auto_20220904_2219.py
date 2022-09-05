from mongoengine_migrate.actions import *

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
    '0001_auto_20220904_2217'
]

# Action chain
actions = [
    DropField('Transactions', 'amount'),
]