#to declare a tuple and unpack given tuple into several variables print addn of all vars
t=(1,2,3,4,5,6,7,8,9)
t1,t2,t3,t4,t5,t6,t7,t8,t9=t
print("sum:",sum(t))

#to get 4th elemennt from last element of tuple
t=(1,2,3,4,5,6,7,8)
print(t[-4])

#calculate multi of all elements
t=(1,2,3,4,5)
product=1
for i in t:
    product*=i
print(product)

#
t=(1,2,3,4,5,6)
t1=(1,2,3,4,5)
o=(i for i in t1 if i in t)
print(tuple(list(o)))

#to convert tuple of integer into tuple of string
t=(1,2,3,4,5)
o=(str(i) for i in t)
print(list(o))       

#to check all elements in tuple are same or not
#1st way
t=(1,2,1,1,1)
if t.count(t[0])==len(t):
    print("all the elements are same in tuple")
else:
    print("all elements are not same")    

#2nd way
t=(1,1,1,1,1)
if all(i==t[0] for i in t):
    print("all elements are same")
else:
     print("all elements are not same")

#WAP to take elements of tuple from user
o=[]
for i in range(5):
   user=int(input("enter elements"))
   o.append(user)
print(tuple(o))  

#unpack tuple elements
t=tuple(o)
a,b,c,d,e=t
print(a,b,c,d,e)
print(f"a={a} b={b} c={c} d={d} e={e}")
#print("a{} b{} c{} d{} e{}" .format(a,b,c,d,e))

#WAP to accept elements for nested list 
l=[]
row=int(input("enter num of rows:"))
for i in range(row):
    l1=[]
    a=int(input("enter elements for nested:"))
    for i in range(a):
        b=int(input("enter elements:"))
        l1.append(b)
    l.append(l1)    
print(l)


