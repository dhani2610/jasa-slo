import re

seeder_path = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\database\seeders\DatabaseSeeder.php"

with open(seeder_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define new articles to prepend in $articles
new_articles_code = """        // 5. Featured Articles (Homepage & All Catalog)
        $articles = [
            [
                'title' => 'Training Ahli K3 Umum Resmi: Panduan Sertifikasi dan Lisensi K3 Perusahaan Terakreditasi Nasional',
                'slug' => 'training-ahli-k3-umum-resmi-panduan-sertifikasi-dan-lisensi-k3-perusahaan-terakreditasi-nasional',
                'category' => 'Sertifikasi Ahli K3 Resmi',
                'author' => 'Lead Auditor SMK3 & Master Trainer K3 Korporasi',
                'read_time' => 28,
                'views_count' => 6240,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Panduan komprehensif mengikuti program pembinaan dan sertifikasi resmi Ahli K3 Umum berlisensi sah nasional. Syarat penunjukan, kurikulum pengawasan norma K3, dan kepatuhan perundangan.',
                'content' => AhliK3UmumSchemeService::generateDeepArticle('Training Ahli K3 Umum Resmi: Panduan Sertifikasi dan Lisensi K3 Perusahaan Terakreditasi Nasional', 'Indonesia')['content']
            ],
            [
                'title' => 'Training Ahli K3 Umum Sertifikasi: Standar Kompetensi Personel K3 dan Implementasi SMK3 Korporasi',
                'slug' => 'training-ahli-k3-umum-sertifikasi-standar-kompetensi-personel-k3-dan-implementasi-smk3-korporasi',
                'category' => 'Pembinaan Kompetensi & In-House K3',
                'author' => 'Lead Auditor SMK3 & Master Trainer K3 Korporasi',
                'read_time' => 26,
                'views_count' => 5890,
                'is_featured' => true,
                'is_published' => true,
                'featured_image' => 'https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=80',
                'excerpt' => 'Standar kompetensi Ahli K3 Umum tersertifikasi dalam mengawal audit SMK3 PP 50/2012, formulasi HIRADC, izin kerja aman, dan pengawasan keselamatan kerja industri operasional.',
                'content' => AhliK3UmumSchemeService::generateDeepArticle('Training Ahli K3 Umum Sertifikasi: Standar Kompetensi Personel K3 dan Implementasi SMK3 Korporasi', 'Indonesia')['content']
            ],"""

# Replace the beginning of $articles = [
pattern = r"// 5\. Featured Articles \(Homepage 3 cards\)\s*\$articles = \["
content = re.sub(pattern, new_articles_code, content)

# Update FAQ answer 1
old_faq_ans = "'Lembaga kami menyediakan 6 program pembinaan kompetensi K3 korporat unggulan: 1) Training Pembinaan Ahli K3 Umum Corporate (In-House & Public Certification); 2) Training Audit Sistem Manajemen K3 (SMK3 Korporat 166 Kriteria PP 50/2012); 3) Training Manajemen Risiko K3 Korporasi (HIRADC, IBPPR & JSA Terpadu); 4) Training Investigasi Insiden & Analisis Akar Masalah (RCA & SCAT); 5) Training Kelembagaan & Pengurus P2K3 Bipartit; serta 6) Training Tanggap Darurat & Emergency Response Plan (ERP) Korporat.'"
new_faq_ans = "'Lembaga kami menyediakan 10 program pembinaan kompetensi K3 korporat unggulan: 1) Training Pembinaan Ahli K3 Umum Corporate; 2) Training Audit Sistem Manajemen K3 (SMK3 PP 50/2012); 3) Training Manajemen Risiko K3 (HIRADC, IBPPR & JSA); 4) Training Investigasi Insiden & Analisis Akar Masalah (RCA & SCAT); 5) Training Kelembagaan P2K3 Bipartit; 6) Training Tanggap Darurat & ERP Korporat; 7) Training Ahli K3 Umum Resmi; 8) Training Ahli K3 Umum Sertifikasi; 9) Training Petugas Penanggulangan Kebakaran Industri; serta 10) Training K3 Ruang Terbatas (Confined Space) & Ketinggian.'"

content = content.replace(old_faq_ans, new_faq_ans)

with open(seeder_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated DatabaseSeeder.php successfully!")
