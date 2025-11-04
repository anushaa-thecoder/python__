import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select * from students')
    rows=cursor.fetchall()
    print("row count",cursor.rowcount)
    print("student records:")
    for row in rows:
        print("id:",row[0])
        print("name:",row[1])
        print("age:",row[2])
        print("marks:",row[3])
        print("--------------------------")
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
    cursor.execute('select * from students')
    rows=cursor.fetchone()
    print("row count",cursor.rowcount)
    print("student records:")
    # for row in rows:
    #     print("id:",row[0])
    #     print("name:",row[1])
    #     print("age:",row[2])
    #     print("marks:",row[3])
    #     print("--------------------------")
    rows=cursor.fetchone()
    while rows is not None:
        print(rows)
        rows=cursor.fetchone()
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
    cursor.execute('select * from students')
    rows=cursor.fetchone()
    print("row count",cursor.rowcount)
    print("student records:")
    # for row in rows:
    #     print("id:",row[0])
    #     print("name:",row[1])
    #     print("age:",row[2])
    #     print("marks:",row[3])
    #     print("--------------------------")
    rows=cursor.fetchmany(2)
    while rows: 
        for row in rows:
            print(row)
            rows=cursor.fetchmany()
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
    cursor.execute('select * from students where id=1')
    rows=cursor.fetchall()
    print("row count",cursor.rowcount)
    print("student records:")
    for row in rows:
        print("id:",row[0])
        print("name:",row[1])
        print("age:",row[2])
        print("marks:",row[3])
        print("--------------------------")
except sqlite3.Error as e:
    print("an error occured while inserting data:",e)

finally:
    if conn:
        cursor.close()




