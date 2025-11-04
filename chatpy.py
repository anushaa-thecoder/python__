import re as r
import datetime as d
import random as ra
l=[" Why dont programmers like nature?→ Too many *bugs*",

 'Why did the computer go to therapy?→ Because it had too many *bytes* of anxiety',

 'Why did the scarecrow win an award?→ Because he was outstanding in his *field*',

 'Parallel lines have so much in common...→ Its a shame theyll never meet',

 'Why dont skeletons fight each other?→ They dont have the *guts*'
]
username=None
def chatdada(inp):
     global username
     a=r.search(r"\b(Hi|Hey|Hello)\b",inp,r.I)
     if a:
         return f"{a.group()}! What's Your Name?"
     v=r.search(r"\bmy name is (\w+)",inp,r.I)
     if v: 
          username=v.group(1) 
          if username:
           return f"Nice to meet you {username}!How can I assist yoy today?"
          else:
              return "Nice to meet you!How can I assist yoy today?"
     if r.search(r"\b(who am i)\b",inp,r.I):
          if username:
               return f"You told me your name is {username}"
          else:
               return "You didn't tell me your name"
     if r.search(r"\b(tell me a joke)",inp,r.I):
         return ra.choices(l)
     if r.search(r"\b(what time|date it is)\b",inp,r.I):
         return d.datetime.now()
     if r.search(r"\b(Goodbye|Bye)",inp,r.I):
         if username:
           return f"Goodbye {username}!Have a wonderful day!"
         else:
             return "Goodbye!Have a wonderful day!"
     if r.serach(r"\b(give me regex pattern for email id formation)",inp,r.I):
        return (r"^\w+@[a-z A-Z]{2,8}\.[a-z A-Z]{2,3}$")
     if r.serach(r"\b(give me regex pattern for mobile number formation)"):
         return (r"^[+91]?[7-9][0-9]{9}$")
     
         
     return f"IM NOT ABLE TO UNDERSTAND,PLEASE PUT CORRECT INFORMATION!".capatalize()

print("ChatPy is Running!(type 'exit' to quit)")
while True:
    inp=input("YOU : ")
    o=r.search(r"exit|quit",inp,r.I)
    if o:
        break
    else: 
        print("Bot : ", chatdada(inp))
        
