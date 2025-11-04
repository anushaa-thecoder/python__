import sqlite3
try:
    connection=sqlite3.connect("Cab_System.db")
    cursor=connection.cursor()
    cursor.execute('''
        create table if not exists drivers (
        driver_id integer primary key autoincrement,
        name text,
        car_model text,
        phone_number text,
        available text
    )
    ''')
    connection.commit()
    cursor.execute('''
        create table if not exists booking(
        booking_id integer primary key autoincrement,
        customer_name text,
        pickup text,
        dropoff text,
        distance real,
        fare real,
       driver_id int,
       status text
    )
    ''')
    connection.commit()
except sqlite3.Error as a:
      print("An error occured:",a)
def add_driver():
    driver_name=input("Enter Driver Name:")
    car_model=input("Enter Car Model:")
    phone_number=input("Enter Phone Number:")
    cursor.execute('''insert into drivers(name,car_model,phone_number,available)
                   values(?,?,?,?)''',(driver_name,car_model,phone_number,'Yes',))
    connection.commit()
    if cursor.rowcount:
        print("Driver Added Successfully!")
def View_Available_Drivers():
    cursor.execute('select* from drivers where available=?',('Yes',))
    rows=cursor.fetchall()
    if not rows:
         print("No drivers available right now. Please try again later!")
    for row in rows:
      print("---------------------------")
      print("DRIVER ID:",row[0])
      print("DRIVER NAME:",row[1])
      print("CAR MODEL:",row[2])
      print("PHONE NUMBER:",row[3])
      print("AVAILABILITY:",row[4])
      print("---------------------------")
    connection.commit()
def Book_cab():
     customer_name=input("Enter Name:")
     pickup=(input("Enter Pickup Location:"))
     drop=(input("Enter Drop Location:"))
     distance=int(input("Enter distance:"))
     calc_fare=distance*10 
     print("Total Fare:",calc_fare)
     View_Available_Drivers()
     d_id=int(input("Enter Driver Id:"))
     cursor.execute('select driver_id from drivers where driver_id=?',(d_id,))
     rows=cursor.fetchone()
     if not rows:
          print("Enter Valid Driver Id")
     cursor.execute("""
        insert into booking (customer_name,pickup,dropoff,distance,fare,driver_id,status)
        values (?,?,?,?,?,?,?)
        """,(customer_name,pickup,drop,distance,calc_fare,d_id,'booked'))
     booking_id=cursor.lastrowid
     cursor.execute('''update drivers set available = ?
     where driver_id= ?''',('No', d_id))
     connection.commit()
def Complete_ride():
   book_id=int(input("Enter booking id:"))
   cursor.execute('select booking_id,driver_id from booking where booking_id=?',(book_id,))
   connection.commit()
   rows=cursor.fetchone()
   if not rows:
          print("Enter Valid Booking Id")
   cursor.execute('''update booking set status = ?
     where booking_id= ?''',('Completed', book_id))
   connection.commit()
   cursor.execute('''update drivers set available = ?
     where driver_id=?''',('Yes', rows[1]))
   connection.commit() 
def View_all_bookings():
     pass
while True:
        print("====CAB BOOKING SYSTEM====")
        print("1. Add Driver")
        print("2. View Available Drivers")
        print("3. Book Cab")
        print("4. Complete Ride")
        print("5. View All Bookings")
        print("6. Exit")
        choice=int(input("Enter a choice:"))
        if choice==6:
                print("THANKS FOR REACHING US OUT!")
                break
        if choice==1:
            add_driver()
        elif choice==2:
             View_Available_Drivers()
        elif choice==3:
             Book_cab()
        elif choice==4:
             Complete_ride() 
     #    elif choice==5:
     #         View_all_bookings()  
