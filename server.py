from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    user_input = data.get("input", "")

    print("Received:", user_input)

    # Your Python code here

    return "", 204
