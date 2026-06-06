import streamlit as st

st.set_page_config(
    page_title="SPEKTRA - Materi Kuliah",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>
    .materi-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        margin: 15px 0;
    }
    
    .section-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0 15px 0;
    }
    
    .formula-box {
        background: #f5f5f5;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 15px 0;
        font-family: monospace;
    }
    
    .highlight {
        background: #fff9e6;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 15px 0;
    }
    
    .example-box {
        background: #e8f5e9;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("📚 Materi Kuliah - Pembelajaran Kimia Interaktif")
st.markdown("Akses materi pembelajaran lengkap dengan penjelasan detail, rumus, dan contoh soal")

st.markdown("---")

# Pilih topik
st.subheader("📖 Pilih Topik Pembelajaran")

topics = {
    "Stoichiometri": "stoichiometri",
    "Struktur Atom": "atom",
    "Ikatan Kimia": "ikatan",
    "Reaksi Kimia": "reaksi",
    "Asam dan Basa": "asam_basa"
}

selected_topic = st.selectbox("Pilih Topik:", list(topics.keys()))

st.markdown("---")

# STOICHIOMETRI
if selected_topic == "Stoichiometri":
    st.markdown("""
    <div class='section-header'>
        <h2>⚗️ Stoichiometri - Hukum Perbandingan Massa</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📖 Definisi")
    st.markdown("""
    Stoichiometri adalah cabang ilmu kimia yang mempelajari hubungan kuantitatif antara reaktan dan produk dalam suatu reaksi kimia. 
    Stoichiometri berdasarkan hukum-hukum dasar kimia seperti hukum perbandingan tetap dan hukum perbandingan berganda.
    """)
    
    st.subheader("🔢 Konsep Dasar")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **1. Mol**
        - Satuan jumlah zat
        - 1 mol = 6.022 × 10²³ partikel (Bilangan Avogadro)
        - n = m/Mr (moles = massa/massa molar)
        """)
    
    with col2:
        st.markdown("""
        **2. Massa Molar (Mr)**
        - Jumlah massa relatif atom-atom penyusun senyawa
        - Dinyatakan dalam g/mol
        - Contoh: Mr(H₂O) = 2(1) + 16 = 18 g/mol
        """)
    
    st.markdown("---")
    
    st.subheader("📐 Rumus Stoichiometri")
    
    st.markdown("""
    <div class='formula-box'>
    <strong>Menghitung Jumlah Mol:</strong><br>
    n = m / Mr<br>
    <br>
    Keterangan:<br>
    n = jumlah mol (mol)<br>
    m = massa zat (gram)<br>
    Mr = massa molar (g/mol)<br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='formula-box'>
    <strong>Dari Persamaan Reaksi:</strong><br>
    Jika: aA + bB → cC + dD<br>
    Maka: nA/a = nB/b = nC/c = nD/d<br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📚 Contoh Soal & Pembahasan")
    
    with st.expander("Contoh 1: Menghitung Jumlah Mol"):
        st.markdown("""
        **Soal:** Berapa mol NaCl yang terdapat dalam 58.5 gram NaCl? (Mr NaCl = 58.5)
        
        **Penyelesaian:**
        
        n = m / Mr = 58.5 / 58.5 = 1 mol
        
        **Jawab:** 1 mol NaCl
        """)
    
    with st.expander("Contoh 2: Stoichiometri Reaksi"):
        st.markdown("""
        **Soal:** Persamaan reaksi: 2H₂ + O₂ → 2H₂O
        
        Jika tersedia 8 mol H₂, berapa mol O₂ yang diperlukan dan berapa mol H₂O yang dihasilkan?
        
        **Penyelesaian:**
        
        Dari persamaan: 2H₂ : 1O₂ : 2H₂O
        
        Untuk H₂O yang dihasilkan:
        - nH₂ / 2 = nH₂O / 2
        - 8 / 2 = nH₂O / 2
        - nH₂O = 8 mol
        
        Untuk O₂ yang diperlukan:
        - nH₂ / 2 = nO₂ / 1
        - 8 / 2 = nO₂ / 1
        - nO₂ = 4 mol
        
        **Jawab:** O₂ yang diperlukan = 4 mol, H₂O yang dihasilkan = 8 mol
        """)

# STRUKTUR ATOM
elif selected_topic == "Struktur Atom":
    st.markdown("""
    <div class='section-header'>
        <h2>⚛️ Struktur Atom - Model Atom Bohr dan Mekanika Kuantum</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📖 Definisi")
    st.markdown("""
    Atom terdiri dari inti (proton dan neutron) dan kulit elektron. Struktur atom menjelaskan 
    bagaimana elektron tersusun dalam tingkat energi dan orbital di sekitar inti.
    """)
    
    st.subheader("🔬 Partikel Penyusun Atom")
    
    particles_data = {
        "Partikel": ["Proton", "Neutron", "Elektron"],
        "Simbol": ["p⁺", "n⁰", "e⁻"],
        "Lokasi": ["Inti", "Inti", "Kulit"],
        "Muatan": ["+1", "0", "-1"],
        "Massa (amu)": ["1", "1", "0.0005"]
    }
    
    st.table(particles_data)
    
    st.markdown("---")
    
    st.subheader("📐 Bilangan Kuantum")
    
    st.markdown("""
    <div class='formula-box'>
    <strong>Ada 4 Bilangan Kuantum yang Menjelaskan Posisi Elektron:</strong><br>
    <br>
    1. <strong>n (Bilangan Kuantum Utama):</strong> 1, 2, 3, 4, ... (tingkat energi/kulit)<br>
    2. <strong>l (Bilangan Kuantum Azimut):</strong> 0, 1, 2, ..., (n-1) (tipe orbital: s, p, d, f)<br>
    3. <strong>m (Bilangan Kuantum Magnetik):</strong> -l, ..., 0, ..., +l (orientasi orbital)<br>
    4. <strong>s (Bilangan Kuantum Spin):</strong> +½ atau -½ (arah spin elektron)<br>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📚 Contoh Soal")
    
    with st.expander("Contoh: Menentukan Orbital Elektron"):
        st.markdown("""
        **Soal:** Tentukan orbital dari elektron dengan bilangan kuantum n=3, l=2
        
        **Penyelesaian:**
        - n = 3 (kulit ke-3)
        - l = 2 (orbital d, karena: s=0, p=1, d=2, f=3)
        - Orbital = 3d
        
        **Jawab:** Elektron berada di orbital 3d
        """)

# IKATAN KIMIA
elif selected_topic == "Ikatan Kimia":
    st.markdown("""
    <div class='section-header'>
        <h2>🔗 Ikatan Kimia - Jenis dan Sifat Ikatan</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📖 Definisi")
    st.markdown("""
    Ikatan kimia adalah gaya tarik-menarik yang mengikat atom-atom satu sama lain membentuk senyawa. 
    Ikatan terbentuk untuk mencapai konfigurasi elektron yang stabil.
    """)
    
    st.subheader("🔗 Jenis-Jenis Ikatan Kimia")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='materi-card'>
        <h4>Ikatan Ion</h4>
        <p><strong>Terjadi antara:</strong> Logam + Non-logam</p>
        <p><strong>Cara terbentuk:</strong> Transfer elektron</p>
        <p><strong>Contoh:</strong> NaCl, KBr, MgO</p>
        <p><strong>Sifat:</strong> Larut dalam air, mudah terbakar, konduktor saat cair</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='materi-card'>
        <h4>Ikatan Kovalen</h4>
        <p><strong>Terjadi antara:</strong> Non-logam + Non-logam</p>
        <p><strong>Cara terbentuk:</strong> Berbagi elektron</p>
        <p><strong>Contoh:</strong> H₂, CO₂, CH₄</p>
        <p><strong>Sifat:</strong> Tidak larut dalam air, titik didih rendah</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='materi-card'>
        <h4>Ikatan Logam</h4>
        <p><strong>Terjadi antara:</strong> Logam + Logam</p>
        <p><strong>Cara terbentuk:</strong> Laut elektron</p>
        <p><strong>Contoh:</strong> Fe, Cu, Al</p>
        <p><strong>Sifat:</strong> Konduktor, plastis, lenting</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("💡 Ikatan Kovalen Polar vs Non-Polar")
    
    st.markdown("""
    <div class='highlight'>
    <strong>Perbedaan Keelektronegatifan menentukan polaritas:</strong><br>
    <br>
    • ΔEN = 0 → Kovalen Non-Polar<br>
    • 0 < ΔEN < 1.7 → Kovalen Polar<br>
    • ΔEN ≥ 1.7 → Ikatan Ion<br>
    </div>
    """, unsafe_allow_html=True)

# REAKSI KIMIA
elif selected_topic == "Reaksi Kimia":
    st.markdown("""
    <div class='section-header'>
        <h2>⚗️ Reaksi Kimia - Jenis dan Persamaan Reaksi</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📖 Definisi")
    st.markdown("""
    Reaksi kimia adalah proses perubahan suatu zat menjadi zat lain yang berbeda melalui pemutusan 
    dan pembentukan ikatan kimia.
    """)
    
    st.subheader("🔄 Jenis-Jenis Reaksi Kimia")
    
    with st.expander("1️⃣ Reaksi Sintesis (Kombinasi)"):
        st.markdown("""
        **Persamaan Umum:** A + B → AB
        
        **Contoh:**
        - C + O₂ → CO₂
        - 2H₂ + O₂ → 2H₂O
        """)
    
    with st.expander("2️⃣ Reaksi Dekomposisi"):
        st.markdown("""
        **Persamaan Umum:** AB → A + B
        
        **Contoh:**
        - 2H₂O₂ → 2H₂O + O₂ (pemecahan hidrogen peroksida)
        - 2KMnO₄ → K₂MnO₄ + MnO₂ + O₂
        """)
    
    with st.expander("3️⃣ Reaksi Pertukaran Tunggal"):
        st.markdown("""
        **Persamaan Umum:** A + BC → AC + B
        
        **Contoh:**
        - Zn + CuSO₄ → ZnSO₄ + Cu
        - Fe + 2HCl → FeCl₂ + H₂
        """)
    
    with st.expander("4️⃣ Reaksi Pertukaran Ganda"):
        st.markdown("""
        **Persamaan Umum:** AB + CD → AD + CB
        
        **Contoh:**
        - AgNO₃ + NaCl → AgCl↓ + NaNO₃
        - HCl + NaOH → NaCl + H₂O
        """)
    
    st.markdown("---")
    
    st.subheader("🔍 Menyetarakan Persamaan Reaksi")
    
    st.markdown("""
    <div class='example-box'>
    <strong>Contoh: Menyetarakan Fe + O₂ → Fe₂O₃</strong><br>
    <br>
    1. Hitung atom di setiap sisi<br>
    2. Tentukan unsur dengan jumlah atom paling banyak<br>
    3. Mulai dari atom yang paling kompleks<br>
    4. Verifikasi keseteraan<br>
    <br>
    <strong>Hasil Akhir: 4Fe + 3O₂ → 2Fe₂O₃</strong>
    </div>
    """, unsafe_allow_html=True)

# ASAM DAN BASA
elif selected_topic == "Asam dan Basa":
    st.markdown("""
    <div class='section-header'>
        <h2>🧪 Asam dan Basa - pH dan Buffer</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📖 Definisi")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='materi-card'>
        <h4>Asam</h4>
        <p><strong>Menurut Arrhenius:</strong> Zat yang melepaskan H⁺ dalam air</p>
        <p><strong>Sifat:</strong></p>
        <ul>
        <li>Rasa asam</li>
        <li>pH < 7</li>
        <li>Menggandur kertas lakmus biru</li>
        <li>Contoh: HCl, H₂SO₄</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='materi-card'>
        <h4>Basa</h4>
        <p><strong>Menurut Arrhenius:</strong> Zat yang melepaskan OH⁻ dalam air</p>
        <p><strong>Sifat:</strong></p>
        <ul>
        <li>Rasa pahit, licin</li>
        <li>pH > 7</li>
        <li>Menggandur kertas lakmus merah</li>
        <li>Contoh: NaOH, KOH</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📐 Skala pH")
    
    st.markdown("""
    <div class='formula-box'>
    <strong>pH = -log[H⁺]</strong><br>
    <strong>pOH = -log[OH⁻]</strong><br>
    <strong>pH + pOH = 14</strong><br>
    <br>
    Skala pH:<br>
    • pH < 7 → Asam<br>
    • pH = 7 → Netral<br>
    • pH > 7 → Basa<br>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Download materi
st.subheader("📥 Download Materi")

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        label="📄 Download Ringkasan Materi (PDF)",
        data=b"Materi PDF",
        file_name="Materi_Kimia_SPEKTRA.pdf",
        mime="application/pdf",
        disabled=True
    )

with col2:
    st.download_button(
        label="📋 Download Soal Latihan (DOCX)",
        data=b"Soal Latihan",
        file_name="Soal_Latihan_SPEKTRA.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        disabled=True
    )

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px; margin-top: 30px;">
    <p>📚 Materi Kuliah SPEKTRA | Pembelajaran Kimia Komprehensif | Dibuat dengan ❤️ untuk kemajuan pendidikan</p>
</div>
""", unsafe_allow_html=True)
