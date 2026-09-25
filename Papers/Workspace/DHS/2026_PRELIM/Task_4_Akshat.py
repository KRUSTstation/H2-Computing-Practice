from flask import Flask, render_template, request
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['DHS']
coll = db['Prelims']

app = Flask(__name__, template_folder = './Task_4_web_Akshat')

@app.route('/', methods = ['GET', 'POST'])
def index():
    names = [i['full_name'] for i in coll.find()]

    data = list(coll.find())
    name = request.form.get('name')
    if not name:
        return render_template('index.html', names = names, data = data)

    print(name)
    data = list(coll.find({'full_name': name}))
    print(data)

    return render_template('index.html', names = names, data = data)

app.run()