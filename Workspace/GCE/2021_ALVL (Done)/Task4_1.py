# YOUR ANSWER HERE
from flask import Flask, render_template

app = Flask(__name__, template_folder='Task4_1')

@app.route('/')
def base():
    return render_template('base.html')

app.run()