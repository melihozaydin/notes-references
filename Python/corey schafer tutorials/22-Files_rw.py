# File objects

# The way we are about to open up the test.txt
# file is not recommended
# It is generally good to use context managers instead

"""
we need to specify the opening mode:
-reading,     'r'
-writing,     'w'
-append,      'a'
-read & write 'r+'
"""
f = open('test.txt', 'r')

print(f.name)  # print filename
print(f.mode)  # print file open mode
# When you open a file you need to explicitly close it
f.close()

print('\n')

"""
    Using Context Manager
- the reason for this is if we open it without a cont. manager
we need to remember to close it. Otherwise it will cause memory leaks.

- the file operations only take place within the context manager block as seen below.
- the file is closed automatically when the porgram gets out of the block
"""

with open('test.txt', 'r') as f:
    print(f)

    # returns if file is closed
    print(f.closed)  # returns false because it's in the block

print(f.closed)  # returns true because it's outside the block


print('\n')

# read entire file

# This is not recommended for large files
# because it tries to do it all at once
# so it might cause memory issues on large files
print('Read entire file')

with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)

# Read line by line
print('Read line by line')

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents)

# Read file in loop
# This is the preferred method becasue it is sequential
print('Read entire file in loop')

with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')

# Read a certain amaount of characters from file
print('\nRead a certain amaount of characters from file')

with open('test.txt', 'r') as f:

    print(f.read(55))
    print(f.read(20))

    """
    Note that calling f.read() back to back resumes from
    the char where the last read command left off

    we can use this to read a large file
    which we don't know the size of and specify chunk sizes to read to optimize read speeds
    """

# Read the entires file with small chunks
print('\nRead the entires file with small chunks')

with open('test.txt', 'r') as f:
    size_to_read = 10  # define chunk size
    f_contents = f.read(size_to_read)

    print('', f.tell())  # this tells last position
    # while there is something to read
    while len(f_contents) > 0:
        print(f_contents, end=' -{}- '.format(str(f.tell())))
        f_contents = f.read(size_to_read)

print('\n\nf.seek()')
with open('test.txt', 'r') as f:
    f_contents = f.read(size_to_read)
    print(f_contents)
    f.seek(0)  # resume from 0. char
    print(f_contents)


print('\n\nWriting in files')
"""
in oreder ot be able to write to a file we need to open it in write mode
"""

# this will create the file if it exists
# or it will overwrite it if it exists!!!
# to prevent than you can open in append mode

with open('test2.txt', 'w') as f:
    f.write('testing')
    f.write('with a longline')  # they will append next to last char

    # acts as cursor position it will overwrite
    f.seek(0)
    f.write('R')

# copying file
print('\n')

print('Copy file')
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# in order to open images we need to open in binary mode using 'rb' and 'wb'
# read and write in bytes instead of text
print('Copy imfile')
with open('ivy.jpg', 'rb') as rf:
    with open('ivy_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)

print('Copy imfile in specific chunks')
with open('ivy.jpg', 'rb') as rf:
    with open('ivy_copy2.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        imsize = 0
        """
        # to cut image
        while len(rf_chunk) > 0  and imsize < 20000:
        """

        while len(rf_chunk) > 0:
            imsize = imsize + len(rf_chunk)
            print('Current chunksize -->{:04}, Current written bytes -->{:05}'.format(len(rf_chunk), imsize))
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
