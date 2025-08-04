#lambda function:

#no para no ret type
o=lambda:print("ANUMA")
o()
print(o())
print(type(o))

#with para wuth ret value
o=lambda x:x*2
print(o(3))

#with para no ret type
f1=lambda x:print(x)
f1(2)
print(f1(2))

#no para only ret value
f1=lambda:13
print(f1())
 
#variable arguments
o=lambda *x:sum(x)
print(o(3,2,4,5,6,7,8,9,5))

#anonymous func
print((lambda x:x*8)(4))

#NameError: name 'x' is not defined as lambda func only returns single value
# result= lambda x,y:x+y,x-y
# print(result(1,2))

result= lambda x,y:(x+y,x-y,x*y,x/y)
a,b,c,d=(result(1,2)) #unpacking
print(a,b,c,d)

#check number is even or odd using lambda function
a=int(input("enter a number:"))
l=(lambda x: print("even") if x%2==0 else print("odd"))
l(a)

#even num using filter func
l=[1,2,3,4,5,6,7,8,9,0]
a=filter(lambda x:x%2==0,l)
print(list(a))

#positive number
l=[1,2,3,4,5,6,7,8,9,-1]
a=filter(lambda x:x>=0,l)
print(list(a))

# l=[1,2,3,4,5,6,7,8,9,-1]
# a=filter(lambda x: (if x%2==0: print("even")),l)
# print(list(a))

#create a list of string and filter the words which has len more than or equal to 5
l=["abc", "abcd", "pqrsd","manuuuu","mi"]
a=filter(lambda x:len(x)>=5,l)
print(list(a))

#to sort list of dictionaries using lambda function
l=[{'name': 'MIDS','age': 28},{'name':'KUU','age': 26}]
a=(sorted(l,key=lambda x:x["name"]))
print(a)

#to take a list of numbs find avg of it also filter with numbs greater than avg
l=[1,2,3,4,5,6,7,8,9]
avg=(sum(l)/len(l))
print(avg)
a=filter(lambda x:x>=avg, l)
print(list(a))

#to take list of dictionaries in which key is items and key is price 
l=[{"items": "pen","price": 30},
   {"items": "clipboard","price": 17},
   {"items": "book","price": 90},
   {"items": "pouch","price": 100}]
# a='price'*0.5
a=(sorted(l,key=lambda x:x['price']*0.5))
print(a)

#map function
l=[1,2,3,4,5,6,7]
x=map(lambda x:x*2,l)
print(list(x))

#discount using map function
l=[{"items": "pen","price": 30},
   {"items": "clipboard","price": 17},
   {"items": "book","price": 90},
   {"items": "pouch","price": 100}]
a=map(lambda x:x['price']*0.5,l)
print(list(a))

l=[{'info': {'age':21}},
   {'info': {'age':19}},
   {'info': {'age':30}},
   {'info': {'age':10}}]
a=sorted(l,key=lambda x:x['info']['age'])
print(list(a))

l=['1','2','3','4','5']
a=map(lambda x: int (x),l)
print(list(a))

l=[1,5,0,True,"",-1,-45,False,0.0,{},(),[]]
a=filter(None,l)
print(list(a))

#given a list of strings first filter out string
#having length less than 5 then convert remaining the string to uppercase using map and lambda function
l=["anushka","anumaa","oma","ookay"]
a=filter(lambda x:len(x)<8,l)
b=map(lambda y:y.upper(),a)
print(list(b))


#reduce function:
from functools import reduce
l=[1,2,3,4,5,6,78,9,]
a=reduce(lambda x,y:x+y,l)
print(a)

from functools import reduce
l=[1,2,3,4,5,6,7,8,9,0]
a=list(filter(lambda x:x%2!=0,l))
print(a)
b=reduce(lambda x,y:x+y,a,100)
print(b)


#1.list is given
#2. filter out orders with quantity 0
#3. calculate total price for each valid order
#4. calculate total bill using reduce
from functools import reduce
orders=[{'items':'laptop','price':50000,'quantity':1},
        {'items':'mouse','price':500,'quantity':-1},
        {'items':'keyboard','price':1500,'quantity':2},
        {'items':'monitor','price':12000,'quantity':1},
        {'items':'cable','price':1000,'quantity':3}]
a=filter(lambda x:x['quantity']>0,orders)
#print(list(a))
b=map(lambda x:x['price']*x['quantity'],a)
#print(list(b))
c=reduce(lambda x,y:x+y,b)
print(c)


#mini project:

# Scenario: Hospital Management System (OPD Report)
# * Problem Statement:
# A hospital wants to:

# Maintain a list of outpatient (OPD) records.

# *Compute*:

# 1)Billing per patient (with senior citizen discount)

# 2)Total revenue

# 3)Number of patients eligible for free consultation

# Condition:
# 1)Patients with age > 60 get 20% discount

# 2)Patients with income < ₹15,000 get free consultation

# Hint:In map function use user defined function


patients = [
    {"name": "Amit", "age": 65, "fee": 500, "income": 18000},
    {"name": "Rita", "age": 45, "fee": 500, "income": 12000},  
    {"name": "Suresh", "age": 70, "fee": 500, "income": 10000}, 
    {"name": "Pooja", "age": 30, "fee": 500, "income": 25000},
    {"name": "Ravi", "age": 61, "fee": 500, "income": 20000}   
]

a=map(lambda x:x)