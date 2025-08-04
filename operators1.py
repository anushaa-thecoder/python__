a=float(input("Enter a num"))
b=int(input("Enter a num"))
a+b
print(a+b)
a-b
print(a-b)
a*b
print(a*b)
a/b
print(a/b)
a%b
print(a%b)
a//b #it returns quotient's lower value
print(a//b)
a**b #it returns exponential value
print(a**b)

#Comparision operators
a=5
b=7
print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>b:",a>b)
print("a<b:",a<b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)

#Assignment Operator
a=5
a+=2
print("a+=2:",a)
a=5
a-=5
print("a-=5:",a)
a=5
a*=3
print("a/=3:",a)
a=5
a/=2
print("a+=2:",a)
a=5
a%=8
print("a%=8:",a)
a=5
a**=9
print("a**=9:",a)
a=5
a//=6
print("a//=6:",a)

#logical opeators
a=10
b=20
print(a>10 and b>20)
print(a>10 or b>20)
print(not a)

#bitwise operator: decimal value output
a=10
b=20
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a>>2)
print(a<<2)

#identity operator: checks memory location of object
a=5
b=5
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

#list in identity- memory location is not same
a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

#tuple: if both tuple contains same elements it points to same memory location
a=(1,2,3,4,5)
b=(1,2,3)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

#membership operator: checks member in sequence
a="python"
print("y" in a)
print("y1" not in a)
b=[1,2,3,4]
print("10" in b)
print("100" in b) 

c="12345"
print("1" in c)
print(1 in c) #type error

#precedence of operators:
#(), **, ~, *, /, %, //, +,-,<<,>>, &, ^, |, >,<, ==,!=
#in, not in, is, is not, >=,<=, not, and , or, assignment operator

print(10-3*2)
print((10-3)*2)
print((10-3)**2)
print(10-3**2)
a,b="abc", 0
print(a=='abc' and a=="abcd" or b<2)
print(a=='abc' and a=="abcd" or b=="abcd")
print(10&8|8^10)

#Associativity of operators
#right to left: **, unary operators, lofical not, assignment operators
#rest left to right