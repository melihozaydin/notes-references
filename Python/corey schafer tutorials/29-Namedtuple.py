from collections import namedtuple
# Lightweight object that works like a tuple but more readable

# RGB
# Regular tuple version
color = (55, 155, 255)
print('Tuple red ', color[0])  # Red

"""
This is not very readable or sharable
So you might think about using a dictionary to better explain the variables

The problem with that is you might need the color to be immutable

Namedtuple is the solution
"""
# Dictionary version
color = {'red': 55, 'green': 155, 'blue': 255}
print('Dict red ', color['red'])

# Namedtuple version
# import it first
# then we define a namedtuple
# namedtuple('Name of the namedtuple', ['values', 'for the', 'tuple'])
Color = namedtuple('Color', ['red', 'green', 'blue'])
color = Color(55, 155, 255)

# note that we can stil use it like a normal tuple
print('Namedtuple red:', color[0])

# We can also call it like so
print('Namedtuple red:', color.red)
