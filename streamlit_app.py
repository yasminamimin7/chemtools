import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="SPEKTRA - Smart Platform for Chemical Analysis",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# CSS STYLING
# ==========================
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2d3748 0%, #1a202c 100%);
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px 30px;
        border-radius: 0;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        text-align: center;
    }
    
    .main-header h1 {
        font-size: 3em;
        margin-bottom: 10px;
        font-weight: bold;
    }
    
    .main-header p {
        font-size: 1.2em;
        opacity: 0.95;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        margin: 30px 0;
    }
    
    .feature-card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 6px solid #667eea;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-left-color: #764ba2;
    }
    
    .feature-card h3 {
        color: #2d3748;
        margin-bottom: 15px;
        font-size: 1.5em;
    }
    
    .feature-card p {
        color: #4a5568;
        line-height: 1.6;
    }
    
    .metric-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 20px;
        margin: 30px 0;
    }
    
    .metric-box {
        padding: 25px;
        border-radius: 12px;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .metric-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    .metric-box h3 {
        color: #667eea;
        font-size: 2.5em;
        margin: 10px 0;
    }
    
    .metric-box p {
        color: #4a5568;
        font-size: 1.1em;
    }
    
    .info-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 12px;
        margin: 20px 0;
        text-align: center;
    }
    
    .divider {
        margin: 40px 0;
        border: none;
        height: 2px;
        background: linear-gradient(to right, transparent, #667eea, transparent);
    }
    
    .section-title {
        color: #2d3748;
        font-size: 2em;
        margin: 30px 0 20px 0;
        padding-bottom: 15px;
        border-bottom: 3px solid #667eea;
    }
    
    .footer {
        text-align: center;
        color: #718096;
        padding: 30px 20px;
        margin-top: 40px;
        border-top: 2px solid #e2e8f0;
    }
    
    @media (max-width: 768px) {
        .feature-grid {
            grid-template-columns: 1fr;
        }
        
        .metric-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }
</style>
""", unsafe_allow_html=True)

# ==========================
# MAIN HEADER
# ==========================
st.markdown("""
<div class='main-header'>
    <h1>🧪 SPEKTRA</h1>
    <p>Smart Platform for Chemical Analysis and Laboratory Tools</p>
    <p style='font-size: 1em; opacity: 0.85; margin-top: 10px;'>Platform Terintegrasi untuk Analisis Kimia, Manajemen Laboratorium, dan Pembelajaran Interaktif</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# FEATURE SHOWCASE
# ==========================
st.markdown("<h2 class='section-title'>✨ Fitur Unggulan</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='feature-grid'>
    <div class='feature-card'>
        <h3>🧪 Kalkulator Pengenceran</h3>
        <p>Hitung pengenceran larutan dengan mudah menggunakan rumus M1V1 = M2V2. Tersedia 4 metode perhitungan untuk memudahkan Anda menentukan volume dan konsentrasi yang tepat untuk pengenceran larutan kimia.</p>
    </div>
    
    <div class='feature-card'>
        <h3>🔬 ChemScan</h3>
        <p>Database lengkap bahan kimia dengan informasi detail meliputi: sifat fisik, tingkat bahaya, alat pelindung diri (APD), kondisi penyimpanan yang aman, reaktivitas, dan tindakan darurat untuk keselamatan laboratorium.</p>
    </div>
    
    <div class='feature-card'>
        <h3>📝 Quiz Center</h3>
        <p>Uji pemahaman Anda tentang kimia melalui quiz interaktif dengan bank soal lengkap. Fitur ini dirancang untuk meningkatkan pengetahuan dengan pembahasan detail untuk setiap jawaban.</p>
    </div>
    
    <div class='feature-card'>
        <h3>📚 Materi Kuliah</h3>
        <p>Akses materi pembelajaran kimia yang komprehensif dengan penjelasan detail, rumus-rumus penting, contoh soal, dan tips belajar untuk berbagai topik kimia dari tingkat dasar hingga lanjutan.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================
# STATISTICS
# ==========================
st.markdown("<h2 class='section-title'>📊 Statistik Platform</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class='metric-box'>
        <h3>500+</h3>
        <p>Bahan Kimia</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-box'>
        <h3>100+</h3>
        <p>Quiz Soal</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-box'>
        <h3>50+</h3>
        <p>Materi Pembelajaran</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='metric-box'>
        <h3>24/7</h3>
        <p>Akses Penuh</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# INTRODUCTION
# ==========================
st.markdown("<h2 class='section-title'>🎯 Tentang SPEKTRA</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **SPEKTRA** adalah platform pendidikan dan manajemen laboratorium yang dirancang khusus untuk mendukung pembelajaran kimia modern. 
    
    Dengan antarmuka yang intuitif dan fitur-fitur canggih, SPEKTRA membantu:
    - 🎓 Mahasiswa dalam memahami konsep kimia
    - 👨‍🔬 Peneliti dalam manajemen bahan kimia
    - 🏫 Pengajar dalam menyampaikan materi pembelajaran
    - 🔬 Teknisi laboratorium dalam keselamatan kerja
    """)

with col2:
    st.markdown("""
    **Keunggulan SPEKTRA:**
    
    ✅ Interface modern dan user-friendly  
    ✅ Database bahan kimia paling lengkap  
    ✅ Quiz interaktif dengan pembahasan  
    ✅ Materi pembelajaran terlengkap  
    ✅ Fitur keselamatan laboratorium  
    ✅ Akses 24/7 dari mana saja  
    ✅ Gratis dan open source  
    """)

# ==========================
# QUICK START
# ==========================
st.markdown("<h2 class='section-title'>🚀 Mulai Sekarang</h2>", unsafe_allow_html=True)

st.markdown("""
<div class='info-banner'>
    <h3>Pilih Fitur dari Menu Samping untuk Memulai</h3>
    <p style='margin-top: 10px; font-size: 1.1em;'>Gunakan sidebar (☰) untuk menavigasi ke fitur yang Anda inginkan</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# FEATURES DETAIL
# ==========================
st.markdown("<h2 class='section-title'>📖 Panduan Penggunaan</h2>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs([
    "🧪 Kalkulator", 
    "🔬 ChemScan", 
    "📝 Quiz", 
    "📚 Materi"
])

with tab1:
    st.subheader("🧪 Cara Menggunakan Kalkulator Pengenceran")
    st.markdown("""
    1. **Pilih Metode** - Tentukan variabel apa yang ingin Anda hitung
    2. **Masukkan Data** - Isi nilai yang Anda ketahui
    3. **Klik Hitung** - Dapatkan hasil perhitungan
    4. **Lihat Penjelasan** - Baca cara kerja dan rekomendasi
    
    **Metode yang Tersedia:**
    - Hitung Volume Akhir (V2)
    - Hitung Konsentrasi Akhir (M2)
    - Hitung Konsentrasi Awal (M1)
    - Hitung Volume Awal (V1)
    """)

with tab2:
    st.subheader("🔬 Cara Menggunakan ChemScan")
    st.markdown("""
    1. **Cari Bahan Kimia** - Gunakan search bar untuk mencari
    2. **Baca Informasi** - Lihat sifat fisik dan bahaya
    3. **Perhatikan APD** - Ketahui alat pelindung yang diperlukan
    4. **Download Info** - Simpan data dalam format TXT
    
    **Informasi yang Tersedia:**
    - Sifat Fisik (titik didih, densitas, dll)
    - Tingkat Bahaya
    - Gejala Paparan
    - APD yang Diperlukan
    - Kondisi Penyimpanan
    - Tindakan Darurat
    """)

with tab3:
    st.subheader("📝 Cara Menggunakan Quiz Center")
    st.markdown("""
    1. **Pilih Topik** - Pilih topik yang ingin Anda kuasai
    2. **Tentukan Jumlah Soal** - Sesuaikan tingkat kesulitan
    3. **Jawab Soal** - Pilih jawaban yang tepat
    4. **Lihat Pembahasan** - Pelajari penjelasan jawaban
    5. **Cek Skor** - Lihat hasil dan review jawaban
    
    **Topik Tersedia:**
    - Stoichiometri
    - Struktur Atom
    - Ikatan Kimia
    - Reaksi Kimia
    - Asam dan Basa
    """)

with tab4:
    st.subheader("📚 Cara Menggunakan Materi Kuliah")
    st.markdown("""
    1. **Pilih Topik** - Pilih materi yang ingin dipelajari
    2. **Baca Penjelasan** - Pahami konsep dan teori
    3. **Pelajari Rumus** - Ketahui formula penting
    4. **Lihat Contoh** - Pelajari dari contoh soal
    5. **Download Materi** - Simpan materi untuk referensi
    
    **Topik Pembelajaran:**
    - Stoichiometri
    - Struktur Atom
    - Ikatan Kimia
    - Reaksi Kimia
    - Asam dan Basa
    """)

# ==========================
# FOOTER
# ==========================
st.markdown("""
<div class='footer'>
    <p style='font-size: 1.2em; margin-bottom: 15px;'>🧪 SPEKTRA | Smart Platform for Chemical Analysis and Laboratory Tools</p>
    <p>© 2026 | Dikembangkan dengan ❤️ untuk kemajuan pendidikan kimia</p>
    <p style='margin-top: 15px; font-size: 0.9em;'>Lisensi: Apache 2.0 | Open Source | Gratis untuk semua pengguna</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR
# ==========================
with st.sidebar:
    st.markdown("### 📚 Menu Navigasi")
    st.markdown("""
    Pilih fitur dari menu di atas:
    
    - 🧪 **Kalkulator Pengenceran**
    - 🔬 **ChemScan**
    - 📝 **Quiz Center**
    - 📚 **Materi Kuliah**
    """)
    
    st.divider()
    
    st.markdown("### ℹ️ Informasi")
    st.markdown("""
    **Versi:** 1.0.0  
    **Platform:** Streamlit  
    **Lisensi:** Apache 2.0  
    
    Hubungi kami untuk saran!
    """)
    
    st.divider()
    
    st.markdown("### 🔗 Tautan Cepat")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[GitHub](#)")
    with col2:
        st.markdown("[Dokumentasi](#)")
