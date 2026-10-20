<?php

namespace Database\Seeders;

use App\Models\User;
use App\Models\Setting;
use App\Models\Statistic;
use App\Models\Program;
use App\Models\Article;
use App\Models\Faq;
use App\Services\JasaSloSchemeService;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Schema;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     */
    public function run(): void
    {
        Schema::disableForeignKeyConstraints();

        // 1. Super Admin User
        User::updateOrCreate(
            ['email' => 'admin@jasaslo.my.id'],
            [
                'name' => 'Administrator Jasa SLO Indonesia',
                'password' => Hash::make('admin123'),
                'email_verified_at' => now(),
            ]
        );

        // 2. Settings
        $settings = [
            'site_name' => 'Jasa SLO - Sertifikat Laik Operasi Ketenagalistrikan',
            'site_tagline' => 'Layanan Resmi Inspeksi, Uji Komisioning & Penerbitan Sertifikat Laik Operasi (SLO) Nasional',
            'company_name' => 'Lembaga Inspeksi Teknik & Sertifikasi Ketenagalistrikan Indonesia',
            'license_info' => 'Lembaga Inspeksi Teknik Terakreditasi Standar Uji Kelaikan Operasi Nasional',
            'whatsapp' => '081399810272', // Main WA Utama (Highlighted)
            'whatsapp_detail_1' => '08118500177',
            'whatsapp_detail_2' => '081399810272',
            'whatsapp_detail_3' => '087894580806',
            'whatsapp_detail_4' => '087894580649',
            'email' => 'kontak@jasaslo.my.id',
            'email_secondary' => 'info@jasaslo.my.id',
            'phone' => '081399810272',
            'address' => 'Gedung Pusat Layanan Inspeksi Teknik Ketenagalistrikan & Sertifikasi Laik Operasi, Jakarta',
            'maps_embed' => 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126920.28298835848!2d106.759478!3d-6.2297465!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f3e498c0a531%3A0x7d87f7b2c0e86b0a!2sJakarta%2C%20Indonesia!5e0!3m2!1sen!2sid!4v1700000000000!5m2!1sen!2sid',
            'office_hours' => 'Senin - Jumat: 08.00 - 17.00 WIB | Hotline Konsultasi Cepat SLO & Uji Komisioning WA: 24 Jam',
            'hero_title' => 'Layanan Resmi Jasa SLO (Sertifikat Laik Operasi) & Uji Komisioning Ketenagalistrikan',
            'hero_description' => 'Mitra inspeksi teknik terakreditasi untuk pengujian kelaikan operasi instalasi listrik tegangan rendah, tegangan menengah 20 kV, genset darurat, PLTS atap, dan proteksi petir di 38 provinsi di Indonesia.',
            'about_history' => 'Lembaga Jasa SLO didirikan oleh gabungan insinyur elektro senior, lead inspector teknik ketenagalistrikan, dan praktisi proteksi daya dengan pengalaman lebih dari dua dekade. Kami berdedikasi mendampingi sektor industri manufaktur, gedung komersial, pertambangan, perhotelan, rumah sakit, dan data center dalam menjamin bahwa sistem ketenagalistrikan yang terpasang beroperasi secara aman, andal, ramah lingkungan, dan mengantongi legalitas Sertifikat Laik Operasi (SLO) yang sah dan berkekuatan hukum penuh.',
            'about_vision' => 'Menjadi lembaga inspeksi teknik ketenagalistrikan terdepan, terpercaya, dan tercepat di Indonesia dalam mewujudkan instalasi listrik yang andal, aman dari bahaya kebakaran, dan memenuhi standar kelaikan operasi nasional.',
            'about_mission' => "1. Menyelenggarakan uji pemeriksaan dan komisioning kelaikan operasi instalasi listrik tegangan rendah, menengah, dan pembangkit secara presisi dengan instrumen uji terkalibrasi.\n2. Memberikan layanan penerbitan Sertifikat Laik Operasi (SLO) sah dengan proses transparan, akuntabel, dan berorientasi pada kepuasan pelanggan.\n3. Meningkatkan kompetensi tenaga teknik ketenagalistrikan melalui pelatihan dan sertifikasi SKTTK berstandar kompetensi kerja nasional.\n4. Mendukung keandalan pasokan listrik industri untuk mewujudkan Zero Electrical Fire and Incident di seluruh pelosok tanah air.",
            'floating_wa_text' => 'Halo Admin Jasa SLO Indonesia, saya ingin konsultasi pengurusan Sertifikat Laik Operasi (SLO) dan uji komisioning instalasi listrik perusahaan.'
        ];

        foreach ($settings as $key => $value) {
            Setting::updateOrCreate(['key' => $key], ['value' => $value]);
        }

        // 3. Statistics
        $statistics = [
            [
                'key' => 'slo_terbit',
                'label' => 'Sertifikat SLO Terbit',
                'value' => '18.500+',
                'icon' => 'bi-patch-check-fill',
                'description' => 'Instalasi TR, TM 20 kV, Genset & PLTS Industri Terakreditasi',
                'sort_order' => 1
            ],
            [
                'key' => 'kepatuhan_puil',
                'label' => 'Kepatuhan Standar Uji',
                'value' => '100%',
                'icon' => 'bi-shield-check',
                'description' => 'Uji Isolasi Megger, Tahanan Grounding & Proteksi PUIL Sah',
                'sort_order' => 2
            ],
            [
                'key' => 'jangkauan_provinsi',
                'label' => 'Jangkauan Wilayah Inspeksi',
                'value' => '38',
                'icon' => 'bi-geo-alt-fill',
                'description' => 'Provinsi di Seluruh Wilayah Republik Indonesia',
                'sort_order' => 3
            ],
            [
                'key' => 'kepuasan_klien',
                'label' => 'Tingkat Kepuasan Klien',
                'value' => '99.8%',
                'icon' => 'bi-trophy-fill',
                'description' => 'Didukung Lebih dari 1.500 Perusahaan Multinasional & BUMN',
                'sort_order' => 4
            ]
        ];

        foreach ($statistics as $stat) {
            Statistic::updateOrCreate(['key' => $stat['key']], $stat);
        }

        // 4. Programs Seeding from JasaSloSchemeService
        $programs = JasaSloSchemeService::getMasterPrograms();
        foreach ($programs as $index => $prog) {
            Program::updateOrCreate(
                ['slug' => $prog['slug']],
                [
                    'title' => $prog['title'],
                    'level_name' => $prog['level_name'] ?? 'Layanan Sertifikasi SLO Resmi',
                    'level_code' => $prog['level_code'] ?? 'SLO',
                    'badge' => $prog['badge'] ?? 'Layanan Terakreditasi',
                    'duration' => $prog['duration'] ?? 'Proses Cepat & Akurat',
                    'method' => $prog['method'] ?? 'Inspeksi Visual & Uji Instrumen Digital',
                    'certification' => $prog['certification'] ?? 'Sertifikat Laik Operasi (SLO) Resmi',
                    'price_note' => $prog['price_note'] ?? 'Hubungi Tim Ahli Inspeksi SLO',
                    'target_audience' => $prog['target_audience'] ?? '',
                    'requirements' => json_encode($prog['requirements'] ?? []),
                    'curriculum' => json_encode($prog['curriculum'] ?? []),
                    'facilities' => json_encode($prog['facilities'] ?? []),
                    'short_description' => $prog['short_description'] ?? '',
                    'full_description' => $prog['overview'] ?? ($prog['short_description'] ?? ''),
                    'image' => 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&auto=format&fit=crop&q=80',
                    'is_active' => true,
                    'sort_order' => $index + 1
                ]
            );
        }

        // 5. Featured Articles (Homepage 3 cards)
        $articles = [
            [
                'title' => 'Training Jasa SLO: Panduan Lengkap Sertifikasi Laik Operasi Ketenagalistrikan & Standar PUIL di Indonesia',
                'slug' => 'training-jasa-slo-panduan-lengkap-sertifikasi-laik-operasi-ketenagalistrikan-standar-puil-di-indonesia',
                'category' => 'Panduan Sertifikasi SLO',
                'author' => 'Lead Electrical Inspector & Tim Ahli Ketenagalistrikan',
                'read_time' => 25,
                'views_count' => 6450,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Panduan komprehensif alur permohonan Sertifikat Laik Operasi (SLO), persyaratan berkas single line diagram, tata cara inspeksi lapangan, dan pemenuhan regulasi keselamatan listrik nasional.',
                'content' => JasaSloSchemeService::generateDeepArticle('Training Jasa SLO: Panduan Lengkap Sertifikasi Laik Operasi Ketenagalistrikan & Standar PUIL di Indonesia', 'Indonesia')['content']
            ],
            [
                'title' => 'Jasa SLO: Uji Kelaikan Operasi Instalasi Pemanfaatan Tenaga Listrik Tegangan Rendah & Menengah di Indonesia',
                'slug' => 'jasa-slo-uji-kelaikan-operasi-instalasi-pemanfaatan-tenaga-listrik-tegangan-rendah-menengah-di-indonesia',
                'category' => 'Inspeksi Tegangan Rendah & Menengah',
                'author' => 'Lead Electrical Inspector & Tim Ahli Ketenagalistrikan',
                'read_time' => 28,
                'views_count' => 5890,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Prosedur teknis pengujian kelaikan operasi gardu distribusi, kubikel 20 kV, trafo daya, panel LVMDP, pengukuran tahanan isolasi kabel, dan mitigasi bahaya kebakaran akibat korsleting.',
                'content' => JasaSloSchemeService::generateDeepArticle('Jasa SLO: Uji Kelaikan Operasi Instalasi Pemanfaatan Tenaga Listrik Tegangan Rendah & Menengah di Indonesia', 'Indonesia')['content']
            ],
            [
                'title' => 'Training Jasa SLO: Standardisasi Uji Komisioning & Pengukuran Pembumian Grounding di Indonesia',
                'slug' => 'training-jasa-slo-standardisasi-uji-komisioning-pengukuran-pembumian-grounding-di-indonesia',
                'category' => 'Uji Komisioning & Grounding',
                'author' => 'Lead Electrical Inspector & Tim Ahli Ketenagalistrikan',
                'read_time' => 24,
                'views_count' => 5120,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Metodologi sistematis pengukuran resistansi grounding pembumian titik netral dan proteksi petir di bawah 1-5 Ohm, uji kontinuitas penyetara potensial, serta verifikasi kalibrasi alat ukur digital.',
                'content' => JasaSloSchemeService::generateDeepArticle('Training Jasa SLO: Standardisasi Uji Komisioning & Pengukuran Pembumian Grounding di Indonesia', 'Indonesia')['content']
            ]
        ];

        foreach ($articles as $art) {
            Article::updateOrCreate(['slug' => $art['slug']], $art);
        }

        // 6. FAQs
        $faqs = [
            [
                'question' => 'Apa itu Sertifikat Laik Operasi (SLO) dan mengapa wajib dimiliki oleh setiap pemilik instalasi listrik?',
                'answer' => 'Sertifikat Laik Operasi (SLO) adalah sertifikat resmi yang membuktikan bahwa instalasi tenaga listrik (pemanfaatan, pembangkit, distribusi) telah lulus uji kelaikan operasi teknis dan dinyatakan aman untuk dialiri arus listrik. Memiliki SLO adalah kewajiban hukum untuk mencegah bahaya kebakaran akibat korsleting, melindungi aset industri bernilai tinggi, serta menjadi syarat utama penyambungan dan penambahan daya dari penyedia tenaga listrik.',
                'sort_order' => 1
            ],
            [
                'question' => 'Instalasi listrik apa saja yang dapat dilayani pengurusan dan pengujian SLO-nya oleh lembaga kami?',
                'answer' => 'Kami melayani 8 lingkup pengujian dan sertifikasi kelaikan operasi: 1) Instalasi Pemanfaatan Tenaga Listrik Tegangan Rendah (IPTL TR pabrik, gedung, komersial); 2) Instalasi Pemanfaatan Tenaga Listrik Tegangan Menengah (IPTL TM 20 kV gardu & trafo); 3) Pembangkit Tenaga Listrik Mandiri (Genset Diesel, Turbin & PLTS Atap); 4) Instalasi Distribusi Tenaga Listrik SUTM / SKTM; 5) Sertifikasi Kompetensi Tenaga Teknik Ketenagalistrikan (SKTTK); 6) Pelatihan Uji Komisioning Listrik; 7) Audit Keselamatan Listrik & Kualitas Daya; serta 8) Sertifikasi Sistem Penyalur Petir Terintegrasi.',
                'sort_order' => 2
            ],
            [
                'question' => 'Berapa lama masa berlaku Sertifikat Laik Operasi (SLO) dan kapan harus diperpanjang?',
                'answer' => 'Sesuai standar regulasi keselamatan ketenagalistrikan nasional, Sertifikat Laik Operasi untuk instalasi pemanfaatan tenaga listrik (IPTL) berlaku selama 5 (lima) tahun, sedangkan untuk instalasi pembangkit tenaga listrik (Genset/PLTS) dan instalasi distribusi berlaku selama 5 (lima) tahun. Resertifikasi atau perpanjangan SLO wajib diajukan sebelum masa berlaku habis untuk menjamin bahwa instalasi tetap berada dalam kondisi prima dan laik operasi.',
                'sort_order' => 3
            ],
            [
                'question' => 'Apa saja parameter teknis yang diuji selama sesi inspeksi komisioning di lapangan?',
                'answer' => 'Proses pengujian teknis mencakup: 1) Pemeriksaan visual kesesuaian Single Line Diagram (SLD) dan tata letak panel; 2) Pengukuran tahanan isolasi penghantar (Megger Test); 3) Pengukuran nilai tahanan sistem pembumian (Grounding Test); 4) Uji kontinuitas konduktor proteksi dan urutan fasa (Phase Sequence); 5) Uji karakteristik trip pemutus tenaga (Breaker Test); 6) Uji injeksi sekunder relai proteksi; 7) Uji pembebanan generator (Load Bank Test); serta 8) Pemindaian termografi inframerah pada titik sambungan busbar.',
                'sort_order' => 4
            ],
            [
                'question' => 'Bagaimana prosedur dan estimasi waktu penerbitan Sertifikat Laik Operasi (SLO) melalui lembaga kami?',
                'answer' => 'Prosedur sangat mudah dan cepat: 1) Pengajuan permohonan dan penyerahan dokumen teknis (SLD & data kapasitas daya); 2) Verifikasi administrasi dan penjadwalan tim inspektur teknik; 3) Pelaksanaan inspeksi dan pengujian fisik di lokasi fasilitas klien; 4) Penyusunan Laporan Hasil Pemeriksaan & Pengujian (LHPP); 5) Evaluasi kelaikan teknik; dan 6) Penerbitan resmi Sertifikat Laik Operasi (SLO) berbarcode validasi online dalam waktu 3 hingga 7 hari kerja setelah pengujian dinyatakan lulus.',
                'sort_order' => 5
            ]
        ];

        foreach ($faqs as $faq) {
            Faq::updateOrCreate(['question' => $faq['question']], $faq);
        }

        Schema::enableForeignKeyConstraints();
    }
}
