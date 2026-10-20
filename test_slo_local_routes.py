import urllib.request
import re

base_url = "http://127.0.0.1:8016"

routes = [
    "/",
    "/tentang-kami",
    "/program",
    "/program/jasa-slo-iptl-tegangan-rendah",
    "/program/jasa-slo-iptl-tegangan-menengah",
    "/program/jasa-slo-pembangkit-listrik-genset-plts",
    "/artikel",
    "/artikel/training-jasa-slo-panduan-lengkap-sertifikasi-laik-operasi-ketenagalistrikan-standar-puil-di-indonesia",
    "/wilayah/jawa-barat",
    "/wilayah/jawa-barat/kota-bandung",
    "/wilayah/jawa-barat/kota-bandung/sukajadi",
    "/artikel/training-jasa-slo-panduan-lengkap-sertifikasi-laik-operasi-ketenagalistrikan-standar-puil-di-kota-bandung-jawa-barat",
    "/hubungi-kami",
    "/admin/login"
]

print("=== TESTING LOCAL JASA SLO ROUTES (PORT 8016) ===")
for r in routes:
    url = base_url + r
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode('utf-8', errors='ignore')
            title_m = re.search(r'<title>([^<]+)</title>', body)
            title = title_m.group(1).strip() if title_m else 'No title'
            print(f"[OK 200] {r} -> {title[:65]}")
    except Exception as e:
        print(f"[ERROR] {r} -> {e}")
