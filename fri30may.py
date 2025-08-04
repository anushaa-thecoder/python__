# 30/05/2025


print("asdvb@ghm.com".just(20))
print(" ".rjust(20,'*'))

print("python".ljust(20))
print("python".ljust(20,'*'))

print("     python    ")
print("      python    ".strip())
print("sssspython".strip('s'))
print("python".lstrip())
print("    python".lstrip('s'))

print("python    ".rstrip())
print("python".rstrip('s'))


a="Python"
print("@@@@".join("python0"))

print("python".zfill(20))

b=a.maketrans('y','@')
print(b)
print(a.trnaslate(b))
print(a)
b=a.maketrans('y','@','o')
print(b)
print(a.trnaslate(b))


a='f\th\thd\tdf'

print(a[:-3].expandtabs(4))

# #  program to take a string from a user and check whetger the string upper oot not 
# if yes==convert lower case


n=input("ENter a string:")
if n.isupper():
    print(n.lower())

else:
    print(n)



# # to take a 2 strings from user and if ==replace first ch both sttring ($)
# else replace first ch with @


n=input("Enter a string:")
s=input("Enter a string:")
if n[0]==s[0]:
    print(s.replace(s[0],'$'))
    print(n.replace(n[0],'$'))

else:
    print(s.replace(s[0],'@'))
    print(n.replace(n[0],'@'))




#  to count digits alphabets ,special, symbols in a guiven string 

count=0
count1=0
count2=0

n=input("Enter a string")

for i in n:
    if i.isdigit():
        print()
        count+=1
    elif i.isalpha():
        print()
        count1+=1
    else:
        print()
        count2+=1
print("digits:",count,"alphabets:",count1,"special symbols:",count2)



# to take a string from user 
# and take a character from user
#  and find whether given character is in string or not
# if yes==replace ch  with # and fill given string with 3'0
# else :  fill 5'0

n=input("Enter string:")
s=input("Enter a character")

if s in n:
     p=n.replace(s,'#')
    #  print(n,p.zfill(10))
     print(p.zfill(len(s)+10))
else:
    print(n.zfill(len(n)+5))
    

    


1.
# # to string from user and check given string lower or not
# if yes==count first ch of string and split using [0] character
# else:
#     convert lowercase and partition using [1]

count=0
string=input("Enter a string:")

if string.islower():
    if string[0] in string:
        print(string.split(string[0]))
        print(string.count(string[0]))
else:
    part=string.lower()
    print(part.partition(part[1]))
    print(string.count(string[1]))

# 2.string[0]===replace string ==0 with $


string=input("Enter a string:")
# re=string[0]
print(string.replace(string[0],'$'))