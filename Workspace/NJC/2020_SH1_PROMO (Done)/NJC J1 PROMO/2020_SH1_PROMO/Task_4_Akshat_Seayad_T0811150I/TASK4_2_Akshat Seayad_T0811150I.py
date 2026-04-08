PATH = '../RENAME_FOLDER/'
import csv
import sqlite3

with open(f'{PATH}SCHOOL.TXT') as f:
    data = [i for i in csv.reader(f)][1:]

conn = sqlite3.connect('schools.db')
cursor = conn.cursor()
for info in data:
    cursor.execute(f"INSERT INTO School VALUES ('{info[0]}', '{info[1]}', '{info[2]}')")

with open(f'{PATH}STAFF.TXT') as f:
    data = [i for i in csv.reader(f)][1:]

for info in data:
    cursor.execute(f"INSERT INTO Staff VALUES ('{info[0]}', '{info[1]}', '{info[2]}', '{info[3]}')")

conn.commit()
conn.close()