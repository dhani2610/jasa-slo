import os
import re

service_path = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\app\Services\AhliK3UmumSchemeService.php"

with open(service_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. NEW PROGRAMS 7, 8, 9, 10
programs_to_add = """            [
                'id' => 7,
                'title' => 'Training Ahli K3 Umum Resmi (Sertifikasi Lisensi K3 Korporat Nasional)',
                'slug' => 'training-ahli-k3-umum-resmi',
                'level_code' => 'Ahli K3 Umum Resmi',
                'level_name' => 'Tingkat Nasional / Certified Safety Officer',
                'badge' => 'Sertifikasi Resmi',
                'duration' => '12 Hari (120 Jam Pelajaran)',
                'method' => 'In-House Training & Public Class Terakreditasi Nasional',
                'certification' => 'Sertifikat Kompetensi Ahli K3 Umum Resmi & Lisensi Penunjukan K3',
                'price_note' => 'Hubungi Tim Konsultan Corporate',
                'icon' => 'bi-patch-check-fill',
                'short_description' => 'Program sertifikasi resmi Ahli K3 Umum berlisensi sah nasional untuk mencetak tenaga ahli keselamatan kerja yang kompeten, kredibel, dan berintegritas.',
                'overview' => 'Program Training Ahli K3 Umum Resmi diselenggarakan secara khusus bagi personel yang ditugaskan perusahaan untuk memegang lisensi resmi keselamatan kerja di lingkungan operasional. Peserta dilatih secara intensif mendalami peraturan perundangan keselamatan kerja, teknik pengawasan norma K3 mekanik, bejana tekan, listrik, penanggulangan kebakaran, higiene industri, hingga kelembagaan P2K3 berstandar akreditasi resmi.',
                'target_audience' => 'Calon Ahli K3 Umum Resmi Perusahaan, HSE Officer, Safety Inspector, Supervisor Produksi, Management Trainee, dan HR/GA Manager',
                'curriculum' => [
                    'Modul 1: Kebijakan Nasional & Peraturan Perundangan K3 Terkini di Indonesia',
                    'Modul 2: Teori Penyebab Kecelakaan Kerja, Prinsip Pengendalian & Budaya K3',
                    'Modul 3: Manajemen Risiko Terpadu: HIRADC, IBPPR & Job Safety Analysis (JSA)',
                    'Modul 4: Pengawasan Norma Keselamatan Kerja Mekanik, Pesawat Tenaga & Produksi',
                    'Modul 5: Pengawasan Norma K3 Bejana Tekan, Tangki Timbun & Pesawat Uap',
                    'Modul 6: Pengawasan Norma K3 Instalasi Listrik Industri & Sistem Proteksi Petir',
                    'Modul 7: Pengawasan Norma K3 Penanggulangan Kebakaran & Sistem Proteksi Gedung',
                    'Modul 8: Pengawasan Norma K3 Konstruksi, Kerja di Ketinggian & Ruang Terbatas',
                    'Modul 9: Pengawasan Norma Higiene Industri, Ergonomi & Pengendalian Bahan Kimia B3',
                    'Modul 10: Kelembagaan P2K3 Bipartit & Mekanisme Pelaporan K3 Perusahaan',
                    'Modul 11: Audit Sistem Manajemen K3 (SMK3 PP 50/2012) & Standar ISO 45001:2018',
                    'Modul 12: Praktik Kerja Lapangan (PKL), Penyusunan Kertas Kerja & Seminar Evaluasi'
                ],
                'requirements' => [
                    'Pendidikan minimal D3 atau S1 segala jurusan',
                    'Surat penunjukan atau rekomendasi dari manajemen perusahaan / permohonan mandiri',
                    'Scan ijazah terakhir, transkrip nilai, KTP, dan pasfoto resmi berlatar belakang merah',
                    'Komitmen penuh mengikuti seluruh rangkaian pembinaan teori dan praktik'
                ],
                'facilities' => [
                    'Sertifikat Kompetensi Ahli K3 Umum Resmi & Surat Keputusan Penunjukan (SKP)',
                    'Kartu Lisensi Personel K3 Resmi dengan Barcode Validasi Online',
                    'Pin Logam Ahli K3 & Safety Helmet Standardisasi Personel K3',
                    'Paket Modul Lengkap, Himpunan Regulasi K3, & Template Dokumen HSE Perusahaan',
                    'Keanggotaan Ikatan Alumni Ahli K3 Nasional & Konsultasi Teknis Gratis Seumur Hidup'
                ],
                'meta_title' => 'Training Ahli K3 Umum Resmi | Pembinaan & Lisensi K3 Perusahaan',
                'meta_description' => 'Ikuti Training Ahli K3 Umum Resmi bersertifikat sah. Program pembinaan intensif 12 hari untuk mencetak Ahli K3 Umum kredibel dan siap kerja di berbagai industri.'
            ],
            [
                'id' => 8,
                'title' => 'Training Ahli K3 Umum Sertifikasi (Pembinaan Terakreditasi & In-House Perusahaan)',
                'slug' => 'training-ahli-k3-umum-sertifikasi',
                'level_code' => 'Ahli K3 Sertifikasi',
                'level_name' => 'Tingkat Korporat / Accredited Safety Specialist',
                'badge' => 'Sertifikasi Nasional',
                'duration' => '12 Hari (120 Jam Pelajaran)',
                'method' => 'In-House Training Kustom Perusahaan & Kelas Sertifikasi Terpadu',
                'certification' => 'Sertifikat Kompetensi Ahli K3 Umum Terakreditasi Nasional',
                'price_note' => 'Hubungi Tim Konsultan Corporate',
                'icon' => 'bi-award-fill',
                'short_description' => 'Program pelatihan sertifikasi Ahli K3 Umum dengan fokus penerapan praktis di unit industri untuk memastikan kepatuhan audit SMK3 dan implementasi Zero Harm.',
                'overview' => 'Training Ahli K3 Umum Sertifikasi membekali praktisi industri dengan kompetensi operasional dan analitis dalam mengidentifikasi potensi bahaya, melakukan investigasi kecelakaan, merancang sistem tanggap darurat, dan mengaudit kepatuhan SMK3 PP 50/2012. Dirancang dengan pendekatan studi kasus nyata, simulasi audit, dan pemecahan masalah keselamatan kerja di lapangan.',
                'target_audience' => 'Safety Officer, HSE Coordinator, Plant Manager, Kepala Bengkel/Workshop, Engineering Staff, dan Pengawas Lapangan',
                'curriculum' => [
                    'Modul 1: Kerangka Hukum & Standar Regulasi Keselamatan Kerja Nasional',
                    'Modul 2: Prinsip Dasar Identifikasi Bahaya & Analisis Bahaya Proses Industri',
                    'Modul 3: Formulasi Matriks Risiko HIRADC & Prosedur Izin Kerja Aman (PTW)',
                    'Modul 4: Standar Keselamatan Operasi Mesin, Pesawat Angkat-Angkut & Peralatan Berat',
                    'Modul 5: Keselamatan Sistem Bertekanan: Boiler, Kompresor & Tangki Timbun Bahan Kimia',
                    'Modul 6: Standar Kelistrikan Kerja Aman, Sistem Pembumian & Prosedur LOTO',
                    'Modul 7: Manajemen Pencegahan Kebakaran Industri & Sistem Deteksi Dini Api',
                    'Modul 8: Keselamatan Konstruksi, Galian, Perancah & Sistem Pencegah Jatuh',
                    'Modul 9: Higiene Industri: Pengendalian Bising, Getaran, Debu & Paparan Bahan Berbahaya',
                    'Modul 10: Pengelolaan Komite P2K3 Bipartit & Penyusunan Laporan Triwulan K3',
                    'Modul 11: Implementasi dan Audit SMK3 PP 50/2012 Menuju Standar Golden Flag',
                    'Modul 12: Praktik Audit Lapangan Mandiri, Presentasi Laporan & Evaluasi Akhir'
                ],
                'requirements' => [
                    'Pendidikan minimal Diploma (D3) atau Sarjana (S1) semua jurusan',
                    'Surat tugas dari instansi/perusahaan tempat bekerja atau pendaftaran perorangan',
                    'Salinan KTP, ijazah terakhir, dan pasfoto digital kualitas tinggi',
                    'Mengikuti seluruh sesi evaluasi dan ujian kompetensi tertulis serta wawancara'
                ],
                'facilities' => [
                    'Sertifikat Kelulusan Pelatihan Ahli K3 Umum Sertifikasi Resmi',
                    'Surat Keterangan Pembinaan & Transkrip Nilai Jam Pembelajaran',
                    'E-Book Regulasi K3 Lengkap, SOP Keselamatan Kerja, & Format Matriks HIRADC',
                    'Kit Pelatihan Eksklusif: Tas, Rompi Safety, Helm K3, & Flashdisk Materi',
                    'Bimbingan Pasca Pelatihan untuk Implementasi K3 di Tempat Kerja'
                ],
                'meta_title' => 'Training Ahli K3 Umum Sertifikasi | Pelatihan K3 Perusahaan Terakreditasi',
                'meta_description' => 'Daftar Training Ahli K3 Umum Sertifikasi resmi nasional. Kurikulum komprehensif 12 hari untuk profesional keselamatan dan kesehatan kerja korporasi.'
            ],
            [
                'id' => 9,
                'title' => 'Training Petugas Penanggulangan Kebakaran Industri (Kelas D, C, B, A Korporat)',
                'slug' => 'training-petugas-penanggulangan-kebakaran-industri',
                'level_code' => 'Fire Safety Specialist',
                'level_name' => 'Tingkat Spesialis / Industrial Fire Officer',
                'badge' => 'Proteksi Kebakaran',
                'duration' => '3 - 6 Hari (Sesuai Jenjang Kelas)',
                'method' => 'Teori Sistem Proteksi, Praktik Pemadaman Api Nyata & Simulasi Evakuasi',
                'certification' => 'Sertifikat Petugas Peran Kebakaran Industri Korporasi Resmi',
                'price_note' => 'Hubungi Tim Konsultan Corporate',
                'icon' => 'bi-fire',
                'short_description' => 'Pembinaan tim pemadam kebakaran industri korporat untuk menguasai pengoperasian sarana proteksi kebakaran aktif, pasif, dan pemadaman api darurat.',
                'overview' => 'Kebakaran merupakan ancaman katastropik terbesar bagi aset dan kelangsungan operasional industri. Program ini melatih regu pemadam kebakaran internal perusahaan (Fire Brigade) mulai dari Kelas D (Petugas Peran Kebakaran), Kelas C (Regu Penanggulangan Kebakaran), Kelas B (Koordinator), hingga Kelas A (Ahli K3 Spesialis Kebakaran). Peserta dilatih menguasai teknik pemadaman APAR, hydrant, foam system, serta pembagian kompartemen kebakaran.',
                'target_audience' => 'Anggota Regu Kebakaran Perusahaan, Security Guard, HSE Officer, Maintenance Staff, dan Pengelola Fasilitas Gedung',
                'curriculum' => [
                    'Modul 1: Kimia dan Fisika Api, Fenomena Flashover & Backdraft di Industri',
                    'Modul 2: Karakteristik dan Klasifikasi Kebakaran: Kelas A, B, C, D, dan K',
                    'Modul 3: Inspeksi dan Pengoperasian APAR (Alat Pemadam Api Ringan) Berbagai Media',
                    'Modul 4: Sistem Hydrant Industri: Nozzle Handling, Tekanan Pompa & Hose Management',
                    'Modul 5: Sistem Proteksi Otomatis: Sprinkler, Deluge, Gas Total Flooding & Detektor Api/Asap',
                    'Modul 6: Praktik Pemadaman Api Gas, Cairan Mudah Terbakar & Simulasi Smoke Chamber'
                ],
                'requirements' => [
                    'Sehat jasmani dan tidak memiliki riwayat penyakit asma kronis atau gangguan jantung',
                    'Ditunjuk oleh manajemen perusahaan sebagai tim penanggulangan kebakaran',
                    'Membawa pakaian kerja dan perlengkapan perlindungan pribadi saat sesi praktik'
                ],
                'facilities' => [
                    'Sertifikat Petugas Penanggulangan Kebakaran Industri Terakreditasi Resmi',
                    'Buku Panduan Standar Proteksi Kebakaran Gedung & Industri',
                    'Praktik Langsung Pemadaman Api Nyata (Live Fire Fighting Simulation)',
                    'Konsultasi Perancangan Rencana Penanggulangan Kebakaran Gedung'
                ],
                'meta_title' => 'Training Petugas Penanggulangan Kebakaran Industri Korporasi',
                'meta_description' => 'Pelatihan tim pemadam kebakaran perusahaan Kelas D, C, B, A. Praktik pemadaman api nyata, pengoperasian APAR dan hydrant industri.'
            ],
            [
                'id' => 10,
                'title' => 'Training K3 Ruang Terbatas (Confined Space) & Bekerja pada Ketinggian Korporat',
                'slug' => 'training-k3-ruang-terbatas-confined-space-ketinggian',
                'level_code' => 'High-Risk Safety Officer',
                'level_name' => 'Tingkat Operasi Berisiko Tinggi / High-Risk Specialist',
                'badge' => 'Risiko Tinggi',
                'duration' => '3 Hari (24 Jam Pelajaran)',
                'method' => 'Teori Prosedur Izin Kerja Khusus, Deteksi Gas, Praktik Rigging & Vertical Rescue',
                'certification' => 'Sertifikat Kompetensi K3 Ruang Terbatas & Bekerja di Ketinggian Resmi',
                'price_note' => 'Hubungi Tim Konsultan Corporate',
                'icon' => 'bi-cone-striped',
                'short_description' => 'Pembinaan teknis keselamatan kerja di ruang terbatas (tangki, silo, manhole) dan proteksi jatuh saat bekerja pada struktur berketinggian.',
                'overview' => 'Pekerjaan di ruang terbatas dan bekerja di ketinggian menyumbang persentase fatalitas tertinggi dalam industri. Pelatihan ini memadukan prosedur isolasi energi LOTO, pengetesan atmosfer gas berbahaya (O2, H2S, CO, LEL), ventilasi mekanik, sistem izin masuk (*Entry Permit*), serta standar pemakaian Full Body Harness, lanyard shock absorber, anchor point, dan teknik penyelamatan darurat (*Confined Space & Height Rescue*).',
                'target_audience' => 'Petugas Masuk Ruang Terbatas (Entrant), Petugas Jaga (Attendant), Supervisor Tangki/Silo, Teknisi Menara, Scaffolder, dan Tim HSE',
                'curriculum' => [
                    'Modul 1: Identifikasi Bahaya Ruang Terbatas: Asfiksia, Keracunan Gas & Bahaya Terperangkap',
                    'Modul 2: Prosedur Pengujian Gas Atmosfer Menggunakan Multi-Gas Detector Portabel',
                    'Modul 3: Sistem Ventilasi Positif/Negatif, Purging Gas & Prosedur Isolasi Energi (LOTO)',
                    'Modul 4: Standar Bekerja pada Ketinggian: Fall Prevention, Fall Arrest & Suspended Work',
                    'Modul 5: Inspeksi Full Body Harness, Lifeline, Karabiner, & Kalkulasi Fall Clearance Distance',
                    'Modul 6: Simulasi Penyelamatan Darurat: Tripod Hoist, Escape Breathing Apparatus & Vertical Rescue'
                ],
                'requirements' => [
                    'Pendidikan minimal SLTA/SMK atau sederajat dengan fisik prima',
                    'Bebas dari fobia ketinggian (acrophobia) dan ruang tertutup/sempit (claustrophobia)',
                    'Surat keterangan sehat dari dokter'
                ],
                'facilities' => [
                    'Sertifikat Kompetensi K3 Ruang Terbatas & Ketinggian Resmi Terakreditasi',
                    'Buku Pedoman Keselamatan Bekerja di Ruang Terbatas & Struktur Tinggi',
                    'Praktik Deteksi Gas, Entri Tangki, Simulasi Tripod Evakuasi & Penyelamatan Korban',
                    'Template Form Izin Kerja Masuk Ruang Terbatas & Izin Kerja Ketinggian'
                ],
                'meta_title' => 'Training K3 Ruang Terbatas & Bekerja pada Ketinggian Korporat',
                'meta_description' => 'Pelatihan keselamatan kerja ruang terbatas (confined space) dan ketinggian. Kuasai deteksi gas, izin kerja aman, dan simulasi penyelamatan darurat.'
            ]"""

# Add to getMasterPrograms if not already added
if "'slug' => 'training-ahli-k3-umum-resmi'" not in code:
    prog6_marker = "'slug' => 'training-tanggap-darurat-emergency-response-plan-erp-korporat',"
    idx = code.find(prog6_marker)
    if idx != -1:
        close_b = code.find("            ]", idx)
        if close_b != -1:
            ins = close_b + len("            ]")
            code = code[:ins] + ",\n" + programs_to_add + code[ins:]
            print("Added programs 7, 8, 9, 10 to getMasterPrograms successfully.")

# 2. GENERATE EXACTLY 200 ARTICLE TITLES
# Title 1: Training Ahli K3 Umum Resmi di {region}
# Title 2: Training Ahli K3 Umum Sertifikasi di {region}
# Titles 3-200: Rotating across Training Ahli K3 Umum Resmi, Training Ahli K3 Umum Sertifikasi, Training Ahli K3 Umum Corporate

topics_list = [
    # Topic stems with diverse industries and critical K3 disciplines
    "Implementasi Standar Keselamatan Kerja Terpadu Sektor Manufaktur & Perakitan",
    "Penyusunan Kebijakan K3 & Komitmen Manajemen Tingkat Korporasi",
    "Penerapan 166 Kriteria Audit SMK3 PP 50/2012 Menuju Sertifikasi Golden Flag",
    "Metodologi Identifikasi Bahaya HIRADC & IBPPR Berbasis Pendekatan Ilmiah",
    "Investigasi Kecelakaan Kerja, Bukti 4P & Analisis Akar Masalah SCAT / RCA",
    "Tata Kelola Komite Bipartit Keselamatan Kerja P2K3 & Pelaporan Triwulan",
    "Penyusunan Emergency Response Plan (ERP) & Simulasi Komando Darurat Industri",
    "Pengawasan Norma K3 Pesawat Angkat dan Angkut (Crane, Forklift & Rigging)",
    "Pengawasan Norma K3 Pesawat Tenaga dan Produksi (PTP) & Penggerak Mula",
    "Standar Keselamatan Instalasi Listrik Industri, PUIL & Sistem Proteksi Petir",
    "Manajemen Pencegahan & Penanggulangan Kebakaran Industri Berbagai Kelas APAR & Hydrant",
    "Higiene Industri, Pengukuran Faktor Fisika, Kimia & Biologi Tempat Kerja",
    "Ergonomi Industri, Analisis Postur RULA / REBA & Pencegahan Penyakit Akibat Kerja",
    "Pengelolaan Bahan Berbahaya dan Beracun (B3), Simbol, Label & Lembar Data Keselamatan (MSDS)",
    "Program Pemeriksaan Kesehatan Tenaga Kerja Awal, Berkala & Khusus Fit to Work",
    "Penyusunan Job Safety Analysis (JSA) & Sistem Izin Kerja Aman (Permit to Work)",
    "Analisis Statistik Kecelakaan: Frequency Rate, Severity Rate & Safe Man-Hours",
    "Manajemen K3 Fasilitas Gedung Komersial Bertingkat & Sarana Evakuasi Darurat",
    "Pengawasan Keselamatan Konstruksi, Galian Tanah & Perancah (Scaffolding)",
    "Standar Keselamatan Bejana Tekan, Tangki Timbun Industri & Pesawat Uap Boiler",
    "Keselamatan Bekerja di Ruang Terbatas (Confined Space) & Uji Gas Atmosfer Berbahaya",
    "Keselamatan Bekerja pada Ketinggian, Full Body Harness & Fall Arrest System",
    "Integrasi Sistem Manajemen K3 PP 50/2012 dengan Standar Global ISO 45001:2018",
    "Strategi Membangun Budaya K3 Proaktif Berkelanjutan Menuju Target Zero Harm",
    "Audit Kepatuhan Regulasi K3 Nasional & Manajemen Mitigasi Risiko Legal Korporat",
    "Pengendalian Bahaya Kebisingan, Getaran & Program Konservasi Pendengaran Tenaga Kerja",
    "Tata Kelola Standarisasi Alat Pelindung Diri (APD) & Uji Kelayakan Matriks Proteksi",
    "Manajemen K3 Pergudangan Modern, Racking System & Jalur Lalu Lintas Kendaraan Berat",
    "Safety Leadership, Coaching K3 & Komunikasi Efektif Pengawas Lapangan",
    "Prosedur Karantina Energi, Lockout Tagout (LOTO) & Commissioning Peralatan Industri",
    "Manajemen K3 Kontraktor (Contractor Safety Management System - CSMS) Terpadu",
    "Manajemen Tanggap Darurat Tumpahan Bahan Kimia B3 & Prosedur Dekontaminasi",
    "Penyusunan Standard Operating Procedure (SOP) K3 Berbasis Analisis Risiko Operasional",
    "Standar Penyelenggaraan Fasilitas P3K di Tempat Kerja & Pelatihan First Aider",
    "Audit Internal SMK3: Teknik Wawancara, Verifikasi Sampel Dokumen & Uji Lapangan",
    "Penerapan Konsep Safety Maturity Model & DuPont Bradley Curve di Lini Bisnis",
    "K3 Bidang Logistik, Distribusi Armada Truk & Pelatihan Defensive Driving",
    "Manajemen Risiko Proses Industri Kimia, Petrokimia & Analisis HAZOP Komprehensif",
    "Keselamatan Operasi Pabrik Pengolahan Makanan, Minuman & Standar Sanitasi Industri",
    "Penerapan Norma Keselamatan Kerja Tambang Mineral, Batubara & Fasilitas Smelter",
    "Manajemen K3 Pembangkit Listrik (PLTU, PLTG, PLTA, PLTS) & Gardu Induk Tegangan Tinggi",
    "Standar K3 Rumah Sakit, Fasilitas Kesehatan & Pengendalian Limbah Medis Berbahaya",
    "Manajemen Keselamatan Pengelasan (Hot Work), Pemotongan & Gas Bertekanan Tabung",
    "Pemeriksaan Kelayakan Sling Baja, Shackle, Webbing Sling & Sertifikasi Rigging Gear",
    "Prosedur Penanganan Debu Mudah Meledak (Combustible Dust) di Pabrik & Silo Penyimpanan",
    "Pencegahan Paparan Gas Beracun H2S, CO, SO2 & Standardisasi Detektor Gas Portabel",
    "Penyusunan Matriks Kompetensi K3 & Rencana Pelatihan Berkelanjutan Karyawan",
    "Penyelenggaraan Safety Induction Terstruktur bagi Tamu, Vendor & Pekerja Baru",
    "Sistem Pelaporan Bahaya Hazard Observation & Pengelolaan Tindakan Perbaikan CAPA",
    "Penilaian Risiko Ergonomi Manual Handling, Angkat-Angkut Beban & Tata Letak Kerja",
    "Penerapan Prinsip Inherently Safer Design pada Modifikasi Mesin & Tata Letak Pabrik",
    "Pengendalian Risiko Radiasi Industri, Non-Destructive Testing (NDT) & Sumber Tertutup",
    "Pengawasan Norma K3 Bidang Maritim, Galangan Kapal & Fasilitas Pelabuhan Industri",
    "Manajemen Stres Kerja, Kesehatan Mental Personel & Pencegahan Kelelahan (Fatigue Risk)",
    "Penanganan Insiden Tumpahan Minyak (*Oil Spill Response*) di Darat dan Perairan",
    "Manajemen K3 Fasilitas Data Center, Ruang Server & Proteksi Kebakaran Gas Bersih",
    "Penyusunan Business Continuity Plan (BCP) Berbasis Ketahanan Risiko Operasional K3",
    "Pengawasan Norma K3 Industri Tekstil, Garmen & Pengendalian Debu Serat Kapas",
    "Sertifikasi Personel K3: Jalur Karier, Kualifikasi Kompetensi & Pemeliharaan Lisensi",
    "Tinjauan Manajemen K3 (Management Review) & Evaluasi Kinerja K3 Menuju Golden Flag"
]

# We need exactly 200 titles.
# Title 0: "Training Ahli K3 Umum Resmi di {region}"
# Title 1: "Training Ahli K3 Umum Sertifikasi di {region}"
# Titles 2..199: 198 items.
# We will generate 198 titles using our 60 rich topics with alternating prefixes:
# Prefix A: "Training Ahli K3 Umum Resmi: "
# Prefix B: "Training Ahli K3 Umum Sertifikasi: "
# Prefix C: "Training Ahli K3 Umum Corporate: "

prefixes = [
    "Training Ahli K3 Umum Resmi: ",
    "Training Ahli K3 Umum Sertifikasi: ",
    "Training Ahli K3 Umum Corporate: "
]

new_200_titles = [
    "Training Ahli K3 Umum Resmi di {region}",
    "Training Ahli K3 Umum Sertifikasi di {region}"
]

for i in range(198):
    topic = topics_list[i % len(topics_list)]
    prefix = prefixes[i % len(prefixes)]
    
    # If topic has repeat in further cycles, append subtle sector / phase differentiation
    cycle = i // len(topics_list)
    if cycle == 0:
        variant = f"{prefix}{topic} di {{region}}"
    elif cycle == 1:
        variant = f"{prefix}{topic} (Fokus Sektor Industri Terintegrasi) di {{region}}"
    elif cycle == 2:
        variant = f"{prefix}{topic} (Panduan Kepatuhan Audit & Akreditasi) di {{region}}"
    else:
        variant = f"{prefix}{topic} (Standar Penerapan Operasional Lapangan) di {{region}}"
        
    new_200_titles.append(variant)

print(f"Generated {len(new_200_titles)} titles. Verifying count and sample:")
print(f"Title 1: {new_200_titles[0]}")
print(f"Title 2: {new_200_titles[1]}")
print(f"Title 3: {new_200_titles[2]}")
print(f"Title 4: {new_200_titles[3]}")
print(f"Title 200: {new_200_titles[199]}")

# Build PHP code for get200ArticleTitles
titles_php_lines = []
for t in new_200_titles:
    clean_t = t.replace('"', '\\"')
    titles_php_lines.append(f'            "{clean_t}",')

new_get200_function = "    public static function get200ArticleTitles(): array\n    {\n        return [\n" + "\n".join(titles_php_lines) + "\n        ];\n    }"

# Replace the existing get200ArticleTitles function in code
pattern = r"public static function get200ArticleTitles\(\): array\s*\{.*?\n    \}"
new_code, count = re.subn(pattern, new_get200_function, code, flags=re.DOTALL)

if count == 1:
    print("Replaced get200ArticleTitles successfully!")
    code = new_code
else:
    print(f"Warning: regex matched {count} times")

with open(service_path, "w", encoding="utf-8") as f:
    f.write(code)

print("AhliK3UmumSchemeService.php written successfully!")
