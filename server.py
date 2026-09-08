from flask import Flask, request, render_template
import smtplib, socket

app = Flask(__name__)

def spammer(toAddr):
    toaddrs = [toAddr]
    fromaddrs = "adam.poodleschool.founder@gmail.com"
    message = "Hi, I'm requesting you ."

    numTimes = 10

    with smtplib.SMTP("smtp.gmail.com", 587) as smtpserver:
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

@app.route("/test-smtp")
def test_smtp():
    import socket

    results = {}

    try:
        addresses = socket.getaddrinfo(
            "smtp.gmail.com",
            None,
            socket.AF_UNSPEC,
            socket.SOCK_STREAM
        )

        results["dns"] = list({
            (x[4][0], x[0])
            for x in addresses
        })
    except Exception as e:
        results["dns_error"] = f"{type(e).__name__}: {e}"

    for port in [465, 587]:
        try:
            s = socket.create_connection(
                ("smtp.gmail.com", port),
                timeout=10
            )
            s.close()
            results[f"tcp_{port}"] = "CONNECTED"
        except Exception as e:
            results[f"tcp_{port}"] = f"{type(e).__name__}: {e}"
    
    for host, port in [
        ("smtp.gmail.com", 465),
        ("smtp.gmail.com", 587),
        ("google.com", 443),
    ]:
        try:
            s = socket.create_connection((host, port), timeout=10)
            s.close()
            results[f"{host}:{port}"] = "CONNECTED"
        except Exception as e:
            results[f"{host}:{port}"] = f"{type(e).__name__}: {e}"

    return results

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    user_input = data.get("input", "")

    print("Received:", user_input)

    spammer(user_input)

    return "", 204
