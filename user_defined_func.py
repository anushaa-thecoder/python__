class NegativeNumberException(Exception):
       pass
def check_positive_number(number):
    if number < 0:
          raise NegativeNumberException("number is negative ")
    print("number is positive")
try:
      n=int(input("ENTER A NUMBER:"))
      result=check_positive_number(n)
      print(result)
except NegativeNumberException as e:
      print(e)
except:
      print("ERROR: please enter valid integer")
      

#write a python program to authenticate a username and
#password entered by the user
#if the entered credentials are incorrect,raise a user defined exception
#named FailedException and display appropriate msg

class login(Exception):
      pass
def login_check():
      name="Admin"
      passw="Admin123"
      try:
        n1=input("ENTER USERNAMEEEEE:")
        p1=input("ENTER PASSWORDDDDD:")
        if n1==name and p1==passw:
            print("LOGIN SUCCESFULL YAYYIEEEEE")
            print(f"USERNAME:{name} \n PASSWORD:{passw}")
        else:
            raise login("ERROR: LOGIN UNSUCESSFULL!!!1!")
      except login as l:
           print(l)
      except ValueError:
           print("put valid input!")   
login_check()
             

"""Validate Vehicle Registration ID
Write a Python program that validates a Vehicle Registration ID using custom rules and raises a custom exception if the format is invalid.

Validation Rule:
•	Format: The Registration ID must begin with VR- followed by exactly 4  digits.
•	Example of valid input: VR-1234
If the format is invalid, the program should raise and handle a custom exception named InvalidVehicleDetailsException.

Class Requirements:
1.	InvalidVehicleDetailsException
o	A custom exception class that takes an error message.

2.	VehicleRegistrationSystem
o	Method: validateRegistrationId(registrationId)
o	Checks if the Registration ID is valid based on the format VR-####.
o	If valid, return a success message.
o	If invalid, raise InvalidVehicleDetailsException.

3.	Main Program
o	Ask the user to input the Registration ID.
o	Call validateRegistrationId() from VehicleRegistrationSystem.
o	Print success message or catch and display the error.
Ex 1 .Input:
Enter Registration ID:
VR-1234

Output :Registration ID VR-1234 is valid and can be added to the system.

Ex2. Input:
Enter Registration ID:
VR123

Output:

    Error: Invalid format: Registration ID must be 7 characters (e.g., VR-1234).


  VR-1234 →  Valid
  VR1234 →  Missing dash
   VR-12A4 →  Non-numeric character
  VR-123 →Too short
   AB-1234 →  Incorrect prefix

"""            
    
class InvalidVehicleDetailsException(Exception):
      pass

class VehicleRegistrationSystem:
    def validateRegistrationId(self):
         id=(input("Enter registration id:"))
         if (len(id)<7 and id.startswith("VR-")):
              raise InvalidVehicleDetailsException("ERROR: length of pass should be 7 and must start with 'VR-' ")
         if (id[3:].isdigit() and len(id[3:])<4):
              raise InvalidVehicleDetailsException("ERROR: digit length must start after '-' and 4 digs only ")
         return ("REGISTRATION ID:",id)
try:
     i=VehicleRegistrationSystem()
     print(i.validateRegistrationId())
except InvalidVehicleDetailsException as o:
     print(o)
     


     