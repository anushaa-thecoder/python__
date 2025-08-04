import cal_module
print(cal_module.sub(4,1))

import cal_module as a
print(a.add(1,3))

from cal_module import mul
print(mul(1,2))

# a=12
# b=5
from cal_module import *
a=12
b=5
print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(div(1,2))
print(a,b)

