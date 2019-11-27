# Why use classes?
"""
Logically group our data and functions that is easy to reuse and also easy to build up on

Data and functions --> attributes-methods
"""

# Say we had an app for our company
# and we had to represent the employees in our code
# this is a good use case for a class because
# each employees has a name, address and clearences
# so each employee has specific attributes and methods
# and it would be nice to have a class we could use as a blueprint to create each employee


class employee:
    pass

"""
Class instances:
each employee created with the class is an instance
instances have diffrent mem locations

this is important to differentiate between class variables and instance variables
"""

emp_1 = employee()
emp_2 = employee()

emp_1.first = 'Melih'
emp_1.last = 'Ozaydin'
emp_1.email = 'MelihOzaydin@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.user@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

"""
This is the slow way and doing this makes classes useless
say we wanted to set all this info for each employee when they are created

to make that we use a special init method. think of it as initialize (constructor)
"""
print()
print()


class Employee:
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + lastname + '@company.com'

    def fullname(self):

        return '{} {}'.format(self.firstname, self.lastname)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

'''

When you create a method within a class they take the instance as the first argument.

Self argument in init is passed in automatically as that variable when you assign class to a variable.

Self is just a convention you can use whatever as the instance placeholder in definition (but use 'self' anyway)
'''

'''
Let's create a method in our class that shows an employees full name.
'''
print()

print('emp_1 fullname: ', emp_1.fullname())
print('emp_2 fullname: ', emp_2.fullname())

'''
One common mistake in usage of methods in classes is forgetting 'self' argument

if we didnt use self in fullname for example it when we call it as 'emp_1.fullname' emp_1 instance would get
 passed in anyway but since we didnt define any argument it would raise an error.
'''
'''
The usage of self becomes more obvious when we use classes without defining an instance first. In that case we have to
pass the instance ourselves

Below two statements do exactly the same things
'''
# this passes instance automatically
print(emp_1.fullname())
# But this doesnt know which instance to run the fullname method in the Employee class unless we  pass in 'emp_1'
print(Employee.fullname(emp_1))

