import sqlite3

conn = sqlite3.connect('VA')
c = conn.cursor()

# Create table / run only once
'''
c.execute("""CREATE TABLE pilots (
    first_name text,
    last_name text,
    hours intger,
    money intger)""")
'''

conn.commit()
conn.close()