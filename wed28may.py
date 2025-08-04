# id,type,len
# general purpose functions of string


a="Python@12345"
b="Python@12345"

print("a==b:",a==b)
print("a!=b:",a!=b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)
print("a<b:",a<b)
print("a>b:",a>b)



# program to take take a 2 string from user and check whether they are equal or not

string1=input("Enter a string:")
string2=input("Enter asecond string:")

# print("Equal ",string1==string2)

if string1==string2:
    print("equal:")
else:
    print("not equal:")


a="hElLo WoRlD"

print(a*3)
print("hi"+a)
print("length",len(a))

# strings methods

print("capitalize",a.capitalize())

print("capitalize",a.lower())


print("capitalize",a.upper())

print("capitalize",a.swapcase())


print("capitalize",a.title())

print("capitalize",a.casefold())


s1="Straeß"

print(s1.lower())
print(s1.casefold())


# center    width,sign
print(s1.center(10))
print(s1.center(150,'*'))
print("count(string):","126547852121".count("2"))
print("count(string):","126547852121".count("2",5,10))



print("Endswith(suffix)","458745211387".endswith("1"))
print("Endswith(suffix,start,end)","458745211387".endswith("3",5,10))

print("Endswith(prefix)","458745211387".endswith("1"))
print("Endswith(prefix,start,end)","458745211387".endswith("1",5,10))
