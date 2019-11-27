# Decorators
# Dynamically alter functionality of functions

"""
DO THIS AFTER OOP
"""


def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function()

outer_function()
