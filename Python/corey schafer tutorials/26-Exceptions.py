# These are used to handle possible errors

# When handling multiple exceptions
# make sure to put the more specific ones above the general ones

try:
    # f = open('testfile.txt')  # false
    # var = bad_var  # False

    f = open('names.csv')  # True

# 'raise' allows you to raise any Exception type you want manually
    if f.name == 'corrupt_file.txt':
        raise Exception

except FileNotFoundError as e:
    print('file not found')
    print(e)
except Exception as e:
    print('Something else went wrong')
    print(e)
else:  # This runs code in it if the try block doesn't get an error
    print(f.read())
    f.close()

#  finally would be the block to
#  close a database no matter what happens in the code
finally:  # This runs no matter what happens
    print('Executing finally...')
