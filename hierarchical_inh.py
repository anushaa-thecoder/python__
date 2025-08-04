'''Hierarchical Inheritance:'''
class user:
    def __init__(self,a,b):
        self.username=a
        self.email=b
    def display_info(self):
        print(self.username)
        print(self.email)
class customer(user):
    def __init__(self,a,b):
        super().__init__(a,b)
        self.cart=[]
    def add_to_cart(self):
        cart=input("Enter products you want to add to cart:")
        self.cart.append(cart)
        print(cart,"added to",self.username,"cart")
    def view_cart(self):
        print(self.cart)
class seller(user):
    def __init__(self,a,b):
        super().__init__(a,b)
        self.inventory=[]
    def add_product(self):
        prod=input("enter product name:")
        self.inventory.append(prod)
        print(prod,"added to",self.username,"inventory")
    def view_product(self):
        print(self.inventory)
class admin(user):
    def __init__(self,a,b):
        super().__init__(a,b)
        self.permi=[]
    def permission(self):
        self.permi.append("manage_user")
        self.permi.append("manage_site")
        self.permi.append("view_report")
    def display_inventory(self):
        print(self.permi)    


c=customer("anushka", "anushka123@gmail.com")
c.add_to_cart()
c.view_cart()
c.display_info()
s=seller("seller","seller213@gmail.com")
s.add_product()
s.view_product()
a=admin("admin","admin345@gmail.com")
a.permission()
a.display_inventory()

