#write a python prog to declare a integer list and calculate sum of all elements of list 
#also find min and max of list
a=[1,2,3,4,5,6,7,8,9,0]
print("sum of all elements:", sum(a))
print("max value:",max(a))
print("min value:",min(a))

#write a python program to declare two lists and if both lists are same the repeat both lists 3 times
#else concate the string
a=[1,2,3,4,5,6,7,8,9,0]
b=[1,2,3,4,5,6,7,8,9,0]
if a==b:
    print(a*3,b*3)
else:
     print(a+b)    

a=[1,2,3,4,5,6,7,8,9,0]
b=[1,2,3,4,5,6,7,8,9,10] 
if a==b:
    print(a*3,b*3)
else:
     print(a+b)    

#write a python program to take a number from user and 
#check if the given number is present in list or not
#if yes then find sum of all elements and sort in ascending order
#if not then sort in descending order
o=[1,2,3,4,5,6,7,8,9,0]
a=int(input("enter a number:"))
if a in o:
     print("sum of all elements:",sum(o))
     print("sorting:",sorted(o))
else:
      print("sorting in descending order:",sorted(o,reverse=True))    

#write a python program to declare one list 
#and form second list from one which contains only even numbers using list comprehension
l=[1,2,3,4,5,6,7,8]
o=[i for i in l if i%2==0]
print(o)

#print at even index
l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
o=[l[i] for i in range (len(l)) if i%2==0]
print(o)

#write a python program to take a list from list of words, return only those with
#less than 5 characters
a=["anu","anuma","omaa","maaa"]
o=[]
for i in a:
  if len(i)<5:
      o.append(i)
print(o)      
#comprehension method:
l1=[i for i in l if len(i)<5]
print(l1)

#to convert word in uppercase by list comprehension
a=["anu","anuma","omaa","maaa"]
l1=[i.upper() for i in a]
print(l1)

#1to find second largest number from list
#2to take elements of list from user
#3to remove duplicates 

#2
b=[]
for i in range(5):
  a=int(input("enter a number:"))
  b.append(a)
print(b)

#3
b=[]
b1=[]
for i in range(5):
    a=int(input())
    b.append(a)
print(b)
for i in b:
     if i not in b1:
      b1.append(i)
print(b1)

#write a python program to take a value from user and find it in list else print list as it is
#if its present then replace it with python
#only update first occurance of an element
b1=[]
for i in range(5):
    a=int(input("numbers you want:"))
    b1.append(a)
print(b1)
b=int(input("enter a element:"))
if b in b1:
 index=b1.index(b)
 b1[index]="python"
 print(b1)
else: 
     print(b1)

#count the number of words where length of words is greater then 1st and last character
#are same from given list of words
a=['abcd','aca','aba','bab','xyx']
c=0
for i in a:
    if len(i)>2 and i[0]==i[-1]:
        c+=1
print(c)        

#swapping elements of list
l=[1,2,3,4,5]
l[0],l[-1]=l[-1],l[0]
print(l)

