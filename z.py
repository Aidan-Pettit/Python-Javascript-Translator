from re import sub, search
from create_file import create_file
from keys import keys
from legend import legend


def trans(filename, new_filename, _oglang, _newlang):
    oglang = legend[_oglang]
    newlang = legend[_newlang]

    code_list = []

    file = open(filename)

    # For each line in file,
    for line in file:
        if newlang == 'py':
            sub('}', ' ', line)
            sub('let', ' ', line)
            sub('const', ' ', line)
        # Check each key row
        for key in keys:
            # And replace target if key exists in line
            if search(key[oglang], line):
                newline = sub(key[oglang], key[newlang], line)
                print(key)
                print(newline)
                code_list.append(newline)

    create_file(code_list, new_filename)
