import socket

for port in [25, 465, 587]:
    try:
        print(f"Testing port {port}...")
        s = socket.create_connection(("smtp.gmail.com", port), timeout=10)
        print(f"Port {port}: CONNECTED")
        s.close()
    except Exception as e:
        print(f"Port {port}: FAILED - {type(e).__name__}: {e}")
