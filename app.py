from flask import Flask, render_template, url_for 
import sqlite3
import pdb
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def calendar():
    conn = sqlite3.connect('data/gwennec.db')
    cursor = conn.cursor()

    cursor.execute("SELECT date, payee, amount FROM expense")
    expense_data = cursor.fetchall()
    
    conn.close()

    return render_template('expense.html', expense_data=expense_data)

if __name__ == '__main__':
    app.run(debug=True)
