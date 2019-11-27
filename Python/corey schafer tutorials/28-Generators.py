import random
import memory_profiler as mp  # non-standart library
import time


def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_numbers([1, 2, 3, 4, 5])

print(my_nums)  # returns [1, 4, 9, 16, 25]

print('\n---Generators---')
"""
Generators calculate output only when you ask for it.
they do not store results
"""


def square_numbers_generator(nums):
    for i in nums:
        yield(i*i)  # This is what makes it a generator

my_nums = square_numbers_generator([1, 2, 3, 4, 5])

# returns generator object --> <generator object square_numbers_generator at 0x000001B05C18A2B0>
print(my_nums)

"""
# Returns the next output of generator
# if you run thgrough the end of the generator it will give an error
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

# this will give an error because it's out of inputs
# print(next(my_nums))
"""

# You can also iterate through normally
for num in my_nums:
    print(num)

"""
the advantage over list is
-it's more readable
-more memory efficient

"""

"""
the advantage over a list comprehension
- more efficient
- list comprehension calculates everything beforehand
- generator calculates only when it needs it

list comprehension:
my_nums = [x*x for x in [1, 2, 3, 4, 5]]

generators:
my_nums = (x*x for x in [1, 2, 3, 4, 5])

- You can store results by converting generator to list but you will lose performance:

list(my_nums)
"""

print('\n---Efficiency Comparison---')
# Efficency comparison

names = ['Melih', 'Jessy', 'Corey', 'Steve', 'Rick', 'Thomas', 'Tayfun', 'Beyza', 'Morty', 'Bilge', 'Ahmet']
majors = ['Law', 'Engineering', 'Math', 'Compsci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

print(f'Memory Before: {mp.memory_usage()} Mb')

t1 = time.clock()
people = people_list(1000000)
# people = people_generator(1000000)
t2 = time.clock()

print(f'Memory After: {mp.memory_usage()} Mb')
print(f'Took {t2-t1} seconds.')

print(len(list(people)))

"""
---List Results---
Memory Before: [32.90625] Mb
Memory After: [304.13671875] Mb
Took 1.9506406705925206 seconds.

---Generator Results---
Memory Before: [32.75390625] Mb
Memory After: [32.76171875] Mb
Took 4.345672145110684 e-06 seconds.
"""
