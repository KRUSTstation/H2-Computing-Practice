# Flask
from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='TASK_4_4_Akshat')

@app.route('/')
def base():
    conn = sqlite3.connect('LIBRARY.db')
    cursor = conn.cursor()

    cursor.execute("SELECT BookID, MemberNumber FROM Loan WHERE Returned = 'FALSE'")
    data = cursor.fetchall()

    info = []
    for i in data: # combining all data into a global list called info
        cursor.execute('SELECT FamilyName, GivenName FROM Member WHERE MemberNumber = ?', (i[1],)) # grab names
        name = cursor.fetchone()

        cursor.execute('SELECT Title FROM Book WHERE BookID = ?', (i[0],)) # grab books
        title = cursor.fetchone()[0]

        info.append([name, title])

    return render_template('base.html', info = info)

app.run()