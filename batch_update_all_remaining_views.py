import os
import re

base_dir = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp"
front_dir = os.path.join(base_dir, "resources", "views", "front")
layouts_dir = os.path.join(base_dir, "resources", "views", "layouts")

# Generic replacements dict
replacements = [
    ("Training Drilling Indonesia", "Training Ahli K3 Umum Corporate"),
    ("TRAINING DRILLING INDONESIA", "TRAINING AHLI K3 UMUM CORPORATE"),
    ("Training Drilling", "Training Ahli K3 Umum Corporate"),
    ("TRAINING DRILLING", "TRAINING AHLI K3 UMUM CORP"),
    ("training drilling", "training ahli k3 umum corporate"),
    ("Drilling Rig", "K3 Corporate"),
    ("rig drilling", "K3 corporate"),
    ("Rig Drilling", "K3 Corporate"),
    ("Juru Bor (Driller)", "Ahli K3 Umum Corporate"),
    ("Juru Bor", "Ahli K3 Umum"),
    ("Roughneck", "Auditor SMK3"),
    ("Derrickman", "Analis Risiko HIRADC"),
    ("Well Control", "Manajemen Risiko K3"),
    ("Mud Engineer", "Pengurus P2K3 Bipartit"),
    ("Sertifikasi Rig Resmi", "Sertifikasi K3 Korporat Resmi"),
    ("Sertifikasi Rig", "Sertifikasi Ahli K3"),
    ("operasi rig", "manajemen keselamatan kerja"),
    ("Operasi Rig", "Manajemen Keselamatan Kerja"),
    ("lantai bor", "tempat kerja"),
    ("Lantai Bor", "Tempat Kerja"),
    ("menara bor", "area operasional"),
    ("Menara Bor", "Area Operasional"),
    ("fluida pemboran", "keselamatan proses industri"),
    ("lumpur pemboran", "keselamatan proses industri"),
    ("drilling console", "safety leadership system"),
    ("teknik pengeboran", "keselamatan dan kesehatan kerja korporat"),
    ("Teknik Pengeboran", "Keselamatan & Kesehatan Kerja Korporat"),
    ("pengeboran migas", "industri korporasi"),
    ("Pengeboran Migas", "Industri Korporasi"),
    ("pengeboran", "keselamatan kerja"),
    ("Pengeboran", "Keselamatan Kerja"),
    ("Driller", "Ahli K3"),
    ("driller", "ahli k3"),
    ("IADC WellSharp & IWCF", "SMK3 PP 50/2012 & ISO 45001"),
    ("IADC WellSharp", "SMK3 PP 50/2012"),
    ("IWCF", "ISO 45001"),
    ("Wellsite", "Korporasi"),
    ("wellsite", "korporasi"),
    ("Kemnaker RI & BNSP", "Lembaga Sertifikasi K3 & Standar Korporasi"),
    ("Kemnaker RI", "Lembaga Akreditasi K3"),
    ("Kementerian Ketenagakerjaan", "Lembaga Sertifikasi K3"),
    ("Kementerian ESDM", "Lembaga Sertifikasi K3"),
    ("Kementerian", "Lembaga"),
    ("Dinas Tenaga Kerja", "Manajemen K3"),
    ("Pemerintah", "Otoritas Standar Keselamatan"),
    ("pemerintah", "standar keselamatan kerja"),
    ("200 artikel", "direktori panduan teknis"),
    ("200 Artikel", "Direktori Panduan Teknis"),
    ("(200)", ""),
    ("6000-9000 kata", "pembahasan komprehensif"),
    ("6000-9000 Kata", "Pembahasan Komprehensif"),
    ("6.000-9.000 kata", "pembahasan mendalam"),
    ("6.000 - 9.000 kata", "pembahasan mendalam"),
    ("(6000-9000)", ""),
    ("(6.000-9.000)", ""),
]

# Color CSS replacements
color_replacements = [
    ("#ea580c", "#059669"),
    ("#c2410c", "#047857"),
    ("#d97706", "#10b981"),
    ("#f59e0b", "#10b981"),
    ("#fbbf24", "#34d399"),
    ("#facc15", "#34d399"),
    ("#fef08a", "#a7f3d0"),
    ("#fff7ed", "#ecfdf5"),
    ("#ffedd5", "#ecfdf5"),
    ("#fed7aa", "#a7f3d0"),
    ("#fef3c7", "#ecfdf5"),
    ("#fef9c3", "#ecfdf5"),
    ("#fde68a", "#a7f3d0"),
    ("#0f172a", "#062e22"),
    ("#1e293b", "#09392b"),
    ("#334155", "#0d4a39"),
    ("rgba(234, 88, 12,", "rgba(16, 185, 129,"),
    ("rgba(249, 115, 22,", "rgba(16, 185, 129,"),
    ("rgba(245, 158, 11,", "rgba(16, 185, 129,"),
    ("rgba(251, 191, 36,", "rgba(16, 185, 129,"),
    ("rgba(250, 204, 21,", "rgba(16, 185, 129,"),
]

def clean_file(filepath, is_admin=False):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply text replacements
    for old, new in replacements:
        content = content.replace(old, new)

    # For front views, also replace old orange/yellow color tints with fresh emerald green
    if not is_admin:
        for old, new in color_replacements:
            content = content.replace(old, new)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned & updated: {os.path.basename(filepath)}")

# Clean all front blade files
for fn in os.listdir(front_dir):
    if fn.endswith(".blade.php") and fn != "index.blade.php":
        clean_file(os.path.join(front_dir, fn))

# Clean layouts
clean_file(os.path.join(layouts_dir, "admin.blade.php"), is_admin=True)

print("All remaining views batch updated successfully!")
