import os

base_dir = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp"
admin_dir = os.path.join(base_dir, "resources", "views", "admin")

replacements = [
    ("Training Drilling Indonesia", "Training Ahli K3 Umum Corporate"),
    ("TRAINING DRILLING INDONESIA", "TRAINING AHLI K3 UMUM CORPORATE"),
    ("Training Drilling", "Training Ahli K3 Umum Corporate"),
    ("TRAINING DRILLING", "TRAINING AHLI K3 UMUM CORP"),
    ("training drilling", "training ahli k3 umum corporate"),
    ("Drilling Rig", "K3 Corporate"),
    ("rig drilling", "K3 corporate"),
    ("Rig Drilling", "K3 Corporate"),
    ("Juru Bor", "Ahli K3 Umum"),
    ("Roughneck", "Auditor SMK3"),
    ("Derrickman", "Analis Risiko HIRADC"),
    ("Well Control", "Manajemen Risiko K3"),
    ("Mud Engineer", "Pengurus P2K3"),
    ("Kemnaker RI & BNSP", "Lembaga Sertifikasi K3 & Standar Korporasi"),
    ("Kemnaker RI", "Lembaga Akreditasi K3"),
    ("Kementerian Ketenagakerjaan", "Lembaga Sertifikasi K3"),
    ("Kementerian ESDM", "Lembaga Sertifikasi K3"),
    ("Kementerian", "Lembaga"),
    ("Dinas Tenaga Kerja", "Manajemen K3"),
    ("Pemerintah", "Otoritas Standar Keselamatan"),
    ("pemerintah", "standar keselamatan"),
]

for root, dirs, files in os.walk(admin_dir):
    for fn in files:
        if fn.endswith(".blade.php"):
            fp = os.path.join(root, fn)
            with open(fp, "r", encoding="utf-8") as f:
                c = f.read()
            for old, new in replacements:
                c = c.replace(old, new)
            with open(fp, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Updated admin view: {fn}")

print("Admin views updated!")
