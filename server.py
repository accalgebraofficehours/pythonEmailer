from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

def spammer(toAddr):
    toaddrs = [toAddr]
    fromaddrs = "adam.poodleschool.founder@gmail.com"
    message = "Hi, I'm requesting you ."

    numTimes = 10

    with smtplib.SMTP("smtp.gmail.com", "587") as smtpserver:
      smtpserver.ehlo()
      smtpserver.starttls()
      smtpserver.ehlo()
      smtpserver.login("adam.poodleschool.founder@gmail.com", "zlnzowjgeoalhwcj")
      for i in range(numTimes):
        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(i)

    print("Done!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    user_input = data.get("input", "")

    print("Received:", user_input)

    spammer(toAddr)

    return "", 204
