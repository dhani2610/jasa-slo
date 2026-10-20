import urllib.request
import json

for port in [4040, 4041, 4042]:
    try:
        url = f"http://127.0.0.1:{port}/api/tunnels"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"=== Port {port} Tunnels ===")
            for t in data.get("tunnels", []):
                print(f"Name: {t.get('name')}, Public URL: {t.get('public_url')}, Local Addr: {t.get('config', {}).get('addr')}")
    except Exception as e:
        print(f"Port {port}: {e}")
