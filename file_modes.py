#r+ mode: read and write
f=open("anu.txt","r+")
print(f.read())
f.write("python")
print(f.tell()) #tell: current pointer position
print("___________")
f.seek(0)  #seek: sets pointer to specified position 
print(f.read())

#w+ mode:write and read 
f=open("anu.txt","w+")
f.write("python")
print(f.tell()) #tell: current pointer position
print("___________")
f.seek(0)  #seek: sets pointer to specified position 
print(f.read())

#a+ mode: append and read
f=open("anu.txt","a+")
print(f.read())
f.write("python")
print(f.tell()) #tell: current pointer position
print("___________")
f.seek(0)  #seek: sets pointer to specified position 
print(f.read())

with open("anu.txt","r") as f:
    print(f.read())
    print()
    print("***************")
    print("information of file")
    print(f.name)
    print(f.mode)
    print(f.readable())
    print(f.writable())
print(f.closed)
    

# x mode: it will create new file if it doesnot exits
# and if it is already existed it gives error 
f=open("ab2.txt","x")
f=open("ab2.txt")
print(f.read())


