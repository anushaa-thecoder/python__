#Built-in fucntions for dictionary
d1={"name": "abc", "marks": 30}
print("Length of dictionary d1:", len(d1))  
print("Maximum key in d1:", max(d1))
print("Minimum key in d1:", min(d1))
# print("Sum of keys in d1:", sum(d1))  # This will raise an error because keys are strings
print("Sorted keys in d1:", sorted(d1)) 
print("Reversed keys in d1:", list(reversed(d1)))

#Dictionary methods
#key():Returns list of keys in the dictionary.
d1={"name": "abc", "marks": 30}
print("Keys in d1:", d1.keys())

#values():Returns list of values in the dictionary.
print("Values in d1:", d1.values())

#items():Returns list containing a tuple for each  key-value pairs in the dictionary.
print("Items in d1:", d1.items())

#get(key, default=None):Returns the value for the specified key if it exists, otherwise returns the default value.
print("Value for key 'name':", d1.get("name"))
print("Value for key 'age' with default:", d1.get("age", "Not Found"))

#Modifying Dictionary
#update(other_dict):Updates the dictionary with key-value pairs from another dictionary or iterable.
d2={"age": 25, "city": "New York"}
d1.update(d2)
print("Dictionary after update with d2:", d1)
d1.update({"country": "USA"})
print("Dictionary after adding new key-value pair:", d1)
d1.update(name="xyz", marks=40)
print("Dictionary after updating with new key-value pairs:", d1)

#setdefault(key, default=None):Returns the value for the specified key if it exists,
#                              otherwise sets it to the default value and returns it.

d={1:"one", 2:"two"}
print("Value for key 1 with setdefault:", d.setdefault(1))
print(d)
print("Value for key 3 with setdefault:", d.setdefault(3))
print(d)

#copy():Returns a shallow copy of the dictionary.
d1 = {"name": "abc", "marks": 30}
d_copy = d1.copy()
print("Original dictionary d1:", d1)
print("Shallow copy of d1:", d_copy)

#Removing Items
#pop(key, default=None):Removes the specified key and returns its value.
print("Value removed for key '1':", d.pop(1))
print("Dictionary after pop operation:", d)

print("Value removed for key '1':", d.pop(9,"not found"))
print("Dictionary after pop operation:", d)

#popitem():Removes and returns the last inserted key-value pair as a tuple.
print("Last item removed:", d.popitem())

#clear():Removes all items from the dictionary.
d.clear()
print("Dictionary after clear operation:", d)

# fromkeys(seq, value=None):Creates a new dictionary with keys from sequence and a single value.
d3 = dict.fromkeys(["a", "b", "c"], 0)
print("New dictionary created from keys:", d3)

d4=dict.fromkeys('abc',1)
print(d4)

#classwork 16 june 2025
d={1:"one",2:"two"}
print(d.keys())
print(d.values())
print(d.items())
# print(d[3])
print(d[2])
print(d.get(3,"not found"))


