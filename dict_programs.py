#to declare a dictionary for employee with keys as emp name, emp id, emp salary
#print dictionary
a={"employee name" : "anushka",
   "employee id":123, 
   "employee salary": 40000}
print(a)

#declare same for customer
d={"customer name": "sachin",
   "customer id": 23456,
   "products":["toothpaste", "brush"]}
print(d)

#take 5 keys and values from user
d={}
for i in range(5):
  k=input("enter a key:")
  v=input("enter value:")
  d[k]=v
print(d)

#to check given key is exist in dictionary or not
d={}
for i in range(3):
  k=input("enter a key:")
  v=input("enter value:")
  d[k]=v
print(d)
key=input("enter a key:")
a=d.get(key, "not found")
print(a)

#to take list of strings and return a dictionary where the keys are string length 
#values are list of string of that length ****
l=[]
d={}
for i in range(5):
 a=input("enter string names:")
 l.append(a)
print(l)
for i in l:
   o=len(i)
   if o not in d:
      d[o]=[]
   d[o].append(i)
print(d)  

#to count the frequency of each word in a given sentence using dictionary ******
d={}
str="python is great and python is easy to learn Python"
for i in str.split():
   i=i.lower()
   if i in d:
     d[i]=d[i]+1   
   else:
     d[i]=1
print(d)     

#freq of characters ******

d={}
str="python is great and python is easy to learn Python"
for i in str:
   i=i.lower()
   if i in d:
     d[i]=d[i]+1   
   else:
     d[i]=1
print(d)   

#to remove given key value pair from dictionary
d={}
for i in range(5):
   key=input("enter key:")
   value=input("enter value:")
   d[key]=value
print(d)
k=input("key to be removed:")
print(d.pop(k))
print(d)


#swapping of key and value
d={}
for i in range(3):
   key=input("enter key:")
   value=input("enter value:")
   d[key]=value
print("Before swapping:",d)
swap={}
for i, (k,v) in enumerate(d.items()):
    swap[v]=k
print("After swapping:",swap)    