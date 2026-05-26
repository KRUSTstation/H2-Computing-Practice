# Task 4.1
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__, template_folder="Task_4_web")

type_order = ['Sit Ups', 'Standing Broad Jump', 'Sit And Reach', 'Pull-ups/Inclined Pull-ups', 'Shuttle Run', '2.4km Run']

with open('./Resources/napfa_results.csv') as f:
    data = [i for i in csv.reader(f)]

def quicksort(data, asc):
    if len(data) <= 1:
        return data
    
    pivot = float(data[len(data) // 2][2])
    less = [i for i in data if float(i[2]) < pivot]
    more = [i for i in data if float(i[2]) > pivot]
    equal = [i for i in data if float(i[2]) == pivot]

    if asc:
        return quicksort(less, asc) + equal + quicksort(more, asc)
    else:
        return quicksort(more, asc) + equal + quicksort(less, asc)

@app.route('/', methods=['GET','POST'])
def base():
    station = request.form.get('station')
    order = request.form.get('order')

    if not station or not order: return render_template('base.html', users=data, station='all')

    index = type_order.index(station)
    new_data = [i[:2] + [i[index+2]] for i in data]
    if order == 'ascending':
        new_data = quicksort(new_data, True)
    else:
        new_data = quicksort(new_data, False)

    return render_template('base.html', users=new_data, station=station)

app.run()