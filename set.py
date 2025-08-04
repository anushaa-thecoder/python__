# set : 1)A set is an unordered, unindexed collection of unique elements.
        # 2)It is mutable (can be changed), but its elements must be immutable (like int, str, tuple).
        # 3)Sets are written with curly braces {} or by using the set() function
        # 4) no duplicate elements are allowed in a set.
         


# Set creation
# Creating a set using curly braces
s={}
print("Empty set:", s)
print("Type of s:", type(s))
# Note: The above line creates an empty dictionary, not a set. To create an empty set, use set().


s1 = {1, 2, 3, 4}
print("Set 1:", s1)
s={1,2,3,4,1}
print("Set with duplicates (will be unique):", s)

s2={1,2,2,3,[1,2,3]}  
print("Set with a list (will raise error):", s2) # Note: This line will raise an error because lists are mutable and cannot be added to a set. 

#creting a set using set() function
empty_set = set()  
print("Empty set:", empty_set)
print("Type of empty_set:", type(empty_set))

s2 = set([3, 4, 5, 6])
print("Set 2:", s2)

s3=set("hello")
print("Set from string 'hello':", s3)

s4=set((1, 2, 3, 4,7,4))
print("Set from tuple (1, 2, 3, 4):", s4)

#Accessing elements in a set
# Sets are unordered, so you cannot access elements by index like in lists or tuples.
s={1, 2, 3, 4}
print(s[0])  # This will raise an error because sets do not support indexing.

#Traversing a set
for element in s:
    print("Element:", element)

# Deleting a set

del s 
print(s)

#traversing using while loop
"""NOTE: that traversing using while with set is not directly not possible typecasting it 
into list then iterating it is the only option to traverse it with while loop"""
s={1,2,3,4,5}
l=list(s)
i=0
while i<len(s):
    print(l[i])
    i+=1



