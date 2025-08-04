class demo:
    x=10
    def f2(self):
        self.a=100
        print(self.a)
    @classmethod
    def f1(self):
        print(self.x)
        #print(self.a)
demo.f1()
d=demo()
d.f2()

class mau:
    def f1():
        print("mauuuuu")
mau.f1()
d=mau()
#d.f1() by using object name we cant call f1 method because it is a static method

class mau:
    @staticmethod
    def f1():
        print("mauuuuu")
    def f2(self):
        print("mauuuuu")
mau.f1()
d=mau()
d.f2()
#mau.f2() due to f2 is instance method cant be called with class name
#d.f1() by using object name we cant call f1 method because it is a static method



#class emp
#1.user kadhun emp id ghayyaychi ani tyala validate kaaraychay using static method
#condn: emp starting ani len 6
#1st method constructor:
#emp name id position department
#2.instance method :#promotion if posistion frsher do junior if junior do senior if senior
#do head
#3.branch transfer method: 3 condns
#4. display func: all info of that func


class anumaa:
    a=10 #public
 #   __b=20 private
    _c=30 #protected
print(anumaa.a)
print(anumaa._c)
#print(anumaa.__b)

class demo:
    def f1(self):
        print("public")
    def __f2(self):
        print("private")
    def _f3(self):
        print("protected")
d=demo()
d.f1()
d._f3()
#d.__f2()




class demo:
    def d1(self):
        self.x=10
    def __add__(self,a):
        return self.x+a.x
    def __sub__(self,a):
        return self.x-a.x
    def __mul__(self,a):
        return self.x*a.x
    def __gt__(self,a):
        return self.x>a.x
d=demo()
d2=demo()
d.d1()
d2.d1()
print(d+d2)
print(d-d2)
print(d*d2)
print(d>d2)

class comp:
    def __init__(self,a,b):
        self.i=a
        self.j=b
    def __add__(self,x):
        return self.i+x.i, self.j+x.j
ob=comp(10,20)
obj=comp(10,20)
print(ob+obj)

"""create bank acc class which contains three instance variables which contains acc holder name,
name,initial bal and acc number it contains instance method depo and withd
combine accs using operator overloading concept then transfer funds using operator overloading concepts 
and then compare balance of 2 accs"""

class bank:
    def __init__(self,name,bal,num):
        self.acc_holder_name=name
        self.initial_bal=bal
        self.acc_num=num
    def depo(self):
        self.dep=int(input("enter deposit amount:"))
        self.total_balance=self.initial_bal+self.dep
        print(self.total_balance)
    def withd(self):
        self.withdrawl=int(input("enter withdrawl amount:"))
        if self.initial_bal>self.withdrawl:
         self.total_balance=self.initial_bal-self.withdrawl
         print(self.total_balance)
        else:
            print("Insufficient balance to withdraw!")
    def __add__(self,a):
        return self.dep+a.dep
b=bank("anushka",10000,2343232)
b1=bank("anuma",20000,897921)
b.depo()
b.withd()
print(b+b1)