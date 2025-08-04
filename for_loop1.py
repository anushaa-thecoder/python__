#for loop
#syntax:
#for variable in sequence:
         #statement1
         #statment2

#shorthand for loop
#for variable in sequence: stat1

#examples:
#write a python prog. to print cube of first 100 even numbers
for a in range(2,201,2):
     c=a**3
     print("the cube of", a,  "is:", c)

#Wap to find the sum of series of a number upto nth terms
n=int(input("Enter a number:"))
nth_term=int(input("Enter a term:"))
n1=n
sum=0
for i in range(0,nth_term):
         sum=sum+n
         n=n*10+n1
print(sum)


n=int(input("Enter a number:"))
nth_term=int(input("Enter a term:"))
n1=n
sum=0
for i in range(0,nth_term):
         print(n, end="+")
         sum=sum+n
         n=n*10+n1
print("=",sum)

#to take input from user and print n natural numbers in descending order using for loop
n=int(input("Enter a number:"))
for i in range(n,0,-1):
     print(i)

# range(start,end,step)
print(range(10))
print(range(1,10))
print(range(1,10,2))
for i in range(10):
    print(i , end = "")

    