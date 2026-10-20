import os
import re

base_dir = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp"

forbidden_gov = [
    r"\bkemnaker\b",
    r"\bkementerian\b",
    r"\besdm\b",
    r"\bpemerintah\b",
    r"\bdinas tenaga kerja\b",
]

forbidden_ai = [
    r"\(?200\)?\s*artikel",
    r"\(?6000\s*-\s*9000\)?\s*kata",
    r"\(?6\.000\s*-\s*9\.000\)?\s*kata",
]

forbidden_old_domain = [
    r"\bdrilling\b",
    r"\bjuru bor\b",
    r"\broughneck\b",
    r"\bderrickman\b",
    r"\bwell control\b",
    r"\bmud engineer\b",
]

scan_dirs = [
    os.path.join(base_dir, "resources", "views"),
    os.path.join(base_dir, "app"),
    os.path.join(base_dir, "database", "seeders")
]

gov_findings = []
ai_findings = []
old_findings = []

for sdir in scan_dirs:
    for root, dirs, files in os.walk(sdir):
        for fn in files:
            if fn.endswith((".php", ".blade.php", ".js")):
                fp = os.path.join(root, fn)
                with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                for pat in forbidden_gov:
                    matches = re.findall(pat, content, re.IGNORECASE)
                    if matches:
                        gov_findings.append((fp, pat, len(matches)))

                for pat in forbidden_ai:
                    matches = re.findall(pat, content, re.IGNORECASE)
                    if matches:
                        ai_findings.append((fp, pat, len(matches)))

                for pat in forbidden_old_domain:
                    matches = re.findall(pat, content, re.IGNORECASE)
                    if matches:
                        old_findings.append((fp, pat, len(matches)))

print("=== AUDIT RESULTS ===")
print(f"Government mentions found: {len(gov_findings)}")
for item in gov_findings[:10]:
    print("  GOV:", item)

print(f"\nAI word count mentions found: {len(ai_findings)}")
for item in ai_findings[:10]:
    print("  AI:", item)

print(f"\nOld drilling domain mentions found: {len(old_findings)}")
for item in old_findings[:10]:
    print("  OLD:", item)
