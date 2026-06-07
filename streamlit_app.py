import streamlit as st
import pandas as pd

from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="🧪 SPEKTRA Mini Tools 🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =========================
# THEME MANAGEMENT
# =========================
if 'theme' not in st.session_state:
    st.session_state.theme = 'ocean'

THEME_CONFIG = {
 'ocean': {
    'bg_gradient': 'linear-gradient(135deg, #1e3a5f, #2563eb, #3b82f6, #60a5fa)',
    'primary': '#60a5fa',
    'secondary': '#3b82f6',
    'accent': '#bfdbfe',
    'text': '#ffffff',
    'input_bg': '#1e40af',
    'card_bg': 'rgba(255,255,255,0.12)',
},
 'sunset': {
    'bg_gradient': 'linear-gradient(135deg, #5b2c1d, #8b4513, #b85c38, #d97757)',
    'primary': '#d97757',
    'secondary': '#b85c38',
    'accent': '#ffd6a5',
    'text': '#ffffff',
    'input_bg': '#7a3b20',
    'card_bg': 'rgba(255,255,255,0.12)',
},
    'forest': {
    'bg_gradient': 'linear-gradient(135deg, #1b4332, #2d6a4f, #40916c, #52b788)',
    'primary': '#52b788',
    'secondary': '#40916c',
    'accent': '#b7e4c7',
    'text': '#ffffff',
    'input_bg': '#2d6a4f',
    'card_bg': 'rgba(255,255,255,0.12)',
},
}

theme = THEME_CONFIG[st.session_state.theme]

# =========================
# DYNAMIC STYLING
# =========================
st.markdown(f""" <style> /* Background Animation */ .stApp {{ background: {theme['bg_gradient']}; background-size: 400% 400%; animation: gradientBG 14s ease infinite; color: {theme['text']}; }} [data-testid="stHeader"] {{ background: transparent !important; }} header {{ background: transparent !important; }} @keyframes gradientBG {{ 0% {{background-position: 0% 50%;}} 50% {{background-position: 100% 50%;}} 100% {{background-position: 0% 50%;}} }} /* Glass Container */ .block-container {{ padding-top: 0rem !important; padding-bottom: 1rem !important; border-radius: 20px; background-color: {theme['card_bg']}; box-shadow: 0px 8px 32px rgba(0,0,0,0.3); backdrop-filter: blur(10px); border: 1px solid rgba(45, 156, 219, 0.2); }} /* Text Colors */ h1, h2, h3, h4, h5, h6, p {{ color: {theme['text']} !important; text-shadow: 0 1px 3px rgba(0,0,0,0.4); }} /* Input Fields */ div[data-baseweb="input"] input {{ background-color: {theme['input_bg']} !important; color: {theme['text']} !important; border: 2px solid {theme['primary']} !important; border-radius: 10px !important; padding: 12px !important; }} input::placeholder {{ color: rgba(230, 241, 255, 0.5) !important; }} textarea {{ background-color: {theme['input_bg']} !important; color: {theme['text']} !important; border: 2px solid {theme['primary']} !important; border-radius: 10px !important; }} /* Buttons */ div.stButton > button {{ background-color: {theme['primary']} !important; color: #0b1320 !important; font-weight: bold !important; border-radius: 12px !important; border: none !important; padding: 12px 24px !important; transition: all 0.3s ease !important; }} div.stButton > button:hover {{ background-color: {theme['accent']} !important; transform: translateY(-2px) !important; box-shadow: 0px 8px 16px rgba(45, 156, 219, 0.3) !important; }} /* Sidebar */ section[data-testid="stSidebar"] {{ background: rgba(255,255,255,0.15) !important; backdrop-filter: blur(12px); }} /* Radio Buttons & Selectbox */ div[role="radiogroup"] {{ background-color: {theme['card_bg']} !important; padding: 15px !important; border-radius: 12px !important; border: 1px solid {theme['primary']} !important; }} /* Cards */ .metric-card {{ background: linear-gradient(135deg, {theme['secondary']}, {theme['primary']}); padding: 25px; border-radius: 15px; color: {theme['text']}; box-shadow: 0px 8px 20px rgba(0,0,0,0.3); border: 1px solid {theme['accent']}; }} .success-box {{ background-color: rgba(76, 175, 80, 0.1); border-left: 5px solid #4CAF50; padding: 15px; border-radius: 8px; color: #4CAF50; }} .error-box {{ background-color: rgba(244, 67, 54, 0.1); border-left: 5px solid #f44336; padding: 15px; border-radius: 8px; color: #f44336; }} /* Divider */ hr {{ border: 1px solid {theme['primary']} !important; opacity: 0.5 !important; }} [data-testid="collapsedControl"] {{ background: transparent !important; }} [data-testid="collapsedControl"] svg {{ fill: #FFFFFF !important; stroke: #FFFFFF !important; color: #FFFFFF !important; opacity: 1 !important; }} [data-testid="collapsedControl"] path {{ fill: #FFFFFF !important; stroke: #FFFFFF !important; }} </style> """, unsafe_allow_html=True)

# =========================
# SIDEBAR - THEME & NAVIGATION
# =========================
with st.sidebar:
    st.markdown(f"<h2 style='color:{theme['accent']};'>⚙️ KONTROL PANEL</h2>", unsafe_allow_html=True)
    
    # Theme Selector
    st.subheader("🎨 Pilih Tema")
    theme_choice = st.selectbox(
        "Tema Warna:",
        ["ocean", "sunset", "forest"],
        index=["ocean", "sunset", "forest"].index(st.session_state.theme)
    )
    
    if theme_choice != st.session_state.theme:
        st.session_state.theme = theme_choice
        st.rerun()
    
    # Theme Preview
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌊 Ocean", use_container_width=True):
            st.session_state.theme = 'ocean'
            st.rerun()
    with col2:
        if st.button("🌅 Sunset", use_container_width=True):
            st.session_state.theme = 'sunset'
            st.rerun()
    with col3:
        if st.button("🌲 Forest", use_container_width=True):
            st.session_state.theme = 'forest'
            st.rerun()
    
    st.divider()
    
    # Main Menu
    st.markdown(f"<h3 style='color:{theme['accent']};'>📋 MENU UTAMA</h3>", unsafe_allow_html=True)
    menu = st.radio(
    "",
    [
        "🏠 Beranda",
        "📊 Kalkulator Pengenceran",
        "🔬 ChemScan",
        "⚗️ Reaksi Titrasi",
        "📝 Quiz Center",
        "🎮 Tebak Warna Reaksi",
        "🧠 Analisis Kesalahan",
        "📚 Panduan Lengkap"
    ]
)
    st.divider()

    st.markdown(f"### 📌 Tentang Aplikasi")
    st.info(""" **SPEKTRA Mini Tools v1.0** Platform pembelajaran kimia yang interaktif dan inspiratif! ✨ Fitur: • 🧮 Kalkulator pengenceran dinamis • 🎯 Game quiz warna reaksi • 🔧 Troubleshooting praktikum • 🎨 3 tema warna cantik • 📖 Panduan lengkap """)
# =========================
# DATABASE CHEMSCAN
# =========================

chemical_db = {
    "HCl": {
        "nama":"Hydrochloric Acid",
        "rumus":"HCl",
        "mr":"36.46",
        "bahaya":"Korosif",
        "simbol":"☣️",
        "apd":"Sarung tangan, kacamata",
        "penyimpanan":"Lemari asam",
        "reaktivitas":"Bereaksi dengan basa menghasilkan garam dan air"
    },
    "NaOH": {
        "nama":"Sodium Hydroxide",
        "rumus":"NaOH",
        "mr":"40.00",
        "bahaya":"Korosif kuat",
        "simbol":"⚠️",
        "apd":"Sarung tangan, kacamata",
        "penyimpanan":"Tempat kering",
        "reaktivitas":"Bereaksi dengan asam"
    },
    "KMnO4": {
        "nama":"Potassium Permanganate",
        "rumus":"KMnO₄",
        "mr":"158.03",
        "bahaya":"Oksidator kuat",
        "simbol":"🔥",
        "apd":"Sarung tangan",
        "penyimpanan":"Botol gelap",
        "reaktivitas":"Bereaksi dengan reduktor"
    },
    "AgNO3": {
        "nama":"Silver Nitrate",
        "rumus":"AgNO₃",
        "mr":"169.87",
        "bahaya":"Oksidator",
        "simbol":"☠️",
        "apd":"Sarung tangan",
        "penyimpanan":"Botol gelap",
        "reaktivitas":"Bereaksi dengan ion klorida"
    }
}

# =========================
# TITLE SECTION
# =========================
st.markdown(f""" <div style='text-align:center;margin-bottom:2rem;'> <h1 style='color:{theme['accent']};font-size:3rem;margin:0;'>🔬 SPEKTRA Mini Tools🧪 </h1> <p style='color:{theme['primary']};font-size:1.2rem;margin-top:0.5rem;'> ✨ Smart Platform for Chemistry Analysis and Laboratory Tools ✨ </p> </div> """, unsafe_allow_html=True)

# =========================
# HOME PAGE
# =========================
if menu == "🏠 Beranda":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f""" <div class='metric-card'> <h3>📊 Kalkulator</h3> <p>Hitung pengenceran larutan dengan rumus M₁V₁ = M₂V₂ secara akurat dan cepat</p> <p style='font-size:0.9rem;opacity:0.8;'>💡 Hemat waktu perhitungan!</p> </div> """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f""" <div class='metric-card'> <h3>🎮 Game Quiz</h3> <p>Asah pengetahuan dengan game interaktif tebak warna reaksi kimia</p> <p style='font-size:0.9rem;opacity:0.8;'>🏆 Raih skor tertinggi!</p> </div> """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f""" <div class='metric-card'> <h3>🔧 Troubleshooting</h3> <p>Analisis kesalahan praktikum dan temukan solusi terbaik</p> <p style='font-size:0.9rem;opacity:0.8;'>✅ Praktikum sukses!</p> </div> """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f""" ### 🌟 Mengapa Pilih SPEKTRA? ✅ **User-Friendly** - Interface yang mudah digunakan untuk semua level ✅ **Interaktif** - Belajar sambil bermain dengan cara yang menyenangkan ✅ **Akurat** - Perhitungan presisi dengan validasi data lengkap ✅ **Visualisasi** - Grafik dan animasi untuk memahami konsep ✅ **Responsif** - Bekerja sempurna di desktop dan mobile """)
    
    with col2:
        st.markdown(f""" ### 🎨 Fitur Tema Dinamis Pilih tema favorit Anda di sidebar! 🌊 **Ocean** - Tema biru menenangkan 🌅 **Sunset** - Tema ungu hangat 🌲 **Forest** - Tema hijau segar ### 💡 Tips Memulai 1. Pilih fitur di menu samping 2. Ikuti panduan step-by-step 3. Gunakan riwayat untuk review 4. Bagikan hasil dengan teman! """)

# =========================
# 1. KALKULATOR PENGENCERAN
# =========================
elif menu == "📊 Kalkulator Pengenceran":
    st.markdown(f"<h1 style='color:{theme['accent']};'>📊 Kalkulator Pengenceran</h1>", unsafe_allow_html=True)
    
    st.markdown(f""" <div style='background-color:{theme['secondary']};padding:20px;border-radius:12px;text-align:center;'> <h2 style='color:{theme['accent']};margin:0;'>C₁ × V₁ = C₂ × V₂</h2> <p style='margin-top:10px;opacity:0.9;'>Rumus dasar pengenceran larutan</p> </div> """, unsafe_allow_html=True)
    
    st.divider()
    
    if "history" not in st.session_state:
        st.session_state.history = []
    
    col1, col2 = st.columns(2)
    with col1:
        satuan = st.selectbox("📏 Satuan Volume", ["mL", "L", "μL"])
        satuan_konsentrasi = st.selectbox("⚗️ Satuan Konsentrasi", ["M (Molar)", "N (Normal)", "g/L"])
    with col2:
        cari = st.selectbox("🔍 Variabel yang Dicari", ["V₂ (Volume Akhir)", "C₁ (Konsentrasi Awal)", "C₂ (Konsentrasi Akhir)", "V₁ (Volume Awal)"])
    
    st.divider()
    
    if cari == "V₂ (Volume Akhir)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        with col1:
            C1 = st.number_input(f"C₁ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            V1 = st.number_input(f"V₁ ({satuan})", value=None, placeholder="Misal: 100")
        with col3:
            C2 = st.number_input(f"C₂ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        
        if st.button("🧮 Hitung V₂", use_container_width=True):
            if None in (C1, V1, C2):
                st.markdown("<div class='error-box'>⚠️ Semua kolom harus diisi!</div>", unsafe_allow_html=True)
            elif C2 == 0:
                st.markdown("<div class='error-box'>⚠️ C₂ tidak boleh nol!</div>", unsafe_allow_html=True)
            else:
                V2 = (C1 * V1) / C2
                hasil = f"V₂ = {V2:.3f} {satuan}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C1} × {V1}) ÷ {C2}"
                })
                st.markdown(f"<div class='success-box'>✅ <strong>{hasil}</strong><br><span>Rumus: ({C1} × {V1}) ÷ {C2}</span></div>", unsafe_allow_html=True)
                st.info(f"💡 Artinya: Encerkan {V1} {satuan} larutan {C1} {satuan_konsentrasi} dengan menambahkan air hingga totalnya {V2:.3f} {satuan}")
    
    elif cari == "C₁ (Konsentrasi Awal)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        with col1:
            V1 = st.number_input(f"V₁ ({satuan})", value=None, placeholder="Misal: 100")
        with col2:
            C2 = st.number_input(f"C₂ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        with col3:
            V2 = st.number_input(f"V₂ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("🧮 Hitung C₁", use_container_width=True):
            if None in (V1, C2, V2):
                st.markdown("<div class='error-box'>⚠️ Semua kolom harus diisi!</div>", unsafe_allow_html=True)
            elif V1 == 0:
                st.markdown("<div class='error-box'>⚠️ V₁ tidak boleh nol!</div>", unsafe_allow_html=True)
            else:
                C1 = (C2 * V2) / V1
                hasil = f"C₁ = {C1:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C2} × {V2}) ÷ {V1}"
                })
                st.markdown(f"<div class='success-box'>✅ <strong>{hasil}</strong><br><span>Rumus: ({C2} × {V2}) ÷ {V1}</span></div>", unsafe_allow_html=True)
    
    elif cari == "C₂ (Konsentrasi Akhir)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        with col1:
            C1 = st.number_input(f"C₁ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            V1 = st.number_input(f"V₁ ({satuan})", value=None, placeholder="Misal: 100")
        with col3:
            V2 = st.number_input(f"V₂ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("🧮 Hitung C₂", use_container_width=True):
            if None in (C1, V1, V2):
                st.markdown("<div class='error-box'>⚠️ Semua kolom harus diisi!</div>", unsafe_allow_html=True)
            elif V2 == 0:
                st.markdown("<div class='error-box'>⚠️ V₂ tidak boleh nol!</div>", unsafe_allow_html=True)
            else:
                C2 = (C1 * V1) / V2
                hasil = f"C₂ = {C2:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C1} × {V1}) ÷ {V2}"
                })
                st.markdown(f"<div class='success-box'>✅ <strong>{hasil}</strong><br><span>Rumus: ({C1} × {V1}) ÷ {V2}</span></div>", unsafe_allow_html=True)
    
    elif cari == "V₁ (Volume Awal)":
        st.subheader("📝 Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        with col1:
            C1 = st.number_input(f"C₁ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            C2 = st.number_input(f"C₂ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        with col3:
            V2 = st.number_input(f"V₂ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("🧮 Hitung V₁", use_container_width=True):
            if None in (C1, C2, V2):
                st.markdown("<div class='error-box'>⚠️ Semua kolom harus diisi!</div>", unsafe_allow_html=True)
            elif C1 == 0:
                st.markdown("<div class='error-box'>⚠️ C₁ tidak boleh nol!</div>", unsafe_allow_html=True)
            else:
                V1 = (C2 * V2) / C1
                hasil = f"V₁ = {V1:.3f} {satuan}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C2} × {V2}) ÷ {C1}"
                })
                st.markdown(f"<div class='success-box'>✅ <strong>{hasil}</strong><br><span>Rumus: ({C2} × {V2}) ÷ {C1}</span></div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📜 Riwayat Perhitungan")
    if st.session_state.history:
        history_df = pd.DataFrame(reversed(st.session_state.history))
        st.dataframe(history_df, use_container_width=True, hide_index=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Hapus Semua Riwayat", use_container_width=True):
                st.session_state.history = []
                st.rerun()
        with col2:
            st.info(f"📊 Total perhitungan: {len(st.session_state.history)}")
    else:
        st.markdown("<div style='text-align:center;padding:2rem;opacity:0.7;'><p>Belum ada perhitungan 📭</p></div>", unsafe_allow_html=True)

# =========================
# 2. TEBAK WARNA REAKSI
# =========================
elif menu == "🎮 Tebak Warna Reaksi":
    st.markdown(f"<h1 style='color:{theme['accent']};'>🎮 Game Tebak Warna Reaksi</h1>", unsafe_allow_html=True)
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    soal_list = [
        {"pertanyaan": "KMnO₄ (ungu pekat) + Fe²⁺ → produk berwarna?", "pilihan": ["Ungu pekat", "Tak berwarna", "Coklat tua", "Hijau"], "jawaban": "Tak berwarna", "penjelasan": "KMnO₄ yang ungu tereduksi menjadi Mn²⁺ yang tidak berwarna."},
        {"pertanyaan": "Ag⁺ + Cl⁻ → endapan berwarna?", "pilihan": ["Putih", "Kuning", "Biru", "Merah"], "jawaban": "Putih", "penjelasan": "AgCl membentuk endapan putih yang sangat tidak larut dalam air."},
        {"pertanyaan": "I₂ dalam larutan air → warna?", "pilihan": ["Bening", "Coklat gelap", "Merah cerah", "Kuning pucat"], "jawaban": "Coklat gelap", "penjelasan": "Iodium dalam air membentuk larutan coklat kemerahan yang intens."},
        {"pertanyaan": "CuSO₄ + NaOH berlebih → endapan?", "pilihan": ["Putih murni", "Biru muda", "Biru gelap", "Tidak ada endapan"], "jawaban": "Biru gelap", "penjelasan": "Cu(OH)₂ membentuk endapan biru yang indah."},
        {"pertanyaan": "Fe³⁺ + SCN⁻ → larutan berwarna?", "pilihan": ["Kuning", "Merah darah", "Ungu", "Hijau"], "jawaban": "Merah darah", "penjelasan": "Kompleks [Fe(SCN)]²⁺ memberikan warna merah darah yang kuat."}
    ]
    
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("🏆 Skor", st.session_state.skor)
    with col2: st.metric("❓ Total", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            st.metric("📊 Akurasi", f"{(st.session_state.skor / st.session_state.total)*100:.0f}%")
    
    st.divider()
    tabs = st.tabs([f"Soal {i+1}" for i in range(len(soal_list))])
    for idx, (tab, soal) in enumerate(zip(tabs, soal_list)):
        with tab:
            st.markdown(f"### ❓ {soal['pertanyaan']}")
            jawaban_user = st.radio("Pilih:", soal['pilihan'], key=f"soal_{idx}", label_visibility="collapsed")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Cek Jawaban", key=f"check_{idx}", use_container_width=True):
                    st.session_state.total += 1
                    if jawaban_user == soal['jawaban']:
                        st.session_state.skor += 1
                        st.markdown(f"<div class='success-box'>🎉 <strong>BENAR!</strong><br>{soal['penjelasan']}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='error-box'>❌ Salah. Benar: {soal['jawaban']}<br>{soal['penjelasan']}</div>", unsafe_allow_html=True)
            with col2:
                if st.button("💡 Penjelasan", key=f"hint_{idx}", use_container_width=True):
                    st.info(soal['penjelasan'])

# =========================
# 3. ANALISIS KESALAHAN
# =========================
elif menu == "🧠 Analisis Kesalahan":
    st.markdown("<h1 style='color:white;'>🧠 Analisis Kesalahan Praktikum</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1])
    with col1:
        masalah = st.selectbox("🎯 Pilih masalah:", ["Pilih salah satu...", "❌ Larutan tidak berubah warna", "❌ Hasil titrasi sangat berbeda", "⏱️ End point terlalu cepat"])
    with col2:
        if st.button("🔍 Analisis", use_container_width=True): st.session_state.analisis = True
    
    if 'analisis' in st.session_state and st.session_state.analisis:
        if masalah == "❌ Larutan tidak berubah warna":
            col1, col2, col3 = st.columns(3)
            with col1: st.markdown("### 🔴 Penyebab\n1. Indikator salah\n2. Reagen kadaluarsa")
            with col2: st.markdown("### 🟡 Solusi\n1. Verifikasi indikator\n2. Ganti reagen baru")
            with col3: st.markdown("### 🟢 Pencegahan\n✅ Catat kadaluarsa reagen")
        elif masalah == "❌ Hasil titrasi sangat berbeda":
            col1, col2, col3 = st.columns(3)
            with col1: st.markdown("### 🔴 Penyebab\n1. Baca meniskus salah\n2. Tidak homogen")
            with col2: st.markdown("### 🟡 Solusi\n1. Mata sejajar meniskus\n2. Aduk rata")
            with col3: st.markdown("### 🟢 Pencegahan\n✅ Latih pembacaan alat")

# =========================
# 4. PANDUAN LENGKAP
# =========================
elif menu == "📚 Panduan Lengkap":
    st.markdown("<h1 style='color:white;'>📚 Panduan & Referensi Lengkap</h1>", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["📖 Teori", "🧪 Teknik", "⚗️ Tabel Reaksi", "💡 Tips"])
    with tab1:
        st.markdown("### Rumus Dasar Pengenceran\n$C_1 \times V_1 = C_2 \times V_2$")
    with tab2:
        st.markdown("### Sebelum Praktikum\n- Gunakan APD Lengkap (Jas Lab, Kacamata, Sarung Tangan)")
    with tab3:
        data_reaksi = {
            "Reaksi": ["KMnO₄ (aq) + Fe²⁺", "Ag⁺ + Cl⁻", "Fe³⁺ + SCN⁻"],
            "Warna Produk": ["Tak berwarna", "Putih (endapan)", "Merah darah"],
            "Tipe Reaksi": ["Redoks", "Presipitasi", "Kompleksasi"]
        }
        st.dataframe(pd.DataFrame(data_reaksi), use_container_width=True, hide_index=True)
    with tab4:
        st.markdown("✅ **Persiapan matang** = 80% kesuksesan praktikum.")

# =========================
# CHEMSCAN
# =========================
elif menu == "🔬 ChemScan":
    st.title("🔬 ChemScan")
    bahan = st.selectbox("Pilih Bahan Kimia", list(chemical_db.keys()))
    data = chemical_db[bahan]
    st.subheader(data["nama"])
    st.write("🧪 Rumus :", data["rumus"])
    st.write("⚖️ Mr :", data["mr"])
    st.write("☣️ Bahaya :", data["bahaya"])
    st.write("🚨 Simbol :", data["simbol"])
    st.write("🥽 APD :", data["apd"])

# =========================
# REAKSI TITRASI
# =========================
elif menu == "⚗️ Reaksi Titrasi":
    st.title("⚗️ Reaksi Titrasi")
    jenis = st.selectbox("Pilih Jenis Titrasi", ["Asam Basa", "Permanganometri", "Argentometri"])
    if jenis == "Asam Basa":
        st.latex(r"HCl + NaOH \rightarrow NaCl + H_2O")
        st.success("Indikator PP: tidak berwarna → merah muda")
    elif jenis == "Permanganometri":
        st.latex(r"MnO_4^- + Fe^{2+} \rightarrow Fe^{3+} + Mn^{2+}")
        st.success("Warna ungu KMnO₄ menghilang")

# =========================
# QUIZ CENTER
# =========================
elif menu == "📝 Quiz Center":
    st.title("📝 Quiz Kimia")
    skor = 0
    q1 = st.radio("1. Larutan standar primer untuk NaOH?", ["NaCl", "KHP", "HCl"])
    q2 = st.radio("2. Warna larutan KMnO4?", ["Merah", "Ungu", "Biru"])
    if st.button("Periksa Jawaban"):
        if q1 == "KHP": skor += 1
        if q2 == "Ungu": skor += 1
        st.success(f"Skor Anda = {skor}/2")

st.divider()
# =========================
# FOOTER
# =========================
st.markdown(f""" <div style='text-align:center;padding:1.5rem;border-top:1px solid {theme['primary']};'> <p>🔬 <strong>SPEKTRA Mini Tools v1.0</strong> | © 2026</p> </div> """, unsafe_allow_html=True)
