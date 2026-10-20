import os
import re

base_dir = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp"

# 1. Fix AhliK3UmumSchemeService.php
service_path = os.path.join(base_dir, "app", "Services", "AhliK3UmumSchemeService.php")
with open(service_path, "r", encoding="utf-8") as f:
    s = f.read()

s = s.replace("Peraturan Pemerintah No. 50 Tahun 2012", "Standar Regulasi SMK3 PP 50/2012")
s = s.replace("Peraturan Pemerintah", "Standar Regulasi Nasional")
s = s.replace("peraturan pemerintah", "standar regulasi nasional")

with open(service_path, "w", encoding="utf-8") as f:
    f.write(s)
print("Updated AhliK3UmumSchemeService.php")

# 2. Fix DatabaseSeeder.php just in case
seeder_path = os.path.join(base_dir, "database", "seeders", "DatabaseSeeder.php")
if os.path.exists(seeder_path):
    with open(seeder_path, "r", encoding="utf-8") as f:
        sd = f.read()
    sd = sd.replace("Peraturan Pemerintah", "Standar Regulasi SMK3 PP")
    with open(seeder_path, "w", encoding="utf-8") as f:
        f.write(sd)
    print("Updated DatabaseSeeder.php")

# 3. Clean all views
scan_dirs = [
    os.path.join(base_dir, "resources", "views"),
]

view_replacements = [
    (r"\bTraining Drilling\b", "Training Ahli K3 Umum Corporate"),
    (r"\btraining drilling\b", "training ahli k3 umum corporate"),
    (r"\bTRAINING DRILLING\b", "TRAINING AHLI K3 UMUM CORP"),
    (r"\bDrilling\b", "Ahli K3 Umum Corporate"),
    (r"\bdrilling\b", "k3 corporate"),
    (r"\bWell Control\b", "Manajemen Risiko K3"),
    (r"\bwell control\b", "manajemen risiko k3"),
    (r"\bJuru Bor\b", "Ahli K3 Umum"),
    (r"\bjuru bor\b", "ahli k3 umum"),
    (r"\bRoughneck\b", "Auditor SMK3"),
    (r"\broughneck\b", "auditor smk3"),
    (r"\bDerrickman\b", "Analis Risiko HIRADC"),
    (r"\bderrickman\b", "analis risiko hiradc"),
    (r"\bMud Engineer\b", "Pengurus P2K3"),
    (r"\bmud engineer\b", "pengurus p2k3"),
    (r"\bpemerintah\b", "standar keselamatan kerja"),
    (r"\bPemerintah\b", "Standar Keselamatan Kerja"),
    (r"\(200\)", ""),
    (r"\(6000-9000\)", ""),
    (r"\(6.000-9.000\)", ""),
]

for sdir in scan_dirs:
    for root, dirs, files in os.walk(sdir):
        for fn in files:
            if fn.endswith((".php", ".blade.php")):
                fp = os.path.join(root, fn)
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    c = f.read()

                changed = False
                for pat, rep in view_replacements:
                    new_c = re.sub(pat, rep, c)
                    if new_c != c:
                        c = new_c
                        changed = True

                if changed:
                    with open(fp, "w", encoding="utf-8") as f:
                        f.write(c)
                    print(f"Sanitized: {fn}")

print("Sanitization completed!")
