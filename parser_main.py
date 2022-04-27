import lexer_main
from utils.openfile import extract_table, extract_cfg
from utils.logger import Logger

logger = Logger('./Logs/stack_logger.log')

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
        token_list.append(lexeme[1])
    token_list.pop(0)
    return token_list
    
def top_down_parser(lexeme_list):
    """
    Args: lexeme_list [list] list of lexemes
    returns: 
    """
    token_list = token_list_generator(lexeme_list)
    parse_table = extract_table("Grammer/parser_LALR1_table.tsv")
    cfg = extract_cfg("Grammer/Sheesh_CFG.txt")
    stack = []
    stack.append('$')
    stack.append('0')
    logger.append(stack[::-1])
    # print(top(stack))
    accept_flag = False

    while(not accept_flag):
        if (top(stack).isdigit()):
            row = top(stack)
            col = token_list.pop(0)
        else:
            row = top(stack, 2)
            col = top(stack)

            
        print(f"ROW: {row}, COL: {col}")
        print(f"Parse Table entry: {parse_table[int(row)][col]}")
        temp = parse_table[13]['ARRAY']
        if temp.lower()=='s':
            print("Shift")
        if temp.lower()=='r':
            print("Reduce")

        

        # print(parse_table[int(stack[-1]), :])
        accept_flag = True
        pass
            

    

if __name__ == "__main__":
    lexeme_list = lexer_main.lexermain()
    # lexeme_list = []
    top_down_parser(lexeme_list)