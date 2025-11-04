"""write pp to take a ss of current screen after some time interval"""
import time as t
import pyscreenshot as p   #pyright: ignore[reportMissingImports]
import winsound as w
import os as o
no=5
s="ssop"
o.makedirs(s,exist_ok=True)
for i in range(5):
    img=p.grab()
    filename=o.path.join(s,f"ss{i}.png")
    img.save(filename)
    if i<no:
        w.Beep(1000,200)
        t.sleep(3)
