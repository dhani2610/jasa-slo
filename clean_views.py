import re

# 1. Update resources/views/front/programs.blade.php
prog_blade = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\resources\views\front\programs.blade.php"
with open(prog_blade, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace(
    "@section('title', 'Program Pelatihan & Sertifikasi Operator Keselamatan & Kesehatan Kerja Korporat (Training Ahli K3 Umum Corporate) | Lisensi Rig Resmi')",
    "@section('title', 'Program Pelatihan & Sertifikasi Ahli K3 Umum Corporate | Lisensi & Sertifikasi K3 Korporasi Resmi')"
)
text = text.replace(
    "@section('meta_description', 'Daftar 6 program resmi pelatihan Training Ahli K3 Umum Corporate: Ahli K3 Umum Corporate, Auditor SMK3, Analis Risiko HIRADC, Manajemen Risiko K3 ISO 45001/IADC, Pengurus P2K3 Bipartit, dan Toolpusher.')",
    "@section('meta_description', 'Katalog 10 program resmi pelatihan Training Ahli K3 Umum Corporate: Ahli K3 Umum Corporate, Audit SMK3 PP 50/2012, Manajemen Risiko HIRADC, Investigasi Insiden RCA/SCAT, Kelembagaan P2K3, Tanggap Darurat ERP, Ahli K3 Umum Resmi, Ahli K3 Umum Sertifikasi, Kebakaran Industri, dan K3 Ruang Terbatas & Ketinggian.')"
)
text = text.replace(
    "Skema Sertifikasi Personel Rig Resmi & Standar Energi Internasional",
    "Skema Sertifikasi Ahli K3 Umum & Pengawas Keselamatan Kerja Korporat Nasional"
)
text = text.replace(
    "Enam (6) Skema Resmi <span>Pelatihan Personel Rig & Manajemen Risiko K3</span>",
    "Sepuluh (10) Program Resmi <span>Pelatihan & Sertifikasi Ahli K3 Umum Corporate</span>"
)
text = text.replace(
    "Tingkatkan kompetensi pengoperasian rig pemboran, pemahaman reologi fluida, dan sertifikasi keahlian Anda melalui kurikulum komprehensif, instruktur berlisensi resmi, dan unit praktik simulator rig modern.",
    "Tingkatkan kompetensi pengawasan norma K3 industri, audit SMK3 166 kriteria, manajemen risiko HIRADC, dan kepatuhan perundangan K3 korporasi Anda melalui kurikulum komprehensif, instruktur lead auditor senior, dan sertifikasi terakreditasi resmi."
)
text = text.replace(
    "4 Hotline WhatsApp Layanan Konsultasi & Pendaftaran Rig",
    "4 Hotline WhatsApp Layanan Konsultasi & Pendaftaran K3 Korporasi"
)

with open(prog_blade, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated front/programs.blade.php successfully!")

# 2. Update resources/views/front/index.blade.php
index_blade = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\resources\views\front\index.blade.php"
with open(index_blade, "r", encoding="utf-8") as f:
    idx_text = f.read()

idx_text = idx_text.replace("6 Program K3 Korporat", "10 Program K3 Korporat")
idx_text = idx_text.replace("<!-- 6 PROGRAM RESMI K3 CORPORATE -->", "<!-- 10 PROGRAM RESMI K3 CORPORATE -->")
idx_text = idx_text.replace("6 Program Unggulan Ahli K3 Umum Corporate", "10 Program Unggulan Ahli K3 Umum Corporate")
idx_text = idx_text.replace("6 program pembinaan kompetensi K3", "10 program pembinaan kompetensi K3")

with open(index_blade, "w", encoding="utf-8") as f:
    f.write(idx_text)

print("Updated front/index.blade.php successfully!")
