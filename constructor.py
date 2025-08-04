#default constructor/non parameterised constructor:
class demo:
    def __init__(self): #also known as special method 
        print("constructor")
    def f1(self):
        print("f1")
obj=demo()
obj.f1()
#NOTE: constructor only executes once

#parameterised constructor:
class desk:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def f1(self):
        print(self.a,self.b)
obj=desk(10,20)
obj.f1()
print(obj.__dict__)
obj1=desk(30,60)
obj1.f1()
print(obj1.__dict__)

# constructor overloading is not supported in python also function overloading is not
# class focus:
#     def __init__(self):
#         print("default")
#     def __init__(self,a,b):
#         print("parameterised")
# obj=focus()
# obj1=focus(20,40)

#example of parameterised constructor:
class employee:
    def __init__(self,a,b,c,d):
        self.emp_name=a
        self.salary=b
        self.mob_numb=c
        self.position=d
    def f1(self):
        print(self.emp_name)
        print(self.salary)
        print(self.mob_numb)
        print(self.position)
obj=employee("anushka",40000,1234,"BM")
obj1=employee("anu",20000,246,"SOD")
obj2=employee("mauu",12000,234679,"BOM")
obj.f1()
obj1.f1()
obj2.f1()

#GETTER AND SETTER METHOD:
class student:
    def setName(self,a):
        self.name=a
    def getName(self):
       print(self.name)
    def setNum(self,b):
        self.num=b
    def getNum(self):
       print(self.num)
    def setAge(self,c):
        self.age=c
    def getAge(self):
       print(self.age)
obj=student()
obj.setName("anushka")
obj.setNum(57)
obj.setAge(19)
obj.getName()
obj.getNum()
obj.getAge()
print(obj.__dict__)
obj1=student()
obj1.setName("anumaa")
obj1.getName()
print(obj1.__dict__)

class mau:
    x=1
    def __init__(self,p):
        self.a=p
d=mau(10)
mau.x=100
print(d.__dict__)
print(mau.__dict__)
d1=mau(20)
print(d1.__dict__)
print(mau.__dict__)

