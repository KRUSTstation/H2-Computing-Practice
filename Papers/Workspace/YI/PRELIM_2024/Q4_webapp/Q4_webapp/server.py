from sqlite3 import *


from flask import Flask, render_template, request
app = Flask(__name__, template_folder='Task4_2_Akshat') 

### Your code goes below this line##

@app.route('/')
def index():
    conn = connect('./Q4_webapp/Q4_webapp/LOYALTY.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Concert')
    data = cursor.fetchall()

    conn.close()

    return render_template('index.html', data=data)

@app.route('/booking')
def booking():
    conn = connect('./Q4_webapp/Q4_webapp/LOYALTY.db')
    cursor = conn.cursor()

    cursor.execute('SELECT ConcertName FROM Concert')
    data = cursor.fetchall()

    conn.close()

    return render_template('booking.html', concerts=data)

@app.route('/check', methods=['POST'])
def check():
    email = request.form.get('email')
    password = request.form.get('password')
    concert = request.form.get('concert')
    quantity = request.form.get('quantity')

    conn = connect('./Q4_webapp/Q4_webapp/LOYALTY.db')
    cursor = conn.cursor()

    with conn:
    # login check
        cursor.execute('SELECT * FROM Member WHERE Email = ? AND Password = ?', (email, password))
        data = cursor.fetchone()

        if not data:
            return 'Invalid account'

        # concert id
        cursor.execute('SELECT * FROM Concert WHERE ConcertName = ?', (concert,))
        concert_data = cursor.fetchone()

        if concert_data[2] < quantity:
            return 'Invalid quantity'

        cursor.execute('INSERT INTO Purchase(ConcertID, Email, Quantity) VALUES (?, ?, ?)', (concert_data[0], email, quantity))
        cursor.execute('UPDATE Concert SET Quantity = ? WHERE ConcertID = ?', (concert_data[5] - int(quantity), concert_data[0]))
        conn.commit()
    
    return render_template('success.html', name=data[2], email=email, concert=concert_data, total = int(quantity) * int(concert_data[4]), qantity=quantity)
### Your code goes above this line##

app.run(debug=False, port = 5000)
