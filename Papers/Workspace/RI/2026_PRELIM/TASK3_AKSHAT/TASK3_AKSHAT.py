# Task 3.1
from flask import Flask, render_template, request
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    
    conn = sqlite3.connect('../ResourceFiles/WORKSHOPS.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute('SELECT * FROM Workshop ORDER BY Title ASC')
        records = cursor.fetchall()
    
    return render_template('INDEX.html', data=records)

# Task 3.2
@app.route('/register', methods = ['GET', 'POST'])
def register():  
    conn = sqlite3.connect('../ResourceFiles/WORKSHOPS.db')
    cursor = conn.cursor()

    message = ''

    with conn:
        if request.method == 'POST':
            student_id = request.form.get('student_id')
            workshop_id = request.form.get('workshop_id')

            cursor.execute('SELECT Count(WorkshopID) FROM Registration WHERE WorkshopID = ?', (workshop_id,))
            total_reg = cursor.fetchone()[0]

            cursor.execute('SELECT MaxPlaces FROM Workshop WHERE WorkshopID = ?', (workshop_id,))
            max_reg = cursor.fetchone()[0]

            cursor.execute('SELECT * FROM Registration WHERE WorkshopID = ? AND StudentID = ?', (workshop_id, student_id))
            reg = cursor.fetchall()

            if total_reg >= max_reg:
                message = 'Workshop is full!'
            elif reg:
                message = 'Registration exists!'
            else:
                message = 'Successful registration!'
                cursor.execute('INSERT INTO Registration(StudentID, WorkshopID, RegistrationDate) VALUES (?, ?, ?)', (student_id, workshop_id, datetime.now().date().strftime("%d-%m-%Y")))
                conn.commit()
            
        cursor.execute('SELECT StudentID, StudentName FROM Student ORDER BY StudentID ASC')
        students = cursor.fetchall()

        cursor.execute('SELECT WorkshopID, Title FROM Workshop ORDER BY WorkshopID ASC')
        workshops = cursor.fetchall()
    
    return render_template('REGISTER.html', students = students, workshops = workshops, message = message)

# Task 3.3
@app.route('/report')
def report():
    conn = sqlite3.connect('../ResourceFiles/WORKSHOPS.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute('''
        SELECT W.WorkshopID, W.Title, W.MaxPlaces, Count(R.StudentID) 
        FROM Workshop AS W 
        JOIN Registration AS R
        ON R.WorkshopID = W.WorkshopID
        WHERE R.WorkshopID = W.WorkshopID
        GROUP BY W.WorkshopID, W.Title, W.MaxPlaces
        ORDER BY Count(R.StudentID) DESC, W.Title ASC
        ''')

        data = cursor.fetchall()

    return render_template('REPORT.html', workshops = data, most_popular_workshop = [i[1] for i in data if i[3] == data[0][3]])

app.run()