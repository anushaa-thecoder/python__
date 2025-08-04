class A:
    def __init__(self):
        print("constructor 1 of parent class")
class B:
    def __init__(self):
        print("constructor 2  of parent class")
class C(A,B):
    def __init__(self):
        A.__init__(self)
        super().__init__()
        print("constructor of child class")
    
obj=C()



#method overridding: same func name, same para but diff class aka runtime polymorphism
class A:
    def f1(self):
        print("method 1 of parent class")
class B:
    def f1(self):
        print("method 2  of parent class")
class C(A,B):
    def f1(self):
        A.f1(self)
        B.f1(self)
        print("method child ")
    
obj=C()
obj.f1()



#example:
class device:
    def __init__(self,a):
        self.brand=a
        self.battery_level=100
    def use_battery(self,b):
        self.battery=b
        self.used_bat=self.battery_level-self.battery
    def show_device_info(self):
        print(self.brand)
        print(self.battery_level)
        print(self.battery)
        print(self.used_bat)

class network_enabled:
    def __init__(self):
        self.ip_address="10.123.34.09.000"
    def connect(self):
        self.connected=False
        if self.connected==False:
            print("device not connected")
        else:
            print("device connected successfullyyyyy")
    def sync_data(self):
        if self.connected==True:
            print("Device synced!!!!")
        else:
            print("Device not synced")

class smart(device,network_enabled):
    def __init__(self,a):
        super().__init__(a)
        network_enabled.__init__(self)
        self.step=0
        self.heart_rate=72
    def track_steps(self,step_count):
        self.step_done=step_count
        self.step_done+=step_count
    def measure_heartrate(self,rate):
        self.heart=rate
        self.rate_count=self.heart_rate+rate
    def health_summary(self):
        print("current step count:",self.step)
        print("steps completed:",self.step_done)
        print("heart rate:",self.heart_rate)
        print("heart rate increased by:",self.rate_count)
        
    
obj=smart("NOISE")
obj.use_battery(13)
obj.show_device_info()
obj.connect()
obj.sync_data()
obj.track_steps(1000)
obj.measure_heartrate(30)
obj.health_summary()


        
