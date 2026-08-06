import csv
import sqlite3

with open('./Q4_webapp/Q4_webapp/PURCHASE.TXT') as f:
    data = [i for i in csv.reader(f)][1:]

conn = sqlite3.connect('./Q4_webapp/Q4_webapp/LOYALTY.db')
cursor = conn.cursor()

with conn:
    for i in data:
        cursor.execute('INSERT INTO Purchase(ConcertID, Email, Quantity) VALUES (?, ?, ?)', i)

    conn.commit()