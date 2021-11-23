from stringify_code_list import stringify_code_list


def create_file(code_list, filename):
    code = stringify_code_list(code_list)

    file = open(filename, 'w')
    file.write(code)
