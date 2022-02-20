# all the operators,delimeters and keyword are till token number 58
# after 58 the new tokens will be issued and appended in the map


operator_list = {
    "+": 0,
    "-": 1,
    "*": 2,
    "/": 3,
    "%": 4,
    "&&": 5,
    "||": 6,
    "^": 7,
    "~": 8,
    "=": 9,
    "==": 10,
    "!=": 11,
    "<": 12,
    "<=": 13,
    ">": 14,
    ">=": 15,
}

delimiter_list = {
    "{": 16,
    "}": 17,
    "[": 18,
    "]": 19,
    "(": 20,
    ")": 21,
    ";": 22,
    ",": 23,
}

keywords_map = {
    "False": 24,
    "None": 25,
    "True": 26,
    "and": 27,
    "as": 28,
    "assert": 29,
    "async": 30,
    "await": 31,
    "break": 32,
    "class": 33,
    "continue": 34,
    "def": 35,
    "del": 36,
    "elif": 37,
    "else": 38,
    "except": 39,
    "finally": 40,
    "for": 41,
    "from": 42,
    "global": 43,
    "if": 44,
    "import": 45,
    "in": 46,
    "is": 47,
    "lambda": 48,
    "nonlocal": 49,
    "not": 50,
    "or": 51,
    "pass": 52,
    "raise": 53,
    "return": 54,
    "try": 55,
    "while": 56,
    "with": 57,
    "yield": 58,
}

identifier_list= {
    "------":59
}
