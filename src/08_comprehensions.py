"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [a + 1 for a in range(5)]

# for a in range(5):
#     b = a + 1
#     y.append(b)

print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [a**3 for a in range(9)]

# for a in range(9):
#     y.append(a**3)

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [aa.upper() for aa in a]

# for aa in a:
#     y.append(aa.upper())

print(y)

# might need help with the one below

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# print(type(x[0]))
# print(x)

# for num in x:
#     new_num = int(num)
#     if new_num % 2 == 0:
#         print(new_num)
#         y.append(new_num)

# What do you need between the square brackets to make it work?
y = [int(num) for num in x if int(num) % 2 == 0]

print(y)