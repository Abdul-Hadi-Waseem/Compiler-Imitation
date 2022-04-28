import lexer_main
import sys
from utils.openfile import extract_table, extract_cfg
from utils.logger import Logger
from utils.inputLogger import InputLogger
from SDT_SDD.intermediate_code_gen import intermediate_code_generator
import time

stack_logger = Logger("./Logs/stack_logger.log")
err_logger = Logger("./Logs/err_logger.log")
iptokens = InputLogger("./Logs/iptokens.log")

TABLE_LOC = "Grammer/parser_LALR1_table.tsv"
CFG_LOC = "Grammer/Sheesh_CFG.txt"


def top(stack, n=1):
    """
    Args: stack [list] list of strings
    returns: string
    """
    return stack[-n]


def token_list_generator(lexeme_list):
    """
    Args: lexeme_list [list] list of lexemes
    returns:
    """
    token_list = []
    for lexeme in lexeme_list:
        col = lexeme[1]
        tok = col
        # Gotta replace variables with their token types
        if lexeme[3] == "identifier":
            col_attr = col
            tok = "ID"
        if lexeme[3] == "string_lit":
            col_attr = col
            tok = "STRING_LITERAL"
        if lexeme[3] == "float_lit":
            col_attr = col
            tok = "FLOAT_LITERAL"
        if lexeme[3] == "integer_lit":
            col_attr = col
            tok = "INTEGER_LITERAL"
        token_list.append((tok, lexeme[0]))
    token_list.pop(0)
    return token_list


def print_tokens(token_list):
    print("TOKENS:", end=" ")
    for token in token_list:
        print(token[0], end=" ")
    print()


def top_down_parser(lexeme_list):
    """
    Args: lexeme_list [list] list of lexemes
    returns:
    """
    # Extracting tokens from lexeme list
    token_list = token_list_generator(lexeme_list)
    token_list.append(("$", None))
    # print(f"TOKENS: {token_list}")

    # print_tokens(token_list)

    # Extracting table and cfg from respective files
    parse_table = extract_table(TABLE_LOC)
    cfg = extract_cfg(CFG_LOC)

    # Initializing stack
    stack = []
    stack.append("0")

    stack_logger.append(stack[::-1])
    iptokens.append(token_list)

    accept_flag = False
    isError = False
    curr_lexeme = None
    prev_token1 = None
    prev_token2 = None
    curr_row = None
    prev_row1 = None
    prev_row2 = None
    errcnt = 0
    token_list_size = len(token_list)
    while not accept_flag:
        time.sleep(0.01)
        print(
            "\rProgress : {0}%".format(
                round((token_list_size - (len(token_list)-1)) * 100 / token_list_size, 2)
            ),
            end="\r",
        )

        # print("\n")
        if top(stack).isdigit():
            row = top(stack)
            if isError:
                curr_lexeme = token_list[0][0]
                curr_row = token_list[0][1]
                # print(curr_lexeme)
                isError = False
                continue
            # else:
            # if prev_token == curr_lexeme:
            curr_lexeme = token_list[0][0]
            curr_row = token_list[0][1]
            if prev_token1 != curr_lexeme:
                prev_token2 = prev_token1
                prev_row2 = prev_row1
            prev_token1 = curr_lexeme
            prev_row1 = curr_row
            col = curr_lexeme
        else:
            row = top(stack, 2)
            col = top(stack)
            # print(f"row col after reduce case: ({row},{col})")
            stack.append(parse_table[int(row)][col])
            stack_logger.append(stack[::-1])
            iptokens.append(token_list)
            continue

        # print(f"Parse Table[{row}]['{col}'] entry: {parse_table[int(row)][col]}")
        # temp = parse_table[13]['ARRAY']
        temp = parse_table[int(row)][col]
        if not temp.strip():
            errcnt += 1
            # print("Error Handling Panic Mode :=>")
            isError = True
            stack.pop()
            stack.pop()
            token_list.pop(0)

            # curr_lexeme = token_list[1]

            stack_logger.append(stack[::-1])
            iptokens.append(token_list)
            err_logger.append(f"Error {errcnt}: {prev_token2} , Line : {prev_row2-1}")

            continue

        if temp == "acc":
            accept_flag = True
            continue
            # break

        if temp.isdigit():
            continue

        action = temp[0]
        action_num = temp[1:]

        if action == "s":
            if len(token_list) == 0:
                print("Smthin wrong.")
                exit()
            # print("Shift")
            action_num = int(action_num)
            curr_token = token_list.pop(0)[0]
            stack.append(curr_token)
            str_action_num = str(action_num)
            stack.append(str_action_num)

            stack_logger.append(stack[::-1])
            iptokens.append(token_list)

            continue

        if action == "r":
            # print("Reduce")
            action_num = int(action_num)
            # print(cfg[action_num].split("->")[1].strip().split(" "))
            numpopper = len(cfg[action_num].split("->")[1].strip().split(" "))
            if cfg[action_num].split("->")[1].strip() == "''":
                numpopper = 0
            # print("numpopper : ", numpopper)
            # print("Reducing by production rule : ", cfg[action_num])
            for i in range(numpopper):
                stack.pop()
                stack.pop()

            stack.append(cfg[action_num].split("->")[0].strip())
            stack_logger.append(stack[::-1])
            iptokens.append(token_list)

            # print(stack)
            continue


if __name__ == "__main__":
    # Getting filename from command arguments
    try:
        filename = sys.argv[1]  # Takes filename from the terminal
    except:
        filename = "./default.sheesh"  # filename here if not from terminal

    lexeme_list = lexer_main.lexermain(filename)
    errtok = False
    for a, b, c, inv in lexeme_list:
        if str(inv) == "invalid":
            print(inv)
            errtok = True

    if errtok:
        print("Invalid token exists in the program. Unable to parse!")
        print("\n\n", "-" * 60, "DONE", "-" * 60)
        sys.exit(4)

    # lexeme_list = []
    print("\n\nParsing Starting...")
    top_down_parser(lexeme_list)
    intermediate_code_generator(filename)
    print("\n\n", "-" * 60, "DONE", "-" * 60)
