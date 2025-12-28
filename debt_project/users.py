from db import get_connection

def add_user(first_name,last_name, phone):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (first_name, last_name, phone) VALUES (%s, %s, %s)",
            (first_name, last_name, phone)
        )
        conn.commit()
        print("✅ User saqlandi")
    except Exception as e:
        conn.rollback()
        print(" Xatolik:", e)
    finally:
        cur.close()
        conn.close()

def get_user(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, first_name, last_name FROM users WHERE id = %s",
        (user_id,)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    return user