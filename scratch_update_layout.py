import os
import re

base_dir = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp"
front_views_dir = os.path.join(base_dir, "resources", "views", "front")
layouts_dir = os.path.join(base_dir, "resources", "views", "layouts")

print("Transforming layouts/front.blade.php...")
front_layout_path = os.path.join(layouts_dir, "front.blade.php")
with open(front_layout_path, "r", encoding="utf-8") as f:
    layout_content = f.read()

# Replace titles & meta
layout_content = re.sub(
    r'<title>@yield\(\'title\', [^)]+\)</title>',
    "<title>@yield('title', 'Training Ahli K3 Umum Corporate | Pusat Pembinaan & Sertifikasi K3 Perusahaan Resmi')</title>",
    layout_content
)
layout_content = re.sub(
    r'<meta name="description" content="@yield\(\'meta_description\', [^)]+\)">',
    "<meta name="description" content="@yield('meta_description', 'Pusat pembinaan dan sertifikasi resmi Ahli K3 Umum Corporate, Audit SMK3 166 Kriteria PP 50/2012, HIRADC, dan P2K3 Perusahaan di Indonesia.')">",
    layout_content
)

# Replace :root palette for fresh emerald green & safety orange
old_palette_marker = ":root {"
new_palette = """:root {
            /* TEMA UTAMA: SAFETY EMERALD LIME GREEN & CORPORATE SAFETY ORANGE */
            --primary-green: #10b981; /* Vibrant Emerald Lime Green */
            --primary-green-dark: #059669; /* Deep Forest Emerald */
            --primary-green-deep: #064e3b; /* Rich Dark Pine Green */
            --primary-green-light: #ecfdf5; /* Fresh Mint Tint */
            --primary-green-subtle: #a7f3d0; /* Soft Green Border */
            --primary-green-accent: #22c55e; /* Energetic Neon Green */

            --primary-orange: #f97316; /* Vibrant Safety Orange */
            --primary-orange-dark: #ea580c; /* Deep Amber Orange */
            --primary-orange-deep: #9a3412; /* Rich Burnished Orange */
            --primary-orange-light: #fff7ed; /* Soft Orange Tint */
            --primary-orange-subtle: #ffedd5; /* Warm Orange Border */
            --primary-orange-accent: #fb923c; /* Energetic Neon Orange */

            --primary-purple: #10b981;
            --primary-purple-dark: #059669;
            --primary-purple-deep: #062e22;
            --primary-purple-light: #ecfdf5;
            --primary-purple-subtle: #a7f3d0;
            --primary-purple-accent: #22c55e;

            --primary-yellow: #f97316;
            --primary-yellow-dark: #ea580c;
            --primary-yellow-light: #fff7ed;
            --primary-yellow-subtle: #ffedd5;

            --primary-blue: #10b981;
            --primary-blue-dark: #062e22;

            --bg-dark: #062e22; /* Deep Corporate Slate Emerald */
            --bg-dark-card: #09392b; /* Dark Slate Card */
            --bg-dark-hover: #0d4a39;
            --bg-light: #f0fdf4; /* Soft Emerald Tint */
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

# Find end of :root
root_end = layout_content.find("}", layout_content.find(old_palette_marker))
if root_end != -1:
    layout_content = layout_content[:layout_content.find(old_palette_marker)] + new_palette + layout_content[root_end+1:]

# Update navbar brand logo icon & colors
layout_content = layout_content.replace(
    """<div class="brand-icon">
            <i class="bi bi-cone-striped"></i>
        </div>""",
    """<div class="brand-icon" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); box-shadow: 0 3px 10px rgba(16, 185, 129, 0.38);">
            <i class="bi bi-shield-check"></i>
        </div>"""
)

# Navbar active state with crisp bottom border
layout_content = layout_content.replace(
    """.nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%) scaleX(0);
            width: 82%;
            height: 3px;
            background: #ea580c;
            border-radius: 4px 4px 0 0;
            box-shadow: 0 0 10px rgba(234, 88, 12, 0.75);
            transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }""",
    """.nav-link::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%) scaleX(0);
            width: 85%;
            height: 3px;
            background: #10b981;
            border-radius: 4px 4px 0 0;
            box-shadow: 0 0 10px rgba(16, 185, 129, 0.85);
            transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }"""
)

layout_content = layout_content.replace(
    """.nav-link:hover {
            color: #ea580c;
            background: #fff7ed;
        }""",
    """.nav-link:hover {
            color: #059669;
            background: #ecfdf5;
        }"""
)

layout_content = layout_content.replace(
    """.nav-link.active {
            color: #ea580c;
            background: #fff7ed;
            font-weight: 800;
        }""",
    """.nav-link.active {
            color: #059669;
            background: #ecfdf5;
            font-weight: 800;
        }"""
)

# Compact button "Hubungi"
layout_content = layout_content.replace(
    """.btn-wa-header {
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
        }""",
    """.btn-wa-header {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: #ffffff !important;
            border: 1px solid #a7f3d0;
            font-size: 0.82rem;
            font-weight: 700;
            padding: 7px 16px;
            border-radius: 50px;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            box-shadow: 0 3px 10px rgba(16, 185, 129, 0.3);
            transition: all 0.25s ease;
            text-decoration: none;
            white-space: nowrap;
            flex-shrink: 0;
        }"""
)

layout_content = layout_content.replace(
    """.btn-wa-header:hover {
            background: linear-gradient(135deg, #fef08a 0%, #facc15 100%);
            color: #1e0a3c !important;
            transform: translateY(-1px);
            color: #ffffff;
            box-shadow: 0 5px 15px rgba(16, 185, 129, 0.35);
        }""",
    """.btn-wa-header:hover {
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            color: #ffffff !important;
            transform: translateY(-1px);
            box-shadow: 0 5px 15px rgba(16, 185, 129, 0.45);
        }"""
)

# Update brand text
layout_content = layout_content.replace(
    """<div class="brand-text">
                        <h1>TRAINING <span>DRILLING</span></h1>
                    </div>""",
    """<div class="brand-text">
                        <h1>AHLI K3 UMUM <span>CORP</span></h1>
                    </div>"""
)

with open(front_layout_path, "w", encoding="utf-8") as f:
    f.write(layout_content)

print("Updated layouts/front.blade.php styling!")
