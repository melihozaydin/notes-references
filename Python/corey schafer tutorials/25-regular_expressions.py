"""
Regualar expressions to search for specific patterns of text.
"""
import re

# This is what we are looking for

# Raw string in python is just a text prefixed with 'r' (r'stringexample')
# these just ignore every special expression such as \ etc.

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

"""
This will return
<_sre.SRE_Match object; span=(1, 4), match='abc'>

 'span'is the beginning and ending index of the match

 this is an easy method to gather up searsh results in a readable place

 # this is case and order sensitive
"""

print('\nSimple search')
pattern = re.compile(r'abc')  # seperate out patterns into a variable
matches = pattern.finditer(text_to_search)  # retun iterator containing all matches

for match in matches:
    print(match)


# if you want to search for '.' in text you should use: re.compile(r'\.')
#    or for searching for url's: re.compile(r'abc\.')
#   because '.' is a special character in re module.

"""
Special characters in regex:

.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

# Anchors (match chars that have special conditions)

\b      - Word Boundary(space or tab at the start or end)
\B      - Not a Word Boundary
^       - Beginning of a String(is at the start of a str)
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group



#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
"""

# special regex definitions example
print('\nSpecials')

sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'^Start')
matches = pattern.finditer(sentence)
for match in matches:
    print(match)

# Match phone numbers in the text_to_search var
# we need to use special expressions to ignore dots and dashes
print('\nPhone Numbers')

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # custom pattern to find phones
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# Now use this to find phone numbers in a much larger file
print('\nPhone numbers in data.txt')

"""
   this might return codecs.charmap_decode(input,self.errors,decoding_table)[0]
   use open(, , , encoding='utf-8') to fix
"""
with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    # custom pattern to find phones
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

print('\nPhone numbers with only dashes and dots in between')
# custom pattern to find phones with dashes and dots in between
# this only matches a char that is either a dash or a dot
# if a number has two dashes in between it wont match the second one
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

print('\nPhones that start with either 800 or 900')
# Phones that start with either 800 or 900
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

print('\nall digits between 1-5 in the text')
# Phones that start with either 800 or 900
# you can also do this with letters as well like [a-z]
# character sets have special expressions
# ^ makes it look for everything that is not specified in the char set
pattern = re.compile(r'[1-5]')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


"""
---Quantifiers---
So far we have specified all patterns using single chars at a time
to be able to match multiple chars at a time we can use quantifiers

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - match 0 or One of the cahr spefied before it
{3}     - Exact Number (Amount specifier- \d{3} looks for 3 sequential digits
{3,4}   - Range of Numbers (Minimum, Maximum)

"""

print('\n-------Quantifiers--------')

print('\nphones with ***.***.**** format')
# pattern to find a phone with ***.***.**** format
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# If we dont know the exact format
# Pattern to find all names that start with Mr. / Ms / Mr / Mrs.
print('\nAll names that start with Mr. / Ms / Mr / Mrs.')
# (Mr|Ms|Mrs) is called a group
# it indicates to match either Mr or Ms or Mrs

# ? indicates that the period may or may not exist
# \s indicates a space
# [A-Z] matches any uppercase letter
# \w match any word char
# * indicates that wordchar may or may not exist
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# Pattern to find all emails
print('\nAll emails')
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# [a-zA-Z0-9_.+-] matches all chars that are
# 'a-z', 'A-Z', '0-9', '.', '-'separately indicated

# + before the @ indicates to match one or more of the chars stated above
# until it hits an @ symbol

# Char set ([]) after the at is to get the domain name same principle as before


pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)


# Pattern to find capture just the domin name and expression from a full url
print('\n\nCapture domains from URL\'s')
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#                      https : //www.    nasa  .gov
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for match in matches:
    print(match)
    # you can seperate groups '()' from results
    # indexes are the same as the order in pattern
    print(match.group(0))  # entire Match
    print(match.group(1))  # (www\.)
    print(match.group(2))  # (\w+)
    print(match.group(3))  # (\.\w+)
    print('-----')

# sub method is for substitution
# this substitudes all matched full urls with group 2 and 3
# which turns them into simple urls
subbed_urls = pattern.sub(r'\2\3', urls)
print('\nSimplified urls\n', subbed_urls)  # simplified urls

"""
findall: returns only the matched text
finditer: returns more info such as location

if findall is used for multi groups it will return a list of tuples
and those tuples would contain the matched groups

match method returns only the first match and look for only patterns at the beginning of a string

search method returns only the first match it finds and looks through entire text
"""
"""
----Flags----

for exampleif we wanted to look for 'start' in a text case insensitively
instead of:
re.compile(r'[Ss][Tt][Aa][Rr][Tt])

re.compile(r'start', re.IGNORECASE) or
re.compile(r'start', re.I)
would work.
"""
