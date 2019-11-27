# Aspects of being pythonic
# Duck typing and Easier to ask forgiveness then permission (EAFP)

# ----Duck typing----
# assume if an object moves and acts like a duck it is a duck
# we dont care what type of object we are dealing with
# we only care if it can do what we need it to do
import os


class Duck:
    def quack(self):
        print('Quack, Quack!')

    def fly(self):
        print('Flap, flap!')


class Person:

    def quack(self):
        print('I\'m quacking like a duck!')

    def fly(self):
        print('I\'m flopping my arms!')

"""
The reason this is non-pythonic is because
even though Person class has the functions 'quack' and 'fly' it is treated differently than the Duck class

'if it walks like a duck and quacks like a duck treat it like a duck'
"""


def quack_and_fly_np(thing):
    # Not duck typing(Non-Pythonic)
    if isinstance(thing, Duck):  # is thing an instance of duck?
        thing.quack()
        thing.fly()
    else:
        print('This has to be a DUCK!!!')

    print()

print('---Non-Duck typing---')
d = Duck()
quack_and_fly_np(d)

p = Person()
quack_and_fly_np(p)

"""
-Below is the duck typing (pythonic) way of writing this method
- This is more readable

-If the input object doesn't have the requested methods(functions)
it would throw an error

-To prevent this we could put some checks in place
    This is where the EAFP comes in

"""


def quack_and_fly(thing):
    # Duck typing(Pythonic)
    thing.quack()
    thing.fly()

    print()

print('---Duck typing---')

quack_and_fly(d)
quack_and_fly(p)

"""
Look Before you leap(LBYL/ Asking for permission)

- Non-pythonic
-less readable
"""


def quack_and_fly_LBYL(thing):
    if hasattr(thing, 'quack'):  # does it have the attribute?
        if callable(thing.quack):  # can i call it?
            thing.quack()  # call it

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
    print()
print('---Look before you leap---')

quack_and_fly_LBYL(d)
quack_and_fly_LBYL(p)

"""
EAFP way
if it works great
if not handle the error
"""


def quack_and_fly_EAFP(thing):
    # EAFP (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()  # Which doesn' exist
    except AttributeError as e:
        print('Attribute doesn\'t exist')
        print(e)
    print()
print('---EAFP---')
quack_and_fly_EAFP(d)
quack_and_fly_EAFP(p)


print('---Example for EAFP---')

person = {'name': 'Jess', 'age': 23, 'job': 'Programmer'}
person = {'name': 'Jess', 'age': 23}

# LBYL(Non-Pyhtonic)
if 'name' in person and 'age' in person and 'job' in person:
    print(f"I\'m {person['name']}. I\'m {person['age']} years old. I am a {person['job']}")
else:
    print('That index doesn\'t exist')

# EAFP (Pythonic)
try:
    print(f"I\'m {person['name']}. I\'m {person['age']} years old. I am a {person['job']}")

except KeyError as e:
    print(f'Missing {e} key')


print('\n---List Example for EAFP---')

my_list = [1, 2, 3, 4, 5]

# Non pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print('Index does not exist')

# EAFP (Pythonic)
try:
    print(my_list[5])
except IndexError:
    print('That index does not exist')

"""
EAFP is way more readable
- whenever you ask permission you access the object multiple times
- you only access the object once
- you can avoid race conditions as demonstrated in the below example
"""

print('\n---Race condition---')


my_file = '/test.txt'  # False
# my_file = 'test.txt'  # True

"""
# The problem with this is os.access check
# between the time we make the check for access and read it
# the file migth become inaccessible

# EAFP way is better because we directly try to access it
"""

# Race condition (Asking for permission)
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print('File can\'t be accessed')

# No race condition (EAFP)
try:
    f = open(my_file)
except IOError as e:
    print('File can\'t be accessed')
else:
    with f:
        print(f.read())
