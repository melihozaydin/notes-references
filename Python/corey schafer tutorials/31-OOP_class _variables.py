"""
Say we wanted a variable that is the same for every instance(employees)
That would be a Class variable.
"""


class Employee:

    raise_amount = 1.04  # this is a class variable
    num_of_emps = 0

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + lastname + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):

        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Employee.raise_amount

"""
we need to call them in methods as 'class.variable' or 'self.variable'
so we can access these through the the class or an instance of the class.

"""

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print('Employees raise amount: ', Employee.raise_amount)
print("Emp_1's raise amount: ", emp_1.raise_amount)
print("Emp_2's raise amount: ", emp_2.raise_amount)

print()

print("Emp_1 pay before raise: ", emp_1.pay)
emp_1.apply_raise()
print("Emp_1 pay after raise:", emp_1.pay)

"""
when we try to access an attribute on an instance, it will check if
that instance contains that attribute. If it doesn't, it will look if
 the class or any class that it inherits from contains it.

So when we call 'emp_1.raise_amount' emp_1 doesn't have that attribute but the Employee class does.
"""
print()
print()

print('Namespace of Employee class: ', Employee.__dict__)
print()
print('Namespace of emp_1: ', emp_1.__dict__)

print()
print()

"""
if we change the class variable while accessing it through Employee class it will just update it.

But if we change it while accessing through an instance it will create
 an instance variable for that instance and update it.

and whenever we call apply_raise method that specific employee will
 get a diffrent raise amount than all other employees(instances).
 (If apply_raise method is defined with self.raise_amount.)
"""

Employee.raise_amount = 1.05  # access through class
print('Employees raise amount: ', Employee.raise_amount)
print("Emp_1's raise amount: ", emp_1.raise_amount)
print("Emp_2's raise amount: ", emp_2.raise_amount)

print()

print("Emp_1 pay before new raise: ", emp_1.pay)
emp_1.apply_raise()
print("Emp_1 pay after new raise:", emp_1.pay)

print()

emp_2.raise_amount = 1.1  # access through instance
print('Employees raise amount: ', Employee.raise_amount)
print("Emp_1's raise amount: ", emp_1.raise_amount)
print("Emp_2's raise amount: ", emp_2.raise_amount)
print()

# Notice that emp_2 has a new attribute called raise amount
print('Namespace of emp_1: ', emp_1.__dict__)
print('Namespace of emp_2: ', emp_2.__dict__)


print()
"""
so if we defined 'apply_raise' method using 'self.raise_amount' it will use
 the specific raise amount of that employee if it has one
 else it will use the class variable 'raise_amount'.

otherwise if we used 'Employee.raise_amount' for 'apply_raise'
it would use that regardless of the existance of an instance specific raise amount.

Also using sel will allow any subclass to override that constant if they wanted to.
"""

print("Emp_2 pay before new raise: ", emp_2.pay)
emp_2.apply_raise()
print("Emp_2 pay after new raise:", emp_2.pay)

print()
print('---Another Example---')
print()

'''
Say we wanted to know the amount of our employees.
we defined a 'num_of_emp' to update through the init method every time we create one

in this example there is no use case for the num of employees to be diffrent for every instance.
'''
print('Employee Count: ', Employee.num_of_emps)
