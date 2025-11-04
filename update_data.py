import sqlite3
try:
    conn = sqlite3.connect('studs.db')
    cursor = conn.cursor()
    cursor.execute('''
    update students
    set marks = ?
    where name = ?
    ''', (82.0, 'abc'))

    conn.commit()
    rows=cursor.fetchall()
    print("row count",cursor.rowcount)
    if cursor.rowcount == 0:
        print("pqr not found. No update performed.")
    else:
        print("pqr's grade updated.")
        cursor.execute('select * from students')
        updated_row = cursor.fetchone()
        print("Updated row:", updated_row)

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()


"""write a program to accept userid and password from user and change old pass to new password"""
import sqlite3
us1=int(input("enter user id:"))
us2=input("enter new password:")
try:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    update students
    set user_password= ?
    where user_id= ?
    ''', (us2,us1))

    conn.commit()
    # rows=cursor.fetchall()
    # print("row count",cursor.rowcount)
    if cursor.rowcount == 0:
        print("id not found!")
    else:
        print("password updated.")
        cursor.execute('select * from students where user_id=?',(us1,))
        updated_row = cursor.fetchone()
        print("Updated row:", updated_row)

except sqlite3.Error as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()