import urllib.request

routes = [
    "/",
    "/tentang-kami",
    "/program",
    "/program/training-pembinaan-ahli-k3-umum-corporate",
    "/artikel",
    "/wilayah/jawa-barat",
    "/wilayah/jawa-barat/kota-bandung",
    "/wilayah/jawa-barat/kota-bandung/andir",
    "/hubungi-kami",
    "/admin/login",
    "/sitemap.xml",
]

all_passed = True
for r in routes:
    url = f"http://127.0.0.1:8014{r}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            print(f"[{status}] {r}")
            if status != 200:
                all_passed = False
    except Exception as e:
        print(f"[ERR] {r} -> {e}")
        all_passed = False

if all_passed:
    print("ALL ROUTES PASSED HTTP 200 OK!")
else:
    print("SOME ROUTES FAILED!")
