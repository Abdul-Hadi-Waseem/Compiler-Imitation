from hash_maps import keywords_map, identifier_list, operator_list, delimiter_list
from tokenizer_utils import is_valid_token


def token_info(token):
    """
    NOTE: the token needs to be a valid token
    args: token [string]
    """
    try:
        if keywords_map[token]==60:
            return keywords_map[token],"new line"
        # if the token is available in the tokenmap then return its value
        return keywords_map[token], "keyword"
    except:
        # if the token is not available in the token map,
        # add it to the token map and append to the tokenmap and return it
        identifier_list[token] = (
            len(operator_list)
            + len(delimiter_list)
            + len(keywords_map)
            + len(identifier_list)
            + 1
        )
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
    temp_lexeme_list = []
    for linenum, lexeme in lexeme_list:
        operator_value = operator_val(lexeme)
        delimeter_value = delimeter_val(lexeme)
        if operator_value:
            temp_lexeme_list.append([linenum, lexeme, operator_value, "operator"])
            continue
        elif delimeter_value:
            temp_lexeme_list.append([linenum, lexeme, delimeter_value, "delimeter"])
            continue
        if not (delimeter_value or operator_value):
            token_value, token_category = token_info(lexeme)
            # print(f"Op Val : {operator_value}, del val: {delimeter_value}, token val: {token_value}, token category:{token_category}")
            # if (
            #     # not is_valid_token(lexeme) and 
            #     token_category!="new line"):
            #     temp_lexeme_list.append([linenum, lexeme, "err", "invalid"])
            #     continue
            temp_lexeme_list.append([linenum, lexeme, token_value, token_category])
    return temp_lexeme_list


# print("{")
# for num,i in enumerate(identifier_list,60):
#     print(f"\"{i}\":{num},")
# print("}")
