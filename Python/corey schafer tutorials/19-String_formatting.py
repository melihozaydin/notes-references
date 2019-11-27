import datetime

person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and i am ' + str(person['age']) + ' years old'

print('Concatanation \n')
print(sentence)

# This is the not recommended way ^^^^

print('\nFormat\n')
sentence = 'My name is {} and i am {} years old'
print(sentence.format(person['name'], person['age']))

# Normally it orders left to right but you can number placeholders
sentence = 'My name is {0} and i am {1} years old'
print(sentence.format(person['name'], person['age']))

print()

tag = 'hi'
text = 'This is a headline'

sentence = '</{0}>{1}</{0}>'.format(tag, text)
print(sentence)

print('\n Dictionary and list numbering and value access \n')

sentence = 'My name is {0[name]} an i am {0[age]} years old.'.format(person)
print(sentence)


l = ['Jenn', 23]
sentence = 'My name is {0[0]} an i am {0[1]} years old.'.format(l)
print(sentence)

print('\n Class atrributes access \n')


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and i am {0.age} years old.'.format(p1)
print(sentence)

print('\n Keyword arguments in Format \n')

sentence = 'My name is {name} and i am {age} years old.'.format(name='Jenn', age='30')
print(sentence)

print('\n Unpacking Dict \n')
# This is the mos conveniant way
person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {name} and i am {age} years old.'.format(**person)
print(sentence)

print()
print('\n Format and print numbers \n')

for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)  # Zeor padding
    print(sentence)

# Decimal places with format
pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
sentence2 = 'Pi is equal to {:.4f}'.format(pi)

print('\n', sentence, '---', sentence2)


print('\n Example for large number with comma seperators and with 2 decimal places \n')
# : starts formatting, ',' makes readable comma seperators and .2f makes 2 decimals
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

print('\n\n Date time formatting \n')

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# lets say we want it in 'March 01, 2016' format
# docs.python.org/3/library/datetime.html
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061. day of the year.

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j}. day of the year.'.format(my_date)

# you have to number placeholders if you have multiple placeholders but only one format argument
print(sentence)
