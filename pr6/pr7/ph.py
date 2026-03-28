from connect import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
conn.commit()

name = input("Name: ")
phone = input("Phone: ")

cur.execute(
    "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
    (name, phone)
)
conn.commit()

import csv

with open("contacts.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (row[0], row[1])
        )
conn.commit()

cur.execute("SELECT * FROM phonebook")
for row in cur.fetchall():
    print(row)

cur.execute(
    "UPDATE phonebook SET phone = %s WHERE name = %s",
    ("87770000000", "Ali")
)
conn.commit()

cur.execute(
    "DELETE FROM phonebook WHERE name = %s",
    ("Ali",)
)
conn.commit()
