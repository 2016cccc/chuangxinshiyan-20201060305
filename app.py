from flask import Flask, request, render_template
import datetime
import webbrowser

app = Flask(__name__)

messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    global messages

    if request.method == "POST":
        message = request.form["message"]
        time = datetime.datetime.now()
        messages.append((message, time))

    return render_template("index.html.jinja2", messages=messages)

if __name__ == "__main__":
    webbrowser.open_new('http://localhost:5000')
    app.run(debug=True)
