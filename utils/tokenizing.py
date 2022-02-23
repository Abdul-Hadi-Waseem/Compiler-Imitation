import sys, os

sys.path.append(os.path.abspath(os.path.join("..")))

from data.hash_maps import keywords_map, identifier_list, operator_list, delimiter_list
from collections import defaultdict
from utils.tokenizer_utils import (
    is_valid_token,
    is_string_literal,
    is_integer_literal,
    is_float_literal,
)
from colorclass import Color, Windows


total_keywords = len(operator_list) + len(delimiter_list) + len(keywords_map)


def token_info(token):
    """
    NOTE: the token needs to be a valid token
    args: token [string]
    """
    try:
        token_value = keywords_map[token]
        if token == "------":
            return token_value, "new line"
        # if the token is available in the tokenmap then return its value
        return token_value, "keyword"
    except:
        # if the token is not available in the token map,
        # add it to the token map and append to the tokenmap and return it
        if identifier_list[token] == "NULL":
            identifier_list[token] = total_keywords + len(identifier_list)
        else:
            pass
        if is_string_literal(token):
            return identifier_list[token], "string_lit"
        if is_float_literal(token):
            return identifier_list[token], "float_lit"
        if is_integer_literal(token):
            return identifier_list[token], "integer_lit"

        return identifier_list[token], "identifier"


def operator_val(token):
    """
    NOTE: the token needs to be a valid token
    args: token [string]
    """
    try:
        # if the token is available in the tokenmap then return its value
        return operator_list[token]
    except:
        return False


def delimeter_val(token):
    """
    NOTE: the token needs to be a valid token
    args: token [string]
    """
    try:
        # if the token is available in the tokenmap then return its value
        return delimiter_list[token]
    except:
        return False


def addTokenVal(lexeme_list):
    """
    args: lexeme_list [list] list of the tokens
    returns temp_lexeme_list [list] list with updated token number and category
    """
    temp_lexeme_list = []
    for linenum, lexeme in lexeme_list:
        operator_value = operator_val(lexeme)
        delimeter_value = delimeter_val(lexeme)
        if operator_value:
            temp_lexeme_list.append([linenum, lexeme, operator_value, "operator"])
            continue
        elif delimeter_value:
            temp_lexeme_list.append(
                [linenum, lexeme, delimeter_value, Color("delimeter")]
            )
            continue
        if not (delimeter_value or operator_value):
            if is_valid_token(lexeme) or lexeme == "------":
                token_value, token_category = token_info(lexeme)
                # print(f"Op Val : {operator_value}, del val: {delimeter_value}, token val: {token_value}, token category:{token_category}")
                temp_lexeme_list.append([linenum, lexeme, token_value, token_category])
                continue
            else:  # invalid token is added as err and invalid with red colour
                temp_lexeme_list.append(
                    [
                        linenum,
                        lexeme,
                        Color("{red}err{/red}"),
                        Color("{red}invalid{/red}"),
                    ]
                )
    return temp_lexeme_list


# print("{")
# for num,i in enumerate(keywords_map,29):
#     print(f"\"{i}\":{num},")
# print("}")
