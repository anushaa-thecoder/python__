#tuple:1)Tuples are immutable; once created, their content cannot be changed.
        # 2) Tuples can contain heterogeneous elements (different data types).
        #  3)Tuples support nesting — a tuple can contain other tuples or lists.


# Tuple Creation
t1 = ()
print("Empty tuple:", t1)
# Tuple with one element (note the comma)
t2 = (5,)
print("Single element tuple:", t2)
t3 = (1, 2, 3)
print("Tuple with multiple elements:", t3)
t4 = (1, "hello", 3.14, True)
print("Heterogeneous tuple:", t4)
t5 = (1, (2, 3), [4, 5])
print("Nested tuple:", t5)
t4 = 1, 2, 3, 4
print("Tuple without parentheses:", t4)
print("Type of t4:", type(t4))

# Creating a tuple using the tuple() constructor
t6 = tuple([1, 2, 3])
print("Tuple created using tuple() constructor:", t6)

t7 = tuple("hello")
print("Tuple from string:", t7)



# Accessing Elements
t = (10, 20, 30, 40, 50)
print(t[0])  
print(t[-1]) 

# Slicing
print(t[1:4])  
print(t[:3])   
print(t[3:])

# Nested Tuple Access
t = (1, (2, 3), [4, 5])
print(t[1])
print(t[1][0])

#updating a tuple
t = (1, 2, 3)
t[1] = 5  # TypeError: 'tuple' object does not support item assignment

t = (1, (2, 3), [4, 5])
t[2][0] = 6  # This is allowed because the inner list is mutable
print(t)

#traversing a tuple
t=(1, 2, 3, 4, 5)
for item in t:
    print(item)

#tuple comprehension
t = (x * 2 for x in range(5))
print("Tuple comprehension:", list(t)) 

# Deleting a tuple
del t
print(t)


#  Tuple Operations
# Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# Repetition
t4 = t1 * 3
print(t4)

# Membership Testing
t = (1, 2, 3)
print(2 in t) 
print(5 not in t)

# Tuple unpacking
a, b, c = t1
print("Unpacked values:", a, b, c)


# Tuple Functions
t = (4, 1, 7, 3, 1, 4, 4)
print("Tuple:", t)
print("Length:", len(t))  
print("Count of 4:", t.count(4))
print("Index of 7:", t.index(7))
print("Minimum:", min(t))  
print("Maximum:", max(t))  
print("Sum:", sum(t)) 
sorted_list = sorted(t)
print("Sorted:", sorted_list)  # [1, 1, 3, 4, 4, 4, 7]
print("Original tuple after sorting:", t)
