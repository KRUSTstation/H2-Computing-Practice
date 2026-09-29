# Task 4.4
from flask import Flask, render_template, request
import sqlite3
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/houses')
def houses():
    conn = sqlite3.connect('HOUSEALLOCATION.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute('SELECT * FROM HOUSE')
        data = cursor.fetchall()

    return render_template('houses.html', data=data)

@app.route('/edit', methods = ['GET', 'POST'])
def edit():
    if request.method == 'GET':
        return render_template('edit.html')

    name = request.form.get('name')
    department = request.form.get('department')

    conn = sqlite3.connect('HOUSEALLOCATION.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute('SELECT houseName FROM STAFF WHERE name = ? AND department = ?', (name, department))
        house = cursor.fetchone()[0]
        
        if house != 'Unassigned':
            message = f'Teacher {name} from {department} is already in {house} house.'
            
        else:
            cursor.execute('SELECT houseName FROM HOUSE')
            houses = cursor.fetchall()

            house = choice(houses)[0]

            cursor.execute('UPDATE STAFF SET houseName = ? WHERE name = ? AND department = ?', (house, name, department))

            message = f'Teacher {name} from {department} is randomly assigned to {house} house.'

        conn.commit()
    
    return render_template('edit.html', message=message)

@app.route('/teachers')
def teachers():
    conn = sqlite3.connect('HOUSEALLOCATION.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute('SELECT name, houseName FROM STAFF WHERE houseName != ?', ('Unassigned',))
        data = cursor.fetchall()

    teachers = {}
    for item in data:
        if item[1] not in teachers.keys():
            teachers[item[1]] = [item[0]]
        else:
            teachers[item[1]].append(item[0])

    return render_template('teachers.html', data=teachers)

app.run()