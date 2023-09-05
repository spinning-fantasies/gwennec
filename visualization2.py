import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('data/gwennec.db')
cursor = conn.cursor()

# Retrieve data
cursor.execute("SELECT date, amount FROM expense")
data = cursor.fetchall()

# Separate dates and expenses
dates = [entry[0] for entry in data]
expenses = [entry[1] for entry in data]

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(dates, expenses, marker='o', s=50, alpha=0.7)

# Customize the chart
plt.title('Scatter Plot of Expenses by Date')
plt.xlabel('Date')
plt.ylabel('Expense Amount')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Show the plot
plt.tight_layout()
plt.grid(True)  # Add a grid to the plot
plt.show()

# Close the database connection
conn.close()
