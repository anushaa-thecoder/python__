#create timer using tkinter
from tkinter import*
import datetime as dt
import winsound as w
c=Tk()
c.title("TIMER")
c.iconbitmap(r"C:\Users\DEll\Downloads\3003202.ico")
l=Label(c,text=10,bg="pink",fg="black",width=50,height=10,font=("arial black",100))
l.pack()
t=10
def updatetime():
    global t
    if t>=0:
        l.config(text=f"Timer:{t}")
        t=t-1
        c.after(1000,updatetime) #1000= only milisecs are allowed in this syntax
    else:
         w.Beep(1000,2000)
updatetime()
c.mainloop()

#datetime:
from tkinter import *
from tkinter import ttk
import datetime as d
c= Tk()
c.title("datetime")
# c.iconbitmap(r'C:\Users\hp\Desktop\advance python\gui  graphical interface\clock.ico')
p=d.datetime.now()
m=p.minute
l=Label(c,text=f'{p.hour}:{m}:{p.second}',fg='black',bg='pink')
l.pack()
c.mainloop()
