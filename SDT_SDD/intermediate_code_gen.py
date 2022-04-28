import sys
from utils.openfile import openSheeshfile

listt = []
operator_set = set(['+', '-', '*', '/', '(', ')', '^'])  
priority_map = {'+':1, '-':1, '*':2, '/':2, '^':3} 

def ass(equation, print_flag):
   res=equation[0]
   x=arith(equation[2:], print_flag)
   listt.append(equation[0:2]+'R'+str(x))
   res = []
   [res.append(x) for x in listt if x not in res]
   if print_flag ==1:
       print('\t',equation[0:2],'R'+str(x), "\n")
   return res 

def infix_to_postfix(expression): 
    stack = [] 
    opt = ''
    for char in expression:
        if char==")":
            while stack and stack[-1]!= '(':
                opt+=stack.pop()
            stack.pop()
        elif char=='(':  
            stack.append('(')
        elif char not in operator_set:
            opt += char
        else: 
            cond1 = stack and stack[-1]!='('
            cond2 = stack and priority_map[char]<=priority_map[stack[-1]]
            while cond1 and cond2:
                opt+=stack.pop()
                cond1 = stack and stack[-1]!='('
                cond2 = stack and priority_map[char]<=priority_map[stack[-1]]
            stack.append(char)

    while stack:
        opt = opt + stack.pop()
    return opt


def arith(equation, print_flag): #arithmetic
    postfix=infix_to_postfix(equation)
    operators=('+','-','*','/','^')
    if print_flag == 1:
        print("Postfix expression is: ",postfix)
    st=[]
    r_count=1
    if print_flag == 1:   
        print("Three address code is: ") 
    for i in postfix:
        if i not in operators:
            st.append(i)
        else:
            a=st.pop(-1)
            b=st.pop(-1)
            listt.append('R'+str(r_count)+'='+a+i+b+",")
            if print_flag == 1:
                print('\tR'+str(r_count)+'='+a+i+b)
            r_count+=1
            st.append('R'+str(r_count-1))
    return r_count-1

def relt(equation , stmnts, line_number): #relational
    res = ""
    for i in stmnts:
            res = res+ i
    r_count=100+line_number
    t=0
    sts={}
    sts_=["if "+equation+" goto "+str(r_count+3), "T:= "+str(t), " goto "+str(r_count+4),"T:= "+res, "End"] 
    for count in range(r_count, r_count+5):
        sts[count]=sts_[count-r_count]

    for key,value in sts.items():
        print(key,value)
    print('\n') 
        
def elserelt(stmnts, line_number): 
   res = ""
   for i in stmnts:
        res = res+ i
   r_count=100+line_number
   t=0
   sts={}
   sts_=["else "+" goto "+str(r_count+3), "T:= "+str(t), " goto "+str(r_count+4),"T:= "+res, "End"] 
   for count in range(r_count, r_count+5):
        sts[count]=sts_[count-r_count]
   for key, value in sts.items():
        print(key, value)
   print('\n') 

def intermediate_code_generator():
    try:
        filename = sys.argv[1]  # Takes filename from the terminal
    except:
        filename = "default.sheesh"  # uncomment this and give filename here if not from terminal
    f = openSheeshfile(filename)
    lines = f.read().splitlines()
    # print('The Testcase is :\n')
    # for i in lines: print('\t',i)
    
    print('\n') 
    print("Three Address code SECTION => ") 

    list_of_lines = []

    for line in lines:
        list_of_lines.append(line.split(" "))

    for i in range(len(lines)):
        listt = []
        exp1 = ""
        exp2 = ""
        if 'if' in list_of_lines[i]:
            for char in list_of_lines[i]:
                if char=='if': continue
                if char=='(': continue
                if char==')': break
                exp1 = exp1 + char
            i=i+2
            for char in list_of_lines[i]:
                exp2 = exp2 + char
            relt(exp1, ass(exp2, 0), i)
        elif 'elseif' in list_of_lines[i]:
            for char in list_of_lines[i]:
                if char=='elseif': continue
                if char=='(': continue
                if char==')': break
                exp1 = exp1 + char
            i=i+2
            for char in list_of_lines[i]:
                exp2 = exp2 + char
            relt(exp1, ass(exp2, 0), i)
        elif 'else' in list_of_lines[i]:
            for char in list_of_lines[i]:
                if char=='elseif': continue
                if char=='(': continue
                if char==')': break
                exp1 = exp1 + char
            i=i+2
            for char in list_of_lines[i]:
                exp2 = exp2 + char
            elserelt(ass(exp2, 0), i)
        elif '=' in list_of_lines[i]:
            if i>2:
                if 'if' in list_of_lines[i-2] or 'else' in list_of_lines[i-2] or 'elseif' in list_of_lines[i-2]:
                    continue
            prev_char = ''
            enc_flag = 0 
            for char in list_of_lines[i]:
                if char == '=':
                    exp1 = exp1 + prev_char
                    exp1 = exp1 + '='
                    enc_flag = 1
                if enc_flag==1:
                    exp1 = exp1+ char
                prev_char = char
            ass(exp1, 1)