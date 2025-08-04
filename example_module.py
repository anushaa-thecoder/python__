#WAP that generates random alphabetical character
import random
import string
print(random.choice(string.ascii_letters))

#WAP to
import random
import string
print(random.choices(string.ascii_letters, k=8))
s=" "
for i in range(8):
    s=s+random.choice(string.ascii_letters)
print(s)

#wap to generate password
import random
import string
a=""
for i in range(4):
    a=a+random.choice(string.ascii_letters)+random.choice(string.digits)+random.choice(string.punctuation)
print(a)

#to select random element from set,dict,list value
import random
# import string
a=set()
for i in range(3):
    b=int(input("enter set elements:"))
    a.add(b)
print(type(a))

b=[]
for i in range(3):
    n=(int(input("enter list ele:")))
    b.append(n)
print(b)

d={}
for i in range(3):
  k=input("enter a key:")
  v=input("enter value:")
  d[k]=v
print(list(d))

print(random.choice(list(a)))
print(random.choice(b))
print(random.choice(list(d.values())))

