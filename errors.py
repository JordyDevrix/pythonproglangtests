

def invalid_number(line, error_line, code):
    return (f"INVALID_NUMBER_ERROR\n"
            f"\terror at line {line}\n"
            f"\t>> {error_line[line - 1]}\n")


def invalid_string(line, error_line, code):
    return (f"INVALID_STRING_ERROR\n"
            f"\terror at line {line}\n"
            f"\t>> {error_line[line - 1]}\n")


def invalid_variable_name(line, error_line, code):
    return (f"INVALID_VARIABLE_NAME_ERROR\n"
            f"\terror at line {line}\n"
            f"\t>> {error_line[line - 1]}\n"
            f"\t   {'^' * len(code)}")
