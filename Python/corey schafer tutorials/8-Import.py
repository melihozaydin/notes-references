import my_module as mm
import sys

courses = ['History', 'Physics', 'Math', 'CompSci']

index = mm.find_index(courses, 'Math')
print('index of \'Math\' is --> ', index)
print(mm.test)

print()

# places program checks to find module

"""
# looks at current work_dir
# then looks at PYTHONPATH env variables dirs
# then standart library dirs

to add custom path for another module you can:
1- sys.path.append('/custom/path/to/module') # Not Recommended
2-  Add the custom dir path to PYTHONPATH env_variable
"""

print('-----sys.path-----')
print(sys.path)


"""
*-You can give an imported module a short name
    by using 'import module_name as short_name'

*-When you import a module(file) you run its contents

*-you can import specific definitions from a module by
    'from module_name import func_name, func_name2'

*- You also can give shortnames to definitions using as statement
    'from my_module import func1 as f1, func2 as f2'

*- You can import everything by (However it is not recommended)
    'from my_module import *'

*-This is basicly a library functionality
You can call variables and functions defined
in the imported file as if they were
defined in the current script.

*-in order to import a file it needs to be within sys.path

*- The difference between import module and from module import foo is
mainly subjective. Pick the one you like best and be
consistent in your use of it. Here are some points to help you decide.

->import module

*Pros:
-Less maintenance of your import statements. Don't need to add any
additional imports to start using another item from the module

*Cons:
-Typing module.foo in your code can be tedious and redundant
(tedium can be minimized by using import module as mo then typing mo.foo)

->from module import foo

*Pros:
-Less typing to use foo
-More control over which items of a module can be accessed

*Cons:
-To use a new item from the module you have to update your import statement
-You lose context about foo.
For example, it's less clear what ceil() does compared to math.ceil()

Either method is acceptable, but don't use from module import *.

For any reasonable large set of code, if you import * you will likely be
 cementing it into the module, unable to be removed.
 This is because it is difficult to determine what items used in the code are
 coming from 'module', making it easy to get to the point where you think you
 don't use the import any more but it's extremely difficult to be sure.

"""

"""
my_module.py contents:

print('Imported my_module')

test = 'Test Str'


def find_index(to_search, target):
    # find the index of a value in a sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
"""
