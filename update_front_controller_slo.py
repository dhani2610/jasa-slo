import re

controller_path = r"c:\xampp\htdocs\web-pelatihan\jasa-slo\app\Http\Controllers\FrontController.php"

with open(controller_path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace Service import
text = text.replace("use App\\Services\\AhliK3UmumSchemeService;", "use App\\Services\\JasaSloSchemeService;")
text = text.replace("AhliK3UmumSchemeService::", "JasaSloSchemeService::")

# Update WhatsApp default text
text = text.replace(
    "Training Ahli K3 Umum Corp, saya ingin konsultasi pendaftaran pelatihan dan sertifikasi Ahli K3 Umum Corporate, Audit SMK3 166 Kriteria, HIRADC, dan P2K3 untuk wilayah {region}. Mohon info jadwal batch terbaru dan penawaran in-house training.",
    "Jasa SLO Indonesia, saya ingin konsultasi permohonan Sertifikat Laik Operasi (SLO) instalasi listrik (IPTL TR/TM, Genset, PLTS, Distribusi) untuk wilayah {region}. Mohon informasi persyaratan, jadwal inspeksi komisioning, dan estimasi biaya."
)
text = text.replace(
    "Pelatihan Ahli K3 Umum Corporate",
    "Jasa SLO & Sertifikasi Kelaikan Operasi Listrik"
)
text = text.replace(
    "Halo Admin Pusat Training Ahli K3 Umum Corporate, saya ingin info pendaftaran{$progText} di wilayah {$regionText}.",
    "Halo Admin Utama Jasa SLO Indonesia, saya ingin mengajukan permohonan Sertifikat Laik Operasi (SLO){$progText} di wilayah {$regionText}."
)
text = text.replace(
    "Halo CS Pelatihan Ahli K3 Umum Corporate (Hotline 2), mohon info jadwal batch terdekat dan kuota kelas di {$regionText}.",
    "Halo CS Jasa SLO Indonesia (Hotline 2), mohon info jadwal uji komisioning, inspeksi kelaikan listrik, dan kuota sertifikasi di {$regionText}."
)
text = text.replace(
    "Halo Tim Instruktur K3 Korporasi (Hotline 3), saya ingin konsultasi silabus materi sertifikasi Ahli K3 Umum, Audit SMK3, HIRADC, dan P2K3 di {$regionText}.",
    "Halo Tim Inspektur Teknik Ketenagalistrikan (Hotline 3), saya ingin konsultasi teknis pengujian trafo, genset, grounding, dan single line diagram di {$regionText}."
)
text = text.replace(
    "Halo Divisi Kerjasama In-House Training K3 (Hotline 4), kami bermaksud mengajukan proposal pelatihan in-house Ahli K3 Umum di perusahaan kami di {$regionText}.",
    "Halo Tim Sertifikasi SKTTK & Kerjasama Korporat (Hotline 4), kami ingin konsultasi sertifikasi kompetensi personel listrik dan paket uji SLO industri di {$regionText}."
)

# Update hotline descriptions
text = text.replace(
    "'Hotline Utama (Pendaftaran & Batch)'",
    "'Hotline Utama (Permohonan & Sertifikasi SLO)'"
)
text = text.replace(
    "'Layanan informasi jadwal, pendaftaran reguler & konfirmasi kuota kelas terdekat.'",
    "'Layanan resmi konsultasi permohonan Sertifikat Laik Operasi (SLO) TR/TM, Genset, dan PLTS.'"
)
text = text.replace(
    "'Hotline 2 (Layanan Jadwal & Sertifikasi)'",
    "'Hotline 2 (Jadwal Inspeksi & Uji Komisioning)'"
)
text = text.replace(
    "'Bantuan proses registrasi, info sertifikasi kompetensi Ahli K3 Umum & kualifikasi SMK3.'",
    "'Penjadwalan inspeksi lapangan, pengujian alat ukur megger, grounding, dan verifikasi dokumen.'"
)
text = text.replace(
    "'Hotline 3 (Silabus & Teknis Audit SMK3 / HIRADC)'",
    "'Hotline 3 (Konsultasi Teknis Elektro & Proteksi)'"
)
text = text.replace(
    "'Konsultasi kurikulum teknis 166 kriteria audit SMK3, manajemen risiko HIRADC, RCA insiden, dan P2K3.'",
    "'Konsultasi teknis PUIL, Single Line Diagram (SLD), relai proteksi, trafo, dan kualitas daya.'"
)
text = text.replace(
    "'Hotline 4 (In-House & Corporate Training)'",
    "'Hotline 4 (Sertifikasi Tenaga Teknik SKTTK & Korporat)'"
)
text = text.replace(
    "'Pengajuan proposal resmi in-house training dan sertifikasi personel K3 korporasi.'",
    "'Sertifikasi kompetensi personel kelistrikan (SKTTK) dan kontrak inspeksi berkala korporasi.'"
)

# Update Partners list in index()
old_partners = """        $partners = [
            ['name' => 'PT Pertamina (Persero)', 'role' => 'Standardisasi Sistem Manajemen HSE & Pembinaan Ahli K3 Operasional Migas'],
            ['name' => 'PT PLN (Persero)', 'role' => 'Implementasi K3 Ketenagalistrikan & Sertifikasi Pengawas K3 Pembangkit'],
            ['name' => 'PT Astra International Tbk', 'role' => 'Budaya Keselamatan Kerja Terpadu & Audit SMK3 Rantai Pasok Otomotif'],
            ['name' => 'PT Telkom Indonesia Tbk', 'role' => 'K3 Infrastruktur Telekomunikasi & Manajemen Risiko Operasional Lapangan'],
            ['name' => 'PT Unilever Indonesia Tbk', 'role' => 'Zero Harm Initiative & Pelatihan Tim Tanggap Darurat Pabrik Kimia'],
            ['name' => 'PT Indofood Sukses Makmur Tbk', 'role' => 'Sertifikasi Personel P2K3 & Penerapan Higiene Industri Manufaktur Pangan'],
            ['name' => 'PT Adaro Energy Indonesia Tbk', 'role' => 'Manajemen Risiko Tinggi Tambang Batubara & Sistem Pelaporan Insiden'],
            ['name' => 'PT Freeport Indonesia', 'role' => 'Penerapan Golden Safety Rules & Pelatihan Keselamatan Kerja Bawah Tanah'],
            ['name' => 'PT Vale Indonesia Tbk', 'role' => 'Standarisasi Audit SMK3 Pabrik Peleburan Nikel & Tata Kelola ESG'],
            ['name' => 'PT Wijaya Karya (Persero) Tbk', 'role' => 'K3 Konstruksi Gedung Tinggi & Infrastruktur Strategis Nasional'],
        ];"""

new_partners = """        $partners = [
            ['name' => 'PT PLN (Persero)', 'role' => 'Kemitraan Standardisasi Kelaikan Operasi & Penyaluran Tenaga Listrik Konsumen Tegangan Menengah'],
            ['name' => 'PT Indonesia Power', 'role' => 'Uji Komisioning & Sertifikasi Laik Operasi Unit Pembangkitan Thermal dan PLTU'],
            ['name' => 'PT PLN Nusantara Power', 'role' => 'Sertifikasi Kelaikan Operasi Pembangkit Energi Baru Terbarukan (EBT) & PLTS Grid'],
            ['name' => 'PT Pertamina Power Indonesia', 'role' => 'Inspeksi Kelaikan Sistem Kelistrikan Kilang, Captive Power & Gas Turbine'],
            ['name' => 'PT Cikarang Listrindo Tbk', 'role' => 'Uji Proteksi Relai, Trafo Daya & Jaringan Distribusi Kawasan Industri Terpadu'],
            ['name' => 'PT Medco Power Indonesia', 'role' => 'Sertifikasi SLO Pembangkit Panas Bumi (PLTP) & Gardu Induk Swasta'],
            ['name' => 'PT Pupuk Indonesia (Persero)', 'role' => 'Sertifikasi Laik Operasi Sistem Kelistrikan Pabrik Pupuk & Instalasi Ex-Proof'],
            ['name' => 'PT Semen Indonesia (Persero) Tbk', 'role' => 'Inspeksi Tegangan Menengah 20 kV, Motor Tegangan Tinggi & Sistem Pembumian'],
            ['name' => 'PT Telkom Data Ekosistem (NeutraDC)', 'role' => 'Uji Kelaikan Operasi Kelistrikan Data Center Tier 3/4 & Sistem Genset Dinamis'],
            ['name' => 'PT Astra Agro Lestari Tbk', 'role' => 'Sertifikasi Kelaikan Operasi Pembangkit Listrik Biogas & Distribusi Pabrik Sawit'],
        ];"""

text = text.replace(old_partners, new_partners)

# Update contact success message
text = text.replace(
    "Tim Konsultan Training Ahli K3 Umum Corporate Indonesia",
    "Tim Ahli Inspeksi Jasa SLO Indonesia"
)

with open(controller_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated FrontController.php successfully for Jasa SLO!")
