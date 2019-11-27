import datetime


class Employee:

    raise_amount = 1.04  # this is a class variable
    num_of_emps = 0

    def __init__(self, firstname, lastname, pay):  # Constructor
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + lastname + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):

        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Employee.raise_amount

    @classmethod  # this is a decorator
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print('Before: ')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# This is the same as Employee.raise_amount = 1.05
Employee.set_raise_amount(1.05)
# But does it with a class method

"""
if you call the class method through an instance
    'emp_1.set_raise_amount(1.05)'
 it will still update the class variable

unlike 'emp_1.raise_amount = 1.05'
which created a new attribute for the instance
"""

print()
print('After: ')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# Class methods as alternative constructors (initializer)
# datetime module uses this to have alternative ways of creating a timestamp

"""
 You can use classmethods in order to provide multiple ways of creating objects

 Lets say we get employee info as str and we need to parse it before creating a new employee.

 so we want to create a claas that takes these strings and creates employees

Below is the slow and tedious way of doing it.
Instead we will make a new classmethod as an alternative init method
"""

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-30000'
emp_str3 = 'Jane-Doe-90000'


# slow way
print('---Slow employee creation: ---')

first, last, pay = emp_str1.split('-')
new_emp1 = Employee(first, last, pay)

first, last, pay = emp_str2.split('-')
new_emp2 = Employee(first, last, pay)

first, last, pay = emp_str3.split('-')
new_emp3 = Employee(first, last, pay)

print(new_emp1.__dict__)
print(new_emp2.__dict__)
print(new_emp3.__dict__)

print('\n')

# Class method way
print('---Class method employee creation: ---')

new_emp1 = Employee.from_string(emp_str1)
new_emp2 = Employee.from_string(emp_str2)
new_emp3 = Employee.from_string(emp_str3)

print(new_emp1.__dict__)
print(new_emp2.__dict__)
print(new_emp3.__dict__)

print('------RESULTS ARE SAME------')

# Staticmethods
"""
-regular methods auto pass the instance as first argument(self)
-class methods auto pass the class as first argument(cls)
-static methods don't pass anything automaticaly

they behave just like functions except they have a logical connection with the class
"""

# there can be mistakes in creating method
# where you make a class method that should be a staticmethod,
# you can distinguish them by
# looking if u access the instance or the class anywhere within the function definition

"""
Say we wanted a function that takes a date and return if it is a workday

This would have a logical connection with our class but doesn't depend on any instance or class variable
"""

my_date = datetime.date(2016, 7, 10)
print('\nIs workday---> ', Employee.is_workday(my_date))
