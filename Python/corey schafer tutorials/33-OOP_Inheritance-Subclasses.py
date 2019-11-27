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

"""
Say we want to create diffrent types of employees, like managers and developers. This is a good example
 because they both have same parameters.

We create a subclass by defining it with the parent class we want it to inherit from.

"""


class Developer(Employee):  # Employee is what class we want to inherit from
    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, prog_lang):
        # this will pass these attributes into parent init method so it will handle those.
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang


dev_1 = Developer('Melih', 'Ozaydin', 50000, 'Python')
dev_2 = Developer('Corey', 'Schafer', 60000, 'Java')

'''
when we instanciated the developer instances python looked into the Developer class and did not find a init method so
it moved up to the inheritance chain and initialized the instances from there.
This chain is called the 'Method resolution order'.
'''

print(dev_1.email)
print(dev_2.email)

# A very helpful function that makes it easy to visualize is
# the help function.

print(help(Developer))

'''
class Developer(Employee)
 |  Method resolution order:
 |      Developer
 |      Employee
 |      builtins.object
'''

# Lets make the developer raise amounts different.
print(dev_1.pay)
dev_1.apply_raise()  # it will use the raise-amount in Developer class.
print(dev_1.pay)

# say we wanted to init our Developer class differently
# so it has a programming language as well as all the other data.
'''
class Developer(Employee):  # Employee is what class we want to inherit from
    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, prog_lang):
        # this will pass these attributes into parent init method so it will handle those.
        super().__init__(firstname, lastname, pay)
        self.prog_lang = prog_lang
'''

print(dev_1.prog_lang)


class Manager(Employee):
    def __init__(self, firstname, lastname, pay, employees=None):
        super().__init__(firstname, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rmv_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

print()
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
print()
mgr_1.add_emp(dev_2)
mgr_1.print_employees()
print()
mgr_1.rmv_emp(dev_2)
mgr_1.print_employees()

print('-----------------------')

# is mgr_1 an instance of Employee class
print(isinstance(mgr_1, Employee))  # True
# is mgr_1 an instance of Developer
print(isinstance(mgr_1, Developer))  # False
# is Manager class a subclass of Employee
print(issubclass(Manager, Employee))  # True
# is Developer class a subclass of Manager
print(issubclass(Developer, Manager))  # False

print('------------------------')
