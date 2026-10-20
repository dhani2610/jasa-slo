import re

path = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\resources\views\front\index.blade.php"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

sections = re.findall(r'<section[^>]*id="([^"]+)"', text)
print("Section IDs:", sections)

# Find any mentions of 'program'
prog_matches = [line.strip() for line in text.splitlines() if "program" in line.lower()]
print(f"Total lines mentioning program: {len(prog_matches)}")
for l in prog_matches[:10]:
    print("  ->", l)
