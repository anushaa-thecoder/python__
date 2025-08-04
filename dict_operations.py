#Note:Arithmetic operators are not applicable to dictionaries in Python.

#Member operators
d1 = {"name": "abc", "Marks": 30}
print("Is 'name' key in d1:", "name" in d1)
print("Is 'age' key in d1:", "age" not in d1)

#Identity operators
a={"name": "abc", "Marks": 30}
b={"name": "abc", "Marks": 30}
print("Is a is b:", a is b)
print("Is a is not b:", a is not b)

#comparison operators
a = {"x": 1, "y": 2,"z":1}
b = {"y": 2, "x": 1}
print(a == b) 
print(a != b)

# Dictionary merge operator
a = {"x": 1}
b = {"y": 2}
print("Union of a and b:", a | b) # Using the union operator to combine dictionaries
print(a)
print(b)

# Dictionary Assignment operator
a = {"x": 1, "y": 2}
b=a
print("Assigning b to a: ", b)
a['x']=10
print("After modifying a, b also changes: ", b)

a |= b
print("Combining two dictionary and assign: ",a)
print(b)

