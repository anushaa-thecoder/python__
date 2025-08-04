#1. while loop for repetedly ask the user to enter a number as a string input 
while(True):
    a=input("enter a no:")
    print(a)

#2. Convert the input to an integer using typecasting.
a=int(input("enter a no:"))
print("you enter a n o:",a) 

#3. If the number is negative, stop the loop using a control statemennt
while(True):
    num=int(input("enter a no:"))
    if(num < 0):
        print("negative no enter.exiting......")
        break
        print("you enter :",num)
#4. otherwise print the no with the messege :"you entered :no"
a=int(input("enter a no :"))
print("you entered a :",a)

# Use while loop to ask the user to enter a  number both  real numbers (e.g., 5, 2.5) and complex 
# numbers (e.g., 3+4j). 
count = 0
while(True):
    num=complex(input("enter a no:"))
    if num.real<0:
        print("negative real part detected existing")
        break
    else:
        count += 1
        print("real part:",num.real,"imaginary part",num.imag)
print(count)


#QD. Given a number num = 100, print it in decimal, hexadecimal, octal, and binary formats, 
# each with the appropriate prefix (0x, 0o, 0b).
num=100
print(hex(num))
# print(dec(num))
print(oct(num))
print(bin(num))


#enter a string and count how many vowel are in 
count = 0 
a=input("enter a string:")
b="aeiouAeiou"
for i in a:
    if(i in b):
        count += 1
print(count)

# febonisis series
sum=0
a = 0
b = 1
num=int(input("enter a term"))
for i in range(num):
    print(a)
    sum=a+b
    a,b = b,sum     


# Factorial no
num=int(input("enter a no:"))
fact = 1
for i in range(1,num + 1):
    fact *= i
print("factorial of",num,"is",fact)


# eg of while loop with else statement
password = "focus@2025"
user=input("enter a pass:")
i=0
while(i<3):
    if(user==password):
        print("correct pass")
        break
else:
    i+=1
    print("incorrect pass")

