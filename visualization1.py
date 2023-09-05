import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('data/gwennec.db')
cursor = conn.cursor()

# Retrieve data and calculate expenses by payee
cursor.execute("SELECT payee, SUM(amount) FROM expense GROUP BY payee")
data = cursor.fetchall()

# Separate payees and expenses
payees = [entry[0] for entry in data]
expenses = [entry[1] for entry in data]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(expenses, labels=payees, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a title
plt.title('Expenses by Payee')

# Show the pie chart
plt.show()

# Close the database connection
conn.close()
