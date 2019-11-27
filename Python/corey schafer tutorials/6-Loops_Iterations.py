# For Loop
nums = [1, 2, 3, 4, 5]

print(nums)

# Break
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)

print()
print()

# continue
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)

print()
print()

# Nesting
for num in nums:
    for letter in 'abc':
        print(num, letter)

print()

# Range()
for i in range(10):
    print(i)

print()

for i in range(1, 11):
    print(i)

print()
print()

# While Loop
x = 0

while x < 10:
    print(x)
    x += 1

print()
print()

while True:
    x += 1  # In a while loop always increment first if using continue
    if x == 25:
        break
    if x == 16:
        continue
    print(x)
