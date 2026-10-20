import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

tunnels = [
    ("Drone (Port 8008)", "https://spotty-limelight-stamina.ngrok-free.dev"),
    ("PTP (Port 8010)", "https://d9fc-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"),
    ("Drilling (Port 8012)", "https://e597-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"),
    ("Ahli K3 Corp (Port 8014)", "https://d651-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app")
]

for name, url in tunnels:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0",
            "ngrok-skip-browser-warning": "69420"
        })
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            print(f"[OK 200] {name} -> {url}")
    except Exception as e:
        print(f"[ERROR] {name} -> {url} ({e})")
