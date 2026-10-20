import os

service_dir = r"c:\xampp\htdocs\web-pelatihan\jasa-slo\app\Services"
os.makedirs(service_dir, exist_ok=True)
service_file = os.path.join(service_dir, "JasaSloSchemeService.php")

# 1. 8 Comprehensive Master Programs
programs = [
    {
        "id": 1,
        "title": "Jasa SLO Instalasi Pemanfaatan Tenaga Listrik Tegangan Rendah (IPTL TR Industri & Komersial)",
        "slug": "jasa-slo-iptl-tegangan-rendah",
        "level_code": "IPTL-TR",
        "level_name": "Tegangan Rendah / Low Voltage Installation",
        "badge": "Layanan Utama",
        "duration": "Proses Cepat (3 - 7 Hari Kerja)",
        "method": "Inspeksi Visual, Pengujian Tahanan Isolasi, Pengukuran Grounding & Uji Pembebanan",
        "certification": "Sertifikat Laik Operasi (SLO) Resmi IPTL TR Berbarcode Validasi Sah",
        "price_note": "Hubungi Tim Ahli Inspeksi SLO",
        "icon": "bi-lightning-charge-fill",
        "short_description": "Layanan sertifikasi kelaikan operasi resmi untuk instalasi listrik tegangan rendah pada bangunan pabrik, pergudangan, gedung bertingkat, rumah sakit, dan pusat komersial.",
        "overview": "Setiap instalasi pemanfaatan tenaga listrik tegangan rendah (TR - 220V/380V) wajib mengantongi Sertifikat Laik Operasi (SLO) sebelum dialiri listrik atau diperpanjang masa berlakunya. Layanan Jasa SLO IPTL TR mencakup audit dokumen diagram satu garis (Single Line Diagram), inspeksi panel hubung bagi (PHB), pengujian kontinuitas, resistansi isolasi penghantar, tahanan pembumian (< 5 Ohm), serta uji pembebanan guna menjamin instalasi aman dari bahaya sengatan listrik, kebakaran akibat hubung singkat, dan kegagalan sistem kelistrikan.",
        "target_audience": "Pemilik Pabrik, General Manager Operasional, Building Manager Gedung Komersial, Facility Engineering, Kontraktor Instalatur Listrik, dan Tim HSE Perusahaan",
        "curriculum": [
            "Modul 1: Standar Regulasi Keselamatan Ketenagalistrikan & Persyaratan PUIL Nasional",
            "Modul 2: Verifikasi Single Line Diagram (SLD), Denah Instalasi & Kapasitas Daya Terpasang",
            "Modul 3: Pemeriksaan Fisik Panel Distribusi Utama (LVMDP) & Sub Distribution Panel (SDP)",
            "Modul 4: Pengujian Resistansi Isolasi Kabel Daya (Megger Test) Sesuai Standar Kelaikan",
            "Modul 5: Pengukuran Nilai Tahanan Pembumian (Grounding Resistance) & Ikatan Penyetara Potensial",
            "Modul 6: Uji Kinerja Pemutus Tenaga Otomatis (MCB, MCCB, ELCB / RCD) & Uji Drop Tegangan",
            "Modul 7: Inspeksi Termografi Panel Listrik untuk Deteksi Titik Panas (*Hotspot Overheating*)",
            "Modul 8: Penyusunan Laporan Hasil Pemeriksaan & Pengujian (LHPP) dan Penerbitan Sertifikat SLO"
        ],
        "requirements": [
            "Gambar Single Line Diagram (SLD) yang telah ditandatangani penanggung jawab teknik",
            "Daftar spesifikasi peralatan utama (kapasitas trafo/sumber daya, kabel penghantar, pemutus arus)",
            "Surat permohonan sertifikasi laik operasi dari manajemen perusahaan/pemilik instalasi",
            "Akses masuk tim inspeksi teknik ke ruang panel dan titik instalasi yang diuji"
        ],
        "facilities": [
            "Sertifikat Laik Operasi (SLO) Resmi dengan Nomor Registrasi Nasional & Barcode Validasi Online",
            "Buku Laporan Hasil Pemeriksaan dan Pengujian (LHPP) Lengkap Berisi Data Teknis Hasil Ukur",
            "Peta Temuan Anomali & Rekomendasi Teknis Perbaikan Instalasi dari Tenaga Ahli",
            "Plat / Stiker Kelaikan Operasi Resmi untuk Ditempelkan pada Panel Utama Fasilitas"
        ],
        "meta_title": "Jasa SLO Instalasi Pemanfaatan Tenaga Listrik Tegangan Rendah (IPTL TR)",
        "meta_description": "Layanan Jasa SLO Resmi Instalasi Tenaga Listrik Tegangan Rendah (IPTL TR) untuk pabrik, gedung komersial, dan industri. Inspeksi uji kelaikan operasi berstandar sah."
    },
    {
        "id": 2,
        "title": "Jasa SLO Instalasi Pemanfaatan Tenaga Listrik Tegangan Menengah (IPTL TM Gardu, Trafo & Cubicle 20 kV)",
        "slug": "jasa-slo-iptl-tegangan-menengah",
        "level_code": "IPTL-TM",
        "level_name": "Tegangan Menengah / Medium Voltage 20 kV",
        "badge": "Prioritas Korporat",
        "duration": "Inspeksi Teknis & Pengujian Komprehensif",
        "method": "Uji Hi-Pot, Uji Karakteristik Trafo, Uji Tahanan Kontak & Kalibrasi Relai Proteksi",
        "certification": "Sertifikat Laik Operasi (SLO) Resmi Gardu Distribusi & Trafo 20 kV",
        "price_note": "Hubungi Tim Ahli Inspeksi SLO",
        "icon": "bi-cpu-fill",
        "short_description": "Sertifikasi kelaikan operasi gardu distribusi listrik, transformator daya, kubikel 20 kV, dan peralatan tegangan menengah untuk memastikan keandalan pasokan listrik industri.",
        "overview": "Instalasi pemanfaatan tenaga listrik tegangan menengah (TM 20 kV) menuntut standar keselamatan yang sangat ketat karena potensi risiko kegagalan isolasi yang dapat memicu ledakan arc flash masif. Layanan Jasa SLO IPTL TM menguji secara menyeluruh kubikel incoming/outgoing, pemutus sirkuit vakum/SF6 (VCB/SF6 Breaker), transformator step-down, sistem proteksi relai arus lebih (OCR) dan gangguan tanah (GFR), tahanan isolasi minyak trafo (Breakdown Voltage Test), serta keandalan interlock keselamatan mekanik dan elektrik.",
        "target_audience": "Plant Manager Pabrik Berat, Electrical Engineering Manager, Supervisor Gardu Induk Swasta, Kontraktor EPC Gardu TM, dan Pengelola Kawasan Industri",
        "curriculum": [
            "Modul 1: Standar Teknis & Kriteria Kelaikan Operasi Gardu Distribusi 20 kV",
            "Modul 2: Inspeksi Visual Kompartemen Busbar, Pemisah (Disconnecting Switch) & Pemutus Tenaga (CB)",
            "Modul 3: Uji Ketahanan Tegangan Tinggi (High Potential / Hi-Pot Test) pada Kubikel & Kabel TM",
            "Modul 4: Pengujian Tahanan Kontak (Contact Resistance Test / Micro-Ohm) pada Sambungan Busbar",
            "Modul 5: Uji Transformator Daya: Insulation Resistance, Rasio Lilitan, Polaritas & Tegangan Tembus Minyak",
            "Modul 6: Injeksi Sekunder Relai Proteksi (Overcurrent Relay & Ground Fault Relay Coordination)",
            "Modul 7: Pemeriksaan Sistem Interlock, Sistem Tripping DC Baterai & Indikator Keberadaan Tegangan",
            "Modul 8: Verifikasi Pembumian Netral Sistem & Laporan Rekomendasi Penerbitan SLO 20 kV"
        ],
        "requirements": [
            "Single Line Diagram (SLD) gardu distribusi 20 kV yang disahkan tenaga teknik kompeten",
            "Data spesifikasi nameplate trafo, kubikel, arrester, dan setting relai proteksi",
            "Jadwal padam (*shutdown schedule*) terkoordinasi untuk pelaksanaan sesi uji injeksi dan hi-pot",
            "Alat pelindung diri (APD) khusus tegangan menengah (helm ber-visior arc flash, sarung tangan 20 kV)"
        ],
        "facilities": [
            "Sertifikat Laik Operasi (SLO) Gardu Listrik Tegangan Menengah 20 kV Resmi Terakreditasi",
            "Laporan Uji Laboratorium Dielektrik Minyak Trafo & Kurva Karakteristik Relai Proteksi",
            "Sertifikat Kalibrasi Alat Uji yang Digunakan dalam Pengujian",
            "Konsultasi Pasca Uji untuk Optimalisasi Koordinasi Proteksi Sistem Kelistrikan"
        ],
        "meta_title": "Jasa SLO Instalasi Listrik Tegangan Menengah 20 kV | Gardu & Trafo Industri",
        "meta_description": "Jasa pengurusan dan uji kelaikan operasi Sertifikat Laik Operasi (SLO) IPTL Tegangan Menengah 20 kV, trafo daya, dan kubikel gardu industri terakreditasi resmi."
    },
    {
        "id": 3,
        "title": "Jasa SLO Pembangkit Tenaga Listrik (Genset Diesel, Gas Turbine & PLTS Atap Korporat)",
        "slug": "jasa-slo-pembangkit-listrik-genset-plts",
        "level_code": "SLO-KIT",
        "level_name": "Pembangkit Listrik / Captive Power Generation",
        "badge": "Pembangkit Mandiri",
        "duration": "Uji Pembebanan Berjenjang & Komisioning",
        "method": "Full Load Bank Testing, Uji Proteksi Generator, Emisi Gas Buang & Sinkronisasi Paralel",
        "certification": "Sertifikat Laik Operasi (SLO) Pembangkit Tenaga Listrik Resmi",
        "price_note": "Hubungi Tim Ahli Inspeksi SLO",
        "icon": "bi-gear-wide-connected",
        "short_description": "Uji kelaikan operasi dan sertifikasi resmi pembangkit listrik mandiri (Captive Power) untuk genset diesel darurat, gas turbine, maupun sistem PLTS Fotovoltaik atap industri.",
        "overview": "Pembangkit tenaga listrik mandiri yang dioperasikan untuk kepentingan sendiri wajib memiliki SLO untuk membuktikan bahwa generator beroperasi efisien, memiliki sistem proteksi yang handal, dan tidak membahayakan sistem tenaga listrik sekitar. Layanan ini mencakup uji beban berjenjang (*Load Bank Test* 25%, 50%, 75%, 100%, 110%), uji Governor & AVR, uji proteksi Reverse Power dan Overfrequency, sistem sinkronisasi otomatis (AMF/ATS), serta pengujian inverter pada instalasi Pembangkit Listrik Tenaga Surya (PLTS).",
        "target_audience": "Operator Genset Industri, Manajer Utilitas Pabrik, Pengelola Data Center, Pengembang Proyek PLTS Surya, dan Kepala Bagian Pemeliharaan Fasilitas",
        "curriculum": [
            "Modul 1: Prinsip Kelaikan Operasi Pembangkitan Listrik Mandiri & Regulasi Keselamatan",
            "Modul 2: Inspeksi Visual Mesin Penggerak, Alternator, Tangki Harian Bahan Bakar & Sistem Pelumasan",
            "Modul 3: Pengujian Tahanan Isolasi Stator, Rotor, & Sistem Eksitasi Generator",
            "Modul 4: Uji Pembebanan Berjenjang Menggunakan Dummy Load / Load Bank Otomatis",
            "Modul 5: Uji Kinerja Automatic Voltage Regulator (AVR), Respon Transient & Pengaturan Frekuensi",
            "Modul 6: Uji Proteksi Generator: Reverse Power Relay, Loss of Excitation, Differential Relay",
            "Modul 7: Khusus PLTS Atap: Uji Inverter, Anti-Islanding Protection, Uji Karakteristik String PV & Proteksi DC",
            "Modul 8: Evaluasi Kinerja Efisiensi Energi, Peredam Bising, Emisi, dan Penerbitan Berita Acara SLO"
        ],
        "requirements": [
            "Spesifikasi teknik generator set / solar PV inverter dan panel sinkronisasi",
            "Kesiapan bahan bakar dan unit beban (beban riil pabrik atau mobile load bank)",
            "Log book pemeliharaan berkala generator dan catatan jam operasi (*running hours*)",
            "Surat permohonan inspeksi teknis dari pimpinan fasilitas"
        ],
        "facilities": [
            "Sertifikat Laik Operasi (SLO) Pembangkit Listrik Resmi Berkekuatan Hukum Sah",
            "Grafik Kinerja Pembebanan Generator (Load Transient Curve & Fuel Consumption Analysis)",
            "Laporan Uji Emisi & Tingkat Kebisingan Sesuai Standar Baku Mutu Industri",
            "Rekomendasi Pemeliharaan Preventif untuk Menjaga Kesiapsiagaan Unit Pembangkit Darurat"
        ],
        "meta_title": "Jasa SLO Pembangkit Tenaga Listrik Genset & PLTS Atap Industri",
        "meta_description": "Uji kelaikan operasi dan sertifikasi resmi SLO Pembangkit Tenaga Listrik (Genset Diesel, Turbin Gas, PLTS Atap Surya). Layanan pengujian profesional dan kredibel."
    },
    {
        "id": 4,
        "title": "Jasa SLO Instalasi Distribusi Tenaga Listrik (Jaringan Distribusi SUTM / SKTM & Gardu Hubung)",
        "slug": "jasa-slo-instalasi-distribusi-listrik",
        "level_code": "SLO-DIS",
        "level_name": "Jaringan Distribusi Listrik / Distribution Network",
        "badge": "Jaringan Listrik",
        "duration": "Inspeksi Jaringan & Pengujian Isolasi Jalur",
        "method": "Uji Kontinuitas Jalur, Pengukuran Tahanan Isolasi Kabel Bawah Tanah, Inspeksi Tiang & ROW",
        "certification": "Sertifikat Laik Operasi (SLO) Distribusi Tenaga Listrik Resmi",
        "price_note": "Hubungi Tim Ahli Inspeksi SLO",
        "icon": "bi-diagram-3-fill",
        "short_description": "Sertifikasi kelaikan operasi jaringan transmisi dan distribusi tenaga listrik industri, saluran udara (SUTM), kabel tanah (SKTM), dan gardu hubung penyulang.",
        "overview": "Keandalan jaringan penyaluran tenaga listrik dari sumber utama menuju titik beban sangat krusial dalam mencegah gangguan pasokan yang merugikan proses produksi. Jasa SLO Distribusi Tenaga Listrik melakukan inspeksi ruang bebas jalur (*Right of Way - ROW*), kelaikan isolator gantung/tumpu, sistem penangkal petir kawat tanah (Ground Wire), uji VLF (Very Low Frequency) pada kabel tegangan menengah berisolasi XLPE bawah tanah, serta koordinasi Recloser dan Sectionalizer.",
        "target_audience": "Pengelola Kawasan Industri, Manajer Infrastruktur Kelistrikan Tambang & Migas, Pengembang Kawasan Mandiri, dan Kontraktor Jaringan Distribusi",
        "curriculum": [
            "Modul 1: Standar Konstruksi & Kelaikan Operasi Jaringan Distribusi Tenaga Listrik",
            "Modul 2: Inspeksi Visual Saluran Udara Tegangan Menengah (SUTM): Tiang, Travers, Isolator & Kawat Tarik",
            "Modul 3: Uji Kelaikan Saluran Kabel Tegangan Menengah (SKTM) Bawah Tanah Metode Uji VLF Hi-Pot",
            "Modul 4: Pengukuran Tahanan Pembumian Kaki Tiang & Lightning Arrester Jalur Distribusi",
            "Modul 5: Pengujian Kelaikan Operasi Gardu Hubung, Air Break Switch (ABS) & Load Break Switch (LBS)",
            "Modul 6: Uji Koordinasi Pengaman Saluran: Fused Cut Out (FCO), Auto Recloser & Sekat Zona Gangguan",
            "Modul 7: Pemeriksaan Ruang Bebas (ROW) dari Rantingan Pohon dan Bangunan Penghalang",
            "Modul 8: Penyusunan Laporan Audit Kelayakan Distribusi & Penerbitan Sertifikat SLO Distribusi"
        ],
        "requirements": [
            "Peta jalur rute distribusi (layout map) dan data panjang saluran kabel/konduktor",
            "Data teknis jenis konduktor, luas penampang, jenis isolator, dan titik penangkal petir",
            "Surat izin koordinasi lintasan dan jadwal pelaksanaan inspeksi lapangan",
            "Tim pendamping dari penanggung jawab operasional jaringan lokal"
        ],
        "facilities": [
            "Sertifikat Laik Operasi (SLO) Instalasi Distribusi Tenaga Listrik Resmi Terakreditasi",
            "Buku Laporan Uji Jalur Lengkap dengan Pemetaan Titik Koordinat GPS Tiang & Gardu",
            "Rekomendasi Pemangkasan Vegetasi & Perbaikan Titik Isolator yang Mengalami Degradasi",
            "Jaminan Kepatuhan Penuh terhadap Standar Regulasi Keselamatan Ketenagalistrikan"
        ],
        "meta_title": "Jasa SLO Instalasi Distribusi Tenaga Listrik SUTM & SKTM Industri",
        "meta_description": "Layanan uji kelaikan operasi dan sertifikasi SLO Distribusi Tenaga Listrik (SUTM, SKTM, Gardu Hubung). Keandalan pasokan listrik industri terjamin aman dan sah."
    },
    {
        "id": 5,
        "title": "Training & Sertifikasi Tenaga Teknik Ketenagalistrikan (SKTTK) Ahli Ketenagalistrikan Nasional",
        "slug": "training-sertifikasi-tenaga-teknik-ketenagalistrikan-skttk",
        "level_code": "SKTTK",
        "level_name": "Sertifikasi Kompetensi Personel / Certified Electrical Engineer",
        "badge": "Kompetensi SDM",
        "duration": "3 - 5 Hari (Pelatihan & Uji Kompetensi)",
        "method": "Pembekalan Teori Teknis, Uji Tertulis, Uji Lisan / Wawancara & Uji Praktik Portofolio",
        "certification": "Sertifikat Kompetensi Tenaga Teknik Ketenagalistrikan (SKTTK) Resmi Berlisensi",
        "price_note": "Hubungi Tim Konsultan Sertifikasi",
        "icon": "bi-award-fill",
        "short_description": "Program pembinaan dan sertifikasi kompetensi tenaga teknik ketenagalistrikan (SKTTK) jenjang operator, teknisi madya, hingga ahli utama di bidang pembangkitan, distribusi, dan instalasi.",
        "overview": "Setiap badan usaha yang memiliki atau mengoperasikan instalasi tenaga listrik diwajibkan memiliki penanggung jawab teknik yang bersertifikat kompetensi (SKTTK). Program ini membekali peserta dengan penguasaan standar kompetensi kerja nasional bidang ketenagalistrikan, regulasi keselamatan kerja kelistrikan, prosedur komisioning, pengujian proteksi, serta tata cara penandatanganan dokumen teknis SLO.",
        "target_audience": "Electrical Engineer, Supervisor Listrik Pabrik, Teknisi Instrumentasi & Daya, Penanggung Jawab Teknik Badan Usaha (PJT), dan Inspektur Ketenagalistrikan",
        "curriculum": [
            "Modul 1: Kerangka Standar Kompetensi Kerja Nasional Bidang Ketenagalistrikan",
            "Modul 2: Regulasi Keselamatan Ketenagalistrikan, SOP Pemeliharaan & Prosedur Tanggap Darurat",
            "Modul 3: Pemahaman Desain Rancang Bangun Instalasi Listrik & Verifikasi Single Line Diagram",
            "Modul 4: Penguasaan Metodologi Inspeksi & Pengujian Kelaikan Operasi (Commissioning Test)",
            "Modul 5: Analisis Hasil Ukur: Resistansi Isolasi, Tahanan Pembumian, Tahanan Kontak & Dielektrik",
            "Modul 6: Keselamatan Bekerja pada Instalasi Bertegangan & Penilaian Risiko Arc Flash",
            "Modul 7: Simulasi Uji Praktik, Penyusunan Dokumen Portofolio & Berita Acara Uji Teknis",
            "Modul 8: Sidang Evaluasi Asesmen Uji Kompetensi Tertulis, Wawancara, dan Verifikasi Bukti Kerja"
        ],
        "requirements": [
            "Pendidikan minimal SMK Teknik Ketenagalistrikan, D3/S1 Teknik Elektro / Mesin / Fisika Teknik",
            "Pengalaman kerja di bidang instalasi, operasi, atau pemeliharaan listrik sesuai jenjang kualifikasi",
            "Surat tugas / rekomendasi dari perusahaan atau permohonan pendaftaran mandiri",
            "CV lengkap, salinan ijazah, KTP, dan pasfoto resmi berlatar belakang merah"
        ],
        "facilities": [
            "Sertifikat Kompetensi Tenaga Teknik Ketenagalistrikan (SKTTK) Resmi dengan Validasi Barcode",
            "Kartu Tanda Kompetensi Personel Ketenagalistrikan",
            "Himpunan Standar PUIL & Kumpulan Modul Teknis Pengujian Instalasi Listrik",
            "Konsultasi Perpanjangan Lisensi & Keanggotaan Forum Insinyur Elektro Korporasi"
        ],
        "meta_title": "Training & Sertifikasi Tenaga Teknik Ketenagalistrikan (SKTTK) Resmi",
        "meta_description": "Program pelatihan dan sertifikasi kompetensi SKTTK resmi untuk teknisi dan insinyur ketenagalistrikan industri. Syarat sah penanggung jawab teknik instalasi listrik."
    },
    {
        "id": 6,
        "title": "Training Uji Kelaikan Operasi, Komisioning & Pengukuran Tahanan Isolasi / Pembumian Listrik",
        "slug": "training-uji-kelaikan-operasi-komisioning-listrik",
        "level_code": "COMM-TEST",
        "level_name": "Teknik Pengujian / Commissioning Specialist",
        "badge": "Praktik Lapangan",
        "duration": "3 Hari (24 Jam Pelajaran)",
        "method": "Teori Standar Uji, Praktik Alat Ukur Megger, Earth Tester, & Simulasi Komisioning",
        "certification": "Sertifikat Pelatihan Uji Kelaikan & Komisioning Instalasi Listrik Terakreditasi",
        "price_note": "Hubungi Tim Konsultan Pelatihan",
        "icon": "bi-speedometer2",
        "short_description": "Pelatihan komprehensif teknik pengukuran tahanan isolasi kabel, resistansi pembumian (grounding), urutan fasa, dan prosedur komisioning instalasi listrik industri.",
        "overview": "Uji komisioning merupakan gerbang utama sebelum instalasi listrik dinyatakan laik operasi. Program pelatihan ini melatih para teknisi dan insinyur kelistrikan mengoperasikan berbagai instrumen uji modern (Insulation Tester, Earth Ground Clamp Meter, Phase Rotation Indicator, Power Quality Analyzer), menganalisis kelayakan nilai ukur terhadap standar PUIL, mendeteksi cacat isolasi tersembunyi, dan menyusun laporan kelaikan komisioning secara profesional.",
        "target_audience": "Teknisi Pemeliharaan Listrik, Staff Commissioning Kontraktor, Quality Control Instalasi Listrik, dan Safety Officer Bidang Elektrikal",
        "curriculum": [
            "Modul 1: Filosofi dan Metodologi Komisioning Instalasi Listrik Industri",
            "Modul 2: Prinsip Pengukuran Tahanan Isolasi Penghantar Menggunakan Megger (500V, 1000V, 2500V, 5000V)",
            "Modul 3: Metode Pengukuran Sistem Pembumian: Fall of Potential 3 Titik, 4 Titik & Clamp-On Method",
            "Modul 4: Pengujian Kontinuitas Konduktor Proteksi & Ikatan Penyetara Potensial (Equipotential Bonding)",
            "Modul 5: Uji Polaritas Arus & Tegangan, Pemeriksaan Urutan Fasa (Phase Sequence CW/CCW)",
            "Modul 6: Pengujian Beban Nol (*No-Load Test*) & Pengujian Berbeban Penuh (*Full Load Test*)",
            "Modul 7: Praktik Langsung Pengoperasian Instrumen Uji Terkalibrasi pada Panel Simulasi",
            "Modul 8: Standardisasi Format Penyusunan Checklist Komisioning & Berita Acara Uji Kelaikan"
        ],
        "requirements": [
            "Pendidikan minimal SMK Listrik / Elektro atau memiliki pengalaman kerja di bidang kelistrikan",
            "Memahami dasar-dasar rangkaian listrik arus bolak-balik (AC) 3-Fasa dan 1-Fasa",
            "Membawa safety shoes dan pakaian kerja untuk sesi praktik laboratorium / lapangan"
        ],
        "facilities": [
            "Sertifikat Pelatihan Uji Kelaikan Operasi & Komisioning Instalasi Listrik",
            "Buku Panduan Standar Operasional Prosedur Pengukuran Kelistrikan Industri",
            "Template Lembar Kerja Komisioning (Commissioning Checklist Form Excel Siap Pakai)",
            "Praktik Menggunakan Instrumen Uji Digital Terkalibrasi Mutakhir"
        ],
        "meta_title": "Training Uji Kelaikan Operasi & Komisioning Instalasi Listrik Industri",
        "meta_description": "Pelatihan teknik komisioning listrik, pengukuran tahanan isolasi megger, dan uji resistansi grounding pembumian sesuai standar keselamatan ketenagalistrikan."
    },
    {
        "id": 7,
        "title": "Training Audit Keselamatan Ketenagalistrikan, Analisis Kualitas Daya & Uji Proteksi Relai",
        "slug": "training-audit-keselamatan-ketenagalistrikan-kualitas-daya",
        "level_code": "AUDIT-PQ",
        "level_name": "Tingkat Lanjut / Electrical Safety & Power Quality Auditor",
        "badge": "Audit & Efisiensi",
        "duration": "4 Hari (32 Jam Pelajaran)",
        "method": "Studi Kasus Gangguan Listrik, Pengoperasian Power Quality Analyzer & Analisis Kurva Trip",
        "certification": "Sertifikat Auditor Keselamatan & Kualitas Daya Ketenagalistrikan",
        "price_note": "Hubungi Tim Konsultan Pelatihan",
        "icon": "bi-graph-up-arrow",
        "short_description": "Pembinaan audit keselamatan listrik tingkat lanjut, pengukuran harmonisa daya, deteksi ketidakseimbangan beban, dan kalibrasi sistem proteksi relai industri.",
        "overview": "Kualitas daya yang buruk (harmonisa tinggi, fluktuasi tegangan, power factor rendah) tidak hanya memboroskan energi tetapi juga berisiko tinggi merusak komponen isolasi dan memicu kebakaran listrik. Pelatihan ini membekali peserta dengan keterampilan melakukan audit keselamatan instalasi listrik menyeluruh, menganalisis profil kualitas daya menggunakan instrumen kelas-A, serta mengkoordinasikan setelan relai proteksi agar mampu mengisolasi gangguan tanpa menyebabkan pemadaman total pabrik.",
        "target_audience": "Energy Manager, Electrical Design Engineer, Maintenance Superintendent, Auditor Energi Industri, dan Konsultan Kelistrikan",
        "curriculum": [
            "Modul 1: Kerangka Kerja Audit Keselamatan Ketenagalistrikan Berbasis Manajemen Risiko",
            "Modul 2: Parameter Kualitas Daya: Voltage Sag, Swell, Transients, Flicker & Total Harmonic Distortion (THD)",
            "Modul 3: Dampak Harmonisa terhadap Transformator, Motor Listrik, Kapasitor Bank & Kabel Netral",
            "Modul 4: Penggunaan Power Quality Analyzer untuk Logging Data 24 Jam & Analisis Bentuk Gelombang",
            "Modul 5: Perancangan Filter Harmonisa Pasif/Aktif & Optimalisasi Automatic Power Factor Controller (APFC)",
            "Modul 6: Koordinasi Proteksi Sistem Kelistrikan: Kurva Waktu-Arus (Time-Current Characteristic / TCC)",
            "Modul 7: Analisis Bahaya Arc Flash: Penentuan Batas Jarak Aman & Pemilihan APD Sesuai Kalori Arc",
            "Modul 8: Penyusunan Laporan Rekomendasi Audit Keselamatan Listrik & Efisiensi Konsumsi Daya"
        ],
        "requirements": [
            "Memiliki latar belakang teknik elektro atau pengalaman minimal 1 tahun di pemeliharaan listrik",
            "Memahami prinsip operasi transformator, motor induksi, dan sistem panel distribusi industri",
            "Membawa laptop untuk sesi simulasi kurva koordinasi proteksi dan analisis log kualitas daya"
        ],
        "facilities": [
            "Sertifikat Auditor Keselamatan Ketenagalistrikan & Power Quality Specialist",
            "Software Toolkit Analisis Kualitas Daya & Template Laporan Audit Kelistrikan",
            "Buku Pedoman Mitigasi Harmonisa & Perhitungan Nilai Arc Flash Boundary",
            "Akses Konsultasi Kasus Gangguan Kelistrikan Bersama Senior Electrical Engineer"
        ],
        "meta_title": "Training Audit Keselamatan Listrik & Analisis Kualitas Daya Industri",
        "meta_description": "Pelatihan audit keselamatan ketenagalistrikan, pengukuran harmonisa kualitas daya (THD), dan koordinasi relai proteksi untuk menjaga stabilitas operasional industri."
    },
    {
        "id": 8,
        "title": "Jasa SLO & Sertifikasi Sistem Penyalur Petir Terintegrasi & Proteksi Surja Industri",
        "slug": "jasa-slo-penyalur-petir-proteksi-surja",
        "level_code": "LIGHTNING-PROT",
        "level_name": "Sistem Proteksi Petir / Lightning Protection & Surge Arrest",
        "badge": "Proteksi Bangunan",
        "duration": "Inspeksi Terminasi Udara, Down Conductor & Uji Grounding",
        "method": "Inspeksi Fisik Head Terminal, Pengukuran Tahanan Pembumian Petir (< 1 Ohm), Uji Klem Sambungan",
        "certification": "Sertifikat Kelaikan Operasi Sistem Penyalur Petir Resmi Terakreditasi",
        "price_note": "Hubungi Tim Ahli Inspeksi SLO",
        "icon": "bi-shield-shaded",
        "short_description": "Layanan inspeksi dan pengujian kelaikan operasi sistem proteksi petir eksternal (Franklin, Sangkar Faraday, ESE) dan proteksi surja internal untuk gedung serta instalasi industri.",
        "overview": "Indonesia memiliki tingkat hari guruh (*Isokeraunic Level*) tertinggi di dunia, menjadikan sistem penyalur petir sebagai benteng utama pelindung keselamatan personel, bangunan, dan peralatan elektronik sensitif dari sambaran petir langsung maupun tegangan surja impuls. Layanan ini mencakup audit sudut proteksi (*Rolling Sphere Method*), kelaikan hantaran penurunan (*Down Conductor*), ketahanan grounding petir khusus (< 1 Ohm), dan pemasangan Surge Protective Device (SPD) terkoordinasi.",
        "target_audience": "Building Manager Gedung Tinggi, HSE Manager Industri Kimia & Minyak Bumi, Pengelola Menara Telekomunikasi, dan Pengawas Proyek Konstruksi",
        "curriculum": [
            "Modul 1: Karakteristik Sambaran Petir di Wilayah Tropis & Standar Proteksi PUIL / Standar Nasional",
            "Modul 2: Evaluasi Tingkat Kebutuhan Proteksi Petir Berdasarkan Indeks Bahaya Gedung & Populasi",
            "Modul 3: Inspeksi Fisik Penangkal Petir Konvensional (Franklin / Faraday) & Sistem Elektrostatis (ESE)",
            "Modul 4: Pengujian Kontinuitas Hantaran Penurunan (Down Conductor) & Bebas Korosi Klem Sambungan",
            "Modul 5: Pengukuran Tahanan Pembumian Khusus Petir Menggunakan Earth Ground Tester Akurasi Tinggi",
            "Modul 6: Sistem Proteksi Petir Internal: Pemasangan & Uji Kinerja Surge Protective Device (SPD) Tipe 1, 2, 3",
            "Modul 7: Evaluasi Ikatan Penyetara Potensial Pembumian Listrik dan Pembumian Petir (*Common Grounding*)",
            "Modul 8: Penyusunan Gambar As-Built Drawing Proteksi Petir & Penerbitan Sertifikat Kelaikan Operasi"
        ],
        "requirements": [
            "Gambar denah atap gedung yang memuat posisi air terminal penangkal petir dan jalur down conductor",
            "Akses aman menuju atap gedung / struktur menara untuk pelaksanaan inspeksi visual fisik",
            "Data riwayat pengukuran grounding petir periode sebelumnya (jika ada perpanjangan)",
            "Kesiapan pendamping teknik dari pihak pengelola gedung / pabrik"
        ],
        "facilities": [
            "Sertifikat Kelaikan Operasi Sistem Penyalur Petir Resmi dengan Barcode Validasi Sah",
            "Buku Laporan Uji Teknis Kelayakan Proteksi Petir Lengkap dengan Dokumentasi Foto",
            "Rekomendasi Pembenahan Jalur Grounding & Penambahan Proteksi Surja pada Panel Sensitif",
            "Plat Pengesahan Kelaikan Penyalur Petir Resmi untuk Dipasang pada Titik Bak Kontrol Grounding"
        ],
        "meta_title": "Jasa SLO & Sertifikasi Sistem Penyalur Petir Gedung & Pabrik Industri",
        "meta_description": "Uji kelaikan dan pengurusan sertifikat resmi instalasi penyalur petir (grounding < 1 Ohm, down conductor, air terminal) untuk gedung, pabrik, dan fasilitas industri."
    }
]

# 2. Rich 200 Article Titles generator
slo_topics = [
    "Panduan Lengkap Sertifikasi Laik Operasi Ketenagalistrikan & Standar PUIL",
    "Uji Kelaikan Operasi Instalasi Pemanfaatan Tenaga Listrik Tegangan Rendah",
    "Uji Kelaikan Operasi Instalasi Pemanfaatan Tenaga Listrik Tegangan Menengah 20 kV",
    "Tata Cara Pemeriksaan, Pengujian & Penerbitan Sertifikat Laik Operasi Sah",
    "Sertifikasi Laik Operasi Pembangkit Listrik Genset Darurat Industri",
    "Sertifikasi Laik Operasi Pembangkit Listrik Tenaga Surya (PLTS) Atap Korporat",
    "Standardisasi Uji Komisioning & Pengukuran Pembumian Grounding Listrik",
    "Inspeksi Termografi Inframerah pada Panel Distribusi Listrik Industri",
    "Uji Tahanan Isolasi Kabel Daya (Megger Test) Berstandar Kelaikan Operasi",
    "Koordinasi Relai Proteksi Arus Lebih & Gangguan Tanah pada Gardu Listrik",
    "Uji Karakteristik & Tegangan Tembus Minyak Transformator Daya Industri",
    "Sertifikasi Kelaikan Operasi Sistem Penyalur Petir & Pembumian Proteksi Surja",
    "Manajemen Keselamatan Bekerja pada Instalasi Listrik Bertegangan Tinggi",
    "Prosedur Karantina Energi, Lockout Tagout (LOTO) & Commissioning Kelistrikan",
    "Analisis Kualitas Daya (Power Quality), Reduksi Harmonisa THD & Kapasitor Bank",
    "Uji Pembebanan Berjenjang Load Bank Generator Set Standby Pabrik",
    "Verifikasi Single Line Diagram (SLD) & Kapasitas Pemutus Arus Circuit Breaker",
    "Audit Keselamatan Kelistrikan Rumah Sakit, Fasilitas Kesehatan & Ruang Operasi",
    "Kelaikan Operasi Instalasi Listrik Fasilitas Data Center & Sistem UPS Redundan",
    "Sertifikasi Laik Operasi Jaringan Distribusi Saluran Udara SUTM & Kabel Tanah SKTM",
    "Mitigasi Bahaya Sengatan Listrik, Arus Bocor ELCB & Ikatan Penyetara Potensial",
    "Uji Ketahanan Tegangan Tinggi (Hi-Pot Test) pada Peralatan Listrik 20 kV",
    "Manajemen Pemeliharaan Preventif Panel Listrik LVMDP & Motor Control Center (MCC)",
    "Pencegahan Bahaya Ledakan Arc Flash & Penentuan Kategori APD Kelistrikan",
    "Standardisasi Penataan Jalur Kabel Cable Tray, Conduit & Penyambungan Kabel",
    "Kelaikan Operasi Sistem Kelistrikan Pabrik Kimia, Petrokimia & Zona Berbahaya Ex-Proof",
    "Uji Coba Fungsi Automatic Transfer Switch (ATS) & Panel Sinkronisasi Generator",
    "Persyaratan Kelaikan Instalasi Listrik Pergudangan Modern & Jalur Forklift Elektrik",
    "Sertifikasi Kompetensi Tenaga Teknik Ketenagalistrikan (SKTTK) Penanggung Jawab Listrik",
    "Audit Keselamatan Listrik Gedung Bertingkat Tinggi & Sistem Evakuasi Darurat",
    "Uji Kelaikan Operasi Pembangkit Listrik Tenaga Biomassa & Turbin Uap Industri",
    "Kelaikan Kelistrikan Fasilitas Pengolahan Air Limbah & Sistem Pompa Submersible",
    "Evaluasi Rugi-Rugi Daya Listrik, Penurunan Drop Tegangan & Efisiensi Energi",
    "Standar Pengujian Relai Diferensial & Proteksi Suhu Winding Trafo Daya",
    "Pemeriksaan Kelaikan Busbar Trunking System & Tap-Off Unit Gedung Komersial",
    "Uji Keselamatan Instalasi Stasiun Pengisian Kendaraan Listrik (SPKLU) Korporat",
    "Sertifikasi Laik Operasi Peralatan Kelistrikan Tambang Terbuka & Smelter Mineral",
    "Inspeksi Rutin Pembumian Tangki Timbun Bahan Bakar & Proteksi Listrik Statis",
    "Penyusunan Berita Acara Uji Kelaikan Operasi & Laporan Hasil Pemeriksaan (LHPP)",
    "Peta Jalan Kepatuhan Regulasi Ketenagalistrikan Menuju Zero Electrical Accident"
]

prefixes = [
    "Training Jasa SLO: ",
    "Jasa SLO Training: ",
    "Jasa SLO: ",
    "Training Sertifikasi Laik Operasi (SLO): ",
    "Jasa Pengurusan SLO: "
]

titles_200 = []
for i in range(200):
    topic = slo_topics[i % len(slo_topics)]
    pfx = prefixes[i % len(prefixes)]
    cycle = i // len(slo_topics)
    if cycle == 0:
        t = f"{pfx}{topic} di {{region}}"
    elif cycle == 1:
        t = f"{pfx}{topic} (Fokus Fasilitas Industri & Komersial) di {{region}}"
    elif cycle == 2:
        t = f"{pfx}{topic} (Standar Komisioning & Kepatuhan Legal) di {{region}}"
    elif cycle == 3:
        t = f"{pfx}{topic} (Panduan Audit & Pengujian Lapangan) di {{region}}"
    else:
        t = f"{pfx}{topic} (Implementasi Keandalan Sistem Kelistrikan) di {{region}}"
    titles_200.append(t)

# Build deep article generator code
service_code = """<?php

namespace App\Services;

use Illuminate\Support\Str;

class JasaSloSchemeService
{
    public static function getMasterPrograms(): array
    {
        return [
"""

for p in programs:
    curriculum_php = ",\n".join([f"                    '{c}'" for c in p["curriculum"]])
    requirements_php = ",\n".join([f"                    '{r}'" for r in p["requirements"]])
    facilities_php = ",\n".join([f"                    '{f}'" for f in p["facilities"]])
    
    service_code += f"""            [
                'id' => {p["id"]},
                'title' => '{p["title"]}',
                'slug' => '{p["slug"]}',
                'level_code' => '{p["level_code"]}',
                'level_name' => '{p["level_name"]}',
                'badge' => '{p["badge"]}',
                'duration' => '{p["duration"]}',
                'method' => '{p["method"]}',
                'certification' => '{p["certification"]}',
                'price_note' => '{p["price_note"]}',
                'icon' => '{p["icon"]}',
                'short_description' => '{p["short_description"]}',
                'overview' => '{p["overview"]}',
                'target_audience' => '{p["target_audience"]}',
                'curriculum' => [
{curriculum_php}
                ],
                'requirements' => [
{requirements_php}
                ],
                'facilities' => [
{facilities_php}
                ],
                'meta_title' => '{p["meta_title"]}',
                'meta_description' => '{p["meta_description"]}'
            ],
"""

service_code += """        ];
    }

    public static function getAllPrograms(): array
    {
        return self::getMasterPrograms();
    }

    public static function getProgramBySlug(string $slug): ?array
    {
        foreach (self::getMasterPrograms() as $prog) {
            if ($prog['slug'] === $slug) {
                return $prog;
            }
        }
        return null;
    }

    public static function get200ArticleTitles(): array
    {
        return [
"""

for t in titles_200:
    clean_t = t.replace('"', '\\"')
    service_code += f'            "{clean_t}",\n'

service_code += """        ];
    }

    public static function generateDeepArticle(string $rawTitle, string $regionName = 'Indonesia'): array
    {
        $formattedTitle = str_replace('{region}', $regionName, $rawTitle);
        $slug = Str::slug($formattedTitle);

        $chapters = [
            [
                'title' => 'Landasan Regulasi Keselamatan Ketenagalistrikan & Standar Kelaikan Operasi Nasional',
                'desc' => 'Kerangka acuan hukum dan persyaratan teknis kelaikan operasi instalasi listrik, prinsip keandalan, keamanan lingkungan, serta perlindungan keselamatan ketenagalistrikan sesuai standar PUIL nasional.'
            ],
            [
                'title' => 'Verifikasi Dokumen Desain Teknis, Single Line Diagram (SLD) & Spesifikasi Komponen',
                'desc' => 'Pemeriksaan kesesuaian gambar skematik diagram satu garis, kapasitas pemutus daya (CB), ukuran penampang kabel penghantar, dan koordinasi proteksi terhadap beban riil terpasang.'
            ],
            [
                'title' => 'Pemeriksaan Visual (Visual Inspection) Tata Letak Panel & Ruang Kelistrikan',
                'desc' => 'Inspeksi fisik kondisi kompartemen panel, jalur kabel (cable routing), penandaan fasa (R-S-T-N-PE), ventilasi ruang gardu, serta jarak aman kerja (working clearance) sesuai standar keselamatan.'
            ],
            [
                'title' => 'Pengujian Tahanan Isolasi (Insulation Resistance Test) Menggunakan Megohmmeter',
                'desc' => 'Prosedur pengujian resistansi dielektrik isolasi kabel antarfasa dan fasa ke tanah dengan injeksi tegangan uji terkalibrasi guna mendeteksi potensi kebocoran arus dan degradasi isolasi.'
            ],
            [
                'title' => 'Pengukuran Resistansi Sistem Pembumian (Grounding Resistance Test) & Ikatan Penyetara',
                'desc' => 'Pengujian nilai tahanan pembumian titik netral, body panel, dan struktur peralatan menggunakan metode Fall of Potential 3 titik untuk memastikan nilai resistansi berada di bawah 5 Ohm.'
            ],
            [
                'title' => 'Uji Kontinuitas Konduktor Proteksi & Verifikasi Urutan Fasa (Phase Sequence)',
                'desc' => 'Pemeriksaan keterhubungan konduktor tanah pengaman (PE), polaritas tegangan, dan uji rotasi fasa searah jarum jam (clockwise) demi mencegah kerusakan pada motor listrik 3-fasa.'
            ],
            [
                'title' => 'Pengujian Karakteristik Pemutus Tenaga Otomatis (MCB, MCCB, ACB, VCB)',
                'desc' => 'Verifikasi mekanisme tripping termal-magnetik, uji respon kelebihan beban (overload), dan ketahanan hubung singkat pemutus sirkuit utama dan cabang.'
            ],
            [
                'title' => 'Uji Injeksi Sekunder & Koordinasi Relai Proteksi (Overcurrent & Earth Fault Relay)',
                'desc' => 'Pengujian sensitivitas relai pengaman, kalibrasi waktu tunda (time multiplier setting), dan koordinasi kurva arus-waktu agar gangguan terlokalisasi tanpa memicu pemadaman meluas.'
            ],
            [
                'title' => 'Pengujian Kelaikan Operasi Transformator Daya & Uji Tegangan Tembus Minyak Trafo',
                'desc' => 'Pengukuran rasio belitan (TTR), polaritas trafo, tahanan belitan (winding resistance), serta uji kekuatan dielektrik isolasi minyak transformator bertegangan menengah 20 kV.'
            ],
            [
                'title' => 'Uji Pembebanan Berjenjang Load Bank pada Pembangkit Listrik Mandiri (Genset)',
                'desc' => 'Pemeriksaan stabilitas tegangan dan frekuensi saat generator dibebani 25%, 50%, 75%, dan 100% beban puncak, uji respon Governor, serta keandalan sistem pendinginan mesin.'
            ],
            [
                'title' => 'Uji Kelaikan Operasi Pembangkit Listrik Tenaga Surya (PLTS) Atap & Inverter Grid-Tied',
                'desc' => 'Inspeksi karakteristik string fotovoltaik, pengujian proteksi anti-islanding, efisiensi konversi daya inverter, dan sistem pembumian panel surya industri.'
            ],
            [
                'title' => 'Inspeksi Termografi Inframerah (Thermal Imaging Scan) Deteksi Titik Panas Panel Listrik',
                'desc' => 'Pemindaian radiasi termal pada sambungan baut busbar, terminal sepatu kabel, dan kontak pemutus sirkuit untuk mendeteksi bahaya panas berlebih akibat koneksi longgar.'
            ],
            [
                'title' => 'Pengukuran & Analisis Kualitas Daya (Power Quality, Harmonisa THD & Cos Phi)',
                'desc' => 'Logging data 24 jam parameter tegangan kedip (voltage sag), ketidakseimbangan tegangan 3-fasa, Total Harmonic Distortion (THD-V dan THD-I), serta efisiensi faktor daya kapasitor bank.'
            ],
            [
                'title' => 'Uji Kelaikan Sistem Penyalur Petir & Pengamanan Tegangan Surja (Surge Arrester)',
                'desc' => 'Verifikasi radius proteksi head terminal penangkal petir, uji tahanan pembumian khusus petir (< 1 Ohm), dan pemeriksaan kelaikan modul Surge Protective Device (SPD).'
            ],
            [
                'title' => 'Prosedur Keselamatan Kerja Listrik, Isolasi Energi (LOTO) & Mitigasi Bahaya Arc Flash',
                'desc' => 'Penerapan Standard Operating Procedure (SOP) keselamatan listrik, pemakaian APD berkualifikasi arc flash, penandaan batas aman tegangan, dan prosedur penguncian sakelar daya.'
            ],
            [
                'title' => 'Analisis Hasil Uji Komisioning, Penyusunan LHPP & Penanganan Ketidaksesuaian Teknis',
                'desc' => 'Rangkuman seluruh lembar data hasil uji lapangan, verifikasi kepatuhan terhadap ambang batas toleransi standar, serta perumusan tindakan perbaikan (*Corrective Action*).'
            ],
            [
                'title' => 'Proses Penerbitan Sertifikat Laik Operasi (SLO) Sah & Validasi Registrasi Nasional',
                'desc' => 'Mekanisme penerbitan sertifikat kelaikan resmi berbarcode validasi online, pencatatan nomor register resmi, serta pemasangan pelat sertifikasi di fasilitas kelistrikan.'
            ],
            [
                'title' => 'Peta Jalan Pemeliharaan Listrik Preventif & Prediktif Pasca-Sertifikasi SLO',
                'desc' => 'Panduan penyusunan jadwal perawatan berkala, kalibrasi instrumen ukur tahunan, pemantauan online keandalan sistem kelistrikan, dan persiapan resertifikasi tepat waktu.'
            ]
        ];

        $content = "<h2>Panduan Komprehensif: {$formattedTitle}</h2>\\n\\n";
        $content .= "<p>Dalam operasional fasilitas industri modern, kawasan komersial, gedung bertingkat, dan pusat data yang beroperasi non-stop, ketersediaan pasokan listrik yang stabil, andal, dan aman merupakan urat nadi keberlangsungan bisnis. Pelaksanaan <strong>{$formattedTitle}</strong> di wilayah {$regionName} membuktikan komitmen nyata manajemen dalam menjamin bahwa seluruh instalasi ketenagalistrikan telah memenuhi kaidah keselamatan teknik tertinggi, terbebas dari ancaman korsleting pemicu kebakaran, dan memenuhi persyaratan legalitas kelaikan operasi yang sah.</p>\\n\\n";
        $content .= "<p>Sertifikat Laik Operasi (SLO) adalah bukti otentik bahwa suatu instalasi tenaga listrik telah selesai dibangun, dipasang, dan diuji secara komprehensif melalui serangkaian tahapan komisioning teknik independen. Dokumen panduan ini menguraikan delapan belas pilar audit pengujian kelaikan ketenagalistrikan, mencakup pemeriksaan tegangan rendah (TR), tegangan menengah (TM 20 kV), pembangkit mandiri (genset diesel & PLTS), hingga proteksi petir terpadu yang dirancang sebagai standar acuan bagi pemilik fasilitas, kepala teknisi elektrikal, manajer energi, dan tim keselamatan kerja di {$regionName}.</p>\\n\\n";

        foreach ($chapters as $index => $chap) {
            $num = $index + 1;
            $content .= "<h3>Bab {$num}: {$chap['title']}</h3>\\n";
            $content .= "<p><strong>Fokus Bahasan Teknis:</strong> {$chap['desc']}</p>\\n";

            $content .= "<p>Penerapan audit kelaikan pada bab ini di area operasional {$regionName} berfokus pada evaluasi integritas fisik material dan keandalan kinerja sistem kelistrikan di bawah berbagai skenario operasi. Setiap potensi anomali isolasi atau setelan proteksi yang tidak presisi dapat memicu kegagalan fatal, mulai dari lonjakan panas lokal (*hotspot*), degradasi dielektrik, pelepasan busur api (*arc flash*), hingga pemadaman total pabrik (*blackout*) yang menimbulkan kerugian finansial masif dan membahayakan keselamatan jiwa tenaga kerja.</p>\\n";

            $content .= "<h4>Metodologi Pengujian & Langkah Kerja Standar:</h4>\\n";
            $content .= "<ul>\\n";
            $content .= "<li><strong>Verifikasi Dokumen & Kondisi Lapangan:</strong> Menyelaraskan Single Line Diagram (SLD) terbaru dengan kondisi riil instalasi panel, jenis pemutus arus, serta kapasitas trafo dan kabel di fasilitas {$regionName}.</li>\\n";
            $content .= "<li><strong>Pengukuran Menggunakan Instrumen Terkalibrasi:</strong> Melakukan pengujian presisi dengan alat ukur berstandar laboratorium (Megger Insulation Tester, Digital Earth Tester, Hi-Pot Tester, Power Quality Logger) yang memiliki sertifikat kalibrasi aktif.</li>\\n";
            $content .= "<li><strong>Analisis Deviasi terhadap Ambang Batas:</strong> Membandingkan data hasil ukur dengan kriteria kelaikan PUIL nasional, seperti nilai isolasi minimal 1.000 Ohm per Volt tegangan kerja dan tahanan pembumian maksimal 5 Ohm.</li>\\n";
            $content .= "<li><strong>Penyusunan Berita Acara & Tindakan Korektif:</strong> Mendokumentasikan setiap temuan anomali teknis, menyusun rekomendasi perbaikan berbasis skala prioritas risiko, dan melakukan pengujian ulang (*re-test*) pasca-perbaikan.</li>\\n";
            $content .= "</ul>\\n";

            $content .= "<p>Di samping itu, sinergi antara tim teknisi internal fasilitas {$regionName} dengan tenaga ahli inspeksi teknik ketenagalistrikan independen menjamin objektivitas evaluasi. Pendekatan ini memastikan bahwa sertifikasi kelaikan yang diterbitkan tidak sekadar formalitas administratif, melainkan jaminan mutu operasional yang melindungi aset investasi perusahaan dalam jangka panjang.</p>\\n";

            $content .= "<blockquote>\\n";
            $content .= "<p><strong>Prinsip Keandalan Listrik:</strong> \\\"Instalasi listrik yang laik operasi bukan sekadar memenuhi syarat penyambungan daya, melainkan fondasi keselamatan kerja yang melindungi aset bernilai tinggi, mencegah risiko kebakaran katastropik, dan menjaga kontinuitas proses produksi tanpa henti.\\\"</p>\\n";
            $content .= "</blockquote>\\n";

            $content .= "<p>Melalui penerapan konsisten langkah-langkah di atas, fasilitas industri dan komersial di {$regionName} akan selalu berada pada tingkat keandalan optimal, siap menghadapi audit keselamatan tahunan, serta memperoleh efisiensi pemakaian energi listrik yang lebih tinggi.</p>\\n\\n";
        }

        $content .= "<h3>Kesimpulan & Langkah Pengurusan Sertifikat Laik Operasi di {$regionName}</h3>\\n";
        $content .= "<p>Pelaksanaan menyeluruh tahapan dalam <strong>{$formattedTitle}</strong> menegaskan bahwa kepatuhan kelaikan operasi listrik merupakan investasi strategis dalam memitigasi risiko operasional dan legalitas perusahaan. Fasilitas bisnis di {$regionName} yang memiliki instalasi listrik teruji dan tersertifikasi resmi SLO akan menikmati jaminan ketenangan operasional, kemudahan proses asuransi aset, serta peningkatan reputasi sebagai entitas industri yang bertanggung jawab dan taat regulasi keselamatan kerja.</p>\\n";
        $content .= "<p>Untuk konsultasi teknis, permohonan inspeksi kelaikan, uji komisioning, maupun pengurusan resmi Sertifikat Laik Operasi (SLO) instalasi listrik tegangan rendah, tegangan menengah, genset, dan penangkal petir di {$regionName}, hubungi tim konsultan dan inspektur teknik resmi kami melalui hotline layanan terpadu.</p>\\n";

        return [
            'title' => $formattedTitle,
            'slug' => $slug,
            'region' => $regionName,
            'excerpt' => "Panduan teknis otoritatif {$formattedTitle} mengupas standar inspeksi kelaikan operasi listrik, uji isolasi megger, tahanan grounding, proteksi relai, dan pengurusan sertifikat SLO resmi di {$regionName}.",
            'content' => $content
        ];
    }

    public static function getRegionalArticleList($region, int $limit = 200): array
    {
        if (is_array($region)) {
            $parts = [];
            if (!empty($region['district'])) $parts[] = $region['district'];
            if (!empty($region['city'])) $parts[] = $region['city'];
            if (!empty($region['province'])) $parts[] = $region['province'];
            $regionName = !empty($parts) ? implode(', ', $parts) : 'Indonesia';
        } else {
            $regionName = (string) $region;
        }

        $titles = self::get200ArticleTitles();
        $articles = [];

        foreach (array_slice($titles, 0, $limit) as $index => $tTemplate) {
            $fullTitle = str_replace('{region}', $regionName, $tTemplate);
            $slug = Str::slug($fullTitle);
            $articles[] = [
                'id' => $index + 1,
                'title' => $fullTitle,
                'slug' => $slug,
                'category' => 'Jasa SLO Ketenagalistrikan',
                'region' => $regionName,
                'excerpt' => "Panduan komprehensif mengenai {$fullTitle} untuk memastikan kelaikan operasi instalasi listrik, kepatuhan audit PUIL, dan penerbitan Sertifikat Laik Operasi resmi di {$regionName}.",
                'author' => 'Lead Electrical Inspector & Tim Ahli Ketenagalistrikan',
                'read_time' => 22,
                'views_count' => 180 + ($index * 9) % 420,
                'published_at' => now()->subDays($index % 60)->format('d/m/Y')
            ];
        }

        return $articles;
    }

    public static function getArticleBySlug(string $slug, $region = 'Indonesia'): ?array
    {
        if (is_array($region)) {
            $parts = [];
            if (!empty($region['district'])) $parts[] = $region['district'];
            if (!empty($region['city'])) $parts[] = $region['city'];
            if (!empty($region['province'])) $parts[] = $region['province'];
            $regionName = !empty($parts) ? implode(', ', $parts) : 'Indonesia';
        } else {
            $regionName = (string) $region;
        }

        $titles = self::get200ArticleTitles();
        $foundTitle = null;

        foreach ($titles as $tTemplate) {
            $testTitle = str_replace('{region}', $regionName, $tTemplate);
            if (Str::slug($testTitle) === $slug) {
                $foundTitle = $testTitle;
                break;
            }
        }

        if (!$foundTitle) {
            $cleanTitle = ucwords(str_replace('-', ' ', $slug));
            $foundTitle = $cleanTitle;
        }

        $articleData = self::generateDeepArticle($foundTitle, $regionName);

        return [
            'title' => $articleData['title'],
            'slug' => $slug,
            'category' => 'Jasa SLO Ketenagalistrikan',
            'region' => $regionName,
            'author' => 'Lead Electrical Inspector & Tim Ahli Ketenagalistrikan',
            'read_time' => 22,
            'views_count' => 420,
            'created_at' => now()->subDays(2),
            'excerpt' => $articleData['excerpt'],
            'content' => $articleData['content']
        ];
    }

    public static function getArticleTopics(): array
    {
        return [
            ['name' => 'Semua Topik', 'slug' => 'semua'],
            ['name' => 'SLO Tegangan Rendah', 'slug' => 'slo-tegangan-rendah'],
            ['name' => 'SLO Tegangan Menengah 20 kV', 'slug' => 'slo-tegangan-menengah'],
            ['name' => 'SLO Pembangkit & Genset', 'slug' => 'slo-pembangkit-genset'],
            ['name' => 'Komisioning & Uji Megger', 'slug' => 'komisioning-uji-megger'],
            ['name' => 'Sistem Pembumian (Grounding)', 'slug' => 'sistem-pembumian-grounding'],
            ['name' => 'Proteksi Petir & Surja', 'slug' => 'proteksi-petir-surja'],
            ['name' => 'Kualitas Daya & Harmonisa', 'slug' => 'kualitas-daya-harmonisa'],
        ];
    }

    public static function getOrSynthesizeArticle(string $slug, $region = 'Indonesia'): ?array
    {
        $dbArticle = \\App\\Models\\Article::where('slug', $slug)->first();
        if ($dbArticle) {
            return $dbArticle->toArray();
        }
        return self::getArticleBySlug($slug, $region);
    }
}
"""

with open(service_file, "w", encoding="utf-8") as f:
    f.write(service_code)

print(f"JasaSloSchemeService.php written successfully to {service_file}")
