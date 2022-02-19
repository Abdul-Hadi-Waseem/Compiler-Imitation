import os

# 1. add comment feature

def progress_meter(curr, tot):
    print(f"Progress : {round(curr*100/tot, 2)}%", end="\r")

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
    
    with open(file_path, "r") as f:
        # file_handle = f.read()

        f.seek(0)
        lexeme_list = []
        lexeme_buffer = ""
        cnt = 0
        quote_flag = False
        while True:
            cnt+=1
            # time.sleep(0.001)
            progress_meter(cnt, file_size)
            curr_char = f.read(1)
            if not curr_char:           #Checking EOF
                break

            if curr_char=="\n":         #Increment line count
                line_count+=1

            if quote_flag and curr_char != "\"":
                lexeme_buffer += curr_char

            if not (curr_char.isdigit() or curr_char.lower().isalpha() or curr_char == "_"):        #Delimiter check
                if not lexeme_buffer=="":                                              #Prevent empty symbols
                    lexeme_list.append([line_count, lexeme_buffer])

                if curr_char == "\"":
                    if not quote_flag:
                        quote_flag = True
                    else:
                        quote_flag = False
                    continue

                if curr_char in "<>!=":                                                #Support for <= != == >=
                    temp = f.tell()
                    if f.read(1) == "=":
                        lexeme_buffer = curr_char+"="
                        lexeme_list.append([line_count, lexeme_buffer])
                        lexeme_buffer = ""
                        continue
                    f.seek(temp)
                if curr_char in " \n":                                                 #New line and space are proper delimiters
                    lexeme_buffer = ""
                    continue
                lexeme_list.append([line_count, curr_char])
                lexeme_buffer = ""
                continue
            lexeme_buffer+=curr_char
            
    print("Lexeme seperation successful.")
    return lexeme_list

if __name__ == "__main__":
    lexeme_list = (lexicar("sheeshfile.txt"))
    for lexeme in lexeme_list:
        print(f"{lexeme[0]} : {lexeme[1]}")
        # print(lexeme[1], end=" ")