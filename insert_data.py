import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()

    cursor.execute("""
    insert into students (id, name,age,marks)
    values (?, ?, ?, ?)
    """,(1,'abc',20,90))

    conn.commit()
    cursor.execute("""
    insert into students (id, name,age,marks)
    values (?, ?, ?, ?)
    """,(1,'abc',22,100))

    conn.commit()
    print("records inserted successfully")

except sqlite3.Error as e:
    print("an error occured while inserting data:",e)

finally:
    if conn:
        cursor.close()
        conn.close()




#many data to be inserted:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()

#data to insert:
    lis=[(1,'abc',20,85.5),
        (2,'pqr',19,89.9),
        (3,'lmo',18,90.7),
        ]
    for i in lis:
        cursor.execute("""
        insert into students (id, name,age,marks)
        values (?, ?, ?, ?)
        """,i)

    conn.commit()
    print("records inserted successfully")

except sqlite3.Error as e:
    print("an error occured while inserting data:",e)

finally:
    if conn:
        cursor.close()
        conn.close()


     


import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
#data to insert:
    lis=[(1,'abc',20,85.5),
        (2,'pqr',19,89.9),
        (3,'lmo',18,90.7),
        ]
    # cursor.executemany("""
    #     insert into students (id, name,age,marks)
    #     values (?, ?, ?, ?)
    #     """,lis)
    # print("no. of rows in table",cursor.rowcount)

    conn.commit()
    print("records inserted successfully")

except sqlite3.Error as e:
    print("an error occured while inserting data:",e)

finally:
    if conn:
        cursor.close()
        conn.close()



#write a program to insert data in users table and print all data from users table
import sqlite3
try:
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
#data to insert:
    lis=[(101,'abc','aush','mail.hm',1234),
        (102,'pqr','mau','mailiee.gm',45676),
        (103,'lmo','anu','gmail.am',89088),
        ]
    for i in lis:
        cursor.execute("""
        insert into students(user_id,username,user_password, mail_id,phone_number)
        values (?, ?, ?, ?,?)
        """,i)
    rows=cursor.fetchone()
    while rows is not None:
        print(rows)
        rows=cursor.fetchone()

    conn.commit()
    print("records inserted successfully")

except sqlite3.Error as e:
    print("an error occured while inserting data:",e)

finally:
    if conn:
        cursor.close()
        conn.close()


     
