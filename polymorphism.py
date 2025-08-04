#function overloading
class focus:
    def __init__(self,*a):
        print(a)
    def f1(self,a=10):
        print(a)
f=focus(10)
f1=focus()
f2=focus(1,2,3)
f2.f1(1000)
#in python, variable argument and default parameter are ways through which
#we can achieve function overloading

#addition:
class add:
    def add(self,*add):
        print(sum(add))
f=add()
f.add(10,20,45,90)
    

#area:
from math import pi
class area:
    def calculate_area(self,l=0,b=0):
        if l!=0 and b==0:
          print("SQUARE AREA",l**2)
          print("CIRCLE AREA",pi*l*l)
        elif l!=0 and b!=0:
            print("REACTANGLE AREA",l*b)
            print("TRIANGLE AREA",0.5*l*b)
obj=area()
obj.calculate_area(20)
obj.calculate_area(10,20)

