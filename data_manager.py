import sqlite3

def get_db_connection():
    conn = sqlite3.connect('db/my_database.db')  # Make sure the path is correct
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            hours REAL,
            category TEXT,
            date TEXT
        );
    """)
    conn.commit()
    conn.close()

def add_activity(name, hours, category, date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO activities (name, hours, category, date)
        VALUES (?, ?, ?, ?);
    """, (name, hours, category, date))
    conn.commit()
    conn.close()

def get_all_activities():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities")
    activities = cursor.fetchall()
    conn.close()
    return activities
