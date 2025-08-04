import os
print(f"OS NAME:{os.name}")

print(f"logged in user: {os.getlogin()}")
a=os.getcwd()
print(a)
 

items=os.listdir(a)
for item in items:
      print(f"-{item}") 

#print(os.mkdir("anumaaa")) / give this slash to add sub folders
import os
print(os.makedirs("main/sub/child")) #multiple folder creation
import os
print(os.rename("main","mau"))
import os
print(os.rmdir("mau/sub/child"))
import os
print(os.removedirs("mau/sub"))

import os
user=input("enter folder name:")
print(os.mkdir(user))

# import os
# os.chdir("anu")
# print(os.getcwd())
import os
folder="F"
subfolder="SF"
filename="PJPG"
full_path=os.path.join(folder,subfolder,filename)
print(full_path)

import os
print(os.path.exists(full_path))

print(os.path.isfile("anu.txt"))

import os
print(os.system("py math1.py"))

import os
print(os.system("code"))

