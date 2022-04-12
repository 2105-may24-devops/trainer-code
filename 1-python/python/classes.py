class Person:
    # any instance method in python needs "self" as the first parameter

    # constructor
    def __init__(self, name):
        # private
        self.__identifier = name
        # not private
        self.name = name

    def print_name(self):
        print(self.name)

    # a lot of the behavior of global built-in functions
    # is based on double-underscore (dunder) methods that you can override here
    def __str__(self):
        return f'({self.name})'

    # used by ==
    def __eq__(self, other):
        return self.__identifier == other.__identifier

# print(f'__name__ is {__name__}')

# anything in this condition, only runs if the module is being directly run
# (as opposed to imported)
if __name__ == '__main__':
    # basic OO idea:

    # writing code, we find that some pieces of data
    # are always used together
    student_ids = [1, 2, 3]
    student_names = ['bob', 'tim', 'fred']
    # rather than accidentally associating that data, let's use data structures
    # intelligently to keep it organized together
    student_info = [(1, 'bob'), (2, 'tim'), (3, 'fred')]
    # combine data and associated behavior into one unit called an object
    # encapsulation  - combining these things into one unit
    #    that controls access/its own rules about that stuff

    # classes are templates for making new objects
    # in other languages, you can't tack on new instance variables (aka fields)
        # besides the ones defined by the class. you can in python


    fred = Person('fred')
    fred.job = 'trainer'
    # print(fred.__name)
    fred.print_name()
    Person.print_name(fred) # equivalent to above line
    print(fred)
    str(fred)
    print(f'-- {fred} --')
    print(fred == Person('fred'))
    # do they refer to the same object
    print(fred is Person('fred'))


# a namespace is a context where variables live
# the way that python interprets any name of a variable/etc
#  like fred, Person, print, str, etc
# LEGB namespaces
# first, it checks the local namespace
# then, any enclosing namespaces,
# then, the global namespace,
# then, the built-in namespace (print, str)

var = 5 # global
if True:
    var2 = 5 # global

# functions, including nested functions, have their own namespaces
def func():
    var = 6 # enclosing (relative to func2)
    def print():
        pass

    def func2():
        var = 7 # local
        # print = 5
        print(var)
        # id = 5
        # map
        # filter

func()

var == 5
