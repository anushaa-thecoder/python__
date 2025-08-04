#ex of writting from a binary file
with open("example.bin","wb") as f:
    f.write(b"hello world")

#ex of reading from a binary file
with open("example.bin","rb") as f:
    print(f.read())

#ex of appending from a binary file
with open("example.bin","ab") as f:
    f.write(b"helloooieee")



#NOTE:  extensions in binary files creating are: .bin and .dat

#ex of writting and reading from a binary file
with open("example.dat","wb+") as f:
    f.write(b"hello mauuuuuuu")
    f.seek(0)
    print(f.read())


#ex of reading and writing from a binary file
with open("example.dat","rb+") as f:
    print(f.read())
    f.write(b"helloo kuchuupuchuuuuu")
    f.seek(0)
    print(f.read())


#ex of appending and reading from a binary file
with open("example.dat","ab+") as f:
    print(f.read())
    f.write(b"helloo manyaaaaa")
    f.seek(0)
    print(f.read())

#reading the img
with open("1599659127400.jpg","rb") as f:
    a=(f.read())
    print(a)

#copying img from one file to another file
with open("1599659127400.jpg","rb") as f:
    a=(f.read())
    print(a)
with open("new.jpg","wb") as f1:
    b=f1.write(a)


import pickle
data =[1,2,3,4,5]
with open("data.bin","wb") as f:
    pickle.dump(data,f)
    
with open("data.bin","rb") as f:
    d=pickle.load(f)
    print(d)    


import pickle
d={'name':'mauu','age':12}
with open("data.bin","wb+") as f:
    pickle.dump(d,f)
    f.seek(0)  #pointer at starting
    g=pickle.load(f)
    print(g)



import pickle
b=[]
for i in range(5):
  a=int(input("enter a number:"))
  b.append(a)
a=[1,3,4,5,6,7]
with open("data.dat","wb+") as f:
    pickle.dump(b,f)
    pickle.dump(a,f)
    f.seek(0)
    o=pickle.load(f)
    print(o)
    p=pickle.load(f)
    print(p)


import pickle
d={}
for i in range(2):
  n=input("enter a name:")
  r=input("enter roll number:")
  d[n]=r
with open("data.dat","wb+") as f:
    pickle.dump(d,f)
    f.seek(0)
    print(pickle.load(f))


         
#Write a program to create a function named as search_student ()
#  that searches for a name in the binary file and display the roll number.
import pickle
def search_student(name_to_search):
    with open('data.bin', 'rb') as f:
            student_data = pickle.load(f)
            if student_data['name'] == name_to_search:
                print("Roll Number:", student_data['rollno'])
            else:
                print("Name not found.")

name= input("Enter the name to search: ")
search_student(name)


#write a program to create a function named as update_student()
#that updates the roll number of a student in the binary file
import pickle
def update_student(new_name,new_rollnum):
    with open("data.bin",'rb') as f:
        data = pickle.load(f)

    if data['name']==new_name:
        data['rollno']==new_rollnum
        with open("data.bin","wb") as f:
            pickle.dump(data,f)
        print("roll number updadated sucessfully:")
    else:
        print("name not found!")
 
new_name=input("ENTER THE NAME TO UPDATE:")
new_rollno=input("ENTER THE NEW ROLL NUMBER TO UPDATE:")
update_student(new_name, new_rollno)



import pickle
l=[]
list1=int(input("enter itemcode:"))
l.append(list1)
l1=[]
for i in range(3):
    list2=int(input("enter amount:"))
    l1.append(list2)
l.append(l1)
with open("sales.bin",'wb+') as f:
    pickle.dump(l,f)
    f.seek(0)
    r=pickle.load(f)
    print(r)
    print(sum(l[1]))



import pickle
l1=[]
l2=[]
l3=[]
l4=[] 
count=0
for i in range(3): 
    list1=int(input("enter admission number:"))
    l2.append(list1)
    list2=(input("enter name:"))
    l3.append(list2)
    list3=int(input("enter marks:"))
    l4.append(list3)
l1.append(l2)
l1.append(l3)
l1.append(l4)
# print(l1)
with open("students.dat",'wb+') as f:
    pickle.dump(l1,f)
    f.seek(0)
    r=pickle.load(f)
    # print(r)
    for j in range(len(r)):
        for i in (r[2]):
          if (i>=75):
            print(r[j][j])
            count+=1
          else:
              print("try again!")
print(count)


