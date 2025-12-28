import sqlite3

conn = sqlite3.connect("../database.db")
cur = conn.cursor()

s1 = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
);
"""

s12 = """
INSERT INTO users(name, age)
VALUES ('ali1', 21), ('ali2', 12);
"""

s2 = "SELECT * FROM users;"

# Table yaratish
cur.execute(s1)

# Ma'lumot qo‘shish
cur.executescript(s12)

# O‘zgarishlarni saqlash
conn.commit()

# Ma'lumotlarni olish
cur.execute(s2)

print("bajarildi")

for row in cur:
    print(row)

cur.close()
conn.close()
