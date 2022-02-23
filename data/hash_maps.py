# all the operators,delimeters and keyword are till token number 58
# after 58 the new tokens will be issued and appended in the map
from collections import defaultdict

operator_list = {
    "+": 1,
    "-": 2,
    "*": 3,
    "/": 4,
    "%": 5,
    "&&": 6,
    "||": 7,
    "^": 8,
    "~": 9,
    "=": 10,
    "==": 11,
    "!=": 12,
    "<": 13,
    "<=": 14,
    ">": 15,
    ">=": 16,
}

delimiter_list = {
    "{": 17,
    "}": 18,
    "[": 19,
    "]": 20,
    "(": 21,
    ")": 22,
    ";": 23,
    ",": 24,
}

keywords_map = {
    "False": 25,
    "None": 26,
    "True": 27,
    "and": 28,
    "as": 29,
    "assert": 30,
    "async": 31,
    "await": 32,
    "break": 33,
    "class": 34,
    "continue": 35,
    "def": 36,
    "del": 37,
    "elif": 38,
    "else": 39,
    "except": 40,
    "finally": 41,
    "for": 42,
    "from": 43,
    "global": 44,
    "if": 45,
    "import": 46,
    "in": 47,
    "is": 48,
    "lambda": 49,
    "nonlocal": 50,
    "not": 51,
    "or": 52,
    "pass": 53,
    "raise": 54,
    "return": 55,
    "try": 56,
    "while": 57,
    "with": 58,
    "yield": 59,
    "------": 60,
}

identifier_list = defaultdict(lambda:"NULL")