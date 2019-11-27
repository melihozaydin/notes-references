"""
# Comparison

# single equal is assignment
# double equal return true or false according to equality state

==  # Equal
<   # less
>   # more
<=  # less or equal
>=  # more or equal
!=  # not equal
is  # object identity

"""

# This will print
if True:
    print('Condition is true')

# this will not
if False:
    print('Condition was False')

print()
print()

# control example
language = 'Python'

if language == 'Python':
    print('It\'s Python!! \n')

elif language == 'C++':
    print('It\'s C++ !!')

else:
    print('It\'s neither')

print()
print()

# And, Or, Not (Boolean Ops)

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Access Granted  ')
else:
    print('Credential error')

print()

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Access Granted  ')
else:
    print('Credential error')

print()

if not logged_in:
    print('Please log in')
else:
    print('Welcome')

print()
print()

# Object id (is) vs equal '=='
list_a = [1, 2, 3]
list_b = [1, 2, 3]

print(list_a == list_b)  # this compares contents of variables (returns True)
print(list_a is list_b)  # This checks mem id's of variables (returns False)
print('A-->', id(list_a), 'is not B -->', id(list_b))

print()
print()

"""
# False Values:
    # False
    # None
    # Zero of any numeric value datatype
    # Any empty sequence (list, tuple, string, set...)
    # Any empty mapping. For ex., empty dict. {}

# all else will regiter as true
# such as a filled string or a numeric data not equal to zero
"""
