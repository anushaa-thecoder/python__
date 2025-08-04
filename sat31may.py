# 31/05/2025

# Encoding and decoding functions


# encode(encoding errors):encodes a stringn into bytes using a spacified encoding and error handling scheme.

text="pythón"
print(text.encode('utf-8'))# b'pyth\xc3\xb3'

print(text.encode('ascii')) # raises unicode encoder error

#ignore non ascii
print(text.encode('ascii',errors='ignore'))  #b'pythn'

#replace non ascii
print(text.encode('ascii',errors='replace'))   #b'pyth?n'

#'xmlcharrelfreplace'(replaces with xml character reference)
print(text.encode('ascoo',errors='xmlcharrefreplace')) #b'pyth&#243;

#'backslashreplace'(replaces with python-style unicode escape)
print(text.encode('ascii',errors='backslashreplace'))  # b'pyth\\xf3



# 'namereplace'(python 3.5+- replaces with \n{...}names)
print(text.encode('ascii',errors='nameplace'))  # b'pyth\\N{LATIN SMALL LETTER 0 WITH ACUTE}


sum=0
avg=0
count=0
i="Python@123987P"

# while int(i)<len(i):
for r in i:
    if r.isdecimal():
        # print(r)
        sum=sum+int(r)
        
        
        count+=1
avg=sum/count
print("sum is:",sum)
print("avg is :",avg)
print("count is:",count)



#
a="Python123 programing abc12"

print(len(a.split(" ")))
for i in a:
    x=a.split()
    for x in a:
        if x.isalnum():
            count+=1


count=0
for r in a():
    if r.isalnum():
        print(" ")



text = "Python123 programing abc12"
text=input("Enter a text:")
# Step 1: Split the string by '-'
split_text = text.split("-")

# Step 2: Get the first part (after split)
first_part = split_text[0]  # In this case: 'Python123 programing abc12'

# Step 3: Get the first word from that part
first_word = first_part.split()[0]  # Result: 'Python123'

# Step 4: Detect and count only alphabetic characters
alphabet_count = 0
n_count=0
for char in first_word:
    if char.isalpha():
        if char.isdeciaml():
            n_count+=1
        alphabet_count += 1

