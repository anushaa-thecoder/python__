#write a python program to take two numbers from user and right shift 1st no. by 2nd no.
a=int(input("Enter a num"))
b=int(input("Enter a num"))
print(a>>b)

#write a python program to take 3 numbers from user and calculate double of 3 no.s
a=int(input("Enter a num"))
b=int(input("Enter a num"))
c=int(input("Enter a num"))
print(a+a)
print(b+b)
print(c+c)
d=(a+b+c)*2
f=d/3
print("average:", f)

#write a python program to take a string from user and also take a character to check given character is present in string or not
a=(input("Enter a string"))
b=(input("Enter a character"))
print(b in a)

#write a python program to take a dollar from user and convert into indian rupees
a=int(input("Enter a dollasr value"))
b=a*89
print("Indian rupees:", b)

#write a python program to take a input form user to convert c into f and its viceversa
a=int(input("Enter a farhenit value"))
c = (a - 32) * 5/9
print("converted value to celcius is:", c)
b=int(input("Enter a celcius value"))
f=(b * 9/5) + 32
print("converted value to farhenit is:", f)

# write a python program to check 2 object refers to the same memory location or not
a=int(input("enter a value:"))
b=int(input("enter a value:"))
print(id(a))
print(id(b))
print(a is b )
print(a is not b)