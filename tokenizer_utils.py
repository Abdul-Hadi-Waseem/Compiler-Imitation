

def is_identifier(s):
    """
    Args: s [string] to be evaluated as a identifier

    returns True if it is a valid identifier, False if not 
    """

    # s[0] should be in a-z or A-Z
    # s[1:] should be a-z or A-Z or 0-9 or _ (underscore)
    
    flag = False
    if s[0].lower().isalpha():
        for char in s[1:]:
            if char.isdigit() or char.lower().isalpha() or char == "_":
                flag = True
            else:
                return False
    else:
        return False

    return flag

#testcases
# print(is_identifier("sheesh"))
# print(is_identifier("1sheesh_"))
# print(is_identifier("_sheesh_"))
# print(is_identifier("sheesh__"))
# print(is_identifier("sheesh11_-"))
# print(is_identifier("sheesh11_!@"))



def is_integer_literal(i):
    """
    Args: s [string] to be evaluated as a identifier
    i[0] can be + or - or any non zero digit followed by sequence of digits
    i[0] can be zero , if so then no digit should come after
    returns True if it is a valid identifier, False if not

    """
    flag = False
    if len(i) == 0:
        return False # empty string

    #base case of 0
    if i[0] == "0":
        if len(i)>1:
            return False
        if len(i)==1:
            return True
    elif i[0].isdigit():
        if all([a.isdigit() for a in i[1:]]):
            flag = True
        else:
            return False 
    elif i[0] in "+-":
        if i[1] != "0" and all([a.isdigit() for a in i[2:]]):
            flag = True
        else:
            return False
    else:
        return False

    return flag 

# #testcases
# print(is_integer_literal("0"))
# print(is_integer_literal("112"))
# print(is_integer_literal("ak12q"))
# print(is_integer_literal("-123"))
# print(is_integer_literal("+123"))
# print(is_integer_literal("-03"))
# print(is_integer_literal("03"))
# print(is_integer_literal("-123a"))
# print(is_integer_literal("-0"))
# print(is_integer_literal("+0"))


def is_float_literal(f):
 
  flag = False
    
  float_list = f.split(".")
  if (len(float_list) == 2):
        start, end = float_list
        if is_integer_literal(start) and end.isdigit():
          flag = True 
      
  return flag

#testcases
# print(is_float_literal("0"))
# print(is_float_literal("123"))
# print(is_float_literal("-123.45"))
# print(is_float_literal("-123...45"))
# print(is_float_literal("-123.045"))
# print(is_float_literal("-0123.45"))
# print(is_float_literal("123.45"))
# print(is_float_literal("123...45"))
# print(is_float_literal("13..1..24.5"))
# print(is_float_literal("+0"))
# print(is_float_literal("1.12.33.1.33.24.5"))
# print(is_float_literal("0.0"))



def is_string_literal(s):
    
    """
    Args: s [string] to be evaluated as a valid string literal
    
    start and end character should be a double quote (")
    no newlines, carriage returns, or backslashes allowed
    """
    flag = False
    
    if s[0]=="\"" and s[-1] == "\"":
        #check inside
        for index, char in enumerate(s[1:-1]):
            if char == "\\": 
                if s[index+1+1] in "nrtb":     #escape sequences ? 
                    flag = True
                else:
                    return False #?
            #other than /, it could be anything?
    else:
        return False

    return flag 

print(is_string_literal("\"sheesh\""))
print(is_string_literal("\" \""))
print(is_string_literal("\" \""))
print(is_string_literal("\" \""))
print(is_string_literal("\" \""))
print(is_string_literal("\" \""))
print(is_string_literal("\" \""))
print(is_string_literal("\" \""))
print(is_string_literal("\" \""))

def is_operator(o, operator_list):
    
    """

    """

    return o in operator_list

def is_delimiter(d, delimeter_list):
    """
    
    """
    return d in delimeter_list

#Syntax Specifications Remaining

#for
#while
#if else
#boolean
#All the keywords



