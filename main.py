import requests
import random
import time

INVITE = "WSqNFKQK7r"

def create():
    s = requests.Session()
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "X-Context-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IiwicmVmZXJyZXJfc3RyaW5nIjoiIiwicmVmZXJyZXJfZG9tYWluIjoiZGlzY29yZC5jb20iLCJjdXJyZW50X3N0cmVhbXRyYWNrIjoiIiwidHJhY2tpbmdfbm9kZV9pZCI6IiIsInJlZmVyZWVyX3NvdXJjZSI6IiIsImNsaWVudF9idWlsZF9udW1iZXIiOjM1NzA5LCJ2ZXJzaW9uIjoiMS4wLjkwNjUifQ=="
    })

    username = "vaxynn" + str(random.randint(1000,9999))
    email = f"{username}@gmail.com"

    fp = s.get("https://discord.com/api/v9/experiments").json()["fingerprint"]

    payload = {
        "fingerprint": fp,
        "email": email,
        "username": username,
        "password": "Vaxynn2025!",
        "date_of_birth": "1999-01-01",
        "consent": True,
        "captcha_key": None
    }

    r = s.post("https://discord.com/api/v9/auth/register", json=payload)

    if "token" in r.text:
        token = r.json()["token"]
        print(f"[+] {username} | {token[:50]}...")
        s.headers.update({"authorization": token})
        s.post(f"https://discord.com/api/v10/invites/{INVITE}")
    else:
        print(f"[-] Failed {r.status_code}")

for _ in range(10):
    threading.Thread(target=create).start()
time.sleep(3600)  # 1 hour
