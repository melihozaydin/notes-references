from operator import attrgetter

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li, reverse=True)

print('Sorted List: \t', s_li)
print('Original List: \t', li)

li.sort(reverse=True)  # sort method is list only
print('Original - sorted: \t', li)


tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
print('Tuple Original:\t', tup)
print('Tuple Sorted:\t', sorted(tup, reverse=True))

di = {'name': 'melih', 'Job': 'programming', 'age': None, 'os': 'Windows'}
print('Dict original: \t', di)
print('Sorted dict:\t', sorted(di, reverse=True))

print('\n sorting based on other criteria')
li = [-6, -5, -4, 1, 2, 3]
print()
print('Original List: \t', li)
print('List sorted:\t', sorted(li))
print('List sorted abs:\t', sorted(li, key=abs))
# Key runs each element through the function before sorting

print('\n')


class Employee():

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        # __repr__ tells python how we wnat this function
        # represented when it is printed out
        return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)


def e_sort_name(emp):
    return emp.name


def e_sort_age(emp):
    return emp.age


def e_sort_salary(emp):
    return emp.salary

employees = [e1, e2, e3]
print('Employees: \t', employees)
# this will give an error because it doesnt know how to sort them
# We need a sorting key
# s_employees = sorted(Employees)

print('Employees sorted by name', sorted(employees, key=e_sort_name))
print('Employees sorted by age', sorted(employees, key=e_sort_age))
print('Employees sorted by salary', sorted(employees, key=e_sort_salary))

print()

print('Lambda function \n')
print('Employees sorted with lambda', sorted(employees, key=lambda e: e.name))

print()

print('Attrgetter\n')
print('Employees sorted by age with Attrgetter\n',
      sorted(employees, key=attrgetter('age')))
