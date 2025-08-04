#General pupose functions:
s={1,2,3,4,4,5,5,6}
print(len(s))
print(min(s))
print(max(s))
print(sum(s))
print(all(s))
print(any(s))
print(sorted(s,reverse=True))
print(sum(s,100))
print(list(reversed(list(s))))

#Set functions:
#1. add() function:
s={1,2,3,3,4,4,5}
s.add(10)
#s.add(10,20) gives error only 1 argument is allowed
print(s)
s.add(1)
print(s)
s.add('hello')
print(s)
s.add((1,2,3))
print(s)
# s.add()
# print(s) gives error because only 1 arg allowed

#2. update() function:
s={1,2,3,3,4,4,5,6}
# s.update(10)
# print(s) error cause only iterable objects are allowed
s.update((1,2))
print(s)
s.update('hello')
print(s)
s.update([1,2,3,4,5])
print(s)

#3. remove() function: shows keyerror if element is not present
o={1,1,1,2,3,4,4,5}
o.remove(2)
print(o)

#4. discard function: doesnot show keyerror if element is not present
o={1,1,1,2,3,4,4,5}
o.discard(9)
print(o)

#5. pop() function: removes random number and returns the removed element
o={2,3,4,4,5}
removed=o.pop()
print(removed)
print(o)

#6. clear() function:
o={1,1,2,3,4,4,5}
o.clear()
print(o)


#set operations:

#1. union() function:
s1={1,2,3,4,5,6}
s2={1,5,6,4,35,7}
print("union:",s1.union(s2)) #| pipe operator
print("intersection:",s1.intersection(s2)) #& operator
print("Difference(s1-s2):",s1.difference(s2))# - operator
print("Symmetric Difference:",s1.symmetric_difference(s2)) #^ opertor
print("Issubset:",s1.issubset(s2)) #<= operator
print("issuperset()",s1.issuperset(s2)) #>= operator
print("Disjoint():",s1.isdisjoint(s2))



