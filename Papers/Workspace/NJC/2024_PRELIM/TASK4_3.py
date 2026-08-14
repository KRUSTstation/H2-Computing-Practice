# Task 4.4
from flask import Flask, render_template
import sqlite3

app = Flask(__name__, template_folder='TASK4_3')

@app.route('/')
def index():
    conn = sqlite3.connect('esports.db')
    cursor = conn.cursor()

    teams = set()
    with conn:
        cursor.execute('SELECT TeamName FROM PLAYER')
        for i in [i for i in cursor.fetchall()]:
            teams.add(i[0])

    return render_template('teams.html', teams=teams)

@app.route('/teams/<team>', methods = ['GET'])
def team(team):
    conn = sqlite3.connect('esports.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute('SELECT * FROM PLAYER WHERE TeamName = ?', (team,))
        mem = cursor.fetchall()

    return render_template('members.html', team=team, members=sorted(mem, key=lambda x: int(x[4]), reverse=True))

app.run()