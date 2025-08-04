class Person:
    def __init__(self,name,age,number):
        self.name=name
        self.age=age
        self.phone_number=number
class TravelDetails:
    def __init__(self,mode):
        self.travel_mode=mode
class Tourist(Person,TravelDetails):
      def display(self):
        print(self.name)
        print(self.age)
        print(self.phone_number)
        print(self.travel_mode)
class TouristManagementSystem(Tourist):
    def __init__(self,a,b,c,d):
       Person.__init__(self,a,b,c)
       TravelDetails.__init__(self,d)
    def validate_name(self):
        if self.name.isalpha():
            print("Name is valid")
        else:
            print("Please enter valid name")
    def validate_phone(self):
        if self.phone_number.isdecimal() and len(self.phone_number)==10:
            print("Phone number valid")
        else:
            print("Please enter valid phone number")
    def validate_age(self):
        if self.age>=60 and self.age<=99:
            print("Valid age")
        else:
            print("Please enter a valid age")
    def validate_travel_mode(self):
        if self.travel_mode.lower()=="airways" or self.travel_mode.lower()=="ROADWAYS":
            print("YOUR TRAVEL MODE IS:",self.travel_mode)
        else:
            print("Enter valid travel mode")
    def generate_tourist_id(self):
        na=self.name[0:2]
        ag=self.age
        pn=self.phone_number[0:2]
        tm=self.travel_mode[0:2]
        print("Tourist id generated sucessfully:",na.upper()+str(self.age)+pn+tm.upper())

n=input("ENTER YOUR NAME:")
a=int(input("ENTER YOUR AGE:"))
p=input("ENTER YOUR PHONE NUMBER:")
m=input("ENTER YOUR TRAVEL MODE(AIRWAYS/ROADWAYS):")
obj=TouristManagementSystem(n,a,p,m)
obj.display()
obj.validate_name()
obj.validate_age()
obj.validate_phone()
obj.validate_travel_mode()
obj.generate_tourist_id()

