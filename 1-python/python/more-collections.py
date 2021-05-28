# result = 5/3
# if result:

data = ['asdf', '123', 'Aa']
names = ['asdf', '123', 'Aa']

# builtin functions that operate on sequences
    # zip

    # max
    # min
    # sum
sum([1, 2, 3])
# generator expressions
print(sum(len(x) for x in data))

    # all
    # any
print(all(len(x) > 2 for x in data))
print(any(len(x) > 2 for x in data))

# enumerate

# reversed
for x in reversed(data):
    pass

get_len = lambda x: len(x)

def get_length(x): # equiv to "len" or "lambda x: len(x)"
    return len(x)
def get_second_item(x): # equiv to lambda x: x[1]
    return x[1]
# sorted
print(sorted(data))
print(sorted(data, key=len))
print(sorted(data, key=get_len))
print(sorted(data, key=get_length))
print(sorted(data, key=(lambda x: len(x))))
print(sorted(names, key=lambda name: name[1]))

# result = []
# for x in data:
#     if len(x) > 3:
#         result.append(x)

#  functional programming type functions
# filter
print(list(filter((lambda x: len(x) > 3), data)))
# comprehension syntax is sometimes preferred to using filter
print([x for x in data if len(x) > 3])
# map
print(list(map((lambda x: len(x) > 3), data)))
print(list(map((lambda x: len(x)), data)))
print([len(x) for x in data if len(x) > 2])
# reduce


def get_length_and_first_two_chars(string):
    return len(string), string[0], string[1]

l, *_ = get_length_and_first_two_chars('abcdef')

print(get_length_and_first_two_chars('abcdef'))

one_million = 1_000_000

# sometimes you want to define a function
# that can take in any of many optional parameters
def print_all_args(*args, do_thing = False, **kwargs):
    # if len(args) == 1 and type(args[0]) == 'int':

    print(args)
    print(kwargs)

def helper_function(commonly_used_arg, *args, **kwargs):
    print_all_args(1, commonly_used_arg, 3, '45', *args, myarg=5, do_thing=True, custom_option=False, **kwargs)
