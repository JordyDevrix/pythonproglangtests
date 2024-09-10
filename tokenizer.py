import errors
from stdfunc import *


def tokenizer():
    # SETTINGS
    dec_identifier = "."
    # SETTINGS

    with open("code.txt", "r") as file:
        code = file.read()

    code_lines = code.split("\n")
    tokens = []
    code_length = len(code)
    i = 0
    line = 0

    while i < code_length:

        if code[i] == "#":
            start_i = i
            while i < code_length and code[i] != "\n":
                i += 1
            # tokens.append(("COMMENT", code[start_i:i]))
            continue

        if code[i] == " ":
            i += 1
            continue

        if std_isnumeric(code[i]) or code[i] == dec_identifier:
            start_i = i
            num_type = "INT"
            while i < code_length and std_isnumeric(code[i]):
                i += 1
            if code[i] == dec_identifier:
                i += 1
                num_type = "FLOAT"
            while i < code_length and std_isnumeric(code[i]):
                i += 1
            if code[i] == dec_identifier or std_isalpha(code[i]):
                print(errors.invalid_number(line + 1, code_lines, code[start_i:i]))
                exit(1)
            if num_type == "INT":
                number = str(int(code[start_i:i]))
            else:
                number = str(float(code[start_i:i].replace(",", "."))).replace(".", dec_identifier)
            tokens.append((num_type, number))
            continue

        if code[i] == '"':
            start_i = i + 1
            i += 1
            while i < code_length and code[i] != '"':
                i += 1
            if i < code_length:
                i += 1
            tokens.append(("STRING", code[start_i:i-1]))
            continue

        if code[i] == "'":
            start_i = i + 1
            i += 1
            while i < code_length and code[i] != "'":
                i += 1
            if i < code_length:
                i += 1
            tokens.append(("STRING", code[start_i:i-1]))
            continue

        if code[i:i+5] == "print" and (i+5 == code_length or not std_isalphanumeric(code[i+5])):
            tokens.append(("KEYWORD", "print"))
            i += 5
            continue

        if code[i:i+4] == "read" and (i+4 == code_length or not std_isalphanumeric(code[i+4])):
            tokens.append(("KEYWORD", "read"))
            i += 4
            continue

        if code[i:i+4] == "func" and (i+4 == code_length or not std_isalphanumeric(code[i+4])):
            tokens.append(("KEYWORD", "func"))
            i += 4
            continue

        if code[i:i+2] == "if" and (i+2 == code_length or not std_isalphanumeric(code[i+2])):
            tokens.append(("IFSTATE", "if"))
            i += 2
            continue

        if code[i:i + 4] == "True" and (i + 4 == code_length or not std_isalphanumeric(code[i + 4])):
            tokens.append(("BOOL", "True"))
            i += 4
            continue

        if code[i:i + 5] == "False" and (i + 5 == code_length or not std_isalphanumeric(code[i + 5])):
            tokens.append(("BOOL", "False"))
            i += 5
            continue

        if std_isalpha(code[i]):
            start_i = i
            while i < code_length and (std_isalphanumeric(code[i]) or code[i] == "_"):
                i += 1
            if any(char.isupper() for char in code[start_i:i]):
                print(errors.invalid_variable_name(line + 1, code_lines, code[start_i:i]))
                exit(1)
            tokens.append(("IDENTIFIER", code[start_i:i]))
            continue

        if code[i] == "=":
            tokens.append(("ASSIGN", code[i]))
            i += 1
            continue

        if code[i] in "+-*/":
            tokens.append(("OPERATOR", code[i]))
            i += 1
            continue

        if std_issymb(code[i]):
            tokens.append(("SYMBOL", code[i]))
            i += 1
            continue

        if code[i] == "\n":
            i += 1
            line += 1
            continue

        i += 1

    # for tokenline in tokens:
    #     print(tokenline)
    #     continue
    return tokens

# for token in tokenizer():
#     print(token)
