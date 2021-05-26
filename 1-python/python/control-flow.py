# we have if-else conditionals

# int and input are builtin functions

data = int(input('enter a number: '))
if data == 0:
    print('it was zero')
elif data < 0:
    print('negative')
else:
    data = 'abc'

print(data)

print(type(data))

# while loop
# while input('enter x: ') != 'x':
#     print('error, enter x')

# for loop
# in python, you always iterate over a sequence of some kind
for i in range(0, 5, 1): # or range(5), same thing here
    print(i)

# range is a sequence data type in python
# that is 'lazy', it doesn't precompute the whole thing like a list,
# it calculates each value as needed

# usually you don't even write loops like that... you figure out a way to
# iterate over the collections of data that you'd be using that "i" to access

sequence = [1, 3, 7, 2, 5 ]
for item in sequence:
    print(item)

# comprehension syntax in python is applied here and it's pretty powerful

# if you want to iterate over a list AND have an index as well

for i, item in enumerate(sequence):
    if i > 0:
        print(item != sequence[i - 1])
