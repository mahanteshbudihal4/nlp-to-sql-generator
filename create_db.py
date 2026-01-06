import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("DELETE FROM students")

cursor.executemany(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    [
        ("Alice", 22),
        ("Bob", 20),
        ("Charlie", 23)
    ]
)

conn.commit()
conn.close()

print("Database created successfully")
