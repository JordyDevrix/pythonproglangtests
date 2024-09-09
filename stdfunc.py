
def std_issymb(char: str) -> bool:
    char_list = r"{}()[];,."
    if char in char_list:
        return True
    else:
        return False


def std_isnumeric(char: str) -> bool:
    char_list = r"1234567890"
    if char in char_list:
        return True
    else:
        return False


def std_isalpha(char: str) -> bool:
    char_list_lower = r"abcdefghijklmnopqrstuvwxyz"
    char_list_upper = char_list_lower.upper()
    if char in char_list_lower or char in char_list_upper:
        return True
    else:
        return False


def std_isalphanumeric(char: str) -> bool:
    char_list_lower = r"abcdefghijklmnopqrstuvwxyz"
    char_list_upper = char_list_lower.upper()
    char_list = r"1234567890"
    if (char in char_list_lower) or (char in char_list_upper) or (char in char_list):
        return True
    else:
        return False

