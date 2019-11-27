import os
from datetime import datetime

# this will show all available attributes and modules
# print(dir(os))

print(os.getcwd())  # get current working dir

# chanege cwd
os.chdir('/Users/XTI/Desktop')

print('listdir', os.listdir())

# Creating folders

# os.mkdir('OS-demo/sub-dir1') # this cant make folder trees recursively

os.makedirs('OS-demo/sub-dir1')  # this can make them

os.chdir('/Users/XTI/Desktop/OS-demo')

print()
print(os.listdir())

# Removing files or folders

os.chdir('/Users/XTI/Desktop')
# os.rmdir('OS-demo/sub-dir1')  # this is not recursive
os.removedirs('OS-demo/sub-dir1')  # this is recursive

print(os.listdir())

print()
"""
# Renaming

os.rename('old_name.txt', 'new_name.txt')

"""
# view properties
print('\n', os.stat('new_name.txt'))
print('\n', os.stat('new_name.txt').st_mtime)

# convert timestamp to readable time
mod_time = os.stat('new_name.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print('\n')

"""
See the entire dir tree
os.walk()

this yields a 3 value tuple
---> dir path str
---> folders in that dir
---> file names in that path
"""
"""
path_input = '/Users/XTI/Desktop/Oyn'

for dirpath, dirnames, filenames in os.walk(path_input):
    print('Current path: ', dirpath)
    print('Dirs: ', dirnames)
    print('Files: ', filenames)
    print()
"""

# Accessing env variables
print(os.environ.get('Temp'))

# this path joining is a bad method
file_path = os.environ.get('Temp') + 'new_name.txt'
print('Wrong way: ', file_path)
# This helps out
file_path = os.path.join(os.environ.get('Temp'), 'new_name.txt')
print('Right way: ', file_path)

# Other useful stuff
print(os.path.basename('/tmp/test.txt'))  # get base filename
print(os.path.split('/tmp/test.txt'))  # get both filename an dirname
print(os.path.exists('/tmp/test.txt'))  # check if a path exists

# check if something is a dir or file
print(os.path.isdir('/tmp/test.txt'))  # true if folder
print(os.path.isfile('/tmp/test.txt'))  # true if file

# splitting extensions from path
print(os.path.splitext('/tmp/test.txt'))
