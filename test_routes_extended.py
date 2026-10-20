import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_local = "http://127.0.0.1:8014"
base_ngrok = "https://d651-2a09-bac1-34c0-18-00-1f1-206.ngrok-free.app"

routes = [
    "/",
    "/tentang-kami",
    "/program",
    "/program/training-ahli-k3-umum-resmi",
    "/program/training-ahli-k3-umum-sertifikasi",
    "/artikel",
    "/artikel/training-ahli-k3-umum-resmi-panduan-sertifikasi-dan-lisensi-k3-perusahaan-terakreditasi-nasional",
    "/artikel/training-ahli-k3-umum-sertifikasi-standar-kompetensi-personel-k3-dan-implementasi-smk3-korporasi",
    "/wilayah/jawa-barat",
    "/wilayah/jawa-barat/kota-bandung",
    "/wilayah/jawa-barat/kota-bandung/sukajadi",
    "/artikel/training-ahli-k3-umum-resmi-di-kota-bandung-jawa-barat",
    "/artikel/training-ahli-k3-umum-sertifikasi-di-kota-bandung-jawa-barat"
]

print("=== TESTING LOCAL ROUTES (PORT 8014) ===")
for r in routes:
    url = base_local + r
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>([^<]+)</title>', body)
            title = title_m.group(1).strip() if title_m else 'No title'
            print(f"[OK 200] {r} -> {title[:60]}")
    except Exception as e:
        print(f"[ERROR] {r} -> {e}")

print("\n=== TESTING VIA NGROK PUBLIC TUNNEL ===")
for r in ["/", "/program", "/program/training-ahli-k3-umum-resmi", "/program/training-ahli-k3-umum-sertifikasi", "/wilayah/jawa-barat/kota-bandung"]:
    url = base_ngrok + r
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "ngrok-skip-browser-warning": "69420"})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            print(f"[NGROK OK 200] {r}")
    except Exception as e:
        print(f"[NGROK ERROR] {r} -> {e}")
