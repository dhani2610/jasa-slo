import os

index_file_path = r"c:\xampp\htdocs\web-pelatihan\training-ahli-k3-umum-corp\resources\views\front\index.blade.php"

index_code = """@extends('layouts.front')

@section('title', 'Training Ahli K3 Umum Corporate | Pusat Pembinaan & Sertifikasi K3 Korporasi Resmi')
@section('meta_description', 'Lembaga pembinaan dan sertifikasi resmi Ahli K3 Umum Corporate, Audit SMK3 PP 50/2012 166 Kriteria, HIRADC, IBPPR, Investigasi Insiden SCAT, dan Tata Kelola P2K3 Perusahaan di Indonesia.')

@section('content')
    <!-- HERO SLIDER SECTION (TANPA FOTO - HIGH-TECH CORPORATE SAFETY KPI & TELEMETRY HUD) -->
    <section class="gas-hero-wrapper" style="background: radial-gradient(circle at 80% 20%, rgba(16, 185, 129, 0.22) 0%, transparent 45%), radial-gradient(circle at 10% 80%, rgba(249, 115, 22, 0.15) 0%, transparent 50%), #062e22; color: #ffffff; padding: 60px 0 70px; position: relative; overflow: hidden;">
        <!-- Background Grid Pattern -->
        <div style="position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px); background-size: 36px 36px; pointer-events: none;"></div>

        <div class="container" style="position: relative; z-index: 2;">
            
            <!-- Hero Slider Container -->
            <div class="hero-slider-container" id="heroSlider" style="position: relative; min-height: 480px;">
                
                <!-- SLIDE 1: Pembinaan Ahli K3 Umum Corporate -->
                <div class="hero-slide active" data-slide="1" style="display: block; transition: all 0.5s ease;">
                    <div class="hero-slide-grid">
                        <div>
                            <div class="hero-badge" style="background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.5); color: #6ee7b7; font-size: 0.78rem; font-weight: 800; padding: 6px 16px; border-radius: 30px; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px;">
                                <i class="bi bi-patch-check-fill"></i> Sertifikasi Ahli K3 Umum Corporate Resmi
                            </div>

                            <h1 style="font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 18px; color: #ffffff; letter-spacing: -0.5px;">
                                Training Pembinaan & Sertifikasi Resmi <span style="background: linear-gradient(135deg, #10b981 0%, #34d399 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Ahli K3 Umum Corporate</span>
                            </h1>

                            <p style="font-size: 1.02rem; color: #cbd5e1; line-height: 1.7; margin-bottom: 28px; max-width: 620px;">
                                Membina calon Ahli K3 Umum dan pengawas keselamatan kerja korporasi menguasai regulasi kepatuhan keselamatan kerja nasional, identifikasi bahaya HIRADC/IBPPR, penyusunan laporan triwulan P2K3, serta integrasi budaya K3 proaktif menuju Zero Harm.
                            </p>

                            <div style="display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 32px;">
                                <a href="https://api.whatsapp.com/send?phone=6281399810272&text={{ urlencode('Halo Admin Utama Training Ahli K3 Umum Corporate, saya ingin konsultasi pendaftaran resmi pembinaan Ahli K3 Umum Corporate.') }}" target="_blank" class="btn-primary-green" style="box-shadow: 0 4px 18px rgba(16, 185, 129, 0.45);">
                                    <i class="bi bi-whatsapp"></i> Hotline Utama: 0813-9981-0272
                                </a>
                                <a href="#program" class="btn-outline-white" style="border: 1px solid rgba(255,255,255,0.25); background: rgba(255,255,255,0.06);">
                                    <i class="bi bi-grid-fill"></i> 6 Program K3 Korporat
                                </a>
                            </div>

                            <div style="display: flex; align-items: center; gap: 24px; color: #94a3b8; font-size: 0.85rem; flex-wrap: wrap;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #10b981;"></i> Sertifikasi Lisensi K3 Sah
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #10b981;"></i> Instruktur Lead Auditor Senior
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #10b981;"></i> Simulasi Mock Audit Lapangan
                                </div>
                            </div>
                        </div>

                        <!-- SIMULATED CORPORATE SAFETY KPI HUD -->
                        <div>
                            <div style="background: linear-gradient(145deg, #09392b 0%, #062e22 100%); border: 2px solid rgba(16, 185, 129, 0.4); border-radius: 20px; padding: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.1); position: relative;">
                                <!-- Top Status Bar -->
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.12); padding-bottom: 12px; margin-bottom: 18px;">
                                    <div style="display: flex; align-items: center; gap: 8px;">
                                        <span style="display: inline-block; width: 10px; height: 10px; background: #10b981; border-radius: 50%; box-shadow: 0 0 10px #10b981; animation: pulse 2s infinite;"></span>
                                        <span style="font-size: 0.78rem; font-weight: 800; color: #a7f3d0; text-transform: uppercase; letter-spacing: 0.8px;">CORPORATE SAFETY TELEMETRY HUD</span>
                                    </div>
                                    <span style="font-size: 0.72rem; background: rgba(16, 185, 129, 0.25); color: #6ee7b7; padding: 3px 10px; border-radius: 12px; border: 1px solid rgba(16, 185, 129, 0.4); font-weight: 700;">ZERO LTI ACHIEVED &bull; AUDIT READY</span>
                                </div>

                                <!-- Metric Cards Grid -->
                                <div class="hud-metrics-grid">
                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #a7f3d0; text-transform: uppercase; margin-bottom: 4px;">Jam Kerja Selamat</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #10b981;">14,850,000 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">JAM</span></div>
                                        <div style="font-size: 0.68rem; color: #6ee7b7; margin-top: 2px;">Zero Lost Time Injury (LTI)</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #a7f3d0; text-transform: uppercase; margin-bottom: 4px;">Tingkat Frekuensi LTI</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #38bdf8;">0.00 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">LTIFR</span></div>
                                        <div style="font-size: 0.68rem; color: #bae6fd; margin-top: 2px;">Kategori World-Class Benchmark</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #a7f3d0; text-transform: uppercase; margin-bottom: 4px;">Kepatuhan SMK3 PP 50/2012</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #f97316;">166 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">KRITERIA</span></div>
                                        <div style="font-size: 0.68rem; color: #fed7aa; margin-top: 2px;">Persiapan Sertifikasi Bendera Emas</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #a7f3d0; text-transform: uppercase; margin-bottom: 4px;">Penyelesaian Bahaya</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #10b981;">99.4% <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">CLOSURE</span></div>
                                        <div style="font-size: 0.68rem; color: #6ee7b7; margin-top: 2px;">Mitigasi Bahaya HIRADC Tuntas</div>
                                    </div>
                                </div>

                                <!-- Lower Status Highlights -->
                                <div style="background: rgba(6, 46, 34, 0.5); border-radius: 10px; padding: 12px 14px; display: flex; justify-content: space-between; align-items: center; font-size: 0.78rem;">
                                    <span style="color: #cbd5e1;"><i class="bi bi-shield-check text-success"></i> Status Kelembagaan K3:</span>
                                    <span style="font-weight: 700; color: #6ee7b7;">KOMITE P2K3 AKTIF &bull; AUDIT COMPLIANCE TERVERIFIKASI</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- SLIDE 2: Audit SMK3 PP 50/2012 -->
                <div class="hero-slide" data-slide="2" style="display: none; transition: all 0.5s ease;">
                    <div class="hero-slide-grid">
                        <div>
                            <div class="hero-badge" style="background: rgba(249, 115, 22, 0.2); border: 1px solid rgba(249, 115, 22, 0.5); color: #fb923c; font-size: 0.78rem; font-weight: 800; padding: 6px 16px; border-radius: 30px; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px;">
                                <i class="bi bi-award-fill"></i> Standar Audit SMK3 166 Kriteria
                            </div>

                            <h1 style="font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 18px; color: #ffffff; letter-spacing: -0.5px;">
                                Audit SMK3 PP 50/2012: <span style="background: linear-gradient(135deg, #f97316 0%, #fb923c 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Persiapan Bendera Emas Korporat</span>
                            </h1>

                            <p style="font-size: 1.02rem; color: #cbd5e1; line-height: 1.7; margin-bottom: 28px; max-width: 620px;">
                                Pelatihan komprehensif bagi Auditor Internal SMK3 dan tim compliance korporasi untuk memverifikasi kesesuaian 12 elemen dan 166 kriteria, merancang dokumen bukti objektif, dan mengeliminasi temuan non-conformance.
                            </p>

                            <div style="display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 32px;">
                                <a href="https://api.whatsapp.com/send?phone=6281399810272&text={{ urlencode('Halo Tim Ahli K3 Umum Corporate, saya ingin konsultasi pelatihan persiapan Audit SMK3 PP 50/2012 166 Kriteria.') }}" target="_blank" class="btn-primary-green" style="background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);">
                                    <i class="bi bi-whatsapp"></i> Konsultasi Audit SMK3: 0813-9981-0272
                                </a>
                                <a href="{{ route('program.detail', 'training-audit-sistem-manajemen-k3-smk3-korporat-pp-50-2012') }}" class="btn-outline-white">
                                    <i class="bi bi-file-earmark-check"></i> Silabus 166 Kriteria
                                </a>
                            </div>

                            <div style="display: flex; align-items: center; gap: 24px; color: #94a3b8; font-size: 0.85rem; flex-wrap: wrap;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #f97316;"></i> 12 Elemen Lengkap SMK3
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #f97316;"></i> Template Audit Checklist
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #f97316;"></i> Simulasi Non-Conformance
                                </div>
                            </div>
                        </div>

                        <!-- SIMULATED AUDIT TELEMETRY -->
                        <div>
                            <div style="background: linear-gradient(145deg, #09392b 0%, #062e22 100%); border: 2px solid rgba(249, 115, 22, 0.4); border-radius: 20px; padding: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.55);">
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.12); padding-bottom: 12px; margin-bottom: 18px;">
                                    <div style="display: flex; align-items: center; gap: 8px;">
                                        <span style="display: inline-block; width: 10px; height: 10px; background: #f97316; border-radius: 50%; box-shadow: 0 0 10px #f97316;"></span>
                                        <span style="font-size: 0.78rem; font-weight: 800; color: #fed7aa; text-transform: uppercase; letter-spacing: 0.8px;">SMK3 AUDIT TELEMETRY</span>
                                    </div>
                                    <span style="font-size: 0.72rem; background: rgba(249, 115, 22, 0.2); color: #fb923c; padding: 3px 10px; border-radius: 12px; border: 1px solid rgba(249, 115, 22, 0.35); font-weight: 700;">GOLDEN FLAG PREDICTION: 97.4%</span>
                                </div>

                                <div class="hud-metrics-grid">
                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Kriteria Tingkat Lanjutan</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #f97316;">166 / 166</div>
                                        <div style="font-size: 0.68rem; color: #fb923c; margin-top: 2px;">Seluruh Elemen Terdokumentasi</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Hasil Penilaian Audit</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #10b981;">97.4%</div>
                                        <div style="font-size: 0.68rem; color: #6ee7b7; margin-top: 2px;">Kategori Memuaskan (Bendera Emas)</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Temuan Mayor</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #38bdf8;">0 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">TEMUAN</span></div>
                                        <div style="font-size: 0.68rem; color: #bae6fd; margin-top: 2px;">Zero Major Non-Conformance</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(249, 115, 22, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #fed7aa; text-transform: uppercase; margin-bottom: 4px;">Integrasi ISO 45001</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #10b981;">100%</div>
                                        <div style="font-size: 0.68rem; color: #6ee7b7; margin-top: 2px;">High Level Structure (HLS) Terpadu</div>
                                    </div>
                                </div>

                                <div style="background: rgba(6, 46, 34, 0.5); border-radius: 10px; padding: 12px 14px; display: flex; justify-content: space-between; align-items: center; font-size: 0.78rem;">
                                    <span style="color: #cbd5e1;"><i class="bi bi-patch-check text-warning"></i> Status Penilaian Audit Eksternal:</span>
                                    <span style="font-weight: 700; color: #fed7aa;">REKOMENDASI BENDERA EMAS &bull; SERTIFIKAT TINGKAT UTAMA</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- SLIDE 3: Manajemen Risiko HIRADC, IBPPR & P2K3 -->
                <div class="hero-slide" data-slide="3" style="display: none; transition: all 0.5s ease;">
                    <div class="hero-slide-grid">
                        <div>
                            <div class="hero-badge" style="background: rgba(56, 189, 248, 0.2); border: 1px solid rgba(56, 189, 248, 0.5); color: #38bdf8; font-size: 0.78rem; font-weight: 800; padding: 6px 16px; border-radius: 30px; display: inline-flex; align-items: center; gap: 8px; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.5px;">
                                <i class="bi bi-shield-slash-fill"></i> Manajemen Risiko HIRADC & IBPPR
                            </div>

                            <h1 style="font-size: 2.5rem; font-weight: 800; line-height: 1.2; margin-bottom: 18px; color: #ffffff; letter-spacing: -0.5px;">
                                Mitigasi Bahaya & Investigasi Insiden: <span style="background: linear-gradient(135deg, #38bdf8 0%, #10b981 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">RCA & SCAT Terpadu</span>
                            </h1>

                            <p style="font-size: 1.02rem; color: #cbd5e1; line-height: 1.7; margin-bottom: 28px; max-width: 620px;">
                                Tingkatkan kapabilitas tim K3 dalam identifikasi proaktif potensi bahaya kerja, penyusunan Job Safety Analysis (JSA), serta analisis mendalam akar masalah kecelakaan menggunakan metode SCAT dan Fishbone Diagram.
                            </p>

                            <div style="display: flex; flex-wrap: wrap; gap: 14px; margin-bottom: 32px;">
                                <a href="https://api.whatsapp.com/send?phone=6281399810272&text={{ urlencode('Halo Admin Training Ahli K3 Umum Corporate, saya ingin informasi modul manajemen risiko HIRADC dan investigasi insiden SCAT.') }}" target="_blank" class="btn-primary-green" style="background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);">
                                    <i class="bi bi-whatsapp"></i> Konsultasi HIRADC: 0813-9981-0272
                                </a>
                                <a href="{{ route('program.detail', 'training-manajemen-risiko-k3-korporasi-hiradc-ibppr') }}" class="btn-outline-white">
                                    <i class="bi bi-shield-exclamation"></i> Detail Modul HIRADC
                                </a>
                            </div>

                            <div style="display: flex; align-items: center; gap: 24px; color: #94a3b8; font-size: 0.85rem; flex-wrap: wrap;">
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #38bdf8;"></i> Matriks Risiko 5x5
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #38bdf8;"></i> Hierarki Pengendalian 5 Tingkat
                                </div>
                                <div style="display: flex; align-items: center; gap: 6px;">
                                    <i class="bi bi-check-circle-fill" style="color: #38bdf8;"></i> Incident Investigation Kit
                                </div>
                            </div>
                        </div>

                        <!-- SIMULATED RISK TELEMETRY -->
                        <div>
                            <div style="background: linear-gradient(145deg, #09392b 0%, #062e22 100%); border: 2px solid rgba(56, 189, 248, 0.4); border-radius: 20px; padding: 24px; box-shadow: 0 20px 40px rgba(0,0,0,0.55);">
                                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.12); padding-bottom: 12px; margin-bottom: 18px;">
                                    <div style="display: flex; align-items: center; gap: 8px;">
                                        <span style="display: inline-block; width: 10px; height: 10px; background: #38bdf8; border-radius: 50%; box-shadow: 0 0 10px #38bdf8;"></span>
                                        <span style="font-size: 0.78rem; font-weight: 800; color: #bae6fd; text-transform: uppercase; letter-spacing: 0.8px;">RISK MITIGATION TELEMETRY</span>
                                    </div>
                                    <span style="font-size: 0.72rem; background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 3px 10px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.35); font-weight: 700;">ALARP STATUS: FULLY ACHIEVED</span>
                                </div>

                                <div class="hud-metrics-grid">
                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #bae6fd; text-transform: uppercase; margin-bottom: 4px;">Bahaya Teridentifikasi</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #38bdf8;">1,420 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">TITIK</span></div>
                                        <div style="font-size: 0.68rem; color: #bae6fd; margin-top: 2px;">Pemetaan Area Operasional Menyeluruh</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #bae6fd; text-transform: uppercase; margin-bottom: 4px;">Residual Risk Level</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #10b981;">LOW <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">ALARP</span></div>
                                        <div style="font-size: 0.68rem; color: #6ee7b7; margin-top: 2px;">Tingkat Risiko Diterima & Terkendali</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #bae6fd; text-transform: uppercase; margin-bottom: 4px;">SCAT Incident Closure</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #f97316;">100%</div>
                                        <div style="font-size: 0.68rem; color: #fed7aa; margin-top: 2px;">Tindakan Perbaikan Tuntas Tepat Waktu</div>
                                    </div>

                                    <div style="background: rgba(6, 46, 34, 0.7); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 14px;">
                                        <div style="font-size: 0.72rem; color: #bae6fd; text-transform: uppercase; margin-bottom: 4px;">Permit-to-Work (PTW)</div>
                                        <div style="font-size: 1.55rem; font-weight: 800; color: #10b981;">248 <span style="font-size: 0.8rem; font-weight: 600; color: #cbd5e1;">AKTIF</span></div>
                                        <div style="font-size: 0.68rem; color: #6ee7b7; margin-top: 2px;">Izin Kerja Berisiko Tinggi Terverifikasi</div>
                                    </div>
                                </div>

                                <div style="background: rgba(6, 46, 34, 0.5); border-radius: 10px; padding: 12px 14px; display: flex; justify-content: space-between; align-items: center; font-size: 0.78rem;">
                                    <span style="color: #cbd5e1;"><i class="bi bi-check-all text-success"></i> Status Mitigasi Bahaya Lapangan:</span>
                                    <span style="font-weight: 700; color: #bae6fd;">SISTEM KENDALI BERLAPIS AKTIF &bull; ZERO INCIDENT TARGET</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Slider Controls / Indicators -->
            <div style="display: flex; justify-content: center; align-items: center; gap: 12px; margin-top: 36px;">
                <button type="button" class="slider-dot active" data-target="1" style="width: 32px; height: 8px; border-radius: 4px; border: none; background: #10b981; cursor: pointer; transition: all 0.3s;"></button>
                <button type="button" class="slider-dot" data-target="2" style="width: 10px; height: 8px; border-radius: 4px; border: none; background: rgba(255,255,255,0.3); cursor: pointer; transition: all 0.3s;"></button>
                <button type="button" class="slider-dot" data-target="3" style="width: 10px; height: 8px; border-radius: 4px; border: none; background: rgba(255,255,255,0.3); cursor: pointer; transition: all 0.3s;"></button>
            </div>

        </div>
    </section>

    <!-- KEUNGGULAN SECTION (INTERACTIVE SLIDER / CAROUSEL) -->
    <section class="section-py" style="background: #ffffff; border-bottom: 1px solid #e2e8f0; position: relative;">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 38px;">
                <span class="section-tag">Keunggulan Lembaga Pelatihan K3</span>
                <h2 class="section-title">Mengapa 1.200+ Perusahaan Memilih Kami?</h2>
                <p class="section-desc" style="max-width: 760px; margin: 0 auto;">
                    Kami mengintegrasikan kepatuhan regulasi hukum keselamatan kerja dengan peningkatan efisiensi operasional dan pembentukan budaya K3 berkelas dunia:
                </p>
            </div>

            <!-- Keunggulan Carousel Slider Wrapper -->
            <div class="keunggulan-carousel-wrapper" style="position: relative;">
                <div class="keunggulan-track" id="keunggulanTrack" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
                    
                    <!-- Card 1 -->
                    <div class="keunggulan-card" style="background: #f0fdf4; border: 1px solid #a7f3d0; border-radius: 16px; padding: 26px 22px; transition: all 0.3s ease;">
                        <div style="width: 48px; height: 48px; background: #10b981; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 1.4rem; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);">
                            <i class="bi bi-file-earmark-check-fill"></i>
                        </div>
                        <h3 style="font-size: 1.12rem; font-weight: 800; color: #062e22; margin-bottom: 8px;">166 Kriteria Audit SMK3 & ISO 45001</h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">Kurikulum dirancang komprehensif mengacu pada 12 elemen dan 166 kriteria pemenuhan audit SMK3 PP 50/2012 serta keselarasan dengan sistem manajemen ISO 45001:2018.</p>
                    </div>

                    <!-- Card 2 -->
                    <div class="keunggulan-card" style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 16px; padding: 26px 22px; transition: all 0.3s ease;">
                        <div style="width: 48px; height: 48px; background: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 1.4rem; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(234, 88, 12, 0.35);">
                            <i class="bi bi-person-workspace"></i>
                        </div>
                        <h3 style="font-size: 1.12rem; font-weight: 800; color: #062e22; margin-bottom: 8px;">Instruktur Lead Auditor Berpengalaman</h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">Dipandu oleh praktisi HSE Director, mantan auditor SMK3 senior, serta konsultan manajemen risiko dengan rekam jejak puluhan tahun di industri manufaktur, tambang, dan migas.</p>
                    </div>

                    <!-- Card 3 -->
                    <div class="keunggulan-card" style="background: #f0fdf4; border: 1px solid #a7f3d0; border-radius: 16px; padding: 26px 22px; transition: all 0.3s ease;">
                        <div style="width: 48px; height: 48px; background: #059669; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 1.4rem; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(5, 150, 105, 0.35);">
                            <i class="bi bi-building-check"></i>
                        </div>
                        <h3 style="font-size: 1.12rem; font-weight: 800; color: #062e22; margin-bottom: 8px;">Simulasi Mock Audit & Plant Tour Nyata</h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">Peserta tidak hanya belajar teori, melainkan melakukan simulasi langsung inspeksi K3, penulisan laporan temuan bahaya, serta penyusunan corrective action plan siap pakai.</p>
                    </div>

                    <!-- Card 4 -->
                    <div class="keunggulan-card" style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 16px; padding: 26px 22px; transition: all 0.3s ease;">
                        <div style="width: 48px; height: 48px; background: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 1.4rem; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(234, 88, 12, 0.35);">
                            <i class="bi bi-patch-check-fill"></i>
                        </div>
                        <h3 style="font-size: 1.12rem; font-weight: 800; color: #062e22; margin-bottom: 8px;">Jaminan Legalitas & Lisensi Sah</h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">Sertifikat kompetensi resmi dengan verifikasi barcode online yang diakui penuh untuk pemenuhan syarat tender, pengangkatan Sekretaris P2K3, dan audit kepatuhan.</p>
                    </div>

                    <!-- Card 5 -->
                    <div class="keunggulan-card" style="background: #f0fdf4; border: 1px solid #a7f3d0; border-radius: 16px; padding: 26px 22px; transition: all 0.3s ease;">
                        <div style="width: 48px; height: 48px; background: #10b981; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 1.4rem; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);">
                            <i class="bi bi-geo-alt-fill"></i>
                        </div>
                        <h3 style="font-size: 1.12rem; font-weight: 800; color: #062e22; margin-bottom: 8px;">Layanan In-House ke 38 Provinsi</h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">Kami hadir langsung ke pabrik, kantor pusat, proyek konstruksi, dan fasilitas operasional klien di seluruh pelosok Indonesia dengan modul pelatihan yang dikustomisasi.</p>
                    </div>

                    <!-- Card 6 -->
                    <div class="keunggulan-card" style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 16px; padding: 26px 22px; transition: all 0.3s ease;">
                        <div style="width: 48px; height: 48px; background: #ea580c; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #ffffff; font-size: 1.4rem; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(234, 88, 12, 0.35);">
                            <i class="bi bi-headset"></i>
                        </div>
                        <h3 style="font-size: 1.12rem; font-weight: 800; color: #062e22; margin-bottom: 8px;">Pendampingan P2K3 Pasca Training</h3>
                        <p style="font-size: 0.88rem; color: #475569; line-height: 1.6; margin: 0;">Alumni mendapatkan fasilitas konsultasi lanjutan gratis untuk penyusunan format laporan triwulan P2K3, pemutakhiran matriks risiko, dan persiapan audit sertifikasi.</p>
                    </div>

                </div>
            </div>
        </div>
    </section>

    <!-- 6 PROGRAM RESMI K3 CORPORATE -->
    <section class="section-py" id="program" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 40px;">
                <span class="section-tag">Skema Pembinaan & Sertifikasi Resmi</span>
                <h2 class="section-title">6 Program Unggulan Ahli K3 Umum Corporate</h2>
                <p class="section-desc" style="max-width: 780px; margin: 0 auto;">
                    Program komprehensif yang dirancang untuk menjawab kebutuhan kepatuhan hukum, audit sertifikasi, dan perlindungan optimal aset serta tenaga kerja perusahaan:
                </p>
            </div>

            <div class="programs-grid">
                @foreach($programs as $prog)
                    <div class="program-card">
                        <div class="program-img-wrapper">
                            <img src="{{ $prog->image ?? 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&auto=format&fit=crop&q=80' }}" alt="{{ $prog->title }}" class="program-img" loading="lazy">
                            <span class="program-badge">{{ $prog->badge ?? 'Sertifikasi Resmi' }}</span>
                        </div>

                        <div class="program-body">
                            <div class="program-level">{{ $prog->level_name ?? 'Jenjang Korporasi Utama' }}</div>
                            <h3 class="program-title">{{ $prog->title }}</h3>
                            <p class="program-desc">
                                {{ Str::limit($prog->short_description ?? ($prog->full_description ?? ''), 130) }}
                            </p>

                            <div class="program-meta">
                                <div><i class="bi bi-clock-history" style="color: #10b981;"></i> {{ $prog->duration ?? '12 Hari' }}</div>
                                <div><i class="bi bi-mortarboard-fill" style="color: #10b981;"></i> {{ $prog->method ?? 'In-House & Public' }}</div>
                            </div>

                            <div class="program-footer-btn">
                                <a href="{{ route('program.detail', $prog->slug) }}" class="btn-primary-green" style="width: 100%; justify-content: center; font-size: 0.88rem; padding: 11px 16px;">
                                    <i class="bi bi-info-circle-fill"></i> Detail Program & Silabus
                                </a>
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- STATISTIK (DIBIKIN KEREN DENGAN GLOW HIJAU MUDA & SLATE DARK) -->
    <section class="section-py" style="background: linear-gradient(135deg, #062e22 0%, #09392b 50%, #0d4a39 100%); color: #ffffff; position: relative;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px;">
                @foreach($statistics as $stat)
                    <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 18px; padding: 28px 22px; text-align: center; position: relative; overflow: hidden; backdrop-filter: blur(8px);">
                        <div style="width: 56px; height: 56px; background: rgba(16, 185, 129, 0.2); border-radius: 14px; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; color: #34d399; font-size: 1.6rem; border: 1px solid rgba(16, 185, 129, 0.4);">
                            <i class="bi {{ $stat->icon ?? 'bi-bar-chart-fill' }}"></i>
                        </div>
                        <div style="font-size: 2.6rem; font-weight: 800; color: #34d399; line-height: 1; margin-bottom: 8px; letter-spacing: -1px;">
                            {{ $stat->value }}
                        </div>
                        <h4 style="font-size: 1.05rem; font-weight: 700; color: #ffffff; margin-bottom: 6px;">{{ $stat->label }}</h4>
                        <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.5; margin: 0;">{{ $stat->description }}</p>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- OUR PARTNER / KLIEN PERUSAHAAN KORPORASI -->
    <section class="section-py" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 34px;">
                <span class="section-tag">Kemitraan Korporasi Nasional</span>
                <h2 class="section-title">Dipercaya Pemimpin Industri & Korporasi Multinasional</h2>
                <p class="section-desc" style="max-width: 760px; margin: 0 auto;">
                    Kami bangga mendampingi implementasi keselamatan kerja, sertifikasi personel Ahli K3, dan audit SMK3 di berbagai perusahaan terkemuka di Indonesia:
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px;">
                @foreach($partners as $partner)
                    <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px 16px; text-align: center; transition: all 0.25s ease;">
                        <div style="font-size: 1rem; font-weight: 800; color: #062e22; margin-bottom: 4px;">{{ $partner['name'] }}</div>
                        <div style="font-size: 0.74rem; color: #059669; font-weight: 600;">{{ $partner['role'] }}</div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>

    <!-- KREDIBILITAS & PENGALAMAN (DIKEMAS KEREN & ELEGAN) -->
    <section class="section-py" style="background: #f0fdf4; border-bottom: 1px solid #a7f3d0;">
        <div class="container">
            <div class="kredibilitas-grid">
                <div>
                    <span class="section-tag" style="background: #ecfdf5; color: #064e3b; border: 1px solid #a7f3d0;">Kredibilitas & Pengalaman Teruji</span>
                    <h2 class="section-title" style="text-align: left;">Integritas, Pengalaman & Standar Keunggulan K3 Korporat</h2>
                    <p style="font-size: 0.95rem; color: #475569; line-height: 1.7; margin-bottom: 22px;">
                        Lembaga Training Ahli K3 Umum Corporate didirikan dengan visi mentransformasikan kepatuhan keselamatan kerja menjadi keunggulan daya saing bisnis nyata bagi perusahaan. Dengan rekam jejak lebih dari 15 tahun, kami telah meluluskan lebih dari 24.500 praktisi dan auditor K3 di 38 provinsi di Indonesia.
                    </p>

                    <div style="display: flex; flex-direction: column; gap: 16px; margin-bottom: 28px;">
                        <div style="display: flex; gap: 14px; align-items: flex-start;">
                            <div style="width: 38px; height: 38px; background: #ecfdf5; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #059669; font-size: 1.2rem; flex-shrink: 0; border: 1px solid #a7f3d0;">
                                <i class="bi bi-shield-check"></i>
                            </div>
                            <div>
                                <h4 style="font-size: 0.98rem; font-weight: 700; color: #062e22; margin-bottom: 3px;">Kesesuaian Regulasi Nasional & Standar ISO 45001</h4>
                                <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5; margin: 0;">Kurikulum pelatihan mengacu langsung pada undang-undang keselamatan kerja, 166 kriteria SMK3 PP 50/2012, serta integrasi High Level Structure ISO 45001.</p>
                            </div>
                        </div>

                        <div style="display: flex; gap: 14px; align-items: flex-start;">
                            <div style="width: 38px; height: 38px; background: #ecfdf5; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #059669; font-size: 1.2rem; flex-shrink: 0; border: 1px solid #a7f3d0;">
                                <i class="bi bi-qr-code-scan"></i>
                            </div>
                            <div>
                                <h4 style="font-size: 0.98rem; font-weight: 700; color: #062e22; margin-bottom: 3px;">Sertifikasi & Lisensi Resmi Terverifikasi Online</h4>
                                <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5; margin: 0;">Sertifikat kelulusan dilengkapi nomor registrasi resmi dan barcode verifikasi mandiri untuk memudahkan pengecekan oleh auditor, manajemen, dan divisi HRD.</p>
                            </div>
                        </div>

                        <div style="display: flex; gap: 14px; align-items: flex-start;">
                            <div style="width: 38px; height: 38px; background: #ecfdf5; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #059669; font-size: 1.2rem; flex-shrink: 0; border: 1px solid #a7f3d0;">
                                <i class="bi bi-award-fill"></i>
                            </div>
                            <div>
                                <h4 style="font-size: 0.98rem; font-weight: 700; color: #062e22; margin-bottom: 3px;">Instruktur Bersertifikasi Lead Auditor & Master Trainer</h4>
                                <p style="font-size: 0.84rem; color: #64748b; line-height: 1.5; margin: 0;">Didukung oleh jajaran instruktur senior berkualifikasi Lead Auditor SMK3, konsultan risiko industri, dan praktisi HSE yang aktif di korporasi terkemuka.</p>
                            </div>
                        </div>
                    </div>

                    <a href="{{ route('about') }}" class="btn-primary-green">
                        <i class="bi bi-info-circle-fill"></i> Profil Lengkap & Visi Misi Lembaga
                    </a>
                </div>

                <!-- Showcase Credibility Card -->
                <div>
                    <div style="background: #ffffff; border: 2px solid #a7f3d0; border-radius: 20px; padding: 32px; box-shadow: 0 16px 36px -4px rgba(16, 185, 129, 0.15);">
                        <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #e2e8f0; padding-bottom: 16px; margin-bottom: 20px;">
                            <div style="display: flex; align-items: center; gap: 10px;">
                                <i class="bi bi-patch-check-fill" style="color: #10b981; font-size: 1.8rem;"></i>
                                <div>
                                    <h4 style="font-size: 1.05rem; font-weight: 800; color: #062e22; margin: 0;">STANDAR AKREDITASI K3 KORPORASI</h4>
                                    <span style="font-size: 0.76rem; color: #64748b;">REGISTRASI: K3-CORP-CERT/2026</span>
                                </div>
                            </div>
                            <span style="background: #ecfdf5; color: #064e3b; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid #a7f3d0;">TERAKREDITASI</span>
                        </div>

                        <div style="display: flex; flex-direction: column; gap: 12px; font-size: 0.88rem; color: #334155;">
                            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px dashed #e2e8f0;">
                                <span style="color: #64748b;">Standar Audit K3:</span>
                                <strong style="color: #062e22;">SMK3 PP 50/2012 (166 Kriteria)</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px dashed #e2e8f0;">
                                <span style="color: #64748b;">Standar Manajemen Global:</span>
                                <strong style="color: #062e22;">ISO 45001:2018 Terpadu</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px dashed #e2e8f0;">
                                <span style="color: #64748b;">Metodologi Analisis Risiko:</span>
                                <strong style="color: #062e22;">HIRADC, IBPPR & JSA Komprehensif</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px dashed #e2e8f0;">
                                <span style="color: #64748b;">Sertifikat & Lisensi:</span>
                                <strong style="color: #10b981;">Resmi, Sah & Terverifikasi Barcode</strong>
                            </div>
                            <div style="display: flex; justify-content: space-between; padding: 8px 0;">
                                <span style="color: #64748b;">Cakupan Wilayah Layanan:</span>
                                <strong style="color: #062e22;">38 Provinsi Seluruh Indonesia</strong>
                            </div>
                        </div>

                        <div style="margin-top: 24px; padding: 14px; background: #ecfdf5; border-radius: 12px; text-align: center; border: 1px solid #a7f3d0;">
                            <span style="font-size: 0.82rem; color: #064e3b; font-weight: 700;">
                                <i class="bi bi-whatsapp me-1" style="color: #10b981;"></i> Konsultasi Program K3 Cepat WA: 0813-9981-0272
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- DIREKTORI WILAYAH 38 PROVINSI, KABUPATEN/KOTA & KECAMATAN LENGKAP -->
    <style>
        .wilayah-section-wrap {
            background: #ffffff;
            border-bottom: 1px solid #e2e8f0;
        }
        .island-tab-btn {
            padding: 8px 18px;
            border-radius: 30px;
            font-size: 0.82rem;
            font-weight: 700;
            border: 1px solid #cbd5e1;
            background: #f8fafc;
            color: #475569;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .island-tab-btn:hover {
            border-color: #10b981;
            color: #059669;
            background: #ecfdf5;
        }
        .island-tab-btn.active {
            background: #10b981;
            border-color: #10b981;
            color: #ffffff;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.35);
        }
        .home-province-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            overflow: hidden;
            transition: all 0.25s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.02);
            margin-bottom: 16px;
        }
        .home-province-card:hover {
            border-color: #a7f3d0;
            box-shadow: 0 4px 16px rgba(16, 185, 129, 0.08);
        }
        .prov-header-toggle {
            padding: 14px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            background: #f8fafc;
            border-bottom: 1px solid transparent;
            flex-wrap: wrap;
            gap: 10px;
            transition: background 0.2s ease;
        }
        .prov-header-toggle.is-open {
            background: #ecfdf5;
            border-bottom-color: #a7f3d0;
        }
        .prov-preview-bar {
            padding: 8px 18px;
            background: #ffffff;
            border-bottom: 1px solid #f1f5f9;
            font-size: 0.77rem;
            color: #64748b;
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 6px;
        }
        .prov-preview-tag {
            background: #f1f5f9;
            color: #334155;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.73rem;
            font-weight: 600;
        }
        .prov-drawer-body {
            padding: 18px;
            background: #ffffff;
            border-top: 1px solid #e2e8f0;
        }
        .kabkot-card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 12px;
        }
        .home-kabkot-box {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: all 0.2s ease;
        }
        .home-kabkot-box:hover {
            background: #ffffff;
            border-color: #a7f3d0;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.08);
        }
        .home-kec-pill {
            font-size: 0.72rem;
            color: #334155;
            background: #ffffff;
            border: 1px solid #cbd5e1;
            padding: 2px 7px;
            border-radius: 4px;
            text-decoration: none;
            transition: all 0.15s ease;
            display: inline-block;
        }
        .home-kec-pill:hover {
            border-color: #10b981;
            color: #059669;
            background: #ecfdf5;
        }
    </style>

    <section class="section-py wilayah-section-wrap" id="wilayah">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 32px;">
                <span class="section-tag">Jangkauan Layanan 38 Provinsi • 514 Kab/Kota • Seluruh Kecamatan</span>
                <h2 class="section-title">Direktori Wilayah Pelatihan Ahli K3 Umum Corporate</h2>
                <p class="section-desc" style="max-width: 840px; margin: 0 auto;">
                    Kami menyelenggarakan pelatihan reguler maupun in-house training sertifikasi Ahli K3 Umum Corporate di seluruh 38 provinsi di Indonesia hingga ke tingkat kabupaten, kota, dan kecamatan. Klik pada nama wilayah untuk melihat jadwal, kuota, dan panduan teknis spesifik di daerah Anda:
                </p>
            </div>

            @php
                // Build lightweight structure for Cascading Explorer & Live Search
                $regionsExplorerData = [];
                foreach($provinces as $pSlug => $pr) {
                    $kabkotItems = [];
                    foreach($pr['kabkot'] as $kk) {
                        $kabkotItems[] = [
                            'name' => $kk['name'],
                            'slug' => $kk['slug'],
                            'kecamatan' => $kk['kecamatan'] ?? []
                        ];
                    }
                    $regionsExplorerData[] = [
                        'name' => $pr['name'],
                        'slug' => $pr['slug'],
                        'island' => $pr['island'] ?? 'Lainnya',
                        'total_kabkot' => $pr['total_kabkot'] ?? count($kabkotItems),
                        'kabkot' => $kabkotItems
                    ];
                }
            @endphp

            <!-- 1. CASCADING REGION SELECTOR (PROVINSI -> KABKOT -> KECAMATAN) -->
            <div style="background: linear-gradient(135deg, #062e22 0%, #09392b 100%); border-radius: 16px; padding: 24px; margin-bottom: 28px; box-shadow: 0 10px 25px rgba(6, 46, 34, 0.2);">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px; color: #ffffff;">
                    <i class="bi bi-funnel-fill" style="color: #34d399; font-size: 1.25rem;"></i>
                    <h3 style="font-size: 1.1rem; font-weight: 800; margin: 0;">Pilih Cepat Wilayah Pelatihan (3 Tingkat Bertingkat)</h3>
                </div>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; align-items: end;">
                    <!-- Dropdown Provinsi -->
                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #a7f3d0; margin-bottom: 6px; display: block;">1. Pilih Provinsi:</label>
                        <select id="cascadeProvSelect" style="width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid #10b981; background: #ffffff; color: #0f172a; font-size: 0.86rem; font-weight: 600; outline: none;">
                            <option value="">-- Pilih Provinsi (38 Provinsi) --</option>
                            @foreach($regionsExplorerData as $p)
                                <option value="{{ $p['slug'] }}">{{ $p['name'] }} ({{ $p['total_kabkot'] }} Kab/Kota)</option>
                            @endforeach
                        </select>
                    </div>

                    <!-- Dropdown Kab/Kota -->
                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #a7f3d0; margin-bottom: 6px; display: block;">2. Pilih Kab/Kota:</label>
                        <select id="cascadeKabkotSelect" disabled style="width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid #cbd5e1; background: #f1f5f9; color: #64748b; font-size: 0.86rem; font-weight: 600; outline: none;">
                            <option value="">-- Pilih Kab/Kota Terlebih Dahulu --</option>
                        </select>
                    </div>

                    <!-- Dropdown Kecamatan -->
                    <div>
                        <label style="font-size: 0.78rem; font-weight: 700; color: #a7f3d0; margin-bottom: 6px; display: block;">3. Pilih Kecamatan:</label>
                        <select id="cascadeKecSelect" disabled style="width: 100%; padding: 10px 14px; border-radius: 8px; border: 1px solid #cbd5e1; background: #f1f5f9; color: #64748b; font-size: 0.86rem; font-weight: 600; outline: none;">
                            <option value="">-- Pilih Kecamatan Terlebih Dahulu --</option>
                        </select>
                    </div>

                    <!-- Tombol Eksekusi Buka Halaman Wilayah -->
                    <div>
                        <button type="button" id="btnGoToRegion" class="btn-primary-green" style="width: 100%; justify-content: center; padding: 10px 16px; font-size: 0.88rem; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4);">
                            <i class="bi bi-box-arrow-up-right"></i> Buka Panduan Daerah
                        </button>
                    </div>
                </div>
            </div>

            <!-- 2. TABS PULAU INDONESIA -->
            <div style="display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; margin-bottom: 28px;">
                <button type="button" class="island-tab-btn active" data-island="all">Semua Pulau (38)</button>
                <button type="button" class="island-tab-btn" data-island="Jawa">Jawa</button>
                <button type="button" class="island-tab-btn" data-island="Sumatera">Sumatera</button>
                <button type="button" class="island-tab-btn" data-island="Kalimantan">Kalimantan</button>
                <button type="button" class="island-tab-btn" data-island="Sulawesi">Sulawesi</button>
                <button type="button" class="island-tab-btn" data-island="Bali & Nusa Tenggara">Bali & Nusa Tenggara</button>
                <button type="button" class="island-tab-btn" data-island="Maluku & Papua">Maluku & Papua</button>
            </div>

            <!-- 3. ACCORDION 38 PROVINSI WITH FULL KABUPATEN, KOTA & KECAMATAN -->
            <div id="provincesAccordionContainer">
                @foreach($regionsExplorerData as $prov)
                    <div class="home-province-card" data-island="{{ $prov['island'] }}">
                        <div class="prov-header-toggle" onclick="toggleProvCard(this)">
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <div style="width: 38px; height: 38px; border-radius: 8px; background: #f0fdf4; border: 1px solid #a7f3d0; display: flex; align-items: center; justify-content: center; color: #059669; font-size: 1.15rem;">
                                    <i class="bi bi-geo-alt-fill"></i>
                                </div>
                                <div>
                                    <h3 style="font-size: 1.05rem; font-weight: 800; color: #0f172a; margin: 0;">
                                        {{ $prov['name'] }}
                                    </h3>
                                    <span style="font-size: 0.74rem; color: #64748b;">Pulau {{ $prov['island'] }} • {{ $prov['total_kabkot'] }} Kabupaten / Kota</span>
                                </div>
                            </div>

                            <div style="display: flex; align-items: center; gap: 10px;">
                                <a href="{{ route('wilayah.provinsi', $prov['slug']) }}" class="btn-primary-green" style="padding: 6px 14px; font-size: 0.76rem; border-radius: 20px;" onclick="event.stopPropagation();">
                                    <i class="bi bi-door-open-fill"></i> Detail Provinsi
                                </a>
                                <span class="badge-toggle-icon" style="font-size: 1.2rem; color: #64748b; transition: transform 0.2s;"><i class="bi bi-chevron-down"></i></span>
                            </div>
                        </div>

                        <!-- Mini Preview Tags -->
                        <div class="prov-preview-bar">
                            <span style="font-weight: 700; color: #059669; font-size: 0.74rem;">Daftar Kota:</span>
                            @foreach(array_slice($prov['kabkot'], 0, 6) as $kkPreview)
                                <a href="{{ route('wilayah.kabkot', [$prov['slug'], $kkPreview['slug']]) }}" class="prov-preview-tag">
                                    {{ $kkPreview['name'] }}
                                </a>
                            @endforeach
                            @if(count($prov['kabkot']) > 6)
                                <span style="font-size: 0.73rem; color: #94a3b8;">+{{ count($prov['kabkot']) - 6 }} lainnya...</span>
                            @endif
                        </div>

                        <!-- Drawer Body: Full Kab/Kota & Kecamatan Pills -->
                        <div class="prov-drawer-body" style="display: none;">
                            <div class="kabkot-card-grid">
                                @foreach($prov['kabkot'] as $kk)
                                    <div class="home-kabkot-box">
                                        <div style="margin-bottom: 8px;">
                                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                                <a href="{{ route('wilayah.kabkot', [$prov['slug'], $kk['slug']]) }}" style="font-size: 0.88rem; font-weight: 800; color: #062e22; text-decoration: none;">
                                                    <i class="bi bi-building" style="color: #10b981; margin-right: 4px;"></i> {{ $kk['name'] }}
                                                </a>
                                                <a href="{{ route('wilayah.kabkot', [$prov['slug'], $kk['slug']]) }}" style="font-size: 0.72rem; color: #059669; font-weight: 700; background: #ecfdf5; padding: 2px 8px; border-radius: 4px; text-decoration: none;">
                                                    Pilih Kota &rarr;
                                                </a>
                                            </div>

                                            <!-- Kecamatan Pills Under this Kab/Kota -->
                                            <div style="display: flex; flex-wrap: wrap; gap: 4px; margin-top: 6px;">
                                                @foreach(array_slice($kk['kecamatan'], 0, 8) as $kecName)
                                                    @php $kSlug = Str::slug($kecName); @endphp
                                                    <a href="{{ route('wilayah.kecamatan', [$prov['slug'], $kk['slug'], $kSlug]) }}" class="home-kec-pill" title="Kecamatan {{ $kecName }}">
                                                        {{ $kecName }}
                                                    </a>
                                                @endforeach
                                                @if(count($kk['kecamatan']) > 8)
                                                    <a href="{{ route('wilayah.kabkot', [$prov['slug'], $kk['slug']]) }}" class="home-kec-pill" style="background: #f1f5f9; color: #64748b;">
                                                        +{{ count($kk['kecamatan']) - 8 }} kec
                                                    </a>
                                                @endif
                                            </div>
                                        </div>
                                    </div>
                                @endforeach
                            </div>
                        </div>
                    </div>
                @endforeach
            </div>

        </div>
    </section>

    <!-- ARTIKEL DAERAH TERBARU (3 CARDS DILIMIT SESUAI INSTRUKSI) -->
    <section class="section-py" style="background: #ffffff; border-bottom: 1px solid #e2e8f0;">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 38px;">
                <span class="section-tag">Publikasi & Panduan Praktik</span>
                <h2 class="section-title">Wawasan & Panduan K3 Korporasi</h2>
                <p class="section-desc" style="max-width: 760px; margin: 0 auto;">
                    Artikel teknis komprehensif mengenai strategi keselamatan kerja, pemenuhan audit SMK3, metodologi identifikasi bahaya, dan investigasi insiden di berbagai sektor industri:
                </p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px; margin-bottom: 36px;">
                @foreach($articles as $art)
                    <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column; transition: all 0.25s ease; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                        <div style="height: 200px; overflow: hidden; position: relative;">
                            <img src="{{ $art->featured_image ?? 'https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=800&auto=format&fit=crop&q=80' }}" alt="{{ $art->title }}" style="width: 100%; height: 100%; object-fit: cover;" loading="lazy">
                            <span style="position: absolute; top: 12px; left: 12px; background: rgba(6, 46, 34, 0.85); color: #34d399; font-size: 0.74rem; font-weight: 700; padding: 4px 12px; border-radius: 20px; backdrop-filter: blur(4px);">
                                {{ $art->category ?? 'Ahli K3 Umum Corporate' }}
                            </span>
                        </div>

                        <div style="padding: 22px; display: flex; flex-direction: column; flex-grow: 1;">
                            <div style="display: flex; align-items: center; gap: 14px; font-size: 0.78rem; color: #64748b; margin-bottom: 10px;">
                                <span><i class="bi bi-clock"></i> {{ $art->read_time ?? 25 }} menit</span>
                                <span><i class="bi bi-eye"></i> {{ number_format($art->views_count ?? 150) }} dibaca</span>
                            </div>

                            <h3 style="font-size: 1.1rem; font-weight: 800; color: #062e22; line-height: 1.4; margin-bottom: 12px;">
                                <a href="{{ route('article.detail', $art->slug) }}" style="color: inherit; text-decoration: none;">
                                    {{ $art->title }}
                                </a>
                            </h3>

                            <p style="font-size: 0.86rem; color: #64748b; line-height: 1.6; margin-bottom: 18px; flex-grow: 1;">
                                {{ Str::limit($art->excerpt ?? strip_tags($art->content), 120) }}
                            </p>

                            <a href="{{ route('article.detail', $art->slug) }}" style="display: inline-flex; align-items: center; gap: 6px; color: #059669; font-weight: 700; font-size: 0.86rem; text-decoration: none;">
                                Baca Selengkapnya <i class="bi bi-arrow-right"></i>
                            </a>
                        </div>
                    </div>
                @endforeach
            </div>

            <div style="text-align: center;">
                <a href="{{ route('articles') }}" class="btn-outline-white" style="color: #062e22; border-color: #cbd5e1; background: #f8fafc; display: inline-flex; align-items: center; gap: 8px;">
                    <i class="bi bi-journals"></i> Buka Seluruh Arsip Artikel & Panduan
                </a>
            </div>
        </div>
    </section>

    <!-- FAQ SECTION (ACCORDION MODERN) -->
    <section class="section-py" style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
        <div class="container" style="max-width: 880px;">
            <div class="section-header" style="text-align: center; margin-bottom: 36px;">
                <span class="section-tag">Pertanyaan Sering Diajukan</span>
                <h2 class="section-title">Frequently Asked Questions (FAQ)</h2>
                <p class="section-desc">
                    Pertanyaan umum seputar pembinaan Ahli K3 Umum Corporate, audit SMK3, dan penyelenggaraan in-house training:
                </p>
            </div>

            <div class="faq-list">
                @foreach($faqs as $faq)
                    <div class="faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 12px; overflow: hidden; transition: all 0.2s ease;">
                        <div class="faq-question" style="padding: 18px 22px; font-weight: 700; font-size: 0.96rem; color: #062e22; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                            <span>{{ $faq->question }}</span>
                            <i class="bi bi-plus-lg faq-icon" style="color: #10b981; font-size: 1.1rem; transition: transform 0.2s;"></i>
                        </div>
                        <div class="faq-answer" style="padding: 0 22px 18px; font-size: 0.88rem; color: #475569; line-height: 1.7; display: none;">
                            {{ $faq->answer }}
                        </div>
                    </div>
                @endforeach
            </div>
        </div>
    </section>
@endsection

@push('scripts')
<script>
    // Hero Slider Auto & Manual Toggle
    let currentSlide = 1;
    const totalSlides = 3;
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.slider-dot');

    function goToSlide(n) {
        slides.forEach(s => s.style.display = 'none');
        dots.forEach(d => {
            d.style.background = 'rgba(255,255,255,0.3)';
            d.style.width = '10px';
        });

        const activeSlide = document.querySelector(`.hero-slide[data-slide="${n}"]`);
        const activeDot = document.querySelector(`.slider-dot[data-target="${n}"]`);

        if (activeSlide) activeSlide.style.display = 'block';
        if (activeDot) {
            activeDot.style.background = '#10b981';
            activeDot.style.width = '32px';
        }
        currentSlide = n;
    }

    dots.forEach(dot => {
        dot.addEventListener('click', () => {
            const target = parseInt(dot.getAttribute('data-target'));
            goToSlide(target);
        });
    });

    setInterval(() => {
        let next = currentSlide + 1;
        if (next > totalSlides) next = 1;
        goToSlide(next);
    }, 6500);

    // Island Tabs Filter
    const tabBtns = document.querySelectorAll('.island-tab-btn');
    const provCards = document.querySelectorAll('.home-province-card');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const island = btn.getAttribute('data-island');
            provCards.forEach(card => {
                if (island === 'all' || card.getAttribute('data-island') === island) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // Toggle Province Drawer
    function toggleProvCard(header) {
        const card = header.closest('.home-province-card');
        const drawer = card.querySelector('.prov-drawer-body');
        const icon = header.querySelector('.badge-toggle-icon');

        if (drawer.style.display === 'none' || !drawer.style.display) {
            drawer.style.display = 'block';
            header.classList.add('is-open');
            if (icon) icon.style.transform = 'rotate(180deg)';
        } else {
            drawer.style.display = 'none';
            header.classList.remove('is-open');
            if (icon) icon.style.transform = 'rotate(0deg)';
        }
    }

    // Cascading Region Selector
    const cascadeData = @json($regionsExplorerData);
    const provSelect = document.getElementById('cascadeProvSelect');
    const kabkotSelect = document.getElementById('cascadeKabkotSelect');
    const kecSelect = document.getElementById('cascadeKecSelect');
    const btnGo = document.getElementById('btnGoToRegion');

    let selectedProv = null;
    let selectedKab = null;
    let selectedKec = null;

    if (provSelect) {
        provSelect.addEventListener('change', function() {
            const pSlug = this.value;
            kabkotSelect.innerHTML = '<option value="">-- Pilih Kab/Kota --</option>';
            kecSelect.innerHTML = '<option value="">-- Pilih Kecamatan Terlebih Dahulu --</option>';
            kecSelect.disabled = true;
            kecSelect.style.background = '#f1f5f9';

            if (!pSlug) {
                kabkotSelect.disabled = true;
                kabkotSelect.style.background = '#f1f5f9';
                selectedProv = null;
                return;
            }

            selectedProv = cascadeData.find(item => item.slug === pSlug);
            if (selectedProv && selectedProv.kabkot) {
                selectedProv.kabkot.forEach(k => {
                    const opt = document.createElement('option');
                    opt.value = k.slug;
                    opt.textContent = k.name;
                    kabkotSelect.appendChild(opt);
                });
                kabkotSelect.disabled = false;
                kabkotSelect.style.background = '#ffffff';
                kabkotSelect.style.border = '1px solid #10b981';
            }
        });
    }

    if (kabkotSelect) {
        kabkotSelect.addEventListener('change', function() {
            const kSlug = this.value;
            kecSelect.innerHTML = '<option value="">-- Pilih Kecamatan --</option>';

            if (!kSlug || !selectedProv) {
                kecSelect.disabled = true;
                kecSelect.style.background = '#f1f5f9';
                selectedKab = null;
                return;
            }

            selectedKab = selectedProv.kabkot.find(item => item.slug === kSlug);
            if (selectedKab && selectedKab.kecamatan) {
                selectedKab.kecamatan.forEach(kec => {
                    const opt = document.createElement('option');
                    const cleanSlug = kec.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
                    opt.value = cleanSlug;
                    opt.textContent = kec;
                    kecSelect.appendChild(opt);
                });
                kecSelect.disabled = false;
                kecSelect.style.background = '#ffffff';
                kecSelect.style.border = '1px solid #10b981';
            }
        });
    }

    if (kecSelect) {
        kecSelect.addEventListener('change', function() {
            selectedKec = this.value;
        });
    }

    if (btnGo) {
        btnGo.addEventListener('click', function() {
            const pVal = provSelect ? provSelect.value : '';
            const kVal = kabkotSelect ? kabkotSelect.value : '';
            const cVal = kecSelect ? kecSelect.value : '';

            if (pVal && kVal && cVal) {
                window.location.href = `/wilayah/${pVal}/${kVal}/${cVal}`;
            } else if (pVal && kVal) {
                window.location.href = `/wilayah/${pVal}/${kVal}`;
            } else if (pVal) {
                window.location.href = `/wilayah/${pVal}`;
            } else {
                alert('Silakan pilih minimal Provinsi terlebih dahulu.');
            }
        });
    }

    // FAQ Accordion
    document.querySelectorAll('.faq-question').forEach(q => {
        q.addEventListener('click', () => {
            const item = q.parentElement;
            const ans = item.querySelector('.faq-answer');
            const icon = q.querySelector('.faq-icon');

            if (ans.style.display === 'block') {
                ans.style.display = 'none';
                icon.className = 'bi bi-plus-lg faq-icon';
            } else {
                ans.style.display = 'block';
                icon.className = 'bi bi-dash-lg faq-icon';
            }
        });
    });
</script>
@endpush
"""

with open(index_file_path, "w", encoding="utf-8") as f:
    f.write(index_code)

print("front/index.blade.php written successfully!")
