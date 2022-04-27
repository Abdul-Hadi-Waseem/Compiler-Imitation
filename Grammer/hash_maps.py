# all the operators,delimeters and keyword are till token number 58
# after 58 the new tokens will be issued and appended in the map
from collections import defaultdict

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
    "^": 12,
    "~": 13,
    "=": 14,
    "==": 15,
    "!=": 16,
    "<": 17,
    "<=": 18,
    ">": 19,
    ">=": 20,
}

delimiter_list = {
    "{": 21,
    "}": 22,
    "[": 23,
    "]": 24,
    "(": 25,
    ")": 26,
    ";": 27,
    ",": 28,
}

keywords_map = {
    "False": 29,
    "None": 30,
    "True": 31,
    "and": 32,          #Equivalent to &&
    "as": 33,
    "assert": 34,
    "async": 35,
    "await": 36,
    "yeet": 37,         #Equivalent to break
    "class": 38,
    "continue": 39,
    "def": 40,
    "del": 41,
    "elif": 42,
    "else": 43,
    "except": 44,
    "finally": 45,
    "for": 46,
    "from": 47,
    "global": 48,
    "if": 49,
    "import": 50,
    "in": 51,
    "is": 52,
    "lambda": 53,
    "nonlocal": 54,
    "not": 55,
    "or": 56,          #Equivalent to ||
    "pass": 57,
    "raise": 58,
    "return": 59,
    "shout": 60,
    "try": 61,
    "loop": 62,        #Equivalent to while
    "using": 63,       #Equivalent to with
    "yield": 64,
    "int": 65,
    "float": 66,
    "boolean": 67,
    "string": 68,
    "until": 69,
    "NL": 70,     #Equivalent to newline
    "sheesh": 71      #Equivalent to exit
}

identifier_list = defaultdict(lambda: "NULL")