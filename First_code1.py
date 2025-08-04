#Hello World program
print("hello")
print("world")

#python identifiers declaration rules
#1)It is combination of Alphanumeric character or underscore(_)
pqr=10
print(pqr)
abc123=10
print(abc123)
a_b_c=10
print(a_b_c)

#2)It can't  be start with a digit.
#1abc=10              //SyntaxError

#3)They should not contain  whitespace and speical characters
#abc pqr =10            //SyntaxError
#abc@pqr =100            //SyntaxError

# 4) They are case sensitive 
A=0
a=10

#5) They should not be  a keywords
# if=10                 SyntaxError: invalid syntax

#example
IF=10
_x=10
print(_x)
__x=20
print(__x)
__x__=30
print(__x__)

a=b=c=5
print(a,b,c)         

#Keywords in python  : Note - In python ,all keywords  are in lowercase except True,False,None 
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
# 'while', 'with', 'yield']

