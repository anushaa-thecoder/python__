#Comparison operations on lists
print("Comparison operations on lists")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print("list1 == list2:", list1==list2)  
print("list1 != list2:", list1!=list2)  
print("list1 < list2:", list1<list2)  
print("list1 > list2:", list1>list2)
print("list1 <= list2:", list1<=list2)
print("list1 >= list2:", list1>=list2)

#List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Concatenated list:",list1 + list2)
print("Concatenated list with string:",list1 + 'abc') 
print("Concatenated list with int value:",list1 + 10)

#List Repetition
list1 = [1, 2, 3]
print("Repeated list:", list1 * 3)
# print("Repeated list with string:", list1 * 'abc')
print("Repeated list with  -ve int value:", list1 * -2)

#list copy:
# Copying a list using the copy() method
# Copying a list using the list() constructor
# Copying a list using slicing

a=[2,3,45,1,4]
print("Copying a list using the copy() method")
b = a.copy()
print("Original list:", a)
print("Copied list using copy():", b)
print("Copying a list using the list() constructor")
b = list(a)
print("Copied list using list():", b)
print("Copying a list using slicing")
b = a[:]
print("Copied list using slicing:", b)


#Identitiy operations on lists
print("Identity operations on lists")
list3 = [1, 2, 3]
list4 = list3
print("list3 is list4:", list3 is list4)
print("list3 is not list4:", list3 is not list4)

#Membership operations on lists
print("Membership operations on lists")
list5 = [1, 2, 3, 4, 5]
print("1 in list5:", 1 in list5)
print("6 in list5:", 6 in list5)
print("list5 in list5:", 10 not in list5)


