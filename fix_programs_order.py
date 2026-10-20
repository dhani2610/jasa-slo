import re

service_path = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\app\Services\AhliK3UmumSchemeService.php"

with open(service_path, "r", encoding="utf-8") as f:
    code = f.read()

# Full Program 6
prog6 = """            [
                'id' => 6,
                'title' => 'Training Tanggap Darurat & Emergency Response Plan (ERP) Korporat Terintegrasi',
                'slug' => 'training-tanggap-darurat-emergency-response-plan-erp-korporat',
                'level_code' => 'Emergency Response Specialist',
                'level_name' => 'Tingkat Operasional / Emergency Commander',
                'badge' => 'Kesiapsiagaan Tinggi',
                'duration' => '3 Hari (24 Jam Pelajaran)',
                'method' => 'Drill Evakuasi, Tabletop Exercise, Komando Tanggap Darurat & Mitigasi Krisis',
                'certification' => 'Sertifikat Ahli Manajemen Tanggap Darurat & Krisis Korporasi',
                'price_note' => 'Hubungi Tim Konsultan Corporate',
                'icon' => 'bi-fire',
                'short_description' => 'Pengembangan sistem komando tanggap darurat, prosedur evakuasi massal, simulasi kebakaran, tumpahan bahan kimia, dan kesiapsiagaan menghadapi bencana di korporasi.',
                'overview' => 'Kesiapsiagaan tanggap darurat yang terlatih menyelamatkan nyawa, aset, dan reputasi perusahaan saat krisis terjadi. Pelatihan ini melatih pembentukan Incident Command System (ICS), pemetaan zona evakuasi, penyusunan buku pedoman Emergency Response Plan (ERP), pengoperasian sistem alarm dan sarana proteksi kebakaran, teknik pertolongan pertama pada kecelakaan (P3K), serta perancangan skenario drill berkala.',
                'target_audience' => 'Tim Tanggap Darurat, Fire Warden, Petugas Evakuasi Lantai, Regu Pemadam Kebakaran Perusahaan, Security, dan Petugas P3K',
                'curriculum' => [
                    'Modul 1: Prinsip Manajemen Tanggap Darurat Korporasi & Struktur Incident Command System (ICS)',
                    'Modul 2: Identifikasi Skenario Krisis: Kebakaran, Gempa Bumi, Kebocoran Gas, Tumpahan B3 & Ancaman Bom',
                    'Modul 3: Prosedur Komunikasi Darurat, Kode Bahaya (*Emergency Codes*) & Jalur Komando',
                    'Modul 4: Perencanaan Rute Evakuasi, Assembly Point, Penghitungan Jumlah Personel (*Headcount*)',
                    'Modul 5: Praktik Penggunaan APAR, Hydrant, SCBA, & Tindakan Pertolongan Pertama (First Aid CPR)',
                    'Modul 6: Penyelenggaraan Tabletop Exercise, Full Scale Emergency Drill & Evaluasi Pasca-Insiden'
                ],
                'requirements' => [
                    'Sehat jasmani dan rohani, tidak memiliki fobia terhadap alarm bising atau ruangan gelap/asap',
                    'Anggota tim tanggap darurat atau personel keamanan/fasilitas yang ditunjuk perusahaan',
                    'Membawa pakaian kerja lapangan dan sepatu keselamatan untuk sesi simulasi'
                ],
                'facilities' => [
                    'Buku Panduan Standar Emergency Response Plan (ERP) Korporat Siap Adaptasi',
                    'Sertifikat Ahli Kesiapsiagaan Tanggap Darurat Korporasi Terakreditasi',
                    'Simulasi Pemadaman Api Nyata (Live Fire Fighting) & Evakuasi Terpandu',
                    'Template SOP Kedaruratan & Kartu Kendali Tanggap Darurat Saku (*Emergency Pocket Card*)'
                ],
                'meta_title' => 'Training Tanggap Darurat & Emergency Response Plan (ERP) Korporat',
                'meta_description' => 'Pelatihan tim tanggap darurat perusahaan. Bangun kesiapsiagaan Incident Command System, simulasi evakuasi kebakaran dan krisis industri terintegrasi.'
            ]"""

prog7_to_10 = """            [
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

# Locate start of Program 6
prog6_start = code.find("'id' => 6,")
if prog6_start != -1:
    bracket_before_p6 = code.rfind("[", 0, prog6_start)
    # Find the end of getMasterPrograms: '        ];'
    end_of_gmp = code.find("        ];", prog6_start)
    if end_of_gmp != -1:
        replacement = prog6 + ",\n" + prog7_to_10 + "\n"
        code = code[:bracket_before_p6] + replacement + code[end_of_gmp:]
        print("Reconstructed Program 6 and appended Programs 7..10 cleanly!")

with open(service_path, "w", encoding="utf-8") as f:
    f.write(code)

print("Saved AhliK3UmumSchemeService.php")
