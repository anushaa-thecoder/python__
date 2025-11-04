import re

#1. Search function = it means it search all string
p=r"a|z"
s=input("enter a string:")
r=re.search(p,s)
print(r)
print(type(r))

a=r"a|z"
s=input("Enter a string:")
c=re.search(a,s,re.I)
if(c):
    print("found",c.group(),c.start(),c.end())
else:
    print("Not found!")



# 2.match function = it means it only search 1st occourence
p=r"[0-9]{2}"
s=input("Enter a string:")
r=re.match(p,s)
if r:
    print("Found",r.group(),r.start(),r.end())
else:
    print("Not found!")


#write a program to validate 1st name of a user which contain only alphanumeric character with length min 2 max 10
name=r"^[a-zA-Z0-9]{2,10}$"
user=input("Enter username:")
r=re.search(name,user)
if r:
    print("Validate")
else:
    print("Not validate!")

#pincode are valid or not
p="^4[0-4][1-9]{4}$"
s=input("Enter pincode:")
r=re.search(p,s)
if r:
    print("Valid")
else:
    print("Invalid!")

#url grouping:
import re as r
s= "https://regex101.com or http://RegExp.org  or https://regexr.com"
p = r"https?://\w+\.\w+"
l=r.findall(p,s)
print(l)

#credit card pattern:
import re as r
p=r"\d{4}-\d{4}-\d{4}-\d{4}$"
s=input("Enter credit card number:")
l=r.findall(p,s)
print(l)


#credit card pattern(capturing group):
import re as r
p=r"(\d{4})-(\d{4})-(\d{4})-(\d{4}$)"
s=input("Enter credit card number:")
l=r.search(p,s)
print(l.group(),l.group(1),l.group(2),l.group(3))

#wont run as it is not grouped
# import re as r
# p=r"\d{4}-\d{4}-\d{4}-\d{4}$"
# s=input("Enter credit card number:")
# l=r.search(p,s)
# print(l.group(),l.group(1),l.group(2),l.group(3))

#non capturing:
# (?:) syntax
import re as r
p=r"(?:\d{4})-(\d{4})-(\d{4})-(\d{4}$)"
s=input("Enter credit card number:")
l=r.search(p,s)
print(l.group(),l.group(1),l.group(2),l.group(3))
# print(l.group(),l.group(2),l.group(3),l.group(4)) error as 1st grp is not captured

import re as r
s="""<h1> Python </h1>  
  <i> Python </i>"""
p=r"</?\w+>"
l=r.findall(p,s)
print(l)

import re as r
s="<h1>Python</h1>  or <i>Python</i>"
p=r"(<\w+>(?:\w+)?</\w+>)+"
l=r.findall(p,s)
print(l)

import re as r
s=input("Enter string:")
p=r"(<\w+>(?:\w+)?</\w+>)+"
l=r.findall(p,s)
print(l)

#back refrencing:
import re as r
s=input("Enter string:")
p=r"(\w+)\1"
l=r.findall(p,s)
print(l)

import re as r
s=input("Enter string:")
p=r"(\w)(\w)\1"
l=r.search(p,s)
print(l.group())

import re as r
s=input("Enter string:")
p=r"\b\w*(\w)\1\w*\b"
l=r.search(p,s)
print(l.group())
 
# len min 8 or more upcase lowcase digit
import re as r
s=input("Enter string:")
p=r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)"
if r.findall(p,s):
    print("pass")
else:
    print("fail")


import re as r
t="this is a split by regex"
s=r.split(r'\s+',t,2)
print(s)

import re as r
t="apple,banana;cherry,pineapple"
s=r.split(r'[,;]',t)
print(s)

import re as r
s=input("enter a string:")
p=r.split(r'[!@#$%^&*]',s)
print(p)

import re as r
s='python programming'
o=r.sub(r'\s+','$',s)
print(o)

import re as r
s='this is test123 program45'
o=r.sub(r'\d+','',s,1)
print(o)

#write a program to take a mob no. from user and change 
#first 6 digits with special symbols with regex
import re as r
s=input("enter mobile number:")
o=r.sub(r'\d','*',s,count=6)
print(o)

import re as r
s=input("enter IP address:")
o=r.sub(r'[0]','',s)
print(o)

#extract only prices:
import re as r
s="""
<div class="product">
    <h2>Shirt</h2>
    <span class="price">$19.99</span>
</div>
<div class="product">
    <h2>Shoes</h2>
    <span class="price">$49.50</span>
</div>
<div class="product">
    <h2>Bag</h2>
    <span class="price">₹299</span>
</div>
<div class="product">
    <h2>Watch</h2>
    <span class="price">€75.25</span>
</div>
"""
o=r.findall(r'[\$|€|₹]\d+(?:\.\d{2})?',s)
print(o)

import re as r
p=r'.com'
t="examplecom"
m=r.search(p,t)
print(m.group())

