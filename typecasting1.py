#typecasting
#int(value) : typecasts the given value into int
print(int(10.3))
print(int(True))
#print(int(true))  exception case of keyword
print(int(0b1111))
#print(int(10+5j)) complex no.s cant be typecasted into int
#print(int("abc"))
print(int("11"))
#print(int("0b1111")) given string value cant be typecasted due to binary value in string
#print(int("10.5"))

#float(value) : typecasts the given value into float
print(float(10.3))
print(float(True))
#print(float(true))  exception case of keyword
print(float(0b1111))
#print(float(10+5j)) complex no.s cant be typecasted into float
#print(float("abc"))
print(float("11"))
#print(float("0b1111")) given string value cant be typecasted due to binary value in string
#print(float("0x1111")) given string value cant be typecasted due to hexadecimal value in string
print(float(0xFFFF))
print(float("10.5"))

#complex(value) : typecasts the given value into complex
print(complex(10))
print(complex(True))
print(complex(10.5))
print(complex("10.5"))
#print(complex("0b1111")) cant be typecasted
print(complex(10,20.5))
print(complex(10,20))
# print(complex("10,20"))
# print(complex("10","20"))

#bool(value) : typecasts the given value into boolean
print(bool(-10))
print(bool(10.5))
print(bool(0))
print(bool(0.0))
print(bool(0.01))
print(bool(10))
print(bool(10+5j))
print(bool(0+0j))
print(bool(''))
print(bool('abc'))
print(bool(""))

#str(value) : typecasts the given value into string
a=str(10)
print(type(a))
a=str(10.5)
print(type(a))
a=str(10+5j)
print(type(a))
a=str(True)
print(type(a))
print(a)
a=str(0x1111)
print(type(a))
print(a)
a=str(0b1111)
print(type(a))
print(a)
a=str(0o1111)
print(type(a))
print(a)

#hex(int value): it typecasts given value into hexadecimal string
a=15
b=hex(a)
print(b)
print(type(b))

#bin(int value): it typecasts given value into binary string
a=15
b=bin(a)
print(b)
print(type(b))

#oct(int value): it typecasts given value into octal string
a=15
b=oct(a)
print(b)
print(type(b))

#Character to decimal
a='A'
print("decimal value of character is:", ord(a))

#Deciaml to character
a=65
print("character value of decimal is:", chr(8364))
