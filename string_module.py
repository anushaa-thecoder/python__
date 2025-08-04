import string

#string module constants
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)
print(string.punctuation)

#Example
import string
def analyze_text(text):
    print("Original text:", text)
    
    print("\nCharacter breakdown:")
    for char in text:
        if char in string.ascii_lowercase:
            print(f"'{char}' is a lowercase letter")
        elif char in string.ascii_uppercase:
            print(f"'{char}' is an uppercase letter")
        elif char in string.digits:
            print(f"'{char}' is a digit")
        elif char in string.hexdigits:
            print(f"'{char}' is a hex digit")
        elif char in string.octdigits:
            print(f"'{char}' is an octal digit")
        elif char in string.punctuation:
            print(f"'{char}' is punctuation")
        elif char in string.whitespace:
            print(f"'{char}' is whitespace")
        elif char in string.printable:
            print(f"'{char}' is printable")
        else:
            print(f"'{char}' is unknown or non-printable")

# Example usage
sample = "Hello, World! 123\n12"
analyze_text(sample)