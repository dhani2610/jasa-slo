import re

service_path = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\app\Services\AhliK3UmumSchemeService.php"

with open(service_path, "r", encoding="utf-8") as f:
    content = f.read()

# Check if program 7 already exists
has_prog7 = "'slug' => 'training-ahli-k3-umum-resmi'" in content
has_prog8 = "'slug' => 'training-ahli-k3-umum-sertifikasi'" in content
print(f"Program 7 exists: {has_prog7}")
print(f"Program 8 exists: {has_prog8}")
