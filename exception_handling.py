#
try:
 n1=int(input("enter number 1:"))
 n2=int(input("enter number 2:"))
 print(n1/n2)
except:
    print("enter valid input")
print("hello")

#
try:
    l=[1,2,3]
    print(l[7])
except:
   print("valid index daloo")
print(l)


#
try:
    print(10/0)
except ZeroDivisionError:
   print("zero divide")
except ArithmeticError:
    print("arithmatic")

print("end")


#
try:
    n=float(input("enter number:"))
except Exception as e:
    print(type(e))
    print(e.__class__)
    print(e.__class__.__name__)
    print(e)

#no exception:
try:
    print("try")
except:
    print("except")
finally:
    print("finally")
print("hellooieeee!!!!")

#exception occured at stmt 2
try:
    n1=int(input("enter number 1:"))
    n2=int(input("enter number 2:"))
    print(n1/n2)
except:
    print("except")
finally:
    print("finally")
print("hellooieeee!!!!")

#abnormal termination:
try:
    n1=int(input("enter number 1:"))
    n2=int(input("enter number 2:"))
    print(n1/n2)
except ValueError:
    print("except")
finally:
    print("finally")
print("hellooieeee!!!!")

#abnormal termination:
try:
    n1=int(input("enter number 1:"))
    n2=int(input("enter number 2:"))
    print(n1/n2)
except:
    print("error")
    print(1/0)
finally:
    print("helllooieeee")
print("yummy")


try:
    print("stat1")
    print("stat2")
    print("stat3")
    print("stat4")
    try:
       print("stat5")
       print("stat6")
    except: 
        print("stat7")
    finally:
        print("stat8")
    print("stat9")
except:
    print("stat10")
finally:
    print("stmt11")
print("stat12")


try:
    print(1/0)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")
print("hellooieeee!!!!")

#syntax of all blocks is always:
# try Block
# except Block
# else Block : optional block
# finally block : optional block

"""NOTE: for same try block we can take multiple except block atleast 1 should be there 
but only single finally and else block"""

try:
    print("try")
except:
    print("except")    
try:
    pass
finally:
    print("finally")


