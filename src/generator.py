import random
import time

ips = ["192.168.1.1", "10.0.0.5", "172.16.0.20", "192.168.1.50"]
methods = ["GET", "POST", "PUT"]

def generate_log():
    ip = random.choice(ips)
    method = random.choice(methods)
    return f"{ip} - - [{time.strftime('%d/%b/%Y:%H:%M:%S')}] \"{method} /index.html HTTP/1.1\" 200"

with open("data/access.log", "a") as f:
    for _ in range(10):
        f.write(generate_log() + "\n")

print("Logs generados en data/access.log")
