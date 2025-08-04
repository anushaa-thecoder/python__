
#letters pattern: 
# 29/05/2025

# to print take a string from user and print even part and odd part differently using slicing

s=input("Enter your string:")
# count=2

print(s[0: :2])
print(s[1: :2])



s="python"

print(s.find('y'))   # if true returns 1
print(s.rfind('y,2,5'))   # if false then returns -1
print(s.index('t'))
print(s.index('t',2,5))
# if not then value error
print(s.rindex('t'))
print(s.rindex('t',2,5))


s1=s.replace('p','r')
print(s1)
print(s.replace('p','r'))
print(s.replace('p','r',2))   #2 is optional i.e. count
print(id(s))
print(id(s1))



s='Python'
print(s.isalnum())  # alpha +  numbers
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isspace())   
print(s.isalpha())  # all aphabets
print("\u1255".isdecimal())  # 0to 9
print(s.isdigit())    #0 to 9, sub,sup,unicode
print(s.isnumeric())    #0 to 9, sub,sup,fraction,roman


print("abcper".isprintable())
print("abc\tper".isprintable())
print("abcper".isidentifier())
print("123abcper".isidentifier())
print("_abcper".isidentifier())
print("abc$per".isidentifier())
print("-abcper".isidentifier())


u='sdfgh$fghj$122'
print(u.split())
print(u.split('$',2))
print(u.split('$'))



u="sdfgh$erty231"
print(u.partition("$"))


# to check given string is palindrome or not

n=input("Enter a number:")

print("Palindrome ",n[::]==n[::-1])

n=input("Enter a number:")

if n==n[::-1]:
    print("pali")
else:
    print(("not"))


#   get astring made up of the frist two and last two characters of a given string
# if str len <2  then print empty

n=input("Enter a number:")
if len(n)<2:
    print("empty string:")
else:

    s=n[0:2]
    p=n[:2:-1]

    print(s+p)



#to add ing at the end of the given string (len should be atleast 3)
# if given str aleady ends with ing then + ly at end
# if lenstr<3 print original string 



s=input("Enter a string:")

if s.endswith("ing"):
    print(s[:-3]+"ly")

if len(s)<=3:
    print(s)