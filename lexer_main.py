import os
import time
from matplotlib.pyplot import table
from terminaltables import AsciiTable

from openfile import openSheeshfile, getFileSize
from tokenizing import keywords_map, delimeter_val, operator_val, addTokenVal


def lexicar(file_path):
    """
    Reads a file, generates lexeme list, returns it
    """

    f = openSheeshfile(file_path)

    line_count = 1
    file_size = getFileSize(file_path)
    f.seek(0)
    lexeme_list = []
    lexeme_buffer = ""
    cnt = 0
    quote_flag = False
    cumment_flag = False
    while True:
        cnt += 1
        # time.sleep(0.001)

        print("\rProgress : {0}%".format(round(cnt * 100 / file_size, 2)), end="\r")

        # progress_meter(cnt, file_size)
        curr_char = f.read(1)

        # KEEP THIS AT TOP. COMPATIBILITY THING.
        if not curr_char:  # Checking EOF
            break

        if curr_char == "\n":  # Increment line count
            line_count += 1

        # SUPPORT FOR QUOTES
        if curr_char == '"':
            lexeme_buffer += curr_char
            if not quote_flag:
                quote_flag = True
            else:
                quote_flag = False
            continue

        # COMMENT SUPPORT
        if curr_char == "#":
            f.readline()
            line_count += 1
            continue

        if not (
            curr_char.isdigit()
            or curr_char.lower().isalpha()
            or curr_char in "_"
            or quote_flag
        ):  # Delimiter check
            if not lexeme_buffer == "":  # Prevent empty symbols
                lexeme_list.append(
                    [line_count, lexeme_buffer]
                )  # Appends whatever is in the buffer
            if curr_char in "<>!=":  # Support for <= != == >=
                temp = f.tell()
                if f.read(1) == "=":
                    lexeme_buffer = curr_char + "="
                    lexeme_list.append([line_count, lexeme_buffer])
                    lexeme_buffer = ""
                    continue
                f.seek(temp)

            # space is proper delimiter, so its not appended in lexeme list like other delimiters
            if curr_char == " ":
                lexeme_buffer = ""
                continue

            if curr_char == "\n":  # new line check
                lexeme_list.append([line_count, "------"])
                lexeme_buffer = ""
                continue

            lexeme_list.append([line_count, curr_char])  # Appends the actual delimiter
            lexeme_buffer = ""
            continue

        lexeme_buffer += curr_char
    f.close()

    if not lexeme_buffer == "":  # append if anything still left in the lexeme_buffer
        lexeme_list.append([line_count, lexeme_buffer])
    print("Lexeme seperation successful.")
    lexeme_list = addTokenVal(lexeme_list)
    print(lexeme_list)
    return lexeme_list


if __name__ == "__main__":
    lexeme_list = lexicar("sheeshfile.txt")
    # lexeme_list = [[str(i) for i in j] for j in lexeme_list]
    lexeme_list = [["Token line", "Token", "Token value"]] + lexeme_list
    lexeme_list_table = AsciiTable(lexeme_list)
    print(lexeme_list_table.table)
