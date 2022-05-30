import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('create table login (user_id INTEGER PRIMARY KEY AUTOINCREMENT, name text not null,email text not null)')
print("Table created successfully")
conn.close()

