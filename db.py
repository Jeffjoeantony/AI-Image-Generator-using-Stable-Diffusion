import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO users(name,email) VALUES (?,?)")

conn.commit()
conn.close()