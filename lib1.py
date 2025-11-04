from tkinter import ttk
from tkinter import*
win=Tk()
win.title("GUI APP")
win.iconbitmap(r"C:\Users\DEll\Downloads\python_18894.ico")
win.config(bg='black')
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f'{width}x{height}') #width X height
win.minsize(width=200,height=200)
win.maxsize(width=1200,height=800)
# win.resizable(False,False)
labeling=Label(win,text='WELCOME TO GUI',bg='pink',fg='black',
font=('Arial Black',14,'italic'),width=40,height=5,cursor='plus',
relief='groove')
# labeling.pack()
# labeling.grid() #rows and columns format of label
labeling.place(relx=0.4,rely=0.4,width=100,height=100) #
# ttk.Label(win,text="hello user!").pack()
# win.attributes('-alpha',0.3) transperancy of screen
win.mainloop() #main loop puts the screen on loop it holds the screen also it is kept at last line
