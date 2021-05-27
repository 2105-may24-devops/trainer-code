# you can convert anything into a str with the str() function
str(123.12)
# common string methods
# find (find a substring's index in a string)
# format (but you might as well use f-string)
# is____ (string's characters meet some condition like lowercase)
# lower, upper (convert to lowercase, uppercase)
# replace (replace some substring with another)
# split (breaks up the string into a list of strings by some delimiter)
# strip (drops leading and trailing chars (whitespace by default))

# 'calculation result is: ' + str(34 / 5)
var1 = 34
var2 = 5

print('{0[0]} / {0[1]} result is: {1:.20}'.format([var1, var2], var1 / var2))

# now, we have f-strings
output = f'{var1} / {var2} = {(var1 / var2):e}'
print(output)

# slicing: (not just for stirngs, also for any sequences)
data = 'abcdefghijkl'
print(data[1]) # b
print(data[1:5]) # bcde
print(data[:6]) # abcdef
print(data[-1]) # l
print(data[-3]) # j
print(data[-len(data)]) # a
print(data[3:-2]) # defghij
print(data[::2]) # acegik (every odd letter)
print(data[8:3:-3]) # if

['asd', 123]

data2 = 'asdf' + data[8:3:-3]

i = 0
# while True:
#     input()
#     i += 1
#     print(data[i % len(data)])


def addition(a, b):
    '''Adds two things
    '''
    return a + b

addition('asdf', 'ghjkl') # works
addition(123, 123) # works
addition('asdf', 123) # error

# convert string to list of characters (strings)
list('asdf')
''.join(['a', 's', 'd', 'f'])

'aaa' == 'a' * 3
