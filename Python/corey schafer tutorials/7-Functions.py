def empty_func():
    pass  # leave the function empty for now


def hello_func():
    print('Hello Function')

print()

# This doesn't execute the function but print its mem location
print(hello_func)

hello_func()
hello_func()
hello_func()
hello_func()

print()
print()

# DRY code means not repating yourself
# or assigning variables to change multiple lines easily

# Return


def return_ex():
    return 'Hello Return'

return_ex()  # this won't print anything it becomes what it returns

print(return_ex())  # So you can use it like this

print(return_ex().upper())  # it became a string it can take string methods

print()

# argumants


def argument_ex(greeting, name='You'):  # Default for name is 'You'
    return '{}, {}'.format(greeting, name)

print(argument_ex('Hi'))  # if not given string for name it uses the default
print(argument_ex('Hi', 'melih'))

print()

"""
 *args and **kwargs allow you to pass a variable number of arguments
 to a function. What does variable mean here is that you do not know before
 hand that how many arguments can be passed to your function by the user
 so in this case you use these two keywords.

 *args is used to send a non-keyworded variable length argument list
  to the function

 **kwargs allows you to pass keyworded variable length of arguments
 to a function.

 You should use **kwargs if you want to handle named arguments in a function.

"""


def studen_info(*args, **kwargs):  # arguments and keyword arguments
    print()
    print(args)
    print(kwargs)
    print()

studen_info('Math', 'Art', name='John', age=22)

# args is a tuple with 'Math', 'art'

# kwargs is a dict with keywords and values

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

studen_info(*courses, **info)

# Eample application

# Number of days per month, first value is placeholder for indexin convinience
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    # Return True for leap years, false for others

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

    # Return number of days in that month in that year

    if not 1 <= month <= 12:
        return 'invalid month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print()
print('----------------------------------')
print(days_in_month(1998, 5), ' ', is_leap(1998))
