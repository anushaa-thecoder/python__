#local 
def f1():
    y=20
    print(y)
f1()
# print(y) name error 

#global
a=10
def f2():
    a=20
    print('local value of a:',a)
f2()
print('global value of a:',a)

#global keyword
a=10
def f2():
    global a
    a+=2
    print('local value of a:',a)
f2()
print('global value of a:',a)

#nonlocal: modification for function within function
a=10
def f3():
    a=20
    print(a)
    def f4():
        nonlocal a
        a+=3
        print(a)
    f4()
    print(a)
f3()
print(a)

#passing immutable parameter in function:
def f1(a):
    print(a)
    print(id(a))
x="python"
f1(x)
print(x)
print(id(x))

#id diff because modification and it doesnt effect upon downside value
def f1(a):
    a=a.lower()
    print(a)
    print(id(a))
x="python"
f1(x)
print(x)
print(id(x))

#passing mutable parameter in function:
def f1(a):
    a.append(10)
    print(a)
    print(id(a))
x=([1,2,3,4])
f1(x)
print(x)
print(id(x))

