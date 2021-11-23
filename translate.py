from re import search, sub
from create_file import create_file
from check_indent import check_indent


def translate(filename, new_filename):
    file = open(filename)
    code_list = []
    indent_counter = 0
    mode = 'normal'

    for line in file:
        newline = line
        print(line)

        indent = check_indent(line)
        print(indent)

        if indent < indent_counter:
            code_list.append('' * 4 * indent + '}\n')

        indent_counter = indent

        if line[0] == '\n':
            newline = '\n'

        if line[0] == '#':
            newline = sub('# ', '// ', newline)
            code_list.append(newline)
            continue

        if search('class', line):
            mode = 'class'

        if search('print', line):
            newline = sub('print', 'console.log', newline)

        newline = sub(' and ', ' && ', newline)
        newline = sub(' or ', ' || ', newline)

        if search('if', line):
            newline = sub('if ', 'if (', newline)
            newline = sub(':', ') {', newline)

        if search('for', line):
            newline = sub('in', 'of', newline)
            newline = sub('for ', 'for (let ', newline)
            newline = sub(':', ') {', newline)

        if search('while', line):
            newline = sub('while ', 'while (', newline)
            newline = sub(':', ') {', newline)

        if search('True', line):
            newline = sub('True', 'true', newline)

        if search('False', line):
            newline = sub('False', 'false', newline)

        if search('None', line):
            newline = sub('None', 'null', newline)

        if search('math.', line):
            newline = sub('math.', 'Math.', newline)

        if search('fabs', line):
            newline = sub('fabs', 'abs', newline)

        if search('import math', line):
            newline = ''

        if search('import random', line):
            newline = ''

        if search('random\\.', line):
            newline = sub('random\\.', 'Math.', newline)

        if search(' random', line):
            newline = sub(' random', 'Math.random', newline)

        if mode == 'normal':
            if search('def', line):
                newline = sub('def', 'function', newline)
                newline = sub(':', ' {', newline)

            if search(' = ', line):
                newline = 'let ' + line

        if mode == 'class':
            newline = sub(':', ' {', newline)

            if search('def __init__\\(self, ', line):
                newline = sub('def __init__\\(self, ', 'constructor(', newline)

            if search('def', line):
                newline = sub('def', '', newline)

            if search('\\(self\\)', line):
                newline = sub('\\(self\\)', '()', newline)

            if search('self\\.', line):
                newline = sub('self\\.', 'this.', newline)

        if not line == '':
            code_list.append(newline)

        print(code_list)

    if indent_counter > 0:
        code_list.append('}\n')

    create_file(code_list, new_filename)
    file.close()
