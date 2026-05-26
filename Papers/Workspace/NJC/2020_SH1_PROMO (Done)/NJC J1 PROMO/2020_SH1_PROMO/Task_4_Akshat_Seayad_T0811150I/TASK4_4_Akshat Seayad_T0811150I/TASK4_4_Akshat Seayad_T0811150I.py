from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    conn = sqlite3.connect("C:/Users/aksha/OneDrive/VSC/VSC/Work/NJC/Computing/Practices/Workspace/2020_SH1_PROMO/NJC J1 PROMO/2020_SH1_PROMO/Task_4_Akshat_Seayad_T0811150I/schools.db")
    cursor = conn.cursor()

    substring = f'%{name}%'
    
    cursor.execute('SELECT * FROM School WHERE Name LIKE ?', (substring,))
    names = cursor.fetchall()

    dep = request.form['dep']

    deps = []
    for i in names:
        cursor.execute('SELECT * FROM Staff WHERE SchoolCode = ? AND Department = ?', (i[0], dep))
        temp = cursor.fetchall()
        for temp2 in temp:      
            temp2 = list(temp2)
            temp2.append(i[1])
            temp2.append(i[2])
            deps.append(temp2)
    
    conn.close()
    print(deps)
    return render_template('schools.html', deps=deps)
    
app.run()