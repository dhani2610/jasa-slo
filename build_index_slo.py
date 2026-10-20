import os

index_path = r"c:\xampp\htdocs\web-pelatihan\jasa-slo\resources\views\front\index.blade.php"

index_blade_content = """@extends('layouts.front')

@section('title', 'Jasa SLO - Sertifikat Laik Operasi Ketenagalistrikan | Layanan Resmi Uji Komisioning')
@section('meta_description', 'Layanan resmi Jasa SLO (Sertifikat Laik Operasi), uji komisioning instalasi listrik tegangan rendah, tegangan menengah 20 kV, genset, PLTS, dan proteksi petir di 38 provinsi di Indonesia.')

@section('content')
    <!-- HERO SLIDER SECTION (TANPA FOTO - HIGH-TECH ELECTRICAL POWER GRID TELEMETRY & SLO CERTIFICATION HUD) -->
    <section class="gas-hero-wrapper" style="background: radial-gradient(circle at 80% 20%, rgba(29, 78, 216, 0.25) 0%, transparent 45%), radial-gradient(circle at 10% 80%, rgba(234, 179, 8, 0.15) 0%, transparent 50%), #0a192f; color: #ffffff; padding: 60px 0 70px; position: relative; overflow: hidden;">
        <!-- Background Grid Pattern -->
        <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 36px 36px; pointer-events: none;"></div>

        <div class="container" style="position: relative; z-index: 2;">
            
            <!-- Hero Slider Container -->
            <div class="hero-slider-container" id="heroSlider" style="position: relative; min-height: 480px;">
                
                <!-- SLIDE 1: Jasa SLO Instalasi Pemanfaatan Tenaga Listrik TR & TM -->
                <div class="hero-slide active" data-slide="1" style="display: block; transition: all 0.5s ease;">
                    <div class="hero-slide-grid" style="display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 40px; align-items: center;">
                        <div>
                            <div class="hero-badge" style="background: rgba(29, 78, 216, 0.2); border: 1px solid rgba(56, 189, 248, 0.5); color: #38bdf8; font-size: 0.78rem; font-weight: 800; padding: 6px 16px; border-radius: 30px; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px;">
                                <i class="bi bi-patch-check-fill" style="color: #facc15;"></i> Lembaga Inspeksi Teknik SLO Terakreditasi Resmi
                            </div>

                            <h1 style="font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 18px; color: #ffffff; letter-spacing: -0.5px;">
                                Layanan Resmi <span style="background: linear-gradient(135deg, #38bdf8 0%, #facc15 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Jasa SLO & Sertifikat Laik Operasi</span> Ketenagalistrikan
                            </h1>

                            <p style="font-size: 1.02rem; color: #cbd5e1; line-height: 1.7; margin-bottom: 28px; max-width: 620px;">
                                Melayani pemeriksaan teknis, uji komisioning, pengukuran tahanan isolasi & pembumian (grounding), serta penerbitan Sertifikat Laik Operasi (SLO) sah untuk instalasi listrik tegangan rendah (TR), tegangan menengah (TM 20 kV), pembangkit genset, dan PLTS atap industri di seluruh Indonesia.
                            </p>

                            <div style="display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 32px;">
                                <a href="https://api.whatsapp.com/send?phone=6281399810272&text={{ urlencode('Halo Admin Utama Jasa SLO Indonesia, saya ingin konsultasi pengurusan Sertifikat Laik Operasi (SLO) resmi.') }}" target="_blank" class="btn-primary-green" style="background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%); border: 1px solid #facc15; box-shadow: 0 4px 18px rgba(29, 78, 216, 0.45); color: #ffffff; font-weight: 700; padding: 12px 24px; border-radius: 50px; display: inline-flex; align-items: center; gap: 10px; text-decoration: none;">
                                    <i class="bi bi-whatsapp" style="color: #25d366;"></i> Hotline Utama: 0813-9981-0272
                                </a>
                                <a href="#program" class="btn-outline-white" style="border: 1px solid rgba(255,255,255,0.25); background: rgba(255,255,255,0.06); color: #ffffff; font-weight: 700; padding: 12px 22px; border-radius: 50px; display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">
                                    <i class="bi bi-grid-fill" style="color: #facc15;"></i> 8 Layanan Jasa SLO
                                </a>
                            </div>

                            <div style="display: flex; align-items: center; gap: 24px; color: #94a3b8; font-size: 0.85rem; flex-wrap: wrap;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #facc15;"></i> Sertifikat SLO Berbarcode Sah
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #facc15;"></i> Inspektur Teknik Bersertifikat SKTTK
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #facc15;"></i> Instrumen Uji Terkalibrasi KAN
                                </div>
                            </div>
                        </div>

                        <!-- SIMULATED ELECTRICAL POWER GRID & SLO TELEMETRY HUD -->
                        <div>
                            <div style="background: linear-gradient(145deg, #0f2744 0%, #0a192f 100%); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.1); position: relative;">
                                <!-- Top Status Bar -->
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.12); padding-bottom: 12px; margin-bottom: 18px;">
                                    <div style="display: flex; align-items: center; gap: 8px;">
                                        <span style="display: inline-block; width: 10px; height: 10px; background: #facc15; border-radius: 50%; box-shadow: 0 0 10px #facc15; animation: pulse 2s infinite;"></span>
                                        <span style="font-size: 0.78rem; font-weight: 800; color: #93c5fd; text-transform: uppercase; letter-spacing: 0.8px;">LIVE ELECTRICAL GRID & SLO TELEMETRY</span>
                                    </div>
                                    <span style="font-size: 0.72rem; background: rgba(34, 197, 94, 0.2); color: #86efac; padding: 3px 10px; border-radius: 12px; border: 1px solid rgba(34, 197, 94, 0.4); font-weight: 700;">LAIK OPERASI &bull; 100% PUIL COMPLIANT</span>
                                </div>

                                <!-- Metric Cards Grid -->
                                <div class="hud-metrics-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px;">
                                    <div style="background: rgba(10, 25, 47, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #93c5fd; text-transform: uppercase; margin-bottom: 4px;">Frekuensi Jaringan Listrik</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #38bdf8;">50.00 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">Hz</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Stabil &bull; Standar Nominal</div>
                                    </div>

                                    <div style="background: rgba(10, 25, 47, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #93c5fd; text-transform: uppercase; margin-bottom: 4px;">Tahanan Pembumian (Grounding)</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #facc15;">0.38 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">&Omega;</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Lulus Uji (&lt; 5.0 &Omega; PUIL)</div>
                                    </div>

                                    <div style="background: rgba(10, 25, 47, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #93c5fd; text-transform: uppercase; margin-bottom: 4px;">Tahanan Isolasi Kabel (Megger)</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #38bdf8;">&gt; 500 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">M&Omega;</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Sangat Baik &bull; Bebas Bocor</div>
                                    </div>

                                    <div style="background: rgba(10, 25, 47, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #93c5fd; text-transform: uppercase; margin-bottom: 4px;">Kesehatan Dielektrik Trafo</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #facc15;">99.8 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">%</span></div>
                                        <div style="font-size: 0.68rem; color: #86efac; margin-top: 2px;">Breakdown Voltage 68 kV</div>
                                    </div>
                                </div>

                                <!-- Real-time Telemetry Live Feed -->
                                <div style="background: rgba(6, 15, 29, 0.85); border-radius: 10px; padding: 12px; font-family: monospace; font-size: 0.75rem; color: #cbd5e1; border: 1px solid rgba(255,255,255,0.08);">
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                        <span style="color: #93c5fd;">[INSPECTION-SLO]</span>
                                        <span style="color: #facc15;">18.500+ SERTIFIKAT TERBIT</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                                        <span>Status Proteksi Relai:</span>
                                        <span style="color: #86efac;">COORDINATED (OCR/GFR)</span>
                                    </div>
                                    <div style="display: flex; justify-content: space-between;">
                                        <span>Hasil Termografi Scan:</span>
                                        <span style="color: #86efac;">ZERO THERMAL HOTSPOT</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Hotlines Bar -->
            <div style="margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 0.85rem; color: #94a3b8; font-weight: 600;">Layanan Cepat Tanggap 24 Jam:</span>
                    <span style="font-size: 0.85rem; color: #facc15; font-weight: 800;">4 Hotline WhatsApp Resmi SLO Terverifikasi</span>
                </div>
                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                    @foreach($waNumbers as $num)
                        <a href="{{ $num['url'] }}" target="_blank" style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #ffffff; padding: 6px 14px; border-radius: 8px; font-size: 0.78rem; font-weight: 700; text-decoration: none; display: inline-flex; align-items: center; gap: 6px; transition: all 0.2s ease;">
                            <i class="bi bi-whatsapp" style="color: #25d366;"></i> {{ $num['number'] }}
                        </a>
                    @endforeach
                </div>
            </div>

        </div>
    </section>

    <!-- SECTION 2: 3-TIER CASCADE REGION SELECTOR (PROVINSI -> KABKOT -> KECAMATAN) -->
    <section class="section-py" id="wilayah" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe;">
                    <i class="bi bi-geo-alt-fill" style="color: #eab308;"></i> Jangkauan Seluruh Indonesia
                </span>
                <h2 class="section-title">Pilih Wilayah Layanan Jasa SLO & Sertifikasi Listrik</h2>
                <p class="section-desc">
                    Pilih Provinsi, Kabupaten/Kota, hingga Kecamatan Anda untuk mengakses informasi persyaratan, jadwal inspeksi teknisi kelaikan operasi, dan katalog artikel teknis setempat.
                </p>
            </div>

            <!-- Interactive 3-Tier Cascade Dropdown Card -->
            <div style="max-width: 960px; margin: 0 auto; background: linear-gradient(145deg, #0f2744 0%, #0a192f 100%); border: 2px solid #bfdbfe; border-radius: 20px; padding: 36px; box-shadow: 0 12px 30px rgba(15, 39, 68, 0.15); color: #ffffff;">
                <div style="text-align: center; margin-bottom: 24px;">
                    <h3 style="font-size: 1.25rem; font-weight: 800; color: #ffffff; margin-bottom: 6px;">
                        <i class="bi bi-compass-fill" style="color: #facc15; margin-right: 8px;"></i> Navigasi Cepat Wilayah SLO
                    </h3>
                    <p style="font-size: 0.88rem; color: #cbd5e1;">Tersedia lengkap di 38 Provinsi, 514 Kabupaten/Kota, dan ribuan Kecamatan se-Indonesia:</p>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 24px;">
                    <!-- Dropdown 1: Provinsi -->
                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #93c5fd; text-transform: uppercase; margin-bottom: 8px; display: block;">1. Pilih Provinsi:</label>
                        <select id="provinsiSelect" style="width: 100%; padding: 12px 14px; border-radius: 10px; background: #ffffff; color: #0f172a; font-weight: 600; font-size: 0.9rem; border: 2px solid #38bdf8; outline: none; cursor: pointer;">
                            <option value="">-- Pilih Salah Satu Provinsi --</option>
                            @foreach($provinces as $prov)
                                <option value="{{ $prov['slug'] }}">{{ $prov['name'] }}</option>
                            @endforeach
                        </select>
                    </div>

                    <!-- Dropdown 2: Kab/Kota -->
                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #93c5fd; text-transform: uppercase; margin-bottom: 8px; display: block;">2. Pilih Kabupaten / Kota:</label>
                        <select id="kabkotSelect" disabled style="width: 100%; padding: 12px 14px; border-radius: 10px; background: #e2e8f0; color: #475569; font-weight: 600; font-size: 0.9rem; border: 2px solid #94a3b8; outline: none; cursor: not-allowed;">
                            <option value="">-- Pilih Provinsi Dahulu --</option>
                        </select>
                    </div>

                    <!-- Dropdown 3: Kecamatan -->
                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #93c5fd; text-transform: uppercase; margin-bottom: 8px; display: block;">3. Pilih Kecamatan:</label>
                        <select id="kecamatanSelect" disabled style="width: 100%; padding: 12px 14px; border-radius: 10px; background: #e2e8f0; color: #475569; font-weight: 600; font-size: 0.9rem; border: 2px solid #94a3b8; outline: none; cursor: not-allowed;">
                            <option value="">-- Pilih Kab/Kota Dahulu --</option>
                        </select>
                    </div>
                </div>

                <div style="text-align: center;">
                    <button id="btnGoWilayah" disabled style="background: linear-gradient(135deg, #facc15 0%, #eab308 100%); color: #0f172a; font-weight: 800; font-size: 0.95rem; padding: 12px 32px; border-radius: 50px; border: none; cursor: not-allowed; opacity: 0.6; display: inline-flex; align-items: center; gap: 8px; transition: all 0.25s ease;">
                        <i class="bi bi-arrow-right-circle-fill"></i> Buka Halaman Wilayah Terpilih
                    </button>
                </div>
            </div>

            <!-- Quick Province Grid Pills -->
            <div style="margin-top: 40px;">
                <div style="font-size: 0.85rem; font-weight: 700; color: #64748b; text-transform: uppercase; text-align: center; margin-bottom: 16px;">
                    Akses Cepat 38 Provinsi Utama di Indonesia:
                </div>
                <div style="display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; max-width: 1100px; margin: 0 auto;">
                    @foreach($provinces as $prov)
                        <a href="{{ route('wilayah.provinsi', $prov['slug']) }}" style="background: #f1f5f9; color: #1e3a8a; border: 1px solid #cbd5e1; padding: 6px 14px; border-radius: 20px; font-size: 0.78rem; font-weight: 700; text-decoration: none; transition: all 0.2s ease;">
                            {{ $prov['name'] }}
                        </a>
                    @endforeach
                </div>
            </div>

        </div>
    </section>

    <!-- SECTION 3: 8 LAYANAN RESMI JASA SLO KETENAGALISTRIKAN -->
    <section class="section-py" id="program" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe;">
                    <i class="bi bi-lightning-charge-fill" style="color: #eab308;"></i> Ruang Lingkup Layanan
                </span>
                <h2 class="section-title">8 Layanan Unggulan Jasa SLO & Sertifikasi Listrik</h2>
                <p class="section-desc">
                    Program komprehensif inspeksi teknik, pengujian komisioning, dan sertifikasi kelaikan operasi yang dirancang untuk menjawab kepatuhan regulasi keselamatan ketenagalistrikan serta proteksi aset fasilitas industri:
                </p>
            </div>

            <div class="programs-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 26px;">
                @foreach($programs as $prog)
                    @php
                        $progObj = is_array($prog) ? (object)$prog : $prog;
                        $slug = $progObj->slug ?? '';
                        $detailUrl = route('program.detail', $slug);
                        $directWa = "https://api.whatsapp.com/send?phone=6281399810272&text=" . urlencode("Halo Admin Jasa SLO Indonesia, saya ingin konsultasi layanan {$progObj->title}.");
                    @endphp
                    <div class="program-card" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 4px 14px rgba(29, 78, 216, 0.06); transition: transform 0.3s ease, box-shadow 0.3s ease;">
                        <div class="program-body" style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
                                <span style="background: #eff6ff; color: #1d4ed8; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 6px; text-transform: uppercase; border: 1px solid #bfdbfe;">
                                    {{ $progObj->badge ?? 'Layanan Resmi SLO' }}
                                </span>
                                <span style="font-size: 0.78rem; font-weight: 700; color: #64748b;">
                                    <i class="bi bi-clock-history" style="color: #eab308;"></i> {{ $progObj->duration ?? '3-7 Hari Kerja' }}
                                </span>
                            </div>

                            <h3 class="program-title" style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 10px; line-height: 1.4;">
                                <a href="{{ $detailUrl }}" style="color: inherit; text-decoration: none;">{{ $progObj->title }}</a>
                            </h3>

                            <p class="program-desc" style="font-size: 0.86rem; color: #64748b; line-height: 1.6; margin-bottom: 18px; flex-grow: 1;">
                                {{ Str::limit($progObj->short_description ?? ($progObj->full_description ?? ''), 130) }}
                            </p>

                            <div style="font-size: 0.78rem; color: #1e3a8a; background: #f0fdf4; border: 1px solid #bbf7d0; padding: 8px 12px; border-radius: 8px; margin-bottom: 18px;">
                                <strong><i class="bi bi-patch-check-fill" style="color: #16a34a;"></i> Output:</strong> {{ Str::limit($progObj->certification ?? 'Sertifikat Laik Operasi (SLO) Resmi & Berita Acara Uji', 75) }}
                            </div>

                            <div class="program-footer-btn" style="display: flex; gap: 8px; padding-top: 14px; border-top: 1px solid #f1f5f9;">
                                <a href="{{ $detailUrl }}" class="btn-card-detail" style="flex: 1; text-align: center; background: #f8fafc; color: #1e3a8a; padding: 9px 12px; border-radius: 8px; font-size: 0.82rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 6px; border: 1px solid #cbd5e1; text-decoration: none;">
                                    <i class="bi bi-info-circle"></i> Detail Teknis
                                </a>
                                <a href="{{ $directWa }}" target="_blank" class="btn-card-wa" style="flex: 1; text-align: center; background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%); color: #ffffff; padding: 9px 12px; border-radius: 8px; font-size: 0.82rem; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; gap: 6px; text-decoration: none; border: 1px solid #facc15;">
                                    <i class="bi bi-whatsapp" style="color: #facc15;"></i> Ajukan SLO
                                </a>
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>

            <div style="text-align: center; margin-top: 36px;">
                <a href="{{ route('programs') }}" style="background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%); color: #ffffff; padding: 12px 28px; border-radius: 50px; font-size: 0.88rem; font-weight: 800; display: inline-flex; align-items: center; gap: 8px; text-decoration: none; border: 1px solid #facc15; box-shadow: 0 4px 14px rgba(29, 78, 216, 0.25);">
                    <i class="bi bi-collection-fill" style="color: #facc15;"></i> Buka Katalog Seluruh 8 Layanan Jasa SLO
                </a>
            </div>
        </div>
    </section>

    <!-- SECTION 4: KEUNGGULAN (MODERN INTERACTIVE CARDS) -->
    <section class="section-py" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #fefce8; color: #ca8a04; border-color: #fef08a;">
                    <i class="bi bi-shield-check" style="color: #eab308;"></i> Mengapa Memilih Kami
                </span>
                <h2 class="section-title">Keunggulan Layanan Jasa SLO Ketenagalistrikan</h2>
                <p class="section-desc">
                    Kepercayaan lebih dari 1.500 korporasi nasional dan multinasional dibangun di atas integritas teknis, kecepatan proses, dan sertifikasi resmi berkekuatan hukum penuh.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(29, 78, 216, 0.1); color: #1d4ed8; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-patch-check-fill" style="color: #eab308;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 10px;">Lembaga Inspeksi Terakreditasi</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Sertifikat Laik Operasi (SLO) yang diterbitkan memiliki nomor register sah nasional, dilengkapi barcode validasi digital resmi untuk keperluan legalitas dan asuransi.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(29, 78, 216, 0.1); color: #1d4ed8; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-tools" style="color: #eab308;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 10px;">Instrumen Uji Digital Terkalibrasi</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Pengujian menggunakan peralatan mutakhir (Digital Megohmmeter, Earth Tester, Hi-Pot 20 kV, Thermal Imager, Power Quality Logger) berstatus kalibrasi laboratorium aktif.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(29, 78, 216, 0.1); color: #1d4ed8; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-people-fill" style="color: #eab308;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 10px;">Inspektur Berlisensi SKTTK</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Tim auditor dan inspektur teknik kami berlatar belakang sarjana teknik elektro dengan kualifikasi Tenaga Teknik Ketenagalistrikan (SKTTK) jenjang Madya dan Utama.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(29, 78, 216, 0.1); color: #1d4ed8; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-lightning-charge-fill" style="color: #eab308;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 10px;">Proses Cepat & Responsif</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Mekanisme pemeriksaan yang terstruktur memungkinkan penerbitan laporan hasil uji (LHPP) dan sertifikat SLO selesai dalam waktu 3 hingga 7 hari kerja pasca-uji lulus.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(29, 78, 216, 0.1); color: #1d4ed8; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-geo-alt-fill" style="color: #eab308;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 10px;">Cakupan 38 Provinsi Indonesia</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Jaringan perwakilan tim inspeksi teknik kami siap hadir langsung di lokasi pabrik, kawasan industri, pertambangan, dan gedung komersial Anda di seluruh Indonesia.
                    </p>
                </div>

                <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 28px; transition: all 0.3s ease;">
                    <div style="width: 48px; height: 48px; background: rgba(29, 78, 216, 0.1); color: #1d4ed8; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.4rem; margin-bottom: 18px;">
                        <i class="bi bi-fire" style="color: #eab308;"></i>
                    </div>
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: #0a192f; margin-bottom: 10px;">Mitigasi Kebakaran Listrik</h3>
                    <p style="font-size: 0.88rem; color: #64748b; line-height: 1.6;">
                        Inspeksi kami tidak hanya bertujuan pemenuhan syarat administratif, tetapi secara proaktif mendeteksi potensi bahaya korsleting guna mewujudkan Zero Electrical Fire.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- SECTION 5: ARTIKEL DAERAH (3 CARD DILIMIT) -->
    <section class="section-py" id="artikel" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe;">
                    <i class="bi bi-journal-text" style="color: #eab308;"></i> Publikasi Teknis & Panduan
                </span>
                <h2 class="section-title">Artikel & Panduan Sertifikasi Laik Operasi</h2>
                <p class="section-desc">
                    Rujukan teknis mendalam seputar regulasi keselamatan ketenagalistrikan, uji komisioning trafo, genset, dan instalasi pembumian berstandar PUIL nasional.
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 26px;">
                @foreach($articles as $art)
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 4px 14px rgba(0,0,0,0.04);">
                        <div style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                                <span style="background: #eff6ff; color: #1d4ed8; font-size: 0.72rem; font-weight: 800; padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">
                                    {{ $art->category ?? 'Jasa SLO' }}
                                </span>
                                <span style="font-size: 0.78rem; color: #64748b;">
                                    <i class="bi bi-clock"></i> {{ $art->read_time ?? 22 }} Menit Baca
                                </span>
                            </div>

                            <h3 style="font-size: 1.12rem; font-weight: 800; color: #0a192f; margin-bottom: 12px; line-height: 1.45;">
                                <a href="{{ route('article.detail', $art->slug) }}" style="color: inherit; text-decoration: none;">{{ $art->title }}</a>
                            </h3>

                            <p style="font-size: 0.86rem; color: #64748b; line-height: 1.6; margin-bottom: 20px; flex-grow: 1;">
                                {{ Str::limit($art->excerpt, 140) }}
                            </p>

                            <div style="padding-top: 14px; border-top: 1px solid #f1f5f9; display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-size: 0.78rem; font-weight: 700; color: #1e3a8a;">
                                    <i class="bi bi-person-fill" style="color: #eab308;"></i> {{ Str::limit($art->author ?? 'Tim Ahli SLO', 24) }}
                                </span>
                                <a href="{{ route('article.detail', $art->slug) }}" style="font-size: 0.82rem; font-weight: 800; color: #1d4ed8; display: inline-flex; align-items: center; gap: 4px; text-decoration: none;">
                                    Baca Panduan <i class="bi bi-arrow-right"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>

            <div style="text-align: center; margin-top: 36px;">
                <a href="{{ route('articles') }}" style="background: #ffffff; color: #1d4ed8; border: 2px solid #1d4ed8; padding: 12px 28px; border-radius: 50px; font-size: 0.88rem; font-weight: 800; display: inline-flex; align-items: center; gap: 8px; text-decoration: none;">
                    <i class="bi bi-newspaper" style="color: #eab308;"></i> Buka Seluruh Direktori Artikel Daerah
                </a>
            </div>
        </div>
    </section>

    <!-- SECTION 6: STATISTIK PENCAPAIAN KINERJA -->
    <section class="section-py" style="background: linear-gradient(145deg, #0a192f 0%, #0f2744 100%); color: #ffffff;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 26px; text-align: center;">
                @foreach($statistics as $stat)
                    <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 16px; padding: 32px 20px;">
                        <div style="font-size: 2.2rem; margin-bottom: 8px; color: #facc15;">
                            <i class="bi {{ $stat->icon ?? 'bi-patch-check-fill' }}"></i>
                        </div>
                        <div style="font-size: 2.35rem; font-weight: 800; color: #ffffff; margin-bottom: 6px; letter-spacing: -1px;">
                            {{ $stat->value }}
                        </div>
                        <div style="font-size: 0.95rem; font-weight: 800; color: #38bdf8; margin-bottom: 4px;">
                            {{ $stat->label }}
                        </div>
                        <div style="font-size: 0.78rem; color: #cbd5e1;">
                            {{ $stat->description }}
                        </div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- SECTION 7: MITRA KORPORAT & BUMN -->
    <section class="section-py" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header" style="margin-bottom: 36px;">
                <span class="section-tag" style="background: #eff6ff; color: #1d4ed8; border-color: #bfdbfe;">
                    <i class="bi bi-building-check" style="color: #eab308;"></i> Kepercayaan Industri
                </span>
                <h2 class="section-title">Mitra Sinergi Sektor Ketenagalistrikan & Industri</h2>
                <p class="section-desc">
                    Mendukung keandalan pasokan daya dan sertifikasi laik operasi di berbagai entitas BUMN, perusahaan multinasional, serta utilitas swasta nasional:
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
                @foreach($partners as $partner)
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; display: flex; flex-direction: column;">
                        <div style="font-weight: 800; color: #0a192f; font-size: 0.98rem; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
                            <i class="bi bi-check2-circle" style="color: #1d4ed8;"></i> {{ $partner['name'] }}
                        </div>
                        <div style="font-size: 0.78rem; color: #64748b; line-height: 1.5;">
                            {{ $partner['role'] }}
                        </div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- SECTION 8: FAQ ACCORDION -->
    <section class="section-py" style="background: #f8fafc;">
        <div class="container">
            <div class="section-header">
                <span class="section-tag" style="background: #fefce8; color: #ca8a04; border-color: #fef08a;">
                    <i class="bi bi-question-circle-fill" style="color: #eab308;"></i> Tanya Jawab Resmi
                </span>
                <h2 class="section-title">Pertanyaan Seputar Jasa SLO & Sertifikasi Listrik</h2>
                <p class="section-desc">
                    Informasi penting mengenai legalitas, persyaratan teknis, dan tahapan pengujian kelaikan operasi ketenagalistrikan:
                </p>
            </div>

            <div style="max-width: 820px; margin: 0 auto; display: flex; flex-direction: column; gap: 14px;">
                @foreach($faqs as $i => $faq)
                    <div style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 12px; padding: 20px 24px; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
                        <h3 style="font-size: 1.05rem; font-weight: 800; color: #0a192f; margin-bottom: 8px; display: flex; align-items: flex-start; gap: 10px;">
                            <span style="color: #1d4ed8; font-weight: 800;">Q{{ $i + 1 }}.</span>
                            <span>{{ $faq->question }}</span>
                        </h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.65; margin-left: 28px;">
                            {{ $faq->answer }}
                        </p>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- SCRIPT FOR 3-TIER CASCADE REGION SELECTOR -->
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const provincesData = @json($provinces);
            const provSelect = document.getElementById('provinsiSelect');
            const kabkotSelect = document.getElementById('kabkotSelect');
            const kecSelect = document.getElementById('kecamatanSelect');
            const btnGo = document.getElementById('btnGoWilayah');

            let currentProvSlug = '';
            let currentKabkotSlug = '';
            let currentKecSlug = '';

            provSelect.addEventListener('change', function () {
                currentProvSlug = this.value;
                kabkotSelect.innerHTML = '<option value="">-- Pilih Kabupaten / Kota --</option>';
                kecSelect.innerHTML = '<option value="">-- Pilih Kab/Kota Dahulu --</option>';
                kecSelect.disabled = true;
                kecSelect.style.cursor = 'not-allowed';
                kecSelect.style.background = '#e2e8f0';

                if (!currentProvSlug) {
                    kabkotSelect.disabled = true;
                    kabkotSelect.style.cursor = 'not-allowed';
                    kabkotSelect.style.background = '#e2e8f0';
                    btnGo.disabled = true;
                    btnGo.style.cursor = 'not-allowed';
                    btnGo.style.opacity = '0.6';
                    return;
                }

                const selectedProv = provincesData.find(p => p.slug === currentProvSlug);
                if (selectedProv && selectedProv.kabkot) {
                    selectedProv.kabkot.forEach(k => {
                        const opt = document.createElement('option');
                        opt.value = k.slug;
                        opt.textContent = k.name;
                        kabkotSelect.appendChild(opt);
                    });
                    kabkotSelect.disabled = false;
                    kabkotSelect.style.cursor = 'pointer';
                    kabkotSelect.style.background = '#ffffff';
                }

                btnGo.disabled = false;
                btnGo.style.cursor = 'pointer';
                btnGo.style.opacity = '1';
            });

            kabkotSelect.addEventListener('change', function () {
                currentKabkotSlug = this.value;
                kecSelect.innerHTML = '<option value="">-- Pilih Kecamatan --</option>';

                if (!currentKabkotSlug) {
                    kecSelect.disabled = true;
                    kecSelect.style.cursor = 'not-allowed';
                    kecSelect.style.background = '#e2e8f0';
                    return;
                }

                const selectedProv = provincesData.find(p => p.slug === currentProvSlug);
                if (selectedProv && selectedProv.kabkot) {
                    const selectedKab = selectedProv.kabkot.find(k => k.slug === currentKabkotSlug);
                    if (selectedKab && selectedKab.kecamatan) {
                        selectedKab.kecamatan.forEach(kc => {
                            const opt = document.createElement('option');
                            opt.value = kc.slug;
                            opt.textContent = kc.name;
                            kecSelect.appendChild(opt);
                        });
                        kecSelect.disabled = false;
                        kecSelect.style.cursor = 'pointer';
                        kecSelect.style.background = '#ffffff';
                    }
                }
            });

            kecSelect.addEventListener('change', function () {
                currentKecSlug = this.value;
            });

            btnGo.addEventListener('click', function () {
                if (currentKecSlug && currentKabkotSlug && currentProvSlug) {
                    window.location.href = `/wilayah/${currentProvSlug}/${currentKabkotSlug}/${currentKecSlug}`;
                } else if (currentKabkotSlug && currentProvSlug) {
                    window.location.href = `/wilayah/${currentProvSlug}/${currentKabkotSlug}`;
                } else if (currentProvSlug) {
                    window.location.href = `/wilayah/${currentProvSlug}`;
                }
            });
        });
    </script>
@endsection
"""

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_blade_content)

print("resources/views/front/index.blade.php written successfully for Jasa SLO!")
