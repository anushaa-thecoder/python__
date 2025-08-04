class focus:
    def f1(self):
        print("anuma")
        print(id(self))
obj=focus()
print(id(obj))
obj.f1()
obj1=focus()
print(id(obj1))
obj1.f1()


class student:
    def info(self):
        self.name="anuma"
        self.num=30
    def display(self):
        print(self.name)
        print(self.num)
obj=student()
obj.info()
obj.display()
obj.marks=50
print(obj.__dict__)

obj1=student()
obj1.info()
obj1.display()
print(obj1.__dict__)


class emp:
    def info(self,a,b,c):
        self.name=a
        self.age=b
        self.salary=c
    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
obj=emp()
obj.info("anuma", 30, 2000000)
obj.display()
print(obj.__dict__)

obj1=emp()
obj1.info("anuu", 40, 100000)
obj1.display()
print(obj1.__dict__)



class bank:
      def accept(self,a,b,c):
          self.customer_name=a
          self.acc_num=b
          self.balance=c

      def deposit(self):
          self.dep=int(input("enter amt you want to deposit?"))
          self.balance=self.dep+self.balance
          print(self.balance)
           
      def withdrawl(self):
          self.wit=int(input("enter amt you want to withdrawl"))
          if self.balance>self.wit:
              self.balance=self.balance-self.wit
              print(self.balance)
          else:
              print("insuficcient balance for withdrawl of money!!")
      def display(self):
          print(self.customer_name)
          print(self.acc_num)
          print(self.balance)
          
obj=bank()
obj.accept("anushka",12345,50000)
obj.deposit()
obj.withdrawl()
obj.display()
print(obj.__dict__)


class rectangle:
    def accept(self):
        self.len=int(input("enter length:"))
        self.bre=int(input("enter breadth"))

    def calculate(self):
         self.area=self.len*self.bre
         print(self.area)

obj=rectangle()
obj.accept()
obj.calculate()
print(obj.__dict__)

#make order class 
#consists of instance var:
#1. p name, p quant, p price, disc, total
#1st accept function : from user name quan price
#2nd cal total func
#3rd calculate disc : if total amt>500, 5%
#if total amt>1000,15%
#if total amt>2000,30% 
#else no disc
#4th display func

class order:
    def acc(self):
        self.p_name=(input("enter product:"))
        self.p_quant=int(input("enter product quantity:"))
        self.p_price=int(input("enter product price:"))

    def tot(self):
        self.total=self.p_quant*self.p_price

    def calcu(self):
        if self.total>500:
            self.disc=self.total*0.05
        elif self.total>1000:
            self.disc=self.total*0.15
        elif self.total>2000:
            self.disc=self.total*0.30
        else:
            print("NO DISCOUNT,SORRY!!")

    def disp(self):
        print("PRODUCT:",self.p_name)
        print("QAUNTITY:",self.p_quant)
        print("PRICE:",self.p_price)
        print("TOTAL:",self.total)
        print("DISCOUNT:",self.disc)
        print("TO PAY:",self.total-self.disc)
obj=order()
obj.acc()
obj.tot()
obj.calcu()
obj.disp()


#class variable:
class demo:
    x=1
    def __init__(self):
       demo.y=2
       print(demo.y)
    def f1(self):
        demo.z=3
        print(demo.z)
        print(demo.x)
d=demo()
demo.a=4
print(demo.a)
d.f1()
print(demo.__dict__)

#WAP to track number of objects created for given class
class demo:
   x=0
   def __init__(self):
     demo.x+=1
d=demo()
d1=demo()
print("num of objs:",demo.x)

class demo:
    def f1(x,self):
        print(self)
d=demo()
d.f1(10)

class demo:
    x=10
    def f1(self):
        self.y=20
d1=demo()
d2=demo()
d1.x=30
d1.y=40
demo.x=20
d2.f1()
print(d1.x,d1.y,d2.x,d2.y)


class demo:
    a=30
    def f1(self):
        self.b=40
        self.c=50
d=demo()
d.f1()
print(demo.a, d.b, d.c)
d1=demo()
d1.f1()
demo.a=100
print(demo.a, d.b, d.c)

#
class clg:
    def __init__(self):
        self.name="AHMEDNAGAR CLG"
        self.dep="BSC CA"
    def print(self):
        print(self.name)
        print(self.dep)
class stu:
    def __init__(self):
        self.sname="ANUSHKA"
        self.num=9789098765
    def adm(self,o):
        self.a=o
    def print1(self):
        print(self.sname)
        print(self.num)
        self.a.print()
d=clg()
d1=stu()
d1.adm(d)
d1.print1()




