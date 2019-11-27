# lists and tuples are sequantial data
# Sets are unordered collections of values with no duplicates

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))  # This returns number of elements in list

# Indexing

print(courses[0])  # element with index 0

# all elements including index 1 upto but not including index 3
print(courses[1:3])

print()

# List operations

courses.append('Art')  # this adds an element to the end of list
print(courses)

# İnsert inserts an elemnt into a specified indice
# new element will became the specified index and shift everything after it
courses.insert(3, 'Education')
print('Courses---->>', courses)
print()

# if the new element is a list it will insert the list into a single indice
courses_ins = ['History', 'Math', 'Physics', 'Education', 'CompSci', 'Art']
courses_2 = ['Music', 'Finance']

courses_ins.insert(2, courses_2)

print('Couses_ins --->', courses_ins)
print(courses_ins[2])  # the 2nd indice is a list so there is a list in a list

print('Courses---->', courses)
print()
print()

# This is why extend exists
# it appends each individual item in a list to another list
# append method also makes the mistake which insert does

courses.extend(courses_2)
print('Extend --->', courses)

# Removing elements
courses_ins = ['History', 'Math', 'Physics',
               'Education', 'CompSci', 'Art', 'Music', 'Finance']

courses_ins.remove('Math')  # this removes specified element
print(courses_ins)

print()

# This removes last item from a list and returns that item

courses_ins = ['History', 'Math', 'Physics',
               'Education', 'CompSci', 'Art', 'Music', 'Finance']
popped = courses_ins.pop()
print(popped)
print(courses_ins)

print()

courses_ins = ['History', 'Math', 'Physics',
               'Education', 'CompSci', 'Art', 'Music', 'Finance']


# Sorting

# This reverses elements
courses_ins.reverse()
print(courses)
print()
print()

# Sort method alphebetically sorts

courses_ins.sort()
print('Alphebet sort >> ', courses_ins)
courses_ins.sort(reverse=True)
print('Reverse Sort >> ', courses_ins)
"""
sort by integer so 10 comes after 9
if we sort as str 10 comes after 1
imfiles = sorted(imfiles, key=lambda a: int(
    a.split(".")[0]))  # sort image files by name
"""
print()

# if list has numbers it sorts them in ascending order
# note that the datatypes are still str
nums = ['5', '3', '7', '4', '9', '1', '8', '2']
print('Nums unsorted >> ', nums)

nums.sort()
print('Nums sorted >> ', nums)

nums.sort(reverse=True)
print('Nums Reverse >> ', nums)

print()

# if you want a sorted new list without altering the original

sorted_courses = sorted(courses)
print(courses)
print('Sorted Courses >> ', sorted_courses)

print()
print()

# Other Useful FUnctions

print(nums)
print('Min ', min(nums))
print('Max ', max(nums))

print()

nums = [1, 8, 35, 12, 78]
print(sum(nums))

print()
print()

# Find index of value in list

print('Math index ', courses.index('Math'))
print('Check existance for Math --->', 'Math' in courses)

print()
print()

# loop through each item and do something on each
for item in courses:
    print(item)


print()
print()

# access index of each item
numerate = enumerate(courses)
print('Enumarate ---> ', numerate, '\n')

# Enumarate returns each items Valua and its index

for index, item in enumerate(courses):
    print(index, item)

print()

# You can specify the starting index

for index, item in enumerate(courses, start=1):
    print(index, item)


print()
print()

# List join strings

# Adds str to betwwen items
course_str = ' - '.join(courses)
print(course_str)

# this removes them back
# split up all of this argument and make a list out of whats left
new_list = course_str.split(' - ')
print(new_list)

print()
print()

# Tuples
# You cant modify tuples unlike lists (lists are mutable, tuples are immutable)

# Mutable

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print('list_1 before', list_1)
print('list_2 before', list_2)

# This will change both lists because they are the same object
# It's because lists are mutable

list_1[0] = 'Art'

print('list_1 after  ', list_1)
print('list_2 after  ', list_2)

print()
print()

# because of this we use an immutable object (Tuples)

# Immutable

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print('tuple_1 before  ', tuple_1)
print('tuple_2 before  ', tuple_2)

"""
# This will cause error because they are immutable

tuple_1[0] = 'Art'


print('tuple_1 after  ', tuple_1)
print('tuple_2 after  ', tuple_2)

"""

print()
print()

# Sets
"""
Sets are unordered and they don't contain any duplicates
Every time you print them the order will be different

This makes them efficent to use with
checking if an item exists in a chunk of data
And they are useful for comparing data chunks
"""

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
art_courses = {'Art', 'Math', 'Design', 'History', 'Art'}

print(cs_courses)
print('Math' in cs_courses)

print()

# Common courses
print(cs_courses.intersection(art_courses))

# in cs but not in art
print(cs_courses.difference(art_courses))

# combine sets
print(cs_courses.union(art_courses))


# Creating empty lists tuples and sets

# Empty lists
empty_list = []
empty_list = list()

# Empty tuples

empty_tuple = ()
empty_tuple = tuple()

# Empty sets

"""
#THIS IS WRONG IT CREATES AN EMPTY DICT!

Empty_set = {}
"""
empty_set = set()
