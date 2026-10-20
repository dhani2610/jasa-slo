import os
import re

views_dir = r"c:\xampp\htdocs\web-pelatihan\jasa-slo\resources\views\front"

# 1. Update programs.blade.php
prog_file = os.path.join(views_dir, "programs.blade.php")
with open(prog_file, "r", encoding="utf-8") as f:
    text = f.read()

text = re.sub(
    r"@section\('title', '[^']+'\)",
    "@section('title', 'Layanan Jasa SLO & Sertifikasi Ketenagalistrikan Resmi | Standar PUIL Nasional')",
    text
)
text = re.sub(
    r"@section\('meta_description', '[^']+'\)",
    "@section('meta_description', 'Katalog 8 layanan resmi Jasa SLO (Sertifikat Laik Operasi): IPTL Tegangan Rendah, Tegangan Menengah 20 kV, Genset Pembangkit, PLTS Atap, Distribusi SUTM/SKTM, Uji Komisioning, dan Sertifikasi SKTTK.')",
    text
)
text = text.replace("Skema Sertifikasi Personel Rig Resmi & Standar Energi Internasional", "Lembaga Inspeksi Teknik Terakreditasi & Standar Keselamatan Ketenagalistrikan")
text = text.replace("Skema Sertifikasi Ahli K3 Umum & Pengawas Keselamatan Kerja Korporat Nasional", "Lembaga Inspeksi Teknik Terakreditasi & Standar Keselamatan Ketenagalistrikan")
text = text.replace("Enam (6) Skema Resmi", "Delapan (8) Layanan Resmi")
text = text.replace("Sepuluh (10) Program Resmi", "Delapan (8) Layanan Resmi")
text = text.replace("Pelatihan & Sertifikasi Ahli K3 Umum Corporate", "Jasa SLO & Sertifikasi Kelaikan Operasi Listrik")
text = text.replace(
    "Tingkatkan kompetensi pengawasan norma K3 industri, audit SMK3 166 kriteria, manajemen risiko HIRADC, dan kepatuhan perundangan K3 korporasi Anda melalui kurikulum komprehensif, instruktur lead auditor senior, dan sertifikasi terakreditasi resmi.",
    "Pastikan seluruh instalasi ketenagalistrikan fasilitas industri, komersial, dan pembangkit mandiri Anda lulus uji kelaikan operasi (SLO) berstandar PUIL nasional bersama tim inspektur teknik profesional dan instrumen uji terkalibrasi KAN."
)
text = text.replace("Training Ahli K3 Umum Corporate", "Jasa SLO Indonesia")
text = text.replace("4-5 Hari", "3-7 Hari Kerja")
text = text.replace("Sertifikasi K3 Korporat Resmi", "Layanan Resmi SLO")
text = text.replace("Sertifikasi K3 Korporasi Resmi", "Layanan Resmi SLO")
text = text.replace("Detail & Wilayah", "Detail Teknis & Syarat")
text = text.replace("Chat WA", "Konsultasi SLO")
text = text.replace("4 Hotline WhatsApp Layanan Konsultasi & Pendaftaran K3 Korporasi", "4 Hotline WhatsApp Layanan Resmi Jasa SLO Ketenagalistrikan")
text = text.replace("border: 1px solid #a7f3d0;", "border: 1.5px solid #bfdbfe;")
text = text.replace("color: #062e22;", "color: #0a192f;")
text = text.replace("color: #0d4a39;", "color: #1e3a8a;")
text = text.replace("background: #059669;", "background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);")
text = text.replace("background: linear-gradient(145deg, #062e22 0%, #09392b 100%);", "background: linear-gradient(145deg, #0f2744 0%, #0a192f 100%);")
text = text.replace("border: 1px solid rgba(16, 185, 129, 0.4);", "border: 2px solid rgba(56, 189, 248, 0.4);")

with open(prog_file, "w", encoding="utf-8") as f:
    f.write(text)
print("Updated programs.blade.php")

# 2. Update about.blade.php
about_file = os.path.join(views_dir, "about.blade.php")
with open(about_file, "r", encoding="utf-8") as f:
    abt_text = f.read()

abt_text = re.sub(
    r"@section\('title', '[^']+'\)",
    "@section('title', 'Tentang Kami | Profil Lembaga Inspeksi Teknik Jasa SLO & Sertifikat Laik Operasi')",
    abt_text
)
abt_text = re.sub(
    r"@section\('meta_description', '[^']+'\)",
    "@section('meta_description', 'Profil lembaga inspeksi teknik ketenagalistrikan independen, sejarah, visi, misi, dan kredibilitas tim inspektur teknik dalam pengujian kelaikan operasi listrik di Indonesia.')",
    abt_text
)
abt_text = abt_text.replace("Training Ahli K3 Umum Corporate", "Jasa SLO Indonesia")
abt_text = abt_text.replace("Ahli K3 Umum Corporate", "Sertifikat Laik Operasi (SLO) Ketenagalistrikan")
abt_text = abt_text.replace("Audit SMK3 PP 50/2012", "Standar Uji Kelaikan PUIL")
abt_text = abt_text.replace("HIRADC", "Pengujian Tahanan Isolasi Megger & Grounding")
abt_text = abt_text.replace("P2K3 Bipartit", "Sertifikasi Tenaga Teknik SKTTK")
abt_text = abt_text.replace("Zero Harm", "Zero Electrical Fire & Incident")

with open(about_file, "w", encoding="utf-8") as f:
    f.write(abt_text)
print("Updated about.blade.php")

# 3. Update contact.blade.php
contact_file = os.path.join(views_dir, "contact.blade.php")
with open(contact_file, "r", encoding="utf-8") as f:
    cnt_text = f.read()

cnt_text = re.sub(
    r"@section\('title', '[^']+'\)",
    "@section('title', 'Kontak Kami | Layanan Cepat Permohonan Sertifikat Laik Operasi (Jasa SLO)')",
    cnt_text
)
cnt_text = re.sub(
    r"@section\('meta_description', '[^']+'\)",
    "@section('meta_description', 'Hubungi tim inspektur teknik resmi Jasa SLO untuk permohonan sertifikasi kelaikan operasi listrik tegangan rendah, menengah, genset, dan PLTS di seluruh Indonesia.')",
    cnt_text
)
cnt_text = cnt_text.replace("Training Ahli K3 Umum Corporate", "Jasa SLO Indonesia")
cnt_text = cnt_text.replace("Konsultan K3 Korporat", "Inspektur Teknik Ketenagalistrikan")
cnt_text = cnt_text.replace("Pendaftaran Pelatihan", "Permohonan Sertifikasi SLO")

with open(contact_file, "w", encoding="utf-8") as f:
    f.write(cnt_text)
print("Updated contact.blade.php")

# 4. Update articles.blade.php & article-detail.blade.php
for a_fname in ["articles.blade.php", "article-detail.blade.php"]:
    a_path = os.path.join(views_dir, a_fname)
    with open(a_path, "r", encoding="utf-8") as f:
        art_t = f.read()
    art_t = art_t.replace("Training Ahli K3 Umum Corporate", "Jasa SLO Indonesia")
    art_t = art_t.replace("Ahli K3 Umum Corporate", "Jasa SLO Ketenagalistrikan")
    art_t = art_t.replace("Audit SMK3 PP 50/2012", "Uji Kelaikan Operasi PUIL")
    art_t = art_t.replace("Lead Auditor SMK3 & Master Trainer K3 Korporasi", "Lead Electrical Inspector & Tim Ahli Ketenagalistrikan")
    art_t = art_t.replace("border: 1px solid #a7f3d0;", "border: 1px solid #bfdbfe;")
    art_t = art_t.replace("background: #059669;", "background: #1d4ed8;")
    art_t = art_t.replace("color: #062e22;", "color: #0a192f;")
    with open(a_path, "w", encoding="utf-8") as f:
        f.write(art_t)
    print(f"Updated {a_fname}")

# 5. Update regional views: wilayah-provinsi, wilayah-kabkot, wilayah-kecamatan
for w_fname in ["wilayah-provinsi.blade.php", "wilayah-kabkot.blade.php", "wilayah-kecamatan.blade.php", "program-region-detail.blade.php", "program-detail.blade.php"]:
    w_path = os.path.join(views_dir, w_fname)
    with open(w_path, "r", encoding="utf-8") as f:
        w_t = f.read()
    w_t = w_t.replace("Training Ahli K3 Umum Corporate", "Jasa SLO Ketenagalistrikan")
    w_t = w_t.replace("Training Ahli K3 Umum Corp", "Jasa SLO")
    w_t = w_t.replace("Ahli K3 Umum Corporate", "Jasa SLO (Sertifikat Laik Operasi)")
    w_t = w_t.replace("Lead Auditor SMK3 & Master Trainer K3 Korporasi", "Lead Electrical Inspector & Tim Ahli Ketenagalistrikan")
    w_t = w_t.replace("Audit SMK3 166 Kriteria", "Uji Komisioning & Kelaikan Listrik PUIL")
    w_t = w_t.replace("border: 1px solid #a7f3d0;", "border: 1px solid #bfdbfe;")
    w_t = w_t.replace("background: #059669;", "background: #1d4ed8;")
    w_t = w_t.replace("color: #062e22;", "color: #0a192f;")
    w_t = w_t.replace("background: #ecfdf5;", "background: #eff6ff;")
    w_t = w_t.replace("color: #059669;", "color: #1d4ed8;")
    with open(w_path, "w", encoding="utf-8") as f:
        f.write(w_t)
    print(f"Updated {w_fname}")

print("All front views successfully transformed to Jasa SLO!")
