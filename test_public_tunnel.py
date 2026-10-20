import urllib.request

url = "https://d651-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0",
    "ngrok-skip-browser-warning": "69420"
})

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        print("Public URL Status:", resp.status)
        content = resp.read(1000).decode("utf-8", errors="ignore")
        print("Content Preview:\n", content[:300])
except Exception as e:
    print("Error querying public URL:", e)
