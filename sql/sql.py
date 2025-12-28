import psycopg2

conn = psycopg2.connect(
    dbname="n73_gr",
    user="n73_gr",
    password="123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# 1️⃣ Jadval yaratish
s2 = '''
CREATE TABLE IF NOT EXISTS teacher (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100) UNIQUE
);
'''
cur.execute(s2)

# 2️⃣ Ma’lumot qo‘shish
s3 = '''
INSERT INTO teacher (name, phone, email)
VALUES 
('Ali Karimov', '+998901234567', 'ali.karimov@example.com'),
('Dilnoza Rahimova', '+998933334455', 'dilnoza.rahimova@example.com'),
('Jasur Tursunov', '+998907778899', 'jasur.tursunov@example.com'),
('Malika Xudoyberdiyeva', '+998935551122', 'malika.xudoyberdiyeva@example.com')
ON CONFLICT (email) DO NOTHING;
'''
cur.execute(s3)

# 3️⃣ SELECT qilish
sql1 = '''
SELECT * FROM teacher;
'''
cur.execute(sql1)

rows = cur.fetchall()

for item in rows:
    print(item)

conn.commit()
cur.close()
conn.close()
