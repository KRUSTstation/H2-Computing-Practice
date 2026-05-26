# Task 4.3
from flask import Flask, render_template
import csv

with open('./resources/people.txt') as f:
    data = [i for i in csv.reader(f)]

people = []
for i in data:
    if i[2] == 'Person':
        people.append((Person(i[0], i[1]), i[2]))
    elif i[2] == 'Staff':
        people.append((Staff(i[0], i[1]), i[2]))
    elif i[2] == 'Student':
        people.append((Person(i[0], i[1]), i[2]))

app = Flask(__name__, template_folder="./Task4_3")

@app.route('/')
def base():

    return render_template('base.html', people=people)

app.run()