from flask import Flask, render_template, url_for 
import sqlite3

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def calendar():
    conn = sqlite3.connect('data/gwennec.db')
    cursor = conn.cursor()

    cursor.execute("SELECT date, payee, amount FROM expense ORDER BY date asc")
    expense_data = cursor.fetchall()

    cursor.execute("SELECT SUM(amount) FROM expense;")
    total_expenses = cursor.fetchall()

    conn.close()

    # Generate the URL for 'intake.png' in the 'static' folder
    expense_image_url_1 = url_for('static', filename='expense1.png')
    expense_image_url_2 = url_for('static', filename='expense2.png')


    return render_template('expense.html', expense_data=expense_data, 
                           total_expenses=total_expenses, 
                           expense_image_url_1=expense_image_url_1, 
                           expense_image_url_2=expense_image_url_2
                           )

if __name__ == '__main__':
    app.run(debug=True)
