# python has several data types

# numeric data types -
# int, float
# int for whole numbers
x = 10 + 2

# python is dynamically typed, so we can assign whatever value we want to
# any variable... but type annotations are a good way to keep organized.

# float for fractional numbers or very large numbers
y: float = 10.5

# we have typical arithmetic operators
# + - * / %
# ** for exponent
# // for integer division (regular / will return fractional floats)
print(5 // 2)
print(5 / 2)

# typical comparison operators
# < <= != == >= >

# bool data type, can be True or False.

# typical boolean operators, spelled out as words
print(3 < 4 or 5 < 4)

# str data type (string)
# use single quotes or double quotes, no difference
data = "asdf"
data = 'asdf'
# index strings to get individual characters, which are still type str
data = data[0] # == 'a'
print(data)
longstring = '''
multiline
string
'''

#  use "in" and "not in" operators to check for membership in any sequence
# (a str is a sequence)

print('abc' in 'abcdef') # True

# list data type

data2 = [ 3, 2, 6, 5 ]

print(data2[1]) # 2
