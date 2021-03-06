"""In here define the constants of DanceCat's core."""

# Object's Code
# These codes will be used to identified Models and other object
# through through the system.
OBJECT_CODES = {
    'User': 0,
    'Project': 1,
    'Role': 2,
    'Source': 3
}

# Models' Version
MODEL_VERSION = {
    OBJECT_CODES['User']: 1,
    OBJECT_CODES['Project']: 1,
    OBJECT_CODES['Role']: 1,
    OBJECT_CODES['Source']: 1,
}

# Attribute's Python object type
ATTRIBUTE_TYPES = {
    'TypeToString': {
        str: 'String',
        int: 'Integer',
    },
    'StringToType': {
        'String': str,
        'Integer': int,
    }
}

# Source types
SOURCE_TYPE_CODES = {
    'Base': 0
}

# Source attributes
SOURCE_ATTRIBUTES = {
    SOURCE_TYPE_CODES['Base']: {}
}
