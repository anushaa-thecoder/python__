#Phonebook Application
phone={}
while True:
    print("1. Add Contacts")
    print("2. Search Contacts")
    print("3. View All Contacts")
    print("4. Count Contacts")
    print("5. Delete Contacts")
    print("6. Clear All Contacts")
    print("7. Exit")
    choice=input("Enter a choice you want to go further with:")
    if choice=='1':
      for i in range(3):
         contact_name=input("Enter a name:")
         contact_number=input("Enter contact number:")
         phone[contact_name]=contact_number
         print("SAVED SUCCESSFULLY!")
    elif choice=='2':
       search=input("Enter a contact name:")
       print("Searching for contact:", phone.get(search, "not found"))
    elif choice=='3':
       print("All contacts are listed below:",phone.items())
    elif choice=='4':
       count=len(phone)
       print("Total count of contacts:",count)
    elif choice=='5':
       del phone
       print("DELETED SUCCESSFULLY!")
    elif choice=='6':
       phone.clear()
       print("CLEARED ALL CONTACTS")
    elif choice=='7':
       break
    else:
       print("Please enter a valid choice, Thank you!")

