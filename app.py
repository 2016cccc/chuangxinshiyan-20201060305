from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'mysecret'

messages_file = 'messages.txt'

if not os.path.exists(messages_file):
    with open(messages_file, 'w'):
        pass


@app.route('/')
def index():
    messages = []
    with open(messages_file, 'r') as f:
        for line in f:
            message = line.strip().split(',')
            messages.append(message)
    messages.sort(key=lambda x: x[1], reverse=True)
    return render_template('index.html.jinja2', messages=messages)


@app.route('/submit', methods=['POST'])
def submit():
    content = request.form['content']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(messages_file, 'a') as f:
        f.write(f'{content},{timestamp}\n')
    flash('Your message has been posted.')
    return redirect('/')
