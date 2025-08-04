#write a program to copy content of file 1 to file 2
f=open("I.txt","r")
a=f.read()
f1=open("anu.txt","w")
a=f1.write(a)
f.close()
f1.close()

#2
f=open("I.txt","a")
a=f.write("welcomeeee\n")
f.close()

#3
f=open("I.txt","a")
n=input("Enter name:")
i=(input("enter id:"))
s=(input("enter salary:"))
a=f.write(n+"\n"+i+"\n"+s+"\n")
f.close()

#merge content of 2 files and write in another
f=open("I.txt","r")
f1=open("anu.txt","r")
f2=open("merge.txt","a")
a=f.read()
b=f1.read()
c=f2.write(a+b)
f.close()
f1.close()
f2.close()

#two inputs from user and replace
f=open("merge.txt","r")
name=input("enter name to be replaced:")
nameee=input("enter name to be replaced 1:")
a=f.read()
f=open("merge.txt","a")
b=(a.replace(nameee,name))
d=f.write("\n"+b)
f.close()

#write a program to create a file and enter data in file until user wants
f=open("pqr.txt","a")
while True:
    b=input("Enter data")
    a=f.write("\n"+b)
    c=input("Enter your choice:(y/n)")
    if(c=='n'):
        break
f.close()

