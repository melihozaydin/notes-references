'''
LEGB
Local, Enclosing, Global, Built-in

Local: variables defined within a function

Enclosing: variables in the local scope of enclosinf functions

Global: variables defined in the top level of a module or as global

Built-in: names that are predefined in python

'''

import builtins

x = 'global x'


def test():
    x = 'local x'
    y = 'local y'
    print(y)
    print(x)  # this prints 'local x'

test()

print(x)  # this will print 'global x'
# This will raise an error
# print(y)

print()
'''
it first checked local scope then enclosing then global then built-in
'''


def test2():
    global x
    x = 'global x2'
    y = 'local y2'
    print(y)
    print(x)  # this prints 'global x2'

test2()

print()
print()

# Arguments are also local variables


def test3(z):
    x = 'local x'
    y = 'local y'
    print(y)
    print(x)  # this prints 'local x'
    print(z)  # thi prints 'z argument'

test3('z argument')

print()
print()

m = min([5, 1, 4, 3, 2])
print(m)

print()

# print(dir(builtins))

print()
print()

# ------------------enclosing------------------


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        # adding this makes below line change outer x
        # and causes it to print inner x both times
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)

'''
if we were to delete inner x it would use outer x both times
'''
