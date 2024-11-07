from kuki.core import transcribe
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def update():
    file = request.files["audio"]
    if file:
        text = transcribe(file)

    return f"<span>{text}</span>"
