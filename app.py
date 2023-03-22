from flask import Flask, request, render_template
import datetime
import webbrowser
import os

app = Flask(__name__)

messages = []

file_path = os.path.join(os.getcwd(), "messages.txt")

def write_to_file(message_list):
    with open(file_path, 'w') as f:
        for message in message_list:
            f.write(",".join(message) + "\n")


@app.route("/", methods=["GET", "POST"])
def index():
    global messages

    if request.method == "POST":
        message = request.form["message"]
        color = request.form["colorpicker"]
        time = datetime.datetime.now()
        messages.append((message, time.strftime("%Y-%m-%d %H:%M:%S"), color))
        write_to_file(messages)

    return render_template("index.html.jinja2", messages=messages)

if __name__ == "__main__":
    webbrowser.open_new('http://localhost:5000')
    app.run(debug=True)
    
