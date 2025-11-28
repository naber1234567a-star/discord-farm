import requests
import random
import threading
import time
from faker import Faker
fake = Faker()

INVITE = "WSqNFKQK7r"   # ← your invite code
THREADS = 120             # 50–150 accounts/hour on normal PC

created = 0

def turbo():
    global created
    while True:
        try:
            username = fake.user_name() + str(random.randint(1000,9999))
            email = f"{username.lower()}{random.randint(10000,99999)}@gmail.com"
            password = "Vaxynn2025!"

            s = requests.Session()
            s.headers.update({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3ViX3Byb3BlcnRpZXMiOnsiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiI6Imh0dHBzOi8vZGlzY29yZC5jb20vcmVnaXN0ZXIiLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozNTc3NzcsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            })

            # Get fingerprint
            fp = s.get("https://discord.com/api/v9/experiments").json()["fingerprint"]

            # Register
            payload = {
                "fingerprint": fp,
                "email": email,
                "username": username,
                "password": password,
                "invite": None,
                "consent": True,
                "date_of_birth": "1999-01-01",
                "captcha_key": None
            }

            r = s.post("https://discord.com/api/v9/auth/register", json=payload)

            if "token" in r.text:
                token = r.json()["token"]
                created += 1
                print(f"\033[92m[+] #{created} {username} | {token[:60]}...\033[0m")

                # Join server
                s.headers.update({"authorization": token})
                s.post(f"https://discord.com/api/v10/invites/{INVITE}")

                with open("tokens.txt", "a") as f:
                    f.write(token + "\n")

            else:
                print(f"\033[91m[-] Failed {username}\033[0m")
                time.sleep(1)

        except Exception as e:
            print(f"\033[93m[!] {e}\033[0m")
            time.sleep(0.5)

print("\033[96mTURBO GEN 2025 — 50–150 ACCOUNTS/HOUR — STARTED\033[0m")
for _ in range(THREADS):
    threading.Thread(target=turbo, daemon=True).start()

input("\nPress Enter to stop...")

