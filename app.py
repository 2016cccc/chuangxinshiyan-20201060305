from flask import Flask, request, render_template
import datetime
import webbrowser
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.static_folder = 'static'

messages = []

app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

file_path = os.path.join(os.getcwd(), "messages.txt")

def write_to_file(message_list):
    with open(file_path, 'w') as f:
        for message in message_list:
            f.write(",".join(message) + "\n")

@app.route("/", methods=["GET", "POST"])
def index():
    global messages

    if request.method == 'POST':
        message = request.form['message']
        color = request.form['colorpicker']
        file = request.files['file']

        # Save uploaded file
        filename = secure_filename(file.filename) if file else ""
        if filename:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

        text_color = request.form['colorpicker'] # 获取文本颜色
        time = datetime.datetime.now()
        messages.append((message, time.strftime('%Y-%m-%d %H:%M:%S'), color, filename, text_color))
        write_to_file(messages)

    return render_template('index.html.jinja2', messages=messages)

if __name__ == "__main__":
    webbrowser.open_new('http://localhost:5001')
    app.run(debug=True)