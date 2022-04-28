# all the operators,delimeters and keyword are till token number 58
# after 58 the new tokens will be issued and appended in the map
from collections import defaultdict

# Removed = and ~ from the list
operator_list = {
    "+": 1,
    "-": 2,
    "*": 3,
    "/": 4,
    "%": 5,
    "and": 6,
    "or": 7,
    "not": 8,
    "?": 9,
    ":": 10,
    "^": 11,
    "=": 12,
    "==": 13,
    "!=": 14,
    "<": 15,
    "<=": 16,
    ">": 17,
    ">=": 18,
}

delimiter_list = {
    "{": 19,
    "}": 20,
    "[": 21,
    "]": 22,
    "(": 23,
    ")": 24,
    ";": 25,
    ",": 26,
}

keywords_map = {
    "False": 27,
    "None": 28,
    "True": 29,
    "and": 30,
    "as": 31,
    "assert": 32,
    "async": 33,
    "await": 34,
    "yeet": 35,  # Equivalent to break
    "class": 36,
    "continue": 37,
    "def": 38,
    "del": 39,
    "elif": 40,
    "else": 41,
    "except": 42,
    "finally": 43,
    "for": 44,
    "from": 45,
    "global": 46,
    "if": 47,
    "import": 48,
    "in": 49,
    "is": 50,
    "lambda": 51,
    "nonlocal": 52,
    "not": 53,
    "or": 54,
    "pass": 55,
    "raise": 56,
    "return": 57,
    "shout": 58,
    "try": 59,
    "loop": 60,  # Equivalent to while
    "using": 61,  # Equivalent to with
    "yield": 62,
    "int": 63,
    "float": 64,
    "boolean": 65,
    "string": 66,
    "until": 67,
    "NL": 68,  # Equivalent to newline
    "sheesh": 69,  # Equivalent to exit
    "main": 70,
    "void": 71,
}

identifier_list = defaultdict(lambda: "NULL")
