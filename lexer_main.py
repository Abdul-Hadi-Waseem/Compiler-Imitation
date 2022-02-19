import os
import time
from matplotlib.pyplot import table 
import test
from openfile import openSheeshfile
from tokenizing import keywords_map,delimeter_val,operator_val,addTokenVal
from terminaltables import AsciiTable

def lexicar(file_path):
    """
    Reads a file, generates lexeme list, returns it
    """
    #check if file exists
    if not os.path.exists(file_path):
        print("ERR: File does not exists")
        return []

    line_count = 1
    file_size = os.path.getsize(file_path)
    
    f = openSheeshfile(file_path)
    # file_handle = f.read()

    f.seek(0)
    lexeme_list = []
    lexeme_buffer = ""
    cnt = 0
    quote_flag = False
    cumment_flag = False
    while True:
        cnt+=1
        # time.sleep(0.001)
        
        # print("\rProgress : {0}%".format(round(cnt*100/file_size, 2)), end="\r")
        
        # progress_meter(cnt, file_size)
        curr_char = f.read(1)
        
        #KEEP THIS AT TOP. COMPATIBILITY THING.
        if not curr_char:           #Checking EOF
            break

        if curr_char=="\n":         #Increment line count
            line_count+=1


        #SUPPORT FOR QUOTES
        if curr_char == "\"":
            lexeme_buffer += curr_char
            if not quote_flag:
                quote_flag = True
            else:
                quote_flag = False
            continue


        #COMMENT SUPPORT
        if curr_char == "#":
            cumment_flag = True
            continue
        if cumment_flag:
            if curr_char == "\n":
                cumment_flag = False
            continue


        if not (curr_char.isdigit() or curr_char.lower().isalpha() or curr_char in "_" or quote_flag):        #Delimiter check
            if not lexeme_buffer=="":                                              #Prevent empty symbols
                lexeme_list.append([line_count, lexeme_buffer])                    #Appends whatever is in the buffer

            if curr_char in "<>!=":                                                #Support for <= != == >=
                temp = f.tell()
                if f.read(1) == "=":
                    lexeme_buffer = curr_char+"="
                    print(f"HELLO {lexeme_buffer}")
                    lexeme_list.append([line_count, lexeme_buffer])
                    lexeme_buffer = ""
                    continue                                                      #WARNING: DON'T COMMENT OUT THIS LINE
                f.seek(temp)
            
            #space is proper delimiter, so its not appended in lexeme list like other delimiters
            if curr_char == " ":                                                  
                lexeme_buffer = ""
                continue
            
            #NOTE: chutiyappppp. Please re-write for your own sanity
            if curr_char == "\n":                                                 #new line check 
                # temp = f.tell()
                # if f.read(1) == "\n":
                #     lexeme_buffer = ""
                #     continue

                if lexeme_buffer == "":
                    # f.read(1)
                    continue
                # lexeme_list.append([line_count, lexeme_buffer])
                lexeme_list.append([line_count, "------"])
                lexeme_buffer = ""
                continue

            lexeme_list.append([line_count, curr_char])                          #Appends the actual delimiter
            lexeme_buffer = ""
            continue

        lexeme_buffer+=curr_char
            
    print("Lexeme seperation successful.")
    f.close()
    lexeme_list = addTokenVal(lexeme_list)
    return lexeme_list

if __name__ == "__main__":
    lexeme_list = (lexicar("sheeshfile.txt"))
    # lexeme_list = [[str(i) for i in j] for j in lexeme_list]
    lexeme_list = [["Token line", "Token", "Token value"]]+lexeme_list
    lexeme_list_table = AsciiTable(lexeme_list)
    print(lexeme_list_table.table)
