import os
import re

base_dir = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp"
front_views_dir = os.path.join(base_dir, "resources", "views", "front")
layouts_dir = os.path.join(base_dir, "resources", "views", "layouts")

# 1. UPDATE LAYOUTS/FRONT.BLADE.PHP
front_layout_path = os.path.join(layouts_dir, "front.blade.php")
with open(front_layout_path, "r", encoding="utf-8") as f:
    fc = f.read()

# Replace general titles and descriptions
fc = re.sub(r"Training Drilling [^<]*", "Training Ahli K3 Umum Corporate | Pusat Pembinaan & Sertifikasi K3 Korporasi Resmi", fc)
fc = re.sub(r"TRAINING DRILLING INDONESIA", "TRAINING AHLI K3 UMUM CORPORATE", fc)
fc = re.sub(r"Training Drilling Indonesia", "Training Ahli K3 Umum Corporate", fc)
fc = re.sub(r"TRAINING DRILLING", "TRAINING AHLI K3 UMUM CORP", fc)
fc = re.sub(r"Training Drilling", "Training Ahli K3 Umum Corporate", fc)

# Replace :root palette
old_root_start = fc.find(":root {")
if old_root_start != -1:
    old_root_end = fc.find("}", old_root_start)
    new_root = """:root {
            /* TEMA UTAMA: SAFETY EMERALD LIME GREEN & CORPORATE SAFETY ORANGE */
            --primary-green: #10b981; /* Fresh Emerald Lime Green */
            --primary-green-dark: #059669; /* Forest Emerald */
            --primary-green-deep: #064e3b; /* Dark Pine */
            --primary-green-light: #ecfdf5; /* Soft Emerald Tint */
            --primary-green-subtle: #a7f3d0; /* Soft Green Border */
            --primary-green-accent: #22c55e; /* Neon Lime Accent */

            --primary-orange: #f97316; /* Energetic Safety Orange */
            --primary-orange-dark: #ea580c; /* Deep Safety Orange */
            --primary-orange-deep: #9a3412; /* Burnished Amber */
            --primary-orange-light: #fff7ed; /* Light Amber Tint */
            --primary-orange-subtle: #fed7aa; /* Warm Orange Border */
            --primary-orange-accent: #fb923c;

            --primary-purple: #10b981;
            --primary-purple-dark: #059669;
            --primary-purple-deep: #062e22;
            --primary-purple-light: #ecfdf5;
            --primary-purple-subtle: #a7f3d0;
            --primary-purple-accent: #22c55e;

            --primary-yellow: #f97316;
            --primary-yellow-dark: #ea580c;
            --primary-yellow-light: #fff7ed;
            --primary-yellow-subtle: #fed7aa;

            --primary-blue: #10b981;
            --primary-blue-dark: #062e22;

            --bg-dark: #062e22; /* Rich Deep Corporate Safety Emerald */
            --bg-dark-card: #09392b; /* Dark Slate Emerald Card */
            --bg-dark-hover: #0d4a39;
            --bg-light: #f0fdf4; /* Fresh Green Tint */
            --bg-white: #ffffff;

            --text-dark: #0f172a;
            --text-muted: #64748b;
            --text-light: #cbd5e1;
            --accent-mint: #10b981;
            --accent-amber: #f97316;

            --gold-gradient: linear-gradient(135deg, #10b981 0%, #059669 100%);
            --navy-gradient: linear-gradient(135deg, #062e22 0%, #09392b 50%, #0d4a39 100%);
            --purple-gradient: linear-gradient(135deg, #062e22 0%, #09392b 100%);
            --yellow-gradient: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            --yellow-purple-gradient: linear-gradient(135deg, #10b981 0%, #059669 100%);

            --wa-green: #25d366;
            --wa-green-hover: #20ba5a;
            --border-dark: rgba(16, 185, 129, 0.25);
            --border-light: #a7f3d0;
            --shadow-sm: 0 1px 3px rgba(6, 46, 34, 0.08);
            --shadow-md: 0 4px 6px -1px rgba(6, 46, 34, 0.1), 0 2px 4px -2px rgba(6, 46, 34, 0.06);
            --shadow-lg: 0 12px 28px -6px rgba(6, 46, 34, 0.28);
            --shadow-gold: 0 10px 25px -5px rgba(16, 185, 129, 0.45);
            --radius-md: 8px;
            --radius-lg: 12px;
            --radius-xl: 18px;
        }"""
    fc = fc[:old_root_start] + new_root + fc[old_root_end+1:]

# Replace navbar icon and active link border
fc = fc.replace("bi-cone-striped", "bi-shield-check")
fc = fc.replace("color: #d97706;", "color: #10b981;")
fc = fc.replace("color: #ea580c;", "color: #059669;")
fc = fc.replace("background: #fff7ed;", "background: #ecfdf5;")
fc = fc.replace("background: #fef3c7;", "background: #ecfdf5;")

# Replace Footer Programs
footer_programs_html = """<h4>Program Resmi</h4>
                    <ul class="footer-links">
                        <li><a href="{{ route('program.detail', 'training-pembinaan-ahli-k3-umum-corporate') }}">Pembinaan Ahli K3 Umum Corporate</a></li>
                        <li><a href="{{ route('program.detail', 'training-audit-sistem-manajemen-k3-smk3-korporat-pp-50-2012') }}">Audit SMK3 166 Kriteria PP 50/2012</a></li>
                        <li><a href="{{ route('program.detail', 'training-manajemen-risiko-k3-korporasi-hiradc-ibppr') }}">Manajemen Risiko HIRADC & IBPPR</a></li>
                        <li><a href="{{ route('program.detail', 'training-kelembagaan-pengurus-p2k3-korporat') }}">Tata Kelola Kelembagaan P2K3 Bipartit</a></li>
                        <li><a href="{{ route('programs') }}">Lihat Seluruh 6 Program K3 Korporat</a></li>
                    </ul>"""

fc = re.sub(r'<h4>Program Resmi</h4>\s*<ul class="footer-links">.*?</ul>', footer_programs_html, fc, flags=re.DOTALL)

# Footer desc
footer_desc_html = """<p class="footer-desc">
                        Pusat pembinaan, sertifikasi, dan in-house training Ahli K3 Umum Corporate terakreditasi: Pembinaan Ahli K3 Umum Perusahaan, Auditor SMK3 PP 50/2012 166 Kriteria, Manajemen Risiko HIRADC/IBPPR, Investigasi Insiden SCAT/RCA, serta Kelembagaan P2K3 Bipartit menuju Zero Harm.
                    </p>"""
fc = re.sub(r'<p class="footer-desc">.*?</p>', footer_desc_html, fc, flags=re.DOTALL)

# Footer bottom
footer_bottom_html = """<div class="footer-bottom">
                <div>
                    &copy; {{ date('Y') }} Training Ahli K3 Umum Corporate. Seluruh hak cipta dilindungi.
                </div>
                <div>
                    Pusat Pembinaan & Sertifikasi K3 Korporat • Standar Audit SMK3 PP 50/2012 & ISO 45001:2018 Terakreditasi
                </div>
            </div>"""
fc = re.sub(r'<div class="footer-bottom">.*?</div>\s*</div>\s*</footer>', footer_bottom_html + "\n        </div>\n    </footer>", fc, flags=re.DOTALL)

# WhatsApp Popup header & cards
fc = fc.replace("Customer Care Training Drilling Indonesia", "Customer Care Training Ahli K3 Umum Corporate")
fc = fc.replace("Konsultasi Sertifikasi Rig Drilling & Well Control 24/7", "Konsultasi Ahli K3 Umum, Audit SMK3 & P2K3 Korporat 24/7")
fc = fc.replace("Sertifikasi Personel Rig & Well Control", "Sertifikasi Ahli K3 Umum & Audit SMK3")
fc = fc.replace("Jadwal Batch Pelatihan Drilling & Kuota Kelas", "Jadwal Batch Pelatihan Ahli K3 Umum & Kuota")
fc = fc.replace("Silabus Juru Bor, Well Control & Mud Engineer", "Silabus Audit SMK3, HIRADC & Investigasi Insiden")
fc = fc.replace("In-House Training Operasi Rig Drilling B2B", "In-House Training K3 Perusahaan & Mock Audit SMK3")
fc = fc.replace("Layanan Resmi Terverifikasi Standar Rig Drilling & Well Control", "Layanan Resmi Terverifikasi Standar Ahli K3 Umum & SMK3 PP 50/2012")

with open(front_layout_path, "w", encoding="utf-8") as f:
    f.write(fc)

print("layouts/front.blade.php updated successfully!")
