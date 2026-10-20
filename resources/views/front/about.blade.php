@extends('layouts.front')

@section('title', 'Tentang Kami | Profil Lembaga Inspeksi Teknik Jasa SLO & Sertifikat Laik Operasi')
@section('meta_description', 'Profil lembaga inspeksi teknik ketenagalistrikan independen, sejarah, visi, misi, dan kredibilitas tim inspektur teknik dalam pengujian kelaikan operasi listrik di Indonesia.')

@section('content')

    <!-- HERO ABOUT -->
    <section class="hero-section" style="padding: 56px 0 50px;">
        <div class="container">
            <div class="hero-badge">
                <i class="bi bi-patch-check-fill"></i>
                Pusat Pembinaan & Sertifikasi Resmi Keselamatan & Kesehatan Kerja Korporat (Jasa SLO Indonesia) Nasional
            </div>

            <h1 class="hero-title" style="font-size: 2.35rem;">
                Membangun Keunggulan <span>Manajemen Keselamatan Kerja Keselamatan Kerja & Manajemen Risiko K3</span> di Indonesia
            </h1>

            <p class="hero-lead" style="max-width: 840px;">
                Mendedikasikan diri untuk mencetak Sertifikat Laik Operasi (SLO) Ketenagalistrikan, Operator Tempat Kerja (Auditor SMK3), Operator Menara (Analis Risiko Pengujian Tahanan Isolasi Megger & Grounding), Teknisi Fluida (Pengurus Sertifikasi Tenaga Teknik SKTTK), dan Pengawas Rig (Toolpusher) yang profesional, disiplin, berlisensi sah, dan berkomitmen teguh pada keselamatan kerja Zero Accident.
            </p>
        </div>
    </section>

    <!-- SEJARAH, VISI & MISI SECTION -->
    <section class="section-py">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 36px; margin-bottom: 56px; align-items: center;">
                <div>
                    <span class="section-tag" style="background: #ecfdf5; color: #9a3412; font-size: 0.76rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase;">Sejarah Kami</span>
                    <h2 class="section-title" style="font-size: 1.85rem; margin: 10px 0 18px;">
                        Pelopor Pembinaan Personel Rig & Keahlian Sertifikat Laik Operasi (SLO) Ketenagalistrikan di Seluruh Indonesia
                    </h2>
                    <p style="font-size: 0.92rem; color: #475569; line-height: 1.7; margin-bottom: 14px;">
                        Operasi keselamatan kerja sumur migas, panas bumi (geothermal), pertambangan mineral, dan eksplorasi air tanah dalam merupakan industri berisiko tinggi yang menuntut presisi teknis, pemahaman hidrolika formasi batuan, dan kepatuhan mutlak pada standar keselamatan kerja internasional.
                    </p>
                    <p style="font-size: 0.92rem; color: #475569; line-height: 1.7; margin-bottom: 20px;">
                        Didirikan oleh konsorsium praktisi senior operasi keselamatan kerja lapangan (korporasi), instruktur master manajemen risiko k3 internasional, serta konsultan kelaikan rig terkemuka, <strong>Jasa SLO Indonesia</strong> hadir menjembatani kebutuhan tenaga kerja terampil yang siap kerja di rig onshore maupun offshore di seluruh 38 provinsi Indonesia.
                    </p>
                    <div style="display: flex; gap: 18px; flex-wrap: wrap;">
                        <div style="background: #ecfdf5; border-left: 4px solid #059669; padding: 12px 18px; border-radius: 0 8px 8px 0;">
                            <div style="font-size: 1.3rem; font-weight: 800; color: #062e22;">100%</div>
                            <div style="font-size: 0.78rem; color: #9a3412; font-weight: 600;">Sertifikat Sah & Lisensi Rig Terverifikasi</div>
                        </div>
                        <div style="background: #ecfdf5; border-left: 4px solid #059669; padding: 12px 18px; border-radius: 0 8px 8px 0;">
                            <div style="font-size: 1.3rem; font-weight: 800; color: #062e22;">38</div>
                            <div style="font-size: 0.78rem; color: #9a3412; font-weight: 600;">Provinsi Jangkauan Layanan Rig</div>
                        </div>
                        <div style="background: #ecfdf5; border-left: 4px solid #059669; padding: 12px 18px; border-radius: 0 8px 8px 0;">
                            <div style="font-size: 1.3rem; font-weight: 800; color: #062e22;">16.800+</div>
                            <div style="font-size: 0.78rem; color: #9a3412; font-weight: 600;">Alumni Kru Rig & Ahli K3 Umum</div>
                        </div>
                    </div>
                </div>

                <div style="background: #ffffff; border: 1px solid #a7f3d0; border-radius: var(--radius-xl); padding: 32px; box-shadow: 0 8px 24px rgba(16, 185, 129, 0.05);">
                    <div style="margin-bottom: 28px;">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                            <div style="width: 38px; height: 38px; background: #ecfdf5; color: #059669; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.25rem;">
                                <i class="bi bi-eye-fill"></i>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 800; color: #062e22; margin: 0;">Visi Lembaga</h3>
                        </div>
                        <p style="font-size: 0.9rem; color: #475569; line-height: 1.65; margin: 0;">
                            Menjadi pusat unggulan nasional dan rujukan terdepan dalam pendidikan kejuruan, pembinaan kompetensi manajemen keselamatan kerja, standarisasi manajemen risiko k3, dan sertifikasi resmi profesi keselamatan kerja berdaya saing global.
                        </p>
                    </div>

                    <div style="border-top: 1px solid #a7f3d0; padding-top: 24px;">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
                            <div style="width: 38px; height: 38px; background: #ecfdf5; color: #059669; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.25rem;">
                                <i class="bi bi-bullseye"></i>
                            </div>
                            <h3 style="font-size: 1.25rem; font-weight: 800; color: #062e22; margin: 0;">Misi Lembaga</h3>
                        </div>
                        <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem; color: #475569;">
                            <li style="display: flex; align-items: flex-start; gap: 8px;">
                                <i class="bi bi-check-circle-fill" style="color: #059669; font-size: 1rem; margin-top: 2px;"></i>
                                <span>Menyelenggarakan pelatihan dan sertifikasi kompetensi personel rig berlisensi resmi dengan standar keselamatan kerja industri energi tertinggi.</span>
                            </li>
                            <li style="display: flex; align-items: flex-start; gap: 8px;">
                                <i class="bi bi-check-circle-fill" style="color: #059669; font-size: 1rem; margin-top: 2px;"></i>
                                <span>Mengedukasi kru lapangan mengenai deteksi dini kick formasi, prosedur shut-in darurat, pengoperasian unit BOP, dan kepatuhan sistem keselamatan rig floor.</span>
                            </li>
                            <li style="display: flex; align-items: flex-start; gap: 8px;">
                                <i class="bi bi-check-circle-fill" style="color: #059669; font-size: 1rem; margin-top: 2px;"></i>
                                <span>Membekali peserta dengan keterampilan praktis pengoperasian drawworks, top drive, penanganan pipa bor, sirkulasi fluida, dan formulasi keselamatan proses industri.</span>
                            </li>
                            <li style="display: flex; align-items: flex-start; gap: 8px;">
                                <i class="bi bi-check-circle-fill" style="color: #059669; font-size: 1rem; margin-top: 2px;"></i>
                                <span>Membangun budaya keselamatan proaktif menuju terwujudnya Zero Accident di seluruh manajemen keselamatan kerja darat (onshore) dan lepas pantai (offshore) nasional.</span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- LEGALITAS & AKREDITASI -->
            <div style="background: linear-gradient(145deg, #062e22 0%, #09392b 100%); color: #ffffff; border-radius: 20px; padding: 36px 32px; border: 1px solid rgba(16, 185, 129, 0.4); box-shadow: 0 12px 32px rgba(15, 23, 42, 0.4);">
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
                    <div>
                        <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.35); color: #a7f3d0; font-size: 0.74rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; text-transform: uppercase; margin-bottom: 12px;">
                            <i class="bi bi-patch-check-fill"></i> Standar Internasional & Kredibilitas Resmi
                        </div>
                        <h3 style="font-size: 1.45rem; font-weight: 800; margin-bottom: 8px; color: #ffffff;">Standar Operasional Rig & Kepatuhan Korporasi</h3>
                        <p style="font-size: 0.88rem; color: #a7f3d0; max-width: 680px; margin: 0; line-height: 1.6;">
                            Seluruh program pembinaan mengacu pada Standar Kompetensi Kerja Personel Rig Keselamatan Kerja, Prosedur Keselamatan Manajemen Risiko K3 Internasional (IADC & ISO 45001), Kelaikan Sistem Pengangkat & Sirkulasi Rig, serta kaidah perlindungan lingkungan korporasi terintegrasi.
                        </p>
                    </div>
                    <div>
                        <a href="https://api.whatsapp.com/send?phone=6281399810272&text={{ urlencode('Halo Admin Jasa SLO Indonesia, saya ingin konsultasi jadwal dan pendaftaran sertifikasi keselamatan dan kesehatan kerja korporat rig.') }}" target="_blank" class="btn-primary-green" style="font-size: 0.88rem; padding: 12px 22px;">
                            <i class="bi bi-whatsapp"></i> Hubungi Hotline Utama
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

@endsection
