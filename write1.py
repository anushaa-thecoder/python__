f=open("I.txt",'w')    #if given text file is not existed then created file by default
f.write("Welcome!")
f.close()

#add multiple lines it accept only eterable object
f=open("I.txt",'w')
f.writelines(['abc\n','pqr\n'])
f.close()

#accept file name from user and text file information accept from user
name='diksha.txt'
f=open(name,'w')
l=list(input("Enter list elements:"))
f.writelines(l)
f.close()

#accept information from user and write into the file
name='diksha.txt'
f=open(name,'w')
n=input("Enter name:")
m=input("enter mobile no:")
f.write(n+"\n")
f.write(m)
f.close()