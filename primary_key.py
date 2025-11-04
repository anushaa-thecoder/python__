import sqlite3
try:
    #connect to db(or create it)
    connection=sqlite3.connect("key.db")
    cursor=connection.cursor()
    # cursor.execute('''
    #     create table focus (
    #     id integer primary key autoincrement,
    #     name text
    # )
    # ''')
    cursor.execute('''insert into focus (name) values (?)''',("anushka",))
    print("Table created successfully.")
    connection.commit()

except sqlite3.Error as a:
    print("an error occured:",a)

finally:
    #close the connection safely
    if connection:
        cursor.close()
        connection.close()

