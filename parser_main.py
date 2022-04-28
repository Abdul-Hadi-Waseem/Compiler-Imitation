import lexer_main
from utils.openfile import extract_table, extract_cfg
from utils.logger import Logger

logger = Logger('./Logs/stack_logger.log')
TABLE_LOC = "Grammer/parser_LALR1_table.tsv"
CFG_LOC = "Grammer/Sheesh_CFG.txt"

def top(stack, n=1):
    '''
    Args: stack [list] list of strings
    returns: string
    '''
    return stack[-n]

def token_list_generator(lexeme_list):
    """
    Args: lexeme_list [list] list of lexemes
    returns: 
    """
    token_list = []
    for lexeme in lexeme_list:
        col = lexeme[1]
        #Gotta replace variables with their token types
        if lexeme[3] == 'identifier':
            col_attr = col                  
            token_list.append('ID')
            continue              
        if lexeme[3] == 'string_lit':
            col_attr = col                  
            token_list.append('STRING_LITERAL')            
            continue
        if lexeme[3] == 'float_lit':
            col_attr = col                  
            token_list.append('FLOAT_LITERAL')            
            continue
        if lexeme[3] == 'integer_lit':
            col_attr = col                  
            token_list.append('INTEGER_LITERAL')                      
            continue
        token_list.append(lexeme[1])
    token_list.pop(0)
    return token_list
    
def top_down_parser(lexeme_list):
    """
    Args: lexeme_list [list] list of lexemes
    returns: 
    """
    #Extracting tokens from lexeme list
    token_list = token_list_generator(lexeme_list)
    token_list.append('$')

    #Extracting table and cfg from respective files
    parse_table = extract_table(TABLE_LOC)
    cfg = extract_cfg(CFG_LOC)

    #Initializing stack
    stack = []
    stack.append('0')

    logger.append(stack[::-1])
    accept_flag = False

    while(not accept_flag):
        if (top(stack).isdigit()):
            # SHIFT CASE
            row = top(stack)
            curr_lexeme = token_list[0]
            col = curr_lexeme                      #Coz col cannot be a variable name
        else:
            # REDUCE CASE
            row = top(stack, 2)
            col = top(stack)
            print(f"row col after reduce case: ({row},{col})")
            
            stack.append(parse_table[int(row)][col])
            
            logger.append(stack[::-1])
            
            continue
            
            
        print(f"ROW: {row}, COL: {col}")
        print(f"Parse Table entry: {parse_table[int(row)][col]}")
        # temp = parse_table[13]['ARRAY']
        temp = parse_table[int(row)][col]
        if not temp.strip():
            print("Eror aaya :(")
            exit()

        if temp=="acc":
            accept_flag = True
            continue
            # break
        
        if temp.isdigit():
            
            continue
        action = temp[0]
        action_num = temp[1:]
        
        print(temp)
        if action=='s':
            if (len(token_list)==0):
                print("Smthin wrong.")
                exit()
            print("Shift")
            action_num = int(action_num)
            curr_token = token_list.pop(0)
            stack.append(curr_token)
            str_action_num = str(action_num)
            stack.append(str_action_num)

            logger.append(stack[::-1])

            continue     
            
        if action=='r':
            print("Reduce")
            action_num = int(action_num)
            # print("cfg[action_num].split(" ")[1] : ",cfg[action_num].split("->")[1])
            print(cfg[action_num].split("->")[1].strip().split(" "))
            numpopper = len(cfg[action_num].split("->")[1].strip().split(" "))
            print("numpopper : ",numpopper)
            for i in range(numpopper):
                stack.pop()
                stack.pop()
            
            stack.append(cfg[action_num].split("->")[0].strip())
            # stack.append(str(action_num))

            logger.append(stack[::-1])

            continue     
      
        # # print(parse_table[int(stack[-1]), :])
        # # accept_flag = True
        # pass
            

    

if __name__ == "__main__":
    lexeme_list = lexer_main.lexermain()
    # lexeme_list = []
    top_down_parser(lexeme_list)