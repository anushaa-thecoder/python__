#dictionary:1) A dictionary is a collection of key-value pairs.
#           2) It is unordered (before Python 3.7), mutable, and indexed by keys (not positions).
#           3) Keys must be unique and immutable (e.g., strings, numbers, tuples). 
#           4) Values can be of any data type and can be duplicated.
#           5) Dictionaries are defined using curly braces {} or the dict() constructor.
#           6) They are useful for fast lookups, data retrieval, and representing structured data.

#Creating a dictionary using curly braces
d={}
print("Empty Dictionary:",d)
print(type(d))

d1={"name":"abc", "Marks":30 }
print("Dictionary with key-value pairs:",d1)

d2={1: "one", 2: "two", 3: "three"}
print("Dictionary with integer keys:", d2)

d3={1:[1,2,3], 2:[4,5,6], 3:[7,8,9]}
print("Dictionary with lists as values:", d3)

d4={1:{"name":"abc", "Marks":30}, 2:{"name":"xyz", "Marks":40}}
print("Dictionary with dictionaries as values:", d4)

d5={1:(1,2,3), 2:(4,5,6), 3:(7,8,9)}
print("Dictionary with tuples as values:", d5)

#d6={[1,2]:3, [4,5]:6}  # This will raise an typeerror because lists are mutable and cannot be used as keys

#creating a dictionary using the dict() constructor
d7=dict(name="abc", Marks=30)
print("Dictionary created using dict() constructor:", d7)

d8=dict([(1, "one"), (2, "two"), (3, "three")])
print("Dictionary created from a list of tuples:", d8)

d9=dict(zip(["name", "Marks"], ["abc", 30]))
print("Dictionary created using zip:", d9)

# Accessing values in a dictionary
d1={"name":"abc", "Marks":30 }
print("Accessing value by key 'name':", d1["name"])

#updating values in a dictionary
d1["Marks"] = 35
print("Updated value for key 'Marks':", d1["Marks"])

# Adding a new key-value pair
d1["Age"] = 25
print("Dictionary after adding new key-value pair:", d1)

#Traversing a dictionary
# Using a for loop to iterate through keys
for i in d1:
    print(i)

# Using a for loop to iterate through values
for i in d1:
    print(d1[i])

# Using a for loop to iterate through key-value pairs
for index, key in enumerate(d1):
    print(f"{key}:{ d1[key]}")

#deleting a key-value pair
del d1["Age"]
print("Dictionary after deleting key 'Age':", d1)

del d1
#print("Dictionary after deletion:", d1) #statement will raise a NameError since d1 has been deleted.