# skip the 6 ,12,18 and print the 1 to 50 between no 
for i in range(51):
    if(i==6 or i==12 or i==18):
        continue
    else:
        print(i)
#   pattern
for i in range(3):
    print(i, end=" ")

# ***
# ***
# ***
for i in range(3):
    for j in range(3):
        print("*",end=" ")
    print()

# 111
# 222
# 333
for i in range(1,4):
    for j in range(3):
        print(i,end=" ")
    print()

# 012
# 012
# 012
for i in range(3):
    for j in range(3):
        print(j,end=" ")
    print()

# aaa
# bbb
# ccc
a=65
for i in range(3):
    for j in range(3):
        print(chr(a),end="")
    a+=1
    print()
# homework
a='A'
for i in range(3):
    for j in range(3):
        # print(chr(a),end="")
     ord(a)(a=+1)
    print()
 
# while loop
i=0
while(i<3):
    j=0
    while(j<3):
        print("*",end=" ")
        j+=1
    print()
    i=i+1

# *
# **
# ***
# ****
# *****
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()

# ****
# ***
# **
# *
for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
# 4444
# 333
# 22
# 1
for i in range(4,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()

#   *
#  * *
# * * *
rows=3
for i in range(1,rows+1):
    for k in range(rows-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
#   *
#  **
# ***

rows=6
for i in range(1,rows-2):
    for k in range(rows+2):
        print(" ",end="")
    for j in range(i+4):
        print("*",end="")
    print()  

# 1
# 23
# 456
# 78910
c=1
for i in range(4):
    for j in range(i+1):
        print(c,end=" ")
        c+=1
    print()