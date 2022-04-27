import lexer_main
from utils.openfile import extract_data

def top_down_parser(lexeme_list):
    """
    Args: lexeme_list [list] list of lexemes
    returns: 
    """
    table = extract_data("./Grammer/test.tsv")
    print(table.shape)


if __name__ == "__main__":
    lexeme_list = lexer_main.lexermain()
    top_down_parser(lexeme_list)