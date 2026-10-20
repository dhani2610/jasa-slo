@extends('layouts.front')

@section('title', 'Jasa SLO Ketenagalistrikan ' . $kecamatanData['name'] . ', ' . $kecamatanData['kabkot']['name'] . ' | Sertifikasi Personel Rig Keselamatan Kerja Resmi')
@section('meta_description', 'Layanan resmi pelatihan dan sertifikasi kompetensi K3 Personel Rig Keselamatan Kerja (Jasa SLO (Sertifikat Laik Operasi) Crew) di Kecamatan ' . $kecamatanData['name'] . ', ' . $kecamatanData['kabkot']['name'] . ', ' . $kecamatanData['province']['name'] . '. Hubungi WhatsApp 081399810272.')

@section('content')

    <!-- HERO KECAMATAN -->
    <section class="hero-section" style="padding: 48px 0 44px; text-align: left;">
        <div class="container">
            <div style="font-size: 0.82rem; color: #a7f3d0; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <a href="{{ route('home') }}" style="color: #cbd5e1;"><i class="bi bi-house-door"></i> Beranda</a>
                <span>/</span>
                <a href="{{ route('wilayah.provinsi', $kecamatanData['province']['slug']) }}" style="color: #cbd5e1;">Provinsi {{ $kecamatanData['province']['name'] }}</a>
                <span>/</span>
                <a href="{{ route('wilayah.kabkot', [$kecamatanData['province']['slug'], $kecamatanData['kabkot']['slug']]) }}" style="color: #cbd5e1;">{{ $kecamatanData['kabkot']['name'] }}</a>
                <span>/</span>
                <span style="color: #ffffff; font-weight: 700;">Kecamatan {{ $kecamatanData['name'] }}</span>
            </div>

            <div style="display: flex; gap: 10px; align-items: center; margin-bottom: 14px; flex-wrap: wrap;">
                <span class="hero-badge" style="margin-bottom: 0;">
                    <i class="bi bi-geo-alt-fill"></i> Kecamatan {{ $kecamatanData['name'] }}
                </span>
                <span class="hero-badge" style="margin-bottom: 0; background: rgba(16, 185, 129, 0.2); border-color: #34d399; color: #a7f3d0;">
                    <i class="bi bi-buildings"></i> {{ $kecamatanData['kabkot']['name'] }}
                </span>
                <span class="hero-badge" style="margin-bottom: 0; background: rgba(16, 185, 129, 0.2); border-color: #10b981; color: #a7f3d0;">
                    <i class="bi bi-shield-check"></i> Standar Kompetensi Personel Rig Keselamatan Kerja & Standar Operasional Rig Internasional
                </span>
            </div>

            <h1 class="hero-title" style="margin-left: 0; font-size: 2.2rem; line-height: 1.25; margin-bottom: 14px;">
                Jasa SLO Ketenagalistrikan <span>Kecamatan {{ $kecamatanData['name'] }}</span>
            </h1>

            <p class="hero-lead" style="margin-left: 0; max-width: 880px; margin-bottom: 22px;">
                Penyelenggaraan pelatihan kompetensi Operator Keselamatan & Kesehatan Kerja Korporat (Jasa SLO Ketenagalistrikan) di Kecamatan {{ $kecamatanData['name'] }}, {{ $kecamatanData['kabkot']['name'] }}, Provinsi {{ $kecamatanData['province']['name'] }}. Menguasai standar manajemen keselamatan kerja, keselamatan tempat kerja (Auditor SMK3), operasional menara (Analis Risiko HIRADC), pengendalian tekanan sumur (Manajemen Risiko K3 ISO 45001 & IADC), pengujian BOP bertekanan tinggi, dan formulasi keselamatan proses industri (Pengurus P2K3 Bipartit).
            </p>

            <div class="hero-cta" style="justify-content: flex-start; margin-bottom: 0;">
                <a href="{{ $waLink }}" target="_blank" class="btn-primary-green">
                    <i class="bi bi-whatsapp"></i>
                    Konsultasi Wilayah {{ $kecamatanData['name'] }}
                </a>
                <a href="#kecamatan-nav-box" class="btn-outline-white">
                    <i class="bi bi-pin-map-fill"></i>
                    Pilih Kecamatan Lain
                </a>
            </div>
        </div>
    </section>

    <!-- 6 PROGRAM PELATIHAN -->
    <section class="section-py">
        <div class="container">
            <div class="section-header">
                <span class="section-tag">6 Program Resmi di {{ $kecamatanData['name'] }}</span>
                <h2 class="section-title">Program Sertifikasi Operator Keselamatan & Kesehatan Kerja Korporat (Jasa SLO Ketenagalistrikan) & Lisensi Rig Resmi</h2>
                <p class="section-desc">
                    Tersedia 6 program pelatihan resmi yang masing-masing memiliki panduan modul materi dan silabus kurikulum di Kecamatan {{ $kecamatanData['name'] }}:
                </p>
            </div>

            <div class="programs-grid" style="margin-bottom: 48px;">
                @foreach($programs as $prog)
                    @php
                        $progObj = (object)$prog;
                        $progDetailUrl = route('wilayah.kecamatan.program', [$kecamatanData['province']['slug'], $kecamatanData['kabkot']['slug'], $kecamatanData['slug'], $progObj->slug]);
                    @endphp
                    <div class="program-card">
                        <div class="program-img-wrapper">
                            <img src="{{ $progObj->image ?? 'https://images.unsplash.com/photo-1541888946425-d0fbb18615f3?w=800&auto=format&fit=crop&q=80' }}" alt="{{ $progObj->title }}" class="program-img" loading="lazy">
                            <span class="program-badge">{{ $progObj->badge ?? 'Sertifikasi Resmi' }}</span>
                        </div>

                        <div class="program-body">
                            <div class="program-level">{{ $progObj->level_name ?? 'Sertifikasi Ahli K3 Keselamatan Kerja' }}</div>
                            <h3 class="program-title">{{ $progObj->title }}</h3>
                            <p class="program-desc">
                                {{ Str::limit($progObj->short_description ?? ($progObj->full_description ?? ''), 130) }}
                            </p>

                            <div class="program-meta">
                                <div><i class="bi bi-geo-alt" style="color: #10b981;"></i> {{ $kecamatanData['name'] }}</div>
                                <div><i class="bi bi-journal-check" style="color: #10b981;"></i> Modul Panduan Lengkap</div>
                            </div>

                            <div class="program-footer-btn">
                                <a href="{{ $progDetailUrl }}" class="btn-primary-green" style="width: 100%; justify-content: center; font-size: 0.84rem; padding: 10px 14px;">
                                    <i class="bi bi-collection-play-fill"></i> Buka Direktori Panduan {{ $kecamatanData['name'] }}
                                </a>
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>

            <!-- 4 WHATSAPP HOTLINES -->
            <div class="wa-hotlines-box" style="margin-bottom: 48px;">
                <div class="wa-hotlines-header">
                    <h3><i class="bi bi-telephone-inbound-fill" style="color: var(--accent-mint); margin-right: 8px;"></i> 4 Nomor WhatsApp Resmi Layanan di {{ $kecamatanData['name'] }}</h3>
                    <p>Silakan hubungi kontak resmi kami untuk konsultasi jadwal batch, silabus materi, dan pendaftaran mandiri maupun in-house corporate:</p>
                </div>

                <div class="wa-cards-grid">
                    @foreach($waNumbers as $wa)
                        <div class="wa-hotline-card {{ !empty($wa['is_primary']) ? 'primary-hotline-card' : '' }}">
                            <div class="wa-card-top">
                                <div class="wa-card-icon">
                                    <i class="bi {{ $wa['icon'] }}"></i>
                                </div>
                                <span class="wa-card-badge">{{ $wa['badge'] }}</span>
                            </div>
                            <h4 class="wa-card-title">{{ $wa['title'] }}</h4>
                            <p class="wa-card-desc">{{ $wa['desc'] }}</p>
                            <a href="{{ $wa['url'] }}" target="_blank" class="btn-wa-card">
                                <i class="bi bi-whatsapp"></i> Chat {{ $wa['number'] }}
                            </a>
                        </div>
                    @endforeach
                </div>
            </div>

            <!-- NAVIGASI KECAMATAN LAIN (SEBELUM ARTIKEL AGAR AKSES CEPAT TANPA SCROLL JAUH) -->
            @if(isset($kecamatanList) && count($kecamatanList) > 0)
                <div id="kecamatan-nav-box" style="background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); border: 2px solid #a7f3d0; border-radius: var(--radius-xl); padding: 32px; margin-bottom: 48px; box-shadow: 0 10px 30px -5px rgba(16, 185, 129, 0.1);">
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 1px solid #e2e8f0; padding-bottom: 16px; flex-wrap: wrap; gap: 12px;">
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                                <a href="{{ route('wilayah.kabkot', [$kecamatanData['province']['slug'], $kecamatanData['kabkot']['slug']]) }}" style="font-size: 0.78rem; font-weight: 700; color: #4c1d95; background: #eff6ff; border: 1px solid #bfdbfe; padding: 4px 10px; border-radius: 6px; text-decoration: none;">
                                    <i class="bi bi-arrow-left"></i> {{ $kecamatanData['kabkot']['name'] }}
                                </a>
                                <span style="font-size: 0.78rem; font-weight: 800; background: #062e22; color: #a7f3d0; padding: 4px 12px; border-radius: 20px;">
                                    <i class="bi bi-geo-alt-fill"></i> Kecamatan di {{ $kecamatanData['kabkot']['name'] }}
                                </span>
                            </div>
                            <h2 style="font-size: 1.4rem; font-weight: 800; color: #0a192f; margin: 0;">
                                Pilih Kecamatan Lain di {{ $kecamatanData['kabkot']['name'] }}
                            </h2>
                        </div>
                        <a href="{{ route('wilayah.provinsi', $kecamatanData['province']['slug']) }}" style="font-size: 0.82rem; color: #475569; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
                            <i class="bi bi-globe"></i> Semua Kota di {{ $kecamatanData['province']['name'] }}
                        </a>
                    </div>

                    <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin-bottom: 20px;">
                        Beralih ke kecamatan lain di lingkungan {{ $kecamatanData['kabkot']['name'] }} untuk melihat jadwal pelatihan Jasa SLO Ketenagalistrikan, silabus, dan kontak pendaftaran terdekat:
                    </p>

                    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 10px;">
                        @foreach($kecamatanList as $kec)
                            @php
                                $kecSlug = Str::slug($kec);
                                $isCurrent = ($kecSlug === $kecamatanData['slug']);
                                $kecUrl = route('wilayah.kecamatan', [$kecamatanData['province']['slug'], $kecamatanData['kabkot']['slug'], $kecSlug]);
                            @endphp
                            <a href="{{ $kecUrl }}" style="padding: 10px 14px; border-radius: 8px; text-decoration: none; font-size: 0.86rem; font-weight: 700; display: flex; align-items: center; justify-content: space-between; border: 1px solid {{ $isCurrent ? '#10b981' : '#cbd5e1' }}; background: {{ $isCurrent ? '#ecfdf5' : '#ffffff' }}; color: {{ $isCurrent ? '#854d0e' : '#09392b' }};">
                                <span><i class="bi {{ $isCurrent ? 'bi-check-circle-fill' : 'bi-pin-map' }}" style="color: #10b981; margin-right: 6px;"></i> Kec. {{ $kec }}</span>
                                @if($isCurrent)
                                    <span style="font-size: 0.7rem; background: #10b981; color: #fff; padding: 2px 6px; border-radius: 4px;">Aktif</span>
                                @else
                                    <i class="bi bi-chevron-right" style="color: #94a3b8; font-size: 0.8rem;"></i>
                                @endif
                            </a>
                        @endforeach
                    </div>
                </div>
            @endif

            <!-- MODUL ARTIKEL PANDUAN KECAMATAN -->
            <div id="daftar-artikel" class="section-header" style="margin-top: 48px; text-align: left;">
                <span class="section-tag">Panduan Jasa SLO Ketenagalistrikan</span>
                <h2 class="section-title">Daftar Direktori Panduan Lengkap Jasa SLO Ketenagalistrikan di Kecamatan {{ $kecamatanData['name'] }}</h2>
                <p class="section-desc" style="margin-left: 0;">
                    Kumpulan panduan modul mendalam mencakup standar kompetensi personel rig, prosedur penutupan sumur cepat (shut-in), sistem pengendalian tekanan sumur (Manajemen Risiko K3), pengujian BOP bertekanan tinggi, dan keselamatan tempat kerja di Kecamatan {{ $kecamatanData['name'] }}, {{ $kecamatanData['kabkot']['name'] }}:
                </p>
            </div>

            <div class="articles-grid">
                @foreach($regionalArticles as $art)
                    @php
                        $artObj = (object)$art;
                        $artUrl = route('article.detail', $artObj->slug);
                    @endphp
                    <div class="article-card">
                        <div class="article-badge">
                            <i class="bi bi-bookmark-fill me-1"></i> Modul #{{ $loop->iteration }}
                        </div>
                        <h3 class="article-title">
                            <a href="{{ $artUrl }}">{{ $artObj->title }}</a>
                        </h3>
                        <p class="article-excerpt">
                            Panduan teknis dan standar operasional Jasa SLO Ketenagalistrikan di Kecamatan {{ $kecamatanData['name'] }}. Mengulas regulasi Standar Keselamatan Manajemen Keselamatan Kerja, Standar Manajemen Risiko K3 Internasional (IADC & ISO 45001), perhitungan keselamatan operasi tempat kerja dan penanganan pipa bor, serta sertifikasi kompetensi resmi.
                        </p>
                        <div class="article-footer">
                            <span><i class="bi bi-clock me-1"></i> {{ $artObj->read_time ?? 35 }} Menit Baca (Panduan Lengkap)</span>
                            <a href="{{ $artUrl }}" class="btn-link" style="color: #4c1d95; font-weight: 700;">
                                Baca Selengkapnya <i class="bi bi-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                @endforeach
            </div>

            <!-- GOOGLE MAPS EMBED -->
            <div style="margin-top: 64px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; padding: 24px; box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);">
                <h3 style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                    <i class="bi bi-map-fill text-success"></i> Peta Lokasi Wilayah Kecamatan {{ $kecamatanData['name'] }}, {{ $kecamatanData['kabkot']['name'] }}
                </h3>
                <p style="font-size: 0.86rem; color: #64748b; margin-bottom: 18px;">
                    Kami melayani pelatihan K3 K3 Corporate baik secara publik maupun in-house training langsung ke fasilitas perusahaan Anda di area Kecamatan {{ $kecamatanData['name'] }} dan sekitarnya.
                </p>
                <div style="width: 100%; height: 350px; border-radius: 12px; overflow: hidden; border: 1px solid #cbd5e1;">
                    <iframe src="{{ $mapUrl }}" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
            </div>
        </div>
    </section>

@endsection
