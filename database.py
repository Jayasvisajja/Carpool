import sqlite3

def create_tables():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            phone TEXT,
            password TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rides (
            email TEXT,
            current_location TEXT,
            destination TEXT,
            date TEXT,
            time TEXT,
            lat REAL,
            lon REAL
        )
    ''')

    conn.commit()
    conn.close()

def add_user(email, phone, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?, ?)", (email, phone, password))
    conn.commit()
    conn.close()

def add_ride(email, current_location, destination, date, time, lat, lon):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rides VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (email, current_location, destination, date, time, lat, lon))
    conn.commit()
    conn.close()

def get_all_rides():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rides")
    rides = cursor.fetchall()
    conn.close()
    return rides

def get_user_phone(email):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT phone FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
