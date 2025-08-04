#accepts a string and count the number of upper and lower case letter
# a=0
# b=0
# def f1(s):
#     for i in s:
#         if(i.isupper()):
#             global a
#             a+=1
#         elif(i.islower()):
#             global b
#             b+=1
# s=input("Enter a string:")
# f1(s)
# print(a)
# print(b)

#1:accepts list having even number of elements and swap the elements at adjacent position
#2:accept a number and check whether its a perfect number or not



#1
def swap(list):
    if len(list)%2!=0:
        print("must have even numbers")
    for i in range(0,len(list),2):
        list[i],list[i+1]=list[i+1],list[i]
    return list
list=list(input("enter list:"))
print("list:",list)
result=swap(list)
print("swapped list:",result)