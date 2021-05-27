# exercism exercise "transpose"
def transpose(lines: str) -> str:
    input_list = lines.split('\n') # or splitlines
    input_height = len(input_list)
    input_width = get_input_width(input_list)

    output_list = []

    for colnum in range(input_width):
        output = ''
        for rownum in range(input_height):
            output += get_char(input_list, rownum, colnum)
        output = output.rstrip('*').replace('*', ' ')
        output_list.append(output)

    return '\n'.join(output_list)

def get_char(input_list, rownum, colnum):
    # row = input_list[rownum]
    # if colnum >= len(row):
    #     return '*'
    # return row[colnum]
    try:
        return input_list[rownum][colnum]
    except IndexError:
        return '*'

def get_input_width(input_list):
    # max_length = 0
    # for i in range(len(input_list)):
    #     row = input_list[i]
    #     if len(row) > max_length:
    #         max_length = len(row)

    # max_length = 0
    # for row in input_list:
    #     if len(row) > max_length:
    #         max_length = len(row)

    # list comprehension
    # lengths = [len(x) for x in input_list] # list of ints
    # max_length = max(lengths)

    # generator expression
    # an expression that acts like a sequence, that's not built yet
    max_length = max((len(x) for x in input_list), default=0)

    return max_length

print(transpose("AB\nC"))
print(repr(transpose("AB\nC").split('\n')))
