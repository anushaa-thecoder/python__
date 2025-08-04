f=open("I.txt")
d=f.read()
c=f.readline()   #read line: only read 1st line
a=f.read()       # read complete file
print(d)
print(c)
print(a)
f.close

q=f.readline(2)  # only read 2 characters. size of character which you want to read
print(q)
print(f.readline(3))
f.close()

b=f.readlines()      #it read in list format. it will return list
print(b)
f.close()

#write a program to count number of lines in text file
f=open('kolhe.txt','r')
a=f.readlines()
print(a)
print(len(a))         #count length of list
print(a[6])           #print 6th index line
f.close()
