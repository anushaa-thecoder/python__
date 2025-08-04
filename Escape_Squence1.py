#\n: new line
a="abc\npqr"
print(a)

#\t: tab 
print("abc12344\tpqr")

#\r: carriage return
print("abc\rpqr")
print("abc\rpq")
a= "abcpqr\rxy"
print(a)

#\b: backspace
print("abc\bpqr")
print("abc12344\bpqr")

#\v: vertical tab
print("abc12344 \v pqr")

#\0: null
print("abc12344\0pqr")

#\U: unicode 8 digits
print("abc12344 \U00000100 pqr")

#u:
print("abc12344 \u0100 pqr")

#prevent Escape sequence
print(r"C:\Users\newFolder")
print("C:\\Users\\newFolder")

print(r"C:\Users\DEll\PYTHON")
print(r"\\")