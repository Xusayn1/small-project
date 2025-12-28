from db import get_connection

def add_debt(user_id, amount, debt_type):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO debts (user_id, amount, debt_type)
        VALUES (%s, %s, %s)
        """,
        (user_id, amount, debt_type)
    )

    conn.commit()
    print("✅ Qarz saqlandi")

    cur.close()
    conn.close()

def get_debts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT u.first_name, last_name, u.phone, d.amount, d.debt_type 
        FROM debts d
        JOIN users u ON u.id = d.user_id
    """)

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
