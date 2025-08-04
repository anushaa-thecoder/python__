num1=int(input("Enter 1st number:"))
sign=(input("choose sign:\n +, -,*,/,//,**,%,&,|,<<,>>,^,~\n" ))
num2=int(input("Enter 2nd number:"))
if sign=='+':
    print("The answer is:",num1 + num2 )
elif sign=='-':
    print("The answer is:", num1 - (num2)) 
elif sign=='*':
    print("The answer is:", num1 * num2)  
elif sign=='/':
    print("The answer is:", num1 / num2)  
elif sign=='//':
    print("The answer is:", num1 // num2)  
elif sign=='**':
    print("The answer is:", num1 ** num2) 
elif sign=='%':
    print("The answer is:", num1 % num2)
elif sign=='&':
    print("The answer is:", num1 & num2)  
elif sign=='|':
    print("The answer is:", num1 | num2)
elif sign=='^':
    print("The answer is:", num1 ^ num2)
elif sign=='<<':
    print("The answer is:", num1 << num2)
elif sign=='>>':
    print("The answer is:", num1 >> num2)
elif sign=='~':
      print("The answer is:",~num1)
      print("The answer is:", ~num2)
# else:
#      negation1=~num1
#      negation2=~num2
#      print("The 1st negation value's output is:", negation1)
#      print("The 1st negation value's output is:", negation2)