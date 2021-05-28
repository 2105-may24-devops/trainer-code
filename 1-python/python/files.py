import sys

print(*sys.path)

import classes


# in python, your module (file) can import things from other modules.

nick = classes.Person('nick')

# there is a builtin module that's good for handling command line arguments
# called argparse if you don't want to manually deal with sys.argv

# print(sys.argv)
if len(sys.argv) < 2:
    raise Exception('must provide path')

# in a code context, when you open a file, there's always a question of
# "mode" - read, write, read-write, append, etc
file = open(sys.argv[1], 'r')
# file.read() # whole file contents into str
# file.readline() # one line contents into str (also, what "for x in file" does)
# file.readlines() # whole file contents into a list of strs (lines)
# file
lines = []
for line in file:
    lines.append(line)
    # print(line, end='')

file.close()

# just in case of error, we need finally block, like this
# file = None
# try:
#     file = open(sys.argv[1] + '.bak', 'w')
#     # what if an error is raised during writing the lines
#     file.writelines(lines)
# finally:
#     if file:
#         file.close()

# instead of typing all that, python gave us "with" statement
# try:
with open(sys.argv[1] + '.bak', 'w') as file:
    file.writelines(lines)
# except Exception as e

# there's also pickle
