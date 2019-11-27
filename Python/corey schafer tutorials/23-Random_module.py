"""
This shouldn't be used for cryptography or security
use secrets module instead
"""
import random

value = random.random()  # rand float between [0,1)
print(value)

value = random.uniform(1, 10)  # rand float between [0,10)
print(value)

value = random.randint(1, 6)  # rand int between [1, 6]
print(value)

greeting = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola', 'SA']
value = random.choice(greeting)  # rand element from a given list
print(value + ', Melih')

# Roulette simulation
print('\n Roulette')
colors = ['Red', 'Black', 'Green']
# choose rand element from list 10 times and return results,
# Each element is equally likely to be chosen with, out weights argument
# Weight input is synced with the input lists orders
# Red = 18/38
# Black =  18/38
# Green = 2/38
results = random.choices(colors, weights=[18, 18, 2], k=10)
print(results)

# Card deck simulation
print('\n Card Deck')
deck = list(range(1, 53))
random.shuffle(deck)  # shuffle elements in a list
print('Deck--->', deck)

"""
if we wanted to choose 5 random cards from the deck we shouldn't use random.choises method
because it might get the same card twice

random.sample method is the solution
"""
hand = random.sample(deck, k=5)
print('Hand --->', hand)

print('\n\n')

# Module to create fake info

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Curtis', 'Tayfun', 'Melih', 'Kader', 'Zeynep', 'Beyza']
last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Ozaydin', 'Erdem',
              'Dulkadirogulları', 'Ozbokuboncuklular', 'Tayfur', 'Barbaros']
street_names = ['Main', 'High', 'Argincik', 'Bagcilar', 'Pearl', 'Oak', 'Elm', 'Pine', 'Park', 'Meydan', 'Kosk',
                'Altinoluk', 'Cedar']
fake_cities = ['Metropolis', 'Utopia', 'Mordor', 'Mustafar', 'Naboo', 'Ankara', 'Bursa', 'Kayseri', 'Atlantis',
               'King\'s landing']
states = ['AL', 'AK', 'AZ', 'TR', 'DC', 'FL', 'GA', 'CO', 'CT', 'ID']

for num in range(1, 10):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(500, 570)}-{random.randint(100,999)}-{random.randint(1000, 9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@bogusmail.com'
    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')
