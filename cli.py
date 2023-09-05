import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('data/gwennec.db')
cursor = conn.cursor()

# Create a table to store hours
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expense (
        datetime TEXT,
        payee TEXT,
        amount FLOAT
    );
               '''
)

conn.commit()

while True:
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    payee = input("Enter payee : ")
    amount = float(input("Enter amount (EUR) : "))
    
    # Insert the data into the database
    cursor.execute("INSERT INTO expense VALUES (?, ?, ?)", (date, payee, amount))
    conn.commit()

    another_entry = input("Do you want to enter another expense ? (yes/no): ")
    if another_entry.lower() != 'yes':
        break

# Close the database connection
conn.close()
