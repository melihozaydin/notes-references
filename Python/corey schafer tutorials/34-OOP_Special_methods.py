'''
Special methods we can use in our classes.
some call them magic methods.

they allow us to emulate some built in behavior within python
these are how we implement operator overloading

such as:

print(1 + 2)
print('a' + 'b')

# depending on what objects youre working with the addition has diffrent behavior

also if we print emp_1 instance we get:

print(emp_1)

<__main__.Employee object at 0x000001DA38C349E8>

it would be nice if we could change that behavior

Thats what special methods are for.

special methods are always surrounded by double underscores (__xx__) or dunder.

dunder init means : (__init__) this is also a special method
'''


class Employee:

    raise_amount = 1.04  # this is a class variable
    num_of_emps = 0

    def __init__(self, firstname, lastname, pay):  # Constructor
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Employee.raise_amount

    # this is an unambigous representation of an object and is for debugging

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.firstname, self.lastname, self.pay)

    # this is for representing the object as readable strings

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

# other is the secondary version of self just another object
# These alter the '+' operator and the len function for the instances of this class
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
'''
first we want to at least have the repr method. so if we dont have str
method when we call str on an object it will default back to repr.

'''

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# this will return: '<__main__.Employee object at 0x000001DA38C349E8>' if __str__ is not defined

# it will return: 'Corey Schafer - Corey.Schafer@company.com' if it is defined
print(emp_1)

'''
when the str and repr are both defined repr() and str() methods wont return because it implements into emp_1
so print(emp1) returns str methods output
'''
print()
# to access the repr and str specifically

print(repr(emp_1))  # returns: "Employee('Corey', 'Schafer', '50000')"
print(str(emp_1))  # returns: "Corey Schafer - Corey.Schafer@company.com"

# these and the above give the same results.
print(emp_1.__repr__())
print(emp_1.__str__())
print()


'''
so in  the print(1+2) and print('a' + 'b') example what the plus operator does is :
'''
# these are same
print(1 + 2)
print(int.__add__(1, 2))

# same outputs
print('a' + 'b')
print(str.__add__('a', 'b'))

'''
so we can actually customize how addition works for our objects by creating that __add__ method.

Lets make the employee class able too add salaries together by adding employees.
'''
print()
print(emp_1 + emp_2)

# > pretty much all operations on python are defined by dunder methods you can find them in online docs

print('---examples---')
print()

print(len('test'))
print('test'.__len__())

# We just changed the len method for the Eployee class to show employee name lenghts
print(len(emp_1))
