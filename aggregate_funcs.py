#count func:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select count(id) from students where id=?',(2,)) #it counts the no. of rows 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()

#sum func:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select sum(marks) from students') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#average func:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select avg(marks) from students')  
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()

#min func:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select min(marks) from students') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()

#max func:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select max(marks) from students') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#uppercase:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select upper(name) from students')  
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#lowercase:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select lower(name) from students') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#order by clause:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select*from students order by id') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#desc:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select*from students order by id desc') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()

#desc by name:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select*from students order by name desc') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#limit:used with order by only
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select*from students order by name desc limit 3') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#sort by multiple columns:
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select*from students order by name,id') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


#group by clause: grouping based on given column name
import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    cursor.execute('select id,max(marks) from students group by id') 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close()


import sqlite3
try:
    conn=sqlite3.connect("studs.db")
    cursor=conn.cursor()
    # cursor.execute("alter table students add column city text")
    # conn.commit()
    cursor.execute("insert into students1 values(?,?,?,?)",(1,"mau",19,100)) 
    conn.commit() 
    # cursor.execute("select name from students group by city order by name desc")     
    conn.commit() 
    rows=cursor.fetchall()
    print("student records:")
    for row in rows:
        print(row)

except sqlite3.Error as e:
    print("An error occurred while fetching data:", e)
finally:
    if conn: 
        conn.close













































