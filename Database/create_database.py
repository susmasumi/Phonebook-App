import sqlite3

conn = sqlite3.connect('AccountDB.db')
c = conn.cursor()

table_check_query = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"

if not c.execute(table_check_query).fetchone():
    c.execute('''CREATE TABLE AccountDB (ID INTEGER PRIMARY KEY, 
                                          Name TEXT, 
                                          Number TEXT, 
                                          Email TEXT, 
                                          Password TEXT)''')

conn.commit()
conn.close()
