import sqlite3

# connect to DB and create tables
conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE leagues (league_id INTEGER)')
print("Table created successfully")
conn.close()
