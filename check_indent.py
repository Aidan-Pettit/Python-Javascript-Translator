from math import floor


def check_indent(line):
    whitespaces = 0

    for char in line:
        if not char == ' ':
            break
        else:
            whitespaces += 1

    return floor(whitespaces / 4)
