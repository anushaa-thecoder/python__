#Bulin Functions
l1=[1,2,3,4,5,6,7,8,9,10,2,1]
print(l1)
print(type(l1))
print("Length of string : ",len(l1))
print("Maximum value  from list : ",max(l1))
print("Minimum value  from list : ",min(l1))
print("sum of list element  : ",sum(l1))
print("sum(list,start):  ",sum(l1,100))  # start :Optional. A value that is added to the return value
print("sorted(l) : ",sorted(l1))
print("sorted(list,reverse)",sorted(l1,reverse=True)) 
print("all(l1) : ",all(l1))  # Returns True if all elements of the iterable are true (or if the iterable is empty)
print("any(l1) : ",any(l1))  # Returns True if any element of the iterable is true. If not, it returns False
print("reversed(l1) : ",list(reversed(l1)))  # Returns a reverse iterator over the values of the given sequence
#
s=['a','b','c','d','e','f','g','h','i','j']
print(s)
print(max(s))
print(min(s))


c=[2+2j,4+5j,5+6j,6+6j,7+7j,9+1j]
print(sum(c))
print("sum of complex element in list  : ",sum(c))  # Returns the sum of all elements in the iterable

l=['aaa','av','cda','abcd','aad']
print(l)
print(sorted(l))
print(sorted(l,reverse=True))
print(sorted(l,key=len))

l=[[1,2],[3,4],[1,2,1],[1,3],[1,2,2]]
print(l)
print(sorted(l))
print(sorted(l,reverse=True,key=len))



# list function 
# append function : Adds an element at the end of the list.
l=[1,2,3,4,5]
print("append(element): ",l.append(6))
print("append(element): ",l)
# l.append(7,78)
# print(l)
l.append([10,20,30,40,50])
print("append(element): ",l)
l.append("abc")
print(l)
l.append(1+2j)
print(l)

# extend function : Adds the elements of an iterable (list, tuple, set, etc.) to the end of the list.
l="pthon"
l1=[1,2,3,4,5]
l1.extend(l)
print("extend(squencce) :",l1)
# l1.extend(10)   # TypeError: 'int' object is not iterable
l1.extend(['a','b','c'])
print("extend(squencce) :",l1)
l1.extend(range(1,10))
print("extend(squencce) :",l1)

# insert(index,element) : Inserts an element at a specified position in the list.
l=[1,2,3,4,5]
l.insert(1,"abc")
print("insert(1,'abc'):",l)
l.insert(-2,10)
print("insert(-2,10):",l)
l.insert(-1,20)
print("insert(-1,20):",l)
l.insert(0,30)
print("insert(0,30):",l)
l.insert(4,40)
print("insert(4,40):",l)
l.insert(-5,50)
print("insert(-5,50):",l)
l.insert(6,60)
print("insert(6,60):",l)
l.insert(6,[70,80,90])
print("insert(6,[70,80,90]):",l)

#count(element): Returns the number of occurrences of an element in the list.
l=[1,2,1,3,4,1,5,6,3]
print("count(1): ",l.count(1))
print("count(2): ",l.count(2))
print("count(7): ",l.count(7))


#index(element): Returns the index of the first occurrence of an element in the list
l=[10,20,3,2,4,5]
print("index(3): ",l.index(3))
print("index('3'): ",l.index("3"))
print("index(8): ",l.index(8))

l=[0,1,True,False]
print(l.index(True))
print(l.index(False))

## index(element,start,end): Returns the index of the first occurrence of an element in the list within the specified range.
l=[2,1,3,2,-1]
print(l.index(2))
print(l.index(2,1))
print(l.index(2,1,3))

#reverse(): Reverses the order of the elements in the list in place.
l=[10,20,3,2,4,5]
l.reverse()
print(l)


# sort() : Sorts the elements of the list in ascending order by default.
l=[1,5,6,2,3,4,8,7]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l=['aa','abc','aab','ab','abcd']
l.sort(key=len,reverse=True)
print(l)



# pop():Removes and returns the last element from the list.
#       If an index is specified pop(index), it removes and returns the element at that index.
l=[10,20,3,2,4,5]
print("last element removed : ",l.pop())
print("List after pop(): ",l)
print("pop(2) : ",l.pop(2))
print("List after pop(2): ",l)
# print(l.pop(8))

# remove(element): Removes the first occurrence of the specified element from the list.
l=[10,20,30,40,50]
l.remove(20)
print("List after remove(20): ",l)
l.remove(50)
print("List after remove(50): ",l)
l.remove(300)
print(l)

# clear(): Removes all elements from the list, leaving it empty.
# Note: The clear() method does not delete the list itself; it just removes all elements from it.
l=[10,20,3,2,4,5]
l.clear()
print("List after clear(): ",l)
print("id of list after clear(): ",id(l))

# del statement: Deletes the entire list or a specific element from the list.
a=10
print(a)
del a
print(a)

l=[10,20,3,2,4,5]

del l[1]
print("List after del l[1]: ", l)
del l[2:4]
print("List after del l[2:4]: ", l)
del l
print("List after del l: ", l)  

