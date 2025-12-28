from db import get_connection

users = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255) UNIQUE,
    age INTEGER,
    city VARCHAR(255)
);
"""

debts = """
CREATE TABLE IF NOT EXISTS debts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    amount INTEGER NOT NULL,
    debt_type VARCHAR(10) CHECK (debt_type IN ('got', 'gave'))
);
"""

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(users)
    cur.execute(debts)

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Tables created")
