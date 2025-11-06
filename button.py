from tkinter import ttk
from tkinter import*
win=Tk()
win.title("Button")
win.iconbitmap(r"C:\Users\DEll\Downloads\python_18894.ico")
win.config(bg='black')
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}') 
btn=Button(win,text="Click",height=20,width=30,font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="yellow",activeforeground="red",bd=50)
btn.pack()
win.mainloop()

#button with function:
from tkinter import ttk
from tkinter import*
win=Tk()
win.title("Button")
win.iconbitmap(r"C:\Users\DEll\Downloads\python_18894.ico")
win.config(bg='black')
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}') 
def show():
    btn.config(text="CLOSE")
btn=Button(win,text="OPEN",height=20,width=30,font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="yellow",activeforeground="red",bd=50,command=show)
btn.pack()
win.mainloop()


#change the bg colour when clicked on button:
from tkinter import ttk
from tkinter import*
win=Tk()
win.title("Button")
win.iconbitmap(r"C:\Users\DEll\Downloads\python_18894.ico")
win.config(bg='black')
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}') 
def show():
    btn.config(text="CLOSE",bg="yellow")
btn=Button(win,text="OPEN",height=20,width=30,font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="yellow",activeforeground="red",bd=50,command=show)
btn.pack()
win.mainloop()

#button with lambda function:
from tkinter import ttk
from tkinter import*
win=Tk()
win.title("Button")
win.iconbitmap(r"C:\Users\DEll\Downloads\img4.ico")
win.config(bg='black')
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}') 
def show(A):
    btn.config(text=f"Hello {A}",bg="pink")
user=input("enter a name:")
btn=Button(win,text="HELLO",height=20,width=30,font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="white",activeforeground="pink",bd=50,command=lambda:show(user))
btn.pack()
win.mainloop()


#multiple button with commands:
from tkinter import ttk
from tkinter import*
win=Tk()
win.title("Button")
win.iconbitmap(r"C:\Users\DEll\Downloads\python_18894.ico")
win.config(bg='black')
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}') 
labeling=Label(win,text='CLICK BUTTON',bg='pink',fg='black',
font=('Arial Black',14,'italic'),width=40,height=5,cursor='plus',
relief='groove')
labeling.pack()
def show1():
    labeling.config(text="HII")
def show2():
    labeling.config(text="GOODBYEEE")
btn1=Button(win,text="HELLO",font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="pink",activeforeground="white",bd=50,command=show1)
btn2=Button(win,text="BYE",font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="pink",activeforeground="white",bd=50,command=show2)
btn1.pack()
btn2.pack()
win.mainloop()


#as per the button change the bg colour:
from tkinter import ttk
from tkinter import*
import winsound as w
win=Tk()
win.title("Button")
win.iconbitmap(r"C:\Users\DEll\Downloads\python_18894.ico")
win.config(bg='black')
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}') 
labeling=Label(win,text="CLICK BUTTON TO CHANGE COLOUR",bg='pink',fg='black',
font=('Arial Black',14,'italic'),width=40,height=5,cursor='plus',
relief='groove')
labeling.pack()
def show1(A):
    w.Beep(1000,2000)
    win.config(bg='red')
    labeling.config(text="YOU SELECTED RED")
def show2(B):
    w.Beep(1000,2000)
    win.config(bg='green')
    labeling.config(text="YOU SELECTED GREEN")
def show3(C):
    w.Beep(1000,2000)
    win.config(bg='blue')
    labeling.config(text="YOU SELECTED BLUE")
btn1=Button(win,text="RED",font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="pink",activeforeground="white",bd=10,command=lambda:show1("RED"))
btn2=Button(win,text="GREEN",font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="pink",activeforeground="white",bd=10,command=lambda:show2("GREEN"))
btn3=Button(win,text="GREEN",font=("Arial black",40,'italic'),bg='pink',fg='black',
cursor='plus',relief='groove',activebackground="pink",activeforeground="white",bd=10,command=lambda:show3("BLUE"))
btn1.pack()
btn2.pack()
btn3.pack()
win.mainloop()