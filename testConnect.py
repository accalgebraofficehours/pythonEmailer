import socket

@app.route("/test-ports")
def test_ports():
    results = {}

    for port in [25, 465, 587]:
        try:
            s = socket.create_connection(("smtp.gmail.com", port), timeout=10)
            s.close()
            results[port] = "CONNECTED"
        except Exception as e:
            results[port] = f"{type(e).__name__}: {e}"

    return results
