from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = 'mysecret'

conn = sqlite3.connect('messages.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, timestamp TEXT)''')
conn.commit()


@app.route('/')
def index():
    c.execute('SELECT * FROM messages ORDER BY timestamp DESC')
    messages = c.fetchall()
    return render_template('index.html.jinja2', messages=messages)


@app.route('/submit', methods=['POST'])
def submit():
    content = request.form['content']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('INSERT INTO messages (content, timestamp) VALUES (?, ?)', (content, timestamp))
    conn.commit()
    flash('Your message has been posted.')
    return redirect('/')
