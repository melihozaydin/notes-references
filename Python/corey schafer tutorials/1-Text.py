message = 'Hello World'

message2 = "Message 2"

message3 = "messag'e's'"

message4 = 'message \' 11 '

mesaage5 = """

multine 1
multiline 11

"""

print('Hello world')

print(message, end='')  # print normally ends with a new line unless told otherwise as such

print(message)

print(message2)

print(message3)

print(message4)

print(mesaage5)

# ındexing works like this
# İncludes first indice but leaves out last one
# from firt number until last one
print(message[0:5])

# Leaving index empty is called slicing

print(message[:7])

print(message[3:])

# these print an empty line
print('\n')
print()

# Text methods
# All datatypes have methods
# Method is a function that belongs to an object

print(len(message))  # this returns amount of characters in str

print(message.lower())

print(message.upper())

# This count a strin within a string and return the amount
print(message.count('Hello'))

# The index where a certain string can be found

# This returns a 6 because world can be found starting at the 6th index

print(message.find('World'))
print(message[6:])

# This method replaces a string with a new one
new_message = message.replace('World', 'Universe')
print(new_message)

print()
print()

# Concatanation
# Joining strings

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name

print(message)

# You should use a format method for this

message = '{}, {} Welcome!'.format(greeting, name)
print(message)

print()

# this is called a f-string

message = f'{greeting}, {name} Welcome!'
print(message)

# This shows every available method and attribute with the given variable
print(dir(name.lower()))

print()
print()

# this is a basic help function, str is the string datatype
print(help(str.lower))
