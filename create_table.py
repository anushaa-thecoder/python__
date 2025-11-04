import sqlite3
try:
    #connect to db(or create it)
    connection=sqlite3.connect("studs.db")
    cursor=connection.cursor()
    
    #create table
    cursor.execute('''
        create table if not exists students1 (
        id integer primary key autoincrement,
        name text not null ,
        age integer,
        marks real
    )
    ''')

    print("Table created successfully.")

    #save changes:
    connection.commit()

except sqlite3.Error as a:
    print("an error occured:",a)

finally:
    #close the connection safely
    if connection:
        connection.close()



#write a prog to create a table user with column user id, name, password, mail id, phone number
try:
    #connect to db(or create it)
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    
    #create table
    cursor.execute('''
        create table if not exists user (
        user_id integer,
        username txt,
        user_password text ,
        mail_id text,
        phone_number int
    )
    ''')

    print("Table created successfully.")
    conn.commit()

except sqlite3.Error as a:
    print("an error occured:",a)

finally:
    #close the connection safely
    if conn:
        cursor.close()
        conn.close()
