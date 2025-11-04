import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
     #delete record
    cursor.execute(''' 
    delete from students
    where name=?
    ''',('abc',))

    conn.commit()
    if cursor.rowcount==0:
        print("abc not found, no rec deleted")
    else:
        print("abc's record deleted successfully")
except sqlite3.Error as e:
    print("abc's record deleted successfully")
finally:
    if conn:
        cursor.close()
        conn.close()



import sqlite3
try:
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
     #delete record
    cursor.execute(''' 
    delete from students
    where username=?
    ''',('abc',))

    conn.commit()
    if cursor.rowcount==0:
        print("abc not found, no rec deleted")
    else:
        print("abc's record deleted successfully")
except sqlite3.Error as e:
    print("abc's record deleted successfully")
finally:
    if conn:
        cursor.close()
        conn.close()

#create a database name as cafe.db with a table orders having columns orderid,customername,item,quantity and price 
#
import sqlite3

order_id=int(input("Enter order ID:"))
customer_name=input("Enter customer name:")
item=input("Enter item:")
quantity=int(input("Enter quantity:"))
price=int(input("Enter price:"))
try:
    conn=sqlite3.connect("Cafe.db")
    cursor=conn.cursor()

    #create table
    cursor.execute('''
        create table if not exists Ordrs (
        order_id integer,
        customer_name txt,
        item txt,
        quantity integer,
        price integer
    )
    ''')

    lis=[(1,'anushka','paneer',1,100),
        (2,'prachii','pulaw',2,50),
        (3,'diksha','patis',1,20),
        ]
    for i in lis:
        cursor.execute("""
        insert into students (order_id,customer_name,item,quantity,price)
        values (?, ?, ?,?,?)
        """,i)

    cursor.execute('select * from Orders')
    rows=cursor.fetchall()
    print("row count",cursor.rowcount)
    print("student records:")
    for row in rows:
        print("order_id:",row[0])
        print("customer_name:",row[1])
        print("item:",row[2])
        print("quantity:",row[3])
        print("price:",row[4])
        print("--------------------------")

    cursor.execute('''
    update Orders
    set quantity = ?
    where order_id = ?
    ''', (5, 'pulaw'))

    

    conn.commit()
    rows=cursor.fetchall()
    print("row count",cursor.rowcount)
    if cursor.rowcount == 0:
        print("pqr not found. No update performed.")
    else:
        print("quantity updated.")
        cursor.execute('select * from Orders')
        updated_row = cursor.fetchone()
        print("Updated row:", updated_row)

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()

