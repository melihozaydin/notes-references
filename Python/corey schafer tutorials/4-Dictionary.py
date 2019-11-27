# Key value pairs. Which are like a real dictionary whre the
# word itself is key and its definition is the value

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci'],
           3.14: 'pi'}

print(student['age'])
print(student['name'])
print(student['courses'])  # Keys can be any datatype
print(student[3.14])  # Like here it is a float

"""
if we try to call a non existent key we get an error

print(student['phone'])

to avoid this we can define a default return value
by callingg the key with the get() method
"""

# get() method

print(student.get('phone', 'not found'))

print()
print()

# add an entry to dict

student['phone'] = '555-555-5555'

# If the key already exists it will update

student['name'] = 'Tayfun'

# Alternatively you can use update() method to update or add entries to dict

student.update({'name': 'Kamil', 'age': 21, 'gender': 'Male'})

print(student)

print()

# Removing entries

del student['age']

print(student)
student.update({'name': 'Kamil', 'age': 21, 'gender': 'Male'})

# this can be used to save the removed value elsewhere
age = student.pop('age')

print()
print('Removed value ', age, ' \n__ Dict --->> ', student)

student.update({'name': 'Kamil', 'age': 21, 'gender': 'Male'})

print()
print()

# Dict length
print('Entry count >>', len(student))

# List keys
print(student.keys)
print()

# List Values
print(student.values())
print()

# List every entry
print(student.items())
print()

# loop through items

# This only gets keys
for key in student:
    print(key)

print()

# This will get'em all

for key, value in student.items():
    print(key, value)
