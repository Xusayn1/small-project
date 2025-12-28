import psycopg2
conn = psycopg2.connect(
    dbname= 'n73_gr',
    user = 'n73_gr',
    password = '123',
    host = 'localhost',
    port = '5432'
)

cur = conn.cursor()

s1 =  """
create table if not exists test_table (
    id serial primary key,
    title varchar(50),
    price int not null,
    quantity integer not null ); 
"""
cur.execute(s1)

s2 = """
insert into test_table (title, price, quantity)
values ( 'milk', 12, 15),
       ( 'bread', 5, 10),
       ('eggs', 2, 25), 
       ('sugar', 7, 10)
"""
cur.execute(s2)

s3 = """
select * from test_table
"""
cur.execute(s3)

rows = cur.fetchall()
for items in rows:
    print(items)

conn.commit()
cur.close()
conn.close()


