#take 5 elements from user for set and add them
a=set()
for i in range(5):
    b=int(input("enter elements:"))
    a.add(b)
print(a)

#to take a value from user and delete given value from set
a=set()
for i in range(5):
    b=int(input("enter elements:"))
    a.add(b)
print(a)
rem=int(input("enter an element to be removed:"))
a.discard(rem)
print(a)

#take elements of set from user and convert given set into list if given element present in set
a=set()
for i in range(5):
    b=int(input("enter elements:"))
    a.add(b)
print(a)
present=int(input("enter an element to be searched:"))
if present in a:
    print(list(a))
else:
    print(tuple(a))

#to take iterable object: 
#string, list, tuple from user and add all this in set as a set element

# for string:
a=set()
for i in range(5):
    b=(input("enter elements:"))
    a.update(b)
print(a)

#tuple
a=set()
for i in range(5):
    b=(input("enter elements:"))
    a.update(b)
    print(tuple(b))
print(a)

#list
a=set()
for i in range(5):
    b=(input("enter elements:"))
    print(list(b))
    a.update(b)
print(a)


#to take two sets from user and check if they have common element
a=set()
for i in range(5):
    b=int(input("enter elements:"))
    a.add(b)
print(a)

o=set()
for i in range(5):
    c=int(input("enter elements:"))
    o.add(c)
print(o)
if a|o:
    print("common elements:", a.intersection(o))
else:
     print("no common elements found")

#remove common elements from set 1
a=set()
for i in range(5):
    b=int(input("enter elements:"))
    a.add(b)
print(a)

o=set()
for i in range(5):
    c=int(input("enter elements:"))
    o.add(c)
print(o)
for i in a&o:
    a.remove(i)
    o.remove(i)
    print(a)

#to take elements of two sets from user and check if 1st set is subset of another set
a=set()
for i in range(5):
    b=int(input("enter elements:"))
    a.add(b)
print(a)

o=set()
for i in range(5):
    c=int(input("enter elements:"))
    o.add(c)
print(o)
if a<=o:
    print("1st set is subset of other")
else:
    print("not a subset")

#find 2nd largest number
a={1,2,3,4,5}
b=(tuple(sorted(a,reverse=True)))
print(b)
print(b[1])

