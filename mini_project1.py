import re as r
import datetime as d
username=None
def chatdada(inp):
     a=r.search(r"Hi|Hey|Hello",inp,r.I)
     if a:
         return f"{a.group()}! What's Your Name?"
     global username
     username=inp
     if r.search(r"my name is \w+|\w+",inp,r.I):
          return f"Nice to meet you {username}!How can I assist yoy today?"
     


    
print("ChatPy is Running!(type 'exit' to quit)")
while True:
    inp=input("YOU : ")
    o=r.search(r"exit|quit|bye",inp,r.I)
    if o:
        break
    else: 
        print("Bot : ", chatdada(inp))
        
