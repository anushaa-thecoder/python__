#syntax:
# def funname ():
#     block1
#     block2
# block3    *out of the function stmt

#to call function:
# funname() 

#simple function:
def f1():
    print("Welcome to function")
f1()

#function with return type:
def f2():
    return "ANUMA"
print(f2())

#function with multiple return type:
def f3():
    return 1,2,3,4,5,6,7,8,9,0
a=f3()
print(a)

#unpacking of tuple in function
def f4():
    return 1,2,3,4,5,6,7,8,9,0
a,b,c,d,e,f,g,h,i,j,=f4()
print(a,b,c,d,e,f,g,h,i,j)
print(type(a))

#function with arguments and no return value
def add(a,b):
    print(a+b)
add(10,20)
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
add(x,y)

def f1(a):
    print(type(a))
f1(10)
f1("Hello")
f1([1,2,3])
f1((1,2,3))

#function with arguments and return value
def f1(a,b):
    return a+b, a-b, a*b, a/b, a//b, a**2, b**2, a%b
print(f1(10,20))

#function withn default values
def sum(a,b,c=10):
    print(a*b*c)
# sum(10)
sum(1,2,3)

#function with multiple arguments(*args): Accepts multiple values as a tuple
def add(*args):
    print(args[0]+args[1])
    print(sum(args))
add(1,2,3,4,5)

#function with keyword arguments using **kwargs: Accepts named arguments as a dictionary
def display(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
display(name="ABC",age=25,city="Nagar")

#All in one example
def a(a,b=10,*args,**kwargs):
    print("a=",a)
    print("b=",b)
    print("args=",args)
    print("kwargs=",kwargs)

a(1,2,4,5,x=10,y=10)

#Recursion function:
def mini(n):
    print(n)
    if n==10:
        return
    mini(n+1)

mini(1)

#syntax:
# def funcname():
#     base case
#      return statement
#     recursive case
#    printing stmt
#function calling