import urllib.request
import json

for port in [4040, 4041, 4042, 4043, 4044]:
    try:
        with urllib.request.urlopen(f'http://127.0.0.1:{port}/api/tunnels', timeout=2) as r:
            data = json.loads(r.read())
            print(f"=== Web UI Port {port} ===")
            for t in data.get('tunnels', []):
                print(f"  Name: {t['name']}")
                print(f"  Public URL: {t['public_url']}")
                print(f"  Forwarding to: {t['config']['addr']}")
    except Exception as e:
        print(f"Port {port}: not active or error: {e}")
