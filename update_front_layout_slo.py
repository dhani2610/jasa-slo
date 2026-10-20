import re

layout_path = r"c:\xampp\htdocs\web-pelatihan\jasa-slo\resources\views\layouts\front.blade.php"

with open(layout_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Title and Meta
text = re.sub(
    r"<title>@yield\('title', '[^']+'\)</title>",
    "<title>@yield('title', 'Jasa SLO - Sertifikat Laik Operasi Ketenagalistrikan | Layanan Resmi Uji Komisioning')</title>",
    text
)
text = re.sub(
    r"<meta name=\"description\" content=\"@yield\('meta_description', '[^']+'\)\">",
    "<meta name=\"description\" content=\"@yield('meta_description', 'Layanan resmi Jasa SLO (Sertifikat Laik Operasi), uji komisioning instalasi listrik tegangan rendah, tegangan menengah 20 kV, genset, PLTS, dan proteksi petir di 38 provinsi di Indonesia.')\">",
    text
)

# 2. Add Favicon (Electric Shield with Lightning Bolt in Blue & Yellow)
favicon_tag = """    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M16 2L4 7v9c0 8.84 5.16 13.8 12 15 6.84-1.2 12-6.16 12-15V7L16 2z' fill='%231e40af'/%3E%3Cpath d='M16 4.2L6 8.5v7.5c0 7.2 4.2 11.3 10 12.4 5.8-1.1 10-5.2 10-12.4V8.5L16 4.2z' fill='%232563eb'/%3E%3Cpath d='M17 7l-6 10h5l-2 8 8-11h-5l3-7z' fill='%23facc15'/%3E%3C/svg%3E">
"""
if "<link rel=\"icon\"" not in text:
    text = text.replace("<head>", "<head>\n" + favicon_tag)

# 3. Update CSS Root Palette to Blue & Yellow with Mint Highlights
old_palette = """:root {
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

new_palette = """:root {
            /* TEMA UTAMA: ELECTRIC BLUE & HIGH-VOLTAGE YELLOW (WARNA WEB: BIRU KUNING) */
            --primary-blue: #1d4ed8; /* Vibrant Royal Electric Blue */
            --primary-blue-dark: #1e3a8a; /* Deep Midnight Sapphire */
            --primary-blue-deep: #0a192f; /* Deep Power Grid Navy */
            --primary-blue-light: #eff6ff; /* Soft Ice Blue Tint */
            --primary-blue-subtle: #bfdbfe; /* Soft Sky Blue Border */
            --primary-blue-accent: #38bdf8; /* Bright Cyan Glow */

            --primary-yellow: #eab308; /* High-Voltage Electric Gold / Yellow */
            --primary-yellow-dark: #ca8a04; /* Deep Golden Amber */
            --primary-yellow-deep: #854d0e; /* Burnished Gold */
            --primary-yellow-light: #fefce8; /* Light Amber Glow */
            --primary-yellow-subtle: #fef08a; /* Soft Yellow Border */
            --primary-yellow-accent: #facc15; /* Bright Electric Spark Yellow */

            --primary-green: #10b981; /* Mint / Green Safe Indicator */
            --primary-green-dark: #059669;
            --primary-green-light: #ecfdf5;
            --primary-green-subtle: #a7f3d0;

            --bg-dark: #0a192f; /* Midnight High-Tech Power Navy */
            --bg-dark-card: #0f2744; /* Power Grid Card Background */
            --bg-dark-hover: #173861;
            --bg-light: #f8fafc; /* Crisp Clean Off-White */
            --bg-white: #ffffff;

            --text-dark: #0f172a;
            --text-muted: #64748b;
            --text-light: #cbd5e1;
            --accent-mint: #10b981;
            --accent-amber: #eab308;

            --gold-gradient: linear-gradient(135deg, #facc15 0%, #eab308 100%);
            --navy-gradient: linear-gradient(135deg, #0a192f 0%, #0f2744 50%, #1e3a8a 100%);
            --blue-gradient: linear-gradient(135deg, #1d4ed8 0%, #2563eb 50%, #0284c7 100%);
            --yellow-gradient: linear-gradient(135deg, #facc15 0%, #eab308 100%);
            --yellow-blue-gradient: linear-gradient(135deg, #1d4ed8 0%, #eab308 100%);

            --wa-green: #25d366;
            --wa-green-hover: #20ba5a;
            --border-dark: rgba(56, 189, 248, 0.25);
            --border-light: #bfdbfe;
            --shadow-sm: 0 1px 3px rgba(10, 25, 47, 0.08);
            --shadow-md: 0 4px 6px -1px rgba(10, 25, 47, 0.1), 0 2px 4px -2px rgba(10, 25, 47, 0.06);
            --shadow-lg: 0 12px 28px -6px rgba(10, 25, 47, 0.28);
            --shadow-gold: 0 10px 25px -5px rgba(234, 179, 8, 0.45);
            --radius-md: 8px;
            --radius-lg: 12px;
            --radius-xl: 18px;
        }"""

text = text.replace(old_palette, new_palette)

# 4. Update Nav-link Active Border Bottom Color to Electric Yellow
text = re.sub(
    r"\.nav-link::after\s*\{[^}]*background:\s*[^;]+;",
    """.nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%) scaleX(0);
            width: 85%;
            height: 3px;
            background: #eab308;
            border-radius: 4px 4px 0 0;
            box-shadow: 0 0 10px rgba(234, 179, 8, 0.85);""",
    text
)

text = re.sub(
    r"\.nav-link:hover\s*\{[^}]*\}",
    """.nav-link:hover {
            color: #1d4ed8;
            background: #eff6ff;
        }""",
    text
)

text = re.sub(
    r"\.nav-link\.active\s*\{[^}]*\}",
    """.nav-link.active {
            color: #1d4ed8;
            background: #eff6ff;
            font-weight: 800;
        }""",
    text
)

# 5. Update Header Button "Hubungi" (Compact, Electric Blue + Yellow Border)
old_btn_header = """.btn-wa-header {
            background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
            color: #ffffff !important;
            border: 1px solid #fef08a;
            color: #ffffff;
            font-size: 0.82rem;
            font-weight: 700;
            padding: 7px 16px;
            border-radius: 50px;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            box-shadow: 0 3px 10px rgba(16, 185, 129, 0.25);
            transition: all 0.25s ease;
            text-decoration: none;
            white-space: nowrap;
            flex-shrink: 0;
        }

        .btn-wa-header:hover {
            background: linear-gradient(135deg, #fef08a 0%, #facc15 100%);
            color: #1e0a3c !important;
            transform: translateY(-1px);
            color: #ffffff;
            box-shadow: 0 5px 15px rgba(16, 185, 129, 0.35);
        }"""

new_btn_header = """.btn-wa-header {
            background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
            color: #ffffff !important;
            border: 1px solid #facc15;
            font-size: 0.82rem;
            font-weight: 700;
            padding: 7px 16px;
            border-radius: 50px;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            box-shadow: 0 3px 10px rgba(29, 78, 216, 0.3);
            transition: all 0.25s ease;
            text-decoration: none;
            white-space: nowrap;
            flex-shrink: 0;
        }

        .btn-wa-header:hover {
            background: linear-gradient(135deg, #facc15 0%, #eab308 100%);
            color: #0f172a !important;
            transform: translateY(-1px);
            box-shadow: 0 5px 15px rgba(234, 179, 8, 0.45);
        }"""

text = text.replace(old_btn_header, new_btn_header)

# 6. Update Brand Logo in Navbar
old_brand_html = """                <a href="{{ route('home') }}" class="brand-logo">
                    <div class="brand-icon">
                        <i class="bi bi-shield-check"></i>
                    </div>
                    <div class="brand-text">
                        <h1>TRAINING <span>AHLI K3 UMUM CORP</span></h1>
                    </div>
                </a>"""

new_brand_html = """                <a href="{{ route('home') }}" class="brand-logo">
                    <div class="brand-icon" style="background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%); border: 1.5px solid #facc15; color: #facc15; box-shadow: 0 0 12px rgba(250, 204, 21, 0.4);">
                        <i class="bi bi-lightning-charge-fill"></i>
                    </div>
                    <div class="brand-text">
                        <h1 style="font-size: 1.15rem; font-weight: 800; letter-spacing: -0.5px; color: #1e3a8a; margin: 0;">JASA <span style="color: #eab308;">SLO</span></h1>
                        <span style="font-size: 0.65rem; font-weight: 700; color: #64748b; letter-spacing: 0.5px; text-transform: uppercase; display: block; margin-top: -2px;">Sertifikat Laik Operasi</span>
                    </div>
                </a>"""

text = text.replace(old_brand_html, new_brand_html)

# 7. Update Footer Brand and Content
old_footer_brand = """                    <div class="brand-logo" style="margin-bottom: 14px;">
                        <div class="brand-icon">
                            <i class="bi bi-shield-check"></i>
                        </div>
                        <div class="brand-text">
                            <h3 style="font-size: 0.98rem; font-weight: 800; color: #fff;">TRAINING <span style="color: var(--accent-mint);">AHLI K3 UMUM CORP</span></h3>
                        </div>
                    </div>
                    <p class="footer-desc">
                        Pusat pembinaan, sertifikasi, dan in-house training Ahli K3 Umum Corporate terakreditasi: Pembinaan Ahli K3 Umum Perusahaan, Auditor SMK3 PP 50/2012 166 Kriteria, Manajemen Risiko HIRADC/IBPPR, Investigasi Insiden SCAT/RCA, serta Kelembagaan P2K3 Bipartit menuju Zero Harm.
                    </p>"""

new_footer_brand = """                    <div class="brand-logo" style="margin-bottom: 14px;">
                        <div class="brand-icon" style="background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%); border: 1.5px solid #facc15; color: #facc15;">
                            <i class="bi bi-lightning-charge-fill"></i>
                        </div>
                        <div class="brand-text">
                            <h3 style="font-size: 1.05rem; font-weight: 800; color: #fff;">JASA <span style="color: #facc15;">SLO</span></h3>
                            <span style="font-size: 0.68rem; color: #93c5fd; letter-spacing: 0.5px; text-transform: uppercase; display: block;">Sertifikat Laik Operasi Ketenagalistrikan</span>
                        </div>
                    </div>
                    <p class="footer-desc">
                        Lembaga inspeksi teknik dan sertifikasi kelaikan operasi ketenagalistrikan terakreditasi: Uji Kelaikan Operasi IPTL Tegangan Rendah, Tegangan Menengah 20 kV, Pembangkit Genset Diesel & PLTS Atap, Distribusi SUTM/SKTM, Uji Komisioning Pembumian, Audit PUIL, dan Sertifikasi Tenaga Teknik SKTTK Nasional.
                    </p>"""

text = text.replace(old_footer_brand, new_footer_brand)

# 8. Update Footer Links to Jasa SLO Programs
old_footer_programs = """                        <li><a href="{{ route('program.detail', 'training-pembinaan-ahli-k3-umum-corporate') }}">Pembinaan Ahli K3 Umum Corporate</a></li>
                        <li><a href="{{ route('program.detail', 'training-audit-sistem-manajemen-k3-smk3-korporat-pp-50-2012') }}">Audit SMK3 166 Kriteria PP 50/2012</a></li>
                        <li><a href="{{ route('program.detail', 'training-manajemen-risiko-k3-korporasi-hiradc-ibppr') }}">Manajemen Risiko HIRADC & IBPPR</a></li>
                        <li><a href="{{ route('program.detail', 'training-kelembagaan-pengurus-p2k3-korporat') }}">Tata Kelola Kelembagaan P2K3 Bipartit</a></li>
                        <li><a href="{{ route('programs') }}">Lihat Seluruh 6 Program K3 Korporat</a></li>"""

new_footer_programs = """                        <li><a href="{{ route('program.detail', 'jasa-slo-iptl-tegangan-rendah') }}">Jasa SLO Tegangan Rendah (IPTL TR)</a></li>
                        <li><a href="{{ route('program.detail', 'jasa-slo-iptl-tegangan-menengah') }}">Jasa SLO Tegangan Menengah (20 kV)</a></li>
                        <li><a href="{{ route('program.detail', 'jasa-slo-pembangkit-listrik-genset-plts') }}">Jasa SLO Genset & PLTS Industri</a></li>
                        <li><a href="{{ route('program.detail', 'training-sertifikasi-tenaga-teknik-ketenagalistrikan-skttk') }}">Sertifikasi Tenaga Teknik SKTTK</a></li>
                        <li><a href="{{ route('programs') }}">Lihat Seluruh 8 Layanan Jasa SLO</a></li>"""

text = text.replace(old_footer_programs, new_footer_programs)

# 9. Update Floating WA Modal Text
text = text.replace(
    "Hotline Layanan Resmi Training Ahli K3 Umum Corporate",
    "Hotline Resmi Layanan Jasa SLO & Uji Komisioning Ketenagalistrikan"
)
text = text.replace(
    "Pilih kontak WhatsApp konsultan K3 korporasi sesuai kebutuhan Anda untuk respon prioritas:",
    "Pilih kontak WhatsApp inspektur teknik dan konsultan kelaikan operasi listrik untuk respon cepat 24 jam:"
)

with open(layout_path, "w", encoding="utf-8") as f:
    f.write(text)

print("layouts/front.blade.php updated successfully for Jasa SLO!")
