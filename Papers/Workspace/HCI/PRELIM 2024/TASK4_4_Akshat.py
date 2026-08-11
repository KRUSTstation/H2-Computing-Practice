from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='./TASK4_4_Akshat')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    conn = sqlite3.connect('TRIP.db')
    cursor = conn.cursor()

    date = request.form.get('date')

    with conn:
        cursor.execute('SELECT C.Name, F.DepartCity, F.ArrivalCity, T.Seat FROM Ticket as T JOIN Customer as C ON T.CustomerNo = C.CustomerNo JOIN FLight AS F ON T.FlightNo = F.FlightNo WHERE T.Date = ?', (date,))
        items = cursor.fetchall()

    return render_template('index.html', items=items)

app.run()