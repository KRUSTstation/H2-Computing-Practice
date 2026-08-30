# Task 4.4
from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='Task4_4_Akshat')

@app.route('/')
def index():
    conn = sqlite3.connect('CLINIC.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute('SELECT Q.ID, Q.Priority, P.Name, P.Age, P.Gender FROM Patient AS P JOIN Queue AS Q ON Q.PatientID = P.PatientID WHERE Q.InQueue = 1 ORDER BY Q.Priority DESC, Q.ID ASC')
        data = cursor.fetchall()

    return render_template('index.html', data=data)

app.run()