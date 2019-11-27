nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want n for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# I want n*n for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n*n)
print(my_list)

print('\nComprehensions')
# List comprehension versions of above apps
my_list = [n for n in nums]
print(my_list)

my_list = [n*n for n in nums]
print(my_list)

# Using map + lambda
my_list = map(lambda n: n*n, nums)
print('Map + Lambda --->', my_list)

'''
map runs verything in the list through a certain function
lamda is a anonymous function

it is unraedable so not recommended
'''

print('\n n for each n in nums if the n is even')

my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print('For Loop -- ', my_list)

# Comprehension version
my_list = [n for n in nums if n % 2 == 0]
print('Comprehension -- ', my_list)

# Filter + Lambda
my_list = filter(lambda n: n % 2 == 0, nums)
print('Filter + Lambda -- ', my_list)


print('\nA (Letter, num) pair for each letter in \'abcd\' and ',
      'each number in nums')
# For loop version
my_list = []
for letter in 'abcd':
    for num in nums:
        my_list.append((letter, num))
print('For loop \n', my_list)

# Comprehension version
my_list = [(letter, num) for letter in 'abcd' for num in nums]
print('\n Comprehension \n', my_list)

# Dict Comprehensins
print('\n(name: Hero) for each name, hero in zip(names, heros)')

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name,  hero in zip(names, heros):
    my_dict[name] = hero
print('For loop --> \n', my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print('\nDict Comprehension --> \n', my_dict)
print('Note that Peter is excluded')

print('\n')

# Set comprehensions

nums = [1, 1, 2, 2, 5, 6, 5, 6, 6, 7, 4, 7, 8, 9, 10]
print('Set Comprehension')

my_set = set()
for n in nums:
    my_set.add(n)
print('For loop --> \n', my_set)

my_set = {n for n in nums}
print('Comprehension ---> \n', my_set)

# Generator Expressions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('\nGenerator Expressions\n')
# Function


def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
print('Function)
for i in my_gen:
    print(i)

# Expression
print('expression)
my_gen = (n*n for n in nums)
for i in my_gen:
    print(i)
