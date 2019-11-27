# int
num = 3
# float
num2 = 3.14

# This method retuns datatype as str

print(type(num))
print(type(num2))

# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

print(3 + 10)
print(3 - 2)
print(3 * 3)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(57 % 51)

print()
print()

# Modulus operator is commonly used for controlling odd or even state
#  by taking mod of 2
print(53 % 2)

print()

# Order of operation

print(3 * 2 + 1)
print(3 * (2 + 1))

# operate variable
num = num + 1
print(num)

num += 1
print(num)

num *= 2
print(num)

print()
print()

# Useful functions

# Absolute value
print(abs(-3))

print()

# Round
print(round(3.75))  # Normal rounding op
print(round(3.75, 1))  # Round to first digit after decimal

print()
print()

# Comparison

# single equal is assignment
# double equal return true or false according to equality state
num_1 = 3
num_2 = 2

print(num_1 == num_2)  # Equal
print(num_1 < num_2)   # less
print(num_1 > num_2)   # more
print(num_1 <= num_2)  # less or equal
print(num_1 >= num_2)  # more or equal
print(num_1 != num_2)  # not equal

print()
print()

# Variable type confusion

num = '100'
num2 = '200'

print(num + num2)

print()
# Casting or converting variable

num = int(num)
num2 = int(num2)

print(num + num2)
