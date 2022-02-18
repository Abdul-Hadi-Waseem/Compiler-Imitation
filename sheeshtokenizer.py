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
    
    if (i[0] == "0"):
      if(len(i) == 1):
          flag = True
      else:
          flag = False
    
    elif (i[0] in "123456789"):
      for number in i[1:]:
         if number.isdigit():
           flag = True
         else:
            return False
    
    elif (i[0] == "+" or i[0] == "-"):
      for number in i[1:]:
         if (number.isdigit() and i[1] != 0):
           flag = True
         else:
            return False
    
    else:
        return False
      
    return flag

#testcases
#print(is_integer_literal("0"))
#print(is_integer_literal("112"))
#print(is_integer_literal("akkq"))
#print(is_integer_literal("-123"))

def is_float_literal(f):
    """

    f[0] can be + or - or any non zero digit follwed by a sequence of digits , "." and any sequence of digits   
    f[0] can be zero , if so then in that case nothing else should come after

    """
    flag = False
    decimal_count = 0
    
    if (f[0] == "0"):
      if(len(f) == 1):
          flag = True
      else:
          flag = False
    
    elif (f[0] in "123456789"):
      for decimal in f[1:]:
          if (decimal == "."):
            decimal_count =+ 1
      for number in f[1:]:
         if ((number.isdigit() or number == ".") and (decimal_count == 1)):
           flag = True
         else:
            return False

    elif ((f[0] == "+" or f[0] == "-") and (f[1] in "123456789")):
        for decimal in f[2:]:
          if (decimal == "." ):
            decimal_count =+ 1
        for number in f[1:]:
         if ((number.isdigit() or number == ".") and (decimal_count == 1)):
           flag = True
         else:
            return False
    
    else:
        return False
      
    return flag

#testcases
#print(is_float_literal("0"))
#print(is_float_literal("123"))
#print(is_float_literal("-123.45"))
#print(is_float_literal("-123...45"))
#print(is_float_literal("-123.045"))
#print(is_float_literal("-0123.45"))
#print(is_float_literal("123.45"))
#print(is_float_literal("123...45"))


def is_string_literal():
    pass

