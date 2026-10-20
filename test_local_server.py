import urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:8014", timeout=5) as resp:
        print("HTTP Status Port 8014:", resp.status)
        head = resp.read(500).decode("utf-8", errors="ignore")
        print("Preview:\n", head[:200])
except Exception as e:
    print("Error connecting to 8014:", e)
