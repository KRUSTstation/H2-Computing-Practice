from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='TASK4_4_Akshat')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods = ['POST'])
def update():
    room_id = request.form.get('room_id')
    name = request.form.get('student_name')

    print(room_id, name)

    if not room_id or not name:
        msg = 'Missing room or name'
        
    else:
        conn = sqlite3.connect('SHENZHENGO.db')
        cursor = conn.cursor()
        
        with conn:
            # cursor.execute('SELECT * FROM Student WHERE Student_Name = ?', (name,))
            # i = cursor.fetchone()
            # cursor.execute('SELECT * FROM Room WHERE Room_ID = ?', (room_id,))
            # j = cursor.fetchone()

            # print(i, j)

            # if not i or not j:
            #     msg = 'Invalid room or name'
            #else:
            cursor.execute('UPDATE Student SET Room_ID = ? WHERE Student_Name = ?', (room_id, name))
            msg = 'Updated Successfully'
        
            conn.commit()
    
    return render_template('index.html', message=msg)

@app.route('/display')
def display():
    conn = sqlite3.connect('SHENZHENGO.db')
    cursor = conn.cursor()
    
    with conn:
        cursor.execute('SELECT Student_Name, Student_Gender, Student_Leader, Room_ID FROM Student ORDER BY ROOM_ID ASC')
        items = cursor.fetchall()
    
    return render_template('display.html', items=items)

app.run()