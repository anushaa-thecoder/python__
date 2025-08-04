from abc import ABC, abstractmethod
class focus(ABC):
    @abstractmethod
    def f1(self):
        pass
# s=focus()
# s.f1()  

class anu(focus):
    def f1(self):
        print("hello")
a=anu()
a.f1()

#payment gateway:
"""class payment gateway which is inherited from abc class which contains two abstract methods :
1st pay and 2nd refund both contain a parameter amount, derive class credit card from payment gateway
and implement abstr methods then derive upi payment class from payment gateway which implements 
abstract methods"""
from abc import ABC, abstractmethod
class payment_gateway(ABC):
    @abstractmethod
    def pay(self):
        pass
    def refund(self):
        pass
class credit_card(payment_gateway):
    def pay(self):
        self.pay=int(input("enter amt to be paid using card:"))
        print("paid amount:",self.pay)
    def refund(self):
        self.refund=int(input("enter amt to be refunded using card:"))
        print("refunded amount:",self.refund)
class upi(payment_gateway):
    def pay(self):
        self.pay=int(input("enter amt to be paid using upi:"))
        print("paid amount:",self.pay)
    def refund(self):
        self.refund=int(input("enter amt to be refunded using upi:"))
        print("refunded amount:",self.refund)
u=upi()
c=credit_card()
c.pay()
c.refund()
u.pay()
u.refund()
