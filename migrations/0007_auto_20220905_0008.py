from mongoengine_migrate.actions import *

# Existing data processing policy
# Possible values are: strict, relaxed
policy = "strict"

# Names of migrations which the current one is dependent by
dependencies = [
    '0006_auto_20220905_0007'
]

# Action chain
actions = [
    DropField('Users', 'auto_id_0'),
]