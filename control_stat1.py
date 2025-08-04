#if statement syntax
# if condition:
#     print("statement 1")
# print("statement 2")   

#write a python program to take SP and CP from user and check if the shopkeeper get a profit or loss and print amt after profit and loss
a=int(input("Enter SP"))
b=int(input("Enter CP")) 
if (a>b):
    print("profit")
    print(a-b)
if (a<b):
   print("loss")    
   print(a-b)

#write a python program to entered number is in between 1500 to 2100 if yes then print given no is between the condition
a=int(input("Enter a number"))
if a>=1500 and  a<=2100:
    print("Yes the number is between given range")

# write a python program to calculate absolute value:
a=int(input("enter a value :"))
if a<0 :
    print(-a)

#if else statement syntax
# if (condition):
#     print("statement 1")
# else:   
#     print("statement 2")   

#write a python program to check candidate are elegible or not
a=int(input("enter age :"))
if(a>=18) :
    print("you are eligible")
else:
    print("you are not eligible")

#write a python program to check shape given is rectangle or square
l=int(input("enter length :"))
b=int(input("enter breadth :"))
if l==b:
    print("It is a square")
else:
    print("It is a rectangle")

#write a python program to check if year is leap or not
a=int(input("enter year:"))
if a%400==0 or (a%4==0 and a%100!=0):
   print("It is a leap year")
else:
     print("It is not a leap year") 

#elif statement/elif ladder:
#if the condition is true then if block will execute otherwise next elif block will check for condition if the cond is true elif block will execute or else block will execute
#note: in elif ladder many elif blocks and single else block

#syntax of elif:
# if():
#     print()
# elif():
#     print()
# elif():
#     print()
# else:
#     print()

#example
if(True):
    print("if")
elif(True):
    print("elif1")
elif(True):
    print("elif2")
else:
    print("else")

#a store gives a discount on membership statue and the amount spent members spending over rs.10000
#gets 10% disc. , non memners spending over 15000 gets a 5% disc. and others get no disc.
a=int(input("enter amount:"))
member=(input("Enter membership status(yes/no)"))
if member=="yes" or member=="Yes" and a>=10000:
    d=a*0.1
    print(a-d)
    print("customer member")
elif member=="no" or member=="No" and a>=15000:
    b=a*0.05
    print(a-b)
    print("Non customer member")
else:
    print("No discount")

#A bank introduced an intensive policy of giving bonus to all acc. holder, the policy is as follows:
#a bonus of 2% of the balance is given to everyone.
#a bonus of 5% to women if there balance is more than 5000
#a bonus of 3% to men if there balance is more than 10000
#accept the balance, gender and calculate bonus


balance=int(input("enter balance:"))
gender=(input("Enter gender:"))
if gender=="women" or gender=="Women" and balance>=5000:
   bonus=balance*0.05
   print(bonus)
   total_balance= balance+bonus
   print("bonus given is:", total_balance)
elif gender=="men" or gender=="Men" and balance>=10000:
     bonus=balance*0.03
     print(bonus)
     total_balance=balance+bonus
     print("bonus given is:",total_balance )
else:
    print("the balnce after bonus is:",balance*0.02)

#an electric power distribution company charges are as follows:
#0-200 units= Rs.0.5 per unit
#201-400 units= Rs. 3 per unit+100 rs
#401-600 units=Rs. 4 per unit+200 rs
#for 600 and above unit= Rs. 6 per unit+300 rs

unit=int(input("Enter electricity unit:"))
if unit>=0 and unit<=200:
    total=unit*0.05
    print("total rupees chanrged:",total)
elif unit>=201 and unit<=400:
    total=unit*3+100
    print("total rupees chanrged:",total)
elif unit>=401 and unit<=600:
    total=unit*4+200
    print("total rupees chanrged:",total)
elif unit>=600:
    total=unit*6+300
    print("total rupees chanrged:",total)

#nested if
#syntax:
# if condition:
#     if condition:
#        stat1
#        stat2
#     stat3
# stat4

#nested if else
#syntax:
# if condition:
#     if condition:
#          stat1
#          stat2
#     else:
#          stat3
# else:
#     if condition:
#         stat4
#     else:
#         stat5             

if(1000):
    if(True):
       print("Hello")
       print("Hello1")
    print("if end")  
else:
    if(0):
       print("else if")   
    print("else")     

#short hand if
#syntax:
#if condition: stat1

#short hand if else
#syntax:
# stat1 if condition else stat2

#write a python program to check entered number is even or odd using short hand if else
a=int(input("Enter a num"))
print("even") if(a%2==0) else print("odd")

a=10
b=20
print("a") if a>b else print("=") if(a==b) else print("b")

#find max among 3 numbers
a=int(input("Enter a num"))
b=int(input("Enter a num"))
c=int(input("Enter a num"))
print("a is max") if(a>b) else print("b is max") if (b>c) else print("c  is max")

#take a num from user and check the num is multiple of 3 and 5 or only or only 5
a=int(input("Enter a num"))
if(a%3==0 and a%5==0):
   print("its multiple of 3 and 5 both")
elif(a%5==0):  
     print("its multiple of 5") 
elif(a%3==0):  
    print("Its multiple of 3")
else:
    print("please enter valid input")   


a=(input("Enter a character"))
c="aeiouAEIOU"
if a in c:
    print("it is a vowel")
else:
    print("It is a consonent")    