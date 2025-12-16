import sqlite3

def create_table():
    conn =  sqlite3.connect("expenses.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              amount REAL NOT NULL,
              category TEXT NOT NULL,
              date TEXT NOT NULL
              )
        ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()