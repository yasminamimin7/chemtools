import streamlit as st
import pandas as pd

from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="ðŸ§ª ChemLab Mini Tools",
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
        'bg_gradient': 'linear-gradient(135deg, #0b1320, #102a43, #1f6f8b, #2d9cdb)',
        'primary': '#2d9cdb',
        'secondary': '#1f6f8b',
        'accent': '#00d9ff',
        'text': '#e6f1ff',
        'input_bg': '#0f2740',
        'card_bg': 'rgba(10, 25, 47, 0.75)',
    },
    'sunset': {
        'bg_gradient': 'linear-gradient(135deg, #1a0f2e, #372d5a, #8b4789, #ff6b9d)',
        'primary': '#ff6b9d',
        'secondary': '#8b4789',
        'accent': '#ffd700',
        'text': '#ffe6f0',
        'input_bg': '#2d1b4e',
        'card_bg': 'rgba(26, 15, 46, 0.75)',
    },
    'forest': {
        'bg_gradient': 'linear-gradient(135deg, #0b1f15, #1a3d2a, #2d5a47, #52b788)',
        'primary': '#52b788',
        'secondary': '#2d5a47',
        'accent': '#74c69d',
        'text': '#e6f5f0',
        'input_bg': '#0f2d1f',
        'card_bg': 'rgba(11, 31, 21, 0.75)',
    }
}

theme = THEME_CONFIG[st.session_state.theme]

# =========================
# DYNAMIC STYLING
# =========================
st.markdown(f"""
    <style>
    /* Background Animation */
    .stApp {{
        background: {theme['bg_gradient']};
        background-size: 400% 400%;
        animation: gradientBG 14s ease infinite;
        color: {theme['text']};
    }}

    @keyframes gradientBG {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    /* Glass Container */
    .block-container {{
        padding: 2.5rem;
        border-radius: 20px;
        background-color: {theme['card_bg']};
        box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(45, 156, 219, 0.2);
    }}

    /* Text Colors */
    h1, h2, h3, h4, h5, h6, p, label, span, div {{
        color: {theme['text']} !important;
    }}

    /* Input Fields */
    div[data-baseweb="input"] input {{
        background-color: {theme['input_bg']} !important;
        color: {theme['text']} !important;
        border: 2px solid {theme['primary']} !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }}

    input::placeholder {{
        color: rgba(230, 241, 255, 0.5) !important;
    }}

    textarea {{
        background-color: {theme['input_bg']} !important;
        color: {theme['text']} !important;
        border: 2px solid {theme['primary']} !important;
        border-radius: 10px !important;
    }}

    /* Buttons */
    div.stButton > button {{
        background-color: {theme['primary']} !important;
        color: #0b1320 !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 12px 24px !important;
        transition: all 0.3s ease !important;
    }}

    div.stButton > button:hover {{
        background-color: {theme['accent']} !important;
        transform: translateY(-2px) !important;
        box-shadow: 0px 8px 16px rgba(45, 156, 219, 0.3) !important;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: rgba(10, 25, 47, 0.9) !important;
        border-right: 2px solid {theme['primary']} !important;
    }}

    /* Radio Buttons & Selectbox */
    div[role="radiogroup"] {{
        background-color: {theme['card_bg']} !important;
        padding: 15px !important;
        border-radius: 12px !important;
        border: 1px solid {theme['primary']} !important;
    }}

    /* Cards */
    .metric-card {{
        background: linear-gradient(135deg, {theme['secondary']}, {theme['primary']});
        padding: 25px;
        border-radius: 15px;
        color: {theme['text']};
        box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
        border: 1px solid {theme['accent']};
    }}

    .success-box {{
        background-color: rgba(76, 175, 80, 0.1);
        border-left: 5px solid #4CAF50;
        padding: 15px;
        border-radius: 8px;
        color: #4CAF50;
    }}

    .error-box {{
        background-color: rgba(244, 67, 54, 0.1);
        border-left: 5px solid #f44336;
        padding: 15px;
        border-radius: 8px;
        color: #f44336;
    }}

    /* Toolbar Hide */
    div[data-testid="stToolbar"] {{
        display: none !important;
    }}

    /* Divider */
    hr {{
        border: 1px solid {theme['primary']} !important;
        opacity: 0.5 !important;
    }}
    </style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR - THEME & NAVIGATION
# =========================
with st.sidebar:
    st.markdown(f"<h2 style='color:{theme['accent']};'>âš™ï¸ KONTROL PANEL</h2>", unsafe_allow_html=True)
    
    # Theme Selector
    st.subheader("ðŸŽ¨ Pilih Tema")
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
        if st.button("ðŸŒŠ Ocean", use_container_width=True):
            st.session_state.theme = 'ocean'
            st.rerun()
    with col2:
        if st.button("ðŸŒ… Sunset", use_container_width=True):
            st.session_state.theme = 'sunset'
            st.rerun()
    with col3:
        if st.button("ðŸŒ² Forest", use_container_width=True):
            st.session_state.theme = 'forest'
            st.rerun()
    
    st.divider()
    
    # Main Menu
    st.markdown(f"<h3 style='color:{theme['accent']};'>ðŸ“‹ MENU UTAMA</h3>", unsafe_allow_html=True)
    menu = st.selectbox(
        "Pilih Fitur:",
        [
            "ðŸ  Beranda",
            "ðŸ“Š Kalkulator Pengenceran",
            "ðŸŽ® Tebak Warna Reaksi",
            "ðŸ§  Analisis Kesalahan",
            "ðŸ“š Panduan Lengkap"
        ]
    )
    
    st.divider()
    st.markdown(f"### ðŸ“Œ Tentang Aplikasi")
    st.info("""
    *ChemLab Mini Tools v3.0*
    
    Platform pembelajaran kimia yang interaktif dan inspiratif!
    
    âœ¨ Fitur:
    â€¢ ðŸ§® Kalkulator pengenceran dinamis
    â€¢ ðŸŽ¯ Game quiz warna reaksi
    â€¢ ðŸ”§ Troubleshooting praktikum
    â€¢ ðŸŽ¨ 3 tema warna cantik
    â€¢ ðŸ“– Panduan lengkap
    """)

# =========================
# TITLE SECTION
# =========================
st.markdown(f"""
    <div style='text-align:center;margin-bottom:2rem;'>
        <h1 style='color:{theme['accent']};font-size:3rem;margin:0;'>ðŸ§ª ChemLab Mini Tools</h1>
        <p style='color:{theme['primary']};font-size:1.2rem;margin-top:0.5rem;'>
            âœ¨ Belajar Kimia Lebih Seru dan Interaktif âœ¨
        </p>
    </div>
""", unsafe_allow_html=True)

# =========================
# HOME PAGE
# =========================
if menu == "ðŸ  Beranda":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>ðŸ“Š Kalkulator</h3>
            <p>Hitung pengenceran larutan dengan rumus Mâ‚Vâ‚ = Mâ‚‚Vâ‚‚ secara akurat dan cepat</p>
            <p style='font-size:0.9rem;opacity:0.8;'>ðŸ’¡ Hemat waktu perhitungan!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>ðŸŽ® Game Quiz</h3>
            <p>Asah pengetahuan dengan game interaktif tebak warna reaksi kimia</p>
            <p style='font-size:0.9rem;opacity:0.8;'>ðŸ† Raih skor tertinggi!</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <h3>ðŸ”§ Troubleshooting</h3>
            <p>Analisis kesalahan praktikum dan temukan solusi terbaik</p>
            <p style='font-size:0.9rem;opacity:0.8;'>âœ… Praktikum sukses!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        ### ðŸŒŸ Mengapa Pilih ChemLab?
        
        âœ… *User-Friendly* - Interface yang mudah digunakan untuk semua level
        
        âœ… *Interaktif* - Belajar sambil bermain dengan cara yang menyenangkan
        
        âœ… *Akurat* - Perhitungan presisi dengan validasi data lengkap
        
        âœ… *Visualisasi* - Grafik dan animasi untuk memahami konsep
        
        âœ… *Responsif* - Bekerja sempurna di desktop dan mobile
        """)
    
    with col2:
        st.markdown(f"""
        ### ðŸŽ¨ Fitur Tema Dinamis
        
        Pilih tema favorit Anda di sidebar!
        
        ðŸŒŠ *Ocean* - Tema biru menenangkan
        
        ðŸŒ… *Sunset* - Tema ungu hangat
        
        ðŸŒ² *Forest* - Tema hijau segar
        
        ### ðŸ’¡ Tips Memulai
        
        1. Pilih fitur di menu samping
        2. Ikuti panduan step-by-step
        3. Gunakan riwayat untuk review
        4. Bagikan hasil dengan teman!
        """)

# =========================
# 1. KALKULATOR PENGENCERAN
# =========================
elif menu == "ðŸ“Š Kalkulator Pengenceran":
    st.markdown(f"<h1 style='color:{theme['accent']};'>ðŸ“Š Kalkulator Pengenceran</h1>", unsafe_allow_html=True)
    
    # Formula Display
    st.markdown(f"""
    <div style='background-color:{theme['secondary']};padding:20px;border-radius:12px;text-align:center;'>
        <h2 style='color:{theme['accent']};margin:0;'>Câ‚ Ã— Vâ‚ = Câ‚‚ Ã— Vâ‚‚</h2>
        <p style='margin-top:10px;opacity:0.9;'>Rumus dasar pengenceran larutan</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    if "history" not in st.session_state:
        st.session_state.history = []
    
    # Input Section
    col1, col2 = st.columns(2)
    
    with col1:
        satuan = st.selectbox("ðŸ“ Satuan Volume", ["mL", "L", "Î¼L"])
        satuan_konsentrasi = st.selectbox("âš—ï¸ Satuan Konsentrasi", ["M (Molar)", "N (Normal)", "g/L"])
    
    with col2:
        cari = st.selectbox("ðŸ” Variabel yang Dicari", ["Vâ‚‚ (Volume Akhir)", "Câ‚ (Konsentrasi Awal)", "Câ‚‚ (Konsentrasi Akhir)", "Vâ‚ (Volume Awal)"])
    
    st.divider()
    
    # Calculations
    if cari == "Vâ‚‚ (Volume Akhir)":
        st.subheader("ðŸ“ Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            C1 = st.number_input(f"Câ‚ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            V1 = st.number_input(f"Vâ‚ ({satuan})", value=None, placeholder="Misal: 100")
        with col3:
            C2 = st.number_input(f"Câ‚‚ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        
        if st.button("ðŸ§® Hitung Vâ‚‚", use_container_width=True):
            if None in (C1, V1, C2):
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif C2 == 0:
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Câ‚‚ tidak boleh nol! Periksa kembali data Anda.
                </div>
                """, unsafe_allow_html=True)
            else:
                V2 = (C1 * V1) / C2
                hasil = f"Vâ‚‚ = {V2:.3f} {satuan}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C1} Ã— {V1}) Ã· {C2}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    âœ… <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C1} Ã— {V1}) Ã· {C2}</span>
                </div>
                """, unsafe_allow_html=True)
                
                st.info(f"ðŸ’¡ Artinya: Encerkan {V1} {satuan} larutan {C1} {satuan_konsentrasi} dengan menambahkan air hingga totalnya {V2:.3f} {satuan}")
    
    elif cari == "Câ‚ (Konsentrasi Awal)":
        st.subheader("ðŸ“ Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            V1 = st.number_input(f"Vâ‚ ({satuan})", value=None, placeholder="Misal: 100")
        with col2:
            C2 = st.number_input(f"Câ‚‚ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        with col3:
            V2 = st.number_input(f"Vâ‚‚ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("ðŸ§® Hitung Câ‚", use_container_width=True):
            if None in (V1, C2, V2):
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif V1 == 0:
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Vâ‚ tidak boleh nol!
                </div>
                """, unsafe_allow_html=True)
            else:
                C1 = (C2 * V2) / V1
                hasil = f"Câ‚ = {C1:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C2} Ã— {V2}) Ã· {V1}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    âœ… <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C2} Ã— {V2}) Ã· {V1}</span>
                </div>
                """, unsafe_allow_html=True)
    
    elif cari == "Câ‚‚ (Konsentrasi Akhir)":
        st.subheader("ðŸ“ Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            C1 = st.number_input(f"Câ‚ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            V1 = st.number_input(f"Vâ‚ ({satuan})", value=None, placeholder="Misal: 100")
        with col3:
            V2 = st.number_input(f"Vâ‚‚ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("ðŸ§® Hitung Câ‚‚", use_container_width=True):
            if None in (C1, V1, V2):
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif V2 == 0:
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Vâ‚‚ tidak boleh nol!
                </div>
                """, unsafe_allow_html=True)
            else:
                C2 = (C1 * V1) / V2
                hasil = f"Câ‚‚ = {C2:.4f} {satuan_konsentrasi}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C1} Ã— {V1}) Ã· {V2}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    âœ… <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C1} Ã— {V1}) Ã· {V2}</span>
                </div>
                """, unsafe_allow_html=True)
    
    elif cari == "Vâ‚ (Volume Awal)":
        st.subheader("ðŸ“ Masukkan Data Anda")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            C1 = st.number_input(f"Câ‚ ({satuan_konsentrasi})", value=None, placeholder="Misal: 2.5")
        with col2:
            C2 = st.number_input(f"Câ‚‚ ({satuan_konsentrasi})", value=None, placeholder="Misal: 0.5")
        with col3:
            V2 = st.number_input(f"Vâ‚‚ ({satuan})", value=None, placeholder="Misal: 500")
        
        if st.button("ðŸ§® Hitung Vâ‚", use_container_width=True):
            if None in (C1, C2, V2):
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Semua kolom harus diisi! Lengkapi data terlebih dahulu.
                </div>
                """, unsafe_allow_html=True)
            elif C1 == 0:
                st.markdown("""
                <div class='error-box'>
                    âš ï¸ Câ‚ tidak boleh nol!
                </div>
                """, unsafe_allow_html=True)
            else:
                V1 = (C2 * V2) / C1
                hasil = f"Vâ‚ = {V1:.3f} {satuan}"
                st.session_state.history.append({
                    'waktu': datetime.now().strftime("%H:%M:%S"),
                    'hasil': hasil,
                    'rumus': f"({C2} Ã— {V2}) Ã· {C1}"
                })
                
                st.markdown(f"""
                <div class='success-box'>
                    âœ… <strong>{hasil}</strong><br>
                    <span style='font-size:0.9rem;'>Rumus: ({C2} Ã— {V2}) Ã· {C1}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # History Section
    st.divider()
    st.subheader("ðŸ“œ Riwayat Perhitungan")
    
    if st.session_state.history:
        history_df = pd.DataFrame(reversed(st.session_state.history))
        st.dataframe(history_df, use_container_width=True, hide_index=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("ðŸ—‘ï¸ Hapus Semua Riwayat", use_container_width=True):
                st.session_state.history = []
                st.rerun()
        with col2:
            st.info(f"ðŸ“Š Total perhitungan: {len(st.session_state.history)}")
    else:
        st.markdown("""
        <div style='text-align:center;padding:2rem;opacity:0.7;'>
            <p>Belum ada perhitungan ðŸ“­</p>
            <p style='font-size:0.9rem;'>Mulai hitung di atas untuk melihat riwayat</p>
        </div>
        """, unsafe_allow_html=True)

# =========================
# 2. TEBAK WARNA REAKSI
# =========================
elif menu == "ðŸŽ® Tebak Warna Reaksi":
    st.markdown(f"<h1 style='color:{theme['accent']};'>ðŸŽ® Game Tebak Warna Reaksi</h1>", unsafe_allow_html=True)
    st.write("ðŸ† Asah pengetahuan kimia Anda dengan menjawab pertanyaan tentang warna produk reaksi!")
    
    if 'skor' not in st.session_state:
        st.session_state.skor = 0
        st.session_state.total = 0
    
    soal_list = [
        {
            "pertanyaan": "KMnOâ‚„ (ungu pekat) + FeÂ²âº â†’ produk berwarna?",
            "pilihan": ["Ungu pekat", "Tak berwarna", "Coklat tua", "Hijau"],
            "jawaban": "Tak berwarna",
            "penjelasan": "KMnOâ‚„ yang ungu tereduksi menjadi MnÂ²âº yang tidak berwarna. Warna ungu hilang total! ðŸŽ¨"
        },
        {
            "pertanyaan": "Agâº + Clâ» â†’ endapan berwarna?",
            "pilihan": ["Putih", "Kuning", "Biru", "Merah"],
            "jawaban": "Putih",
            "penjelasan": "AgCl membentuk endapan putih yang sangat tidak larut dalam air. Produk klasik titrasi argentometri! âšª"
        },
        {
            "pertanyaan": "Iâ‚‚ dalam larutan air â†’ warna?",
            "pilihan": ["Bening", "Coklat gelap", "Merah cerah", "Kuning pucat"],
            "jawaban": "Coklat gelap",
            "penjelasan": "Iodium dalam air membentuk larutan coklat kemerahan yang intens. Warna khas dan mudah dikenali! ðŸŸ¤"
        },
        {
            "pertanyaan": "CuSOâ‚„ + NaOH berlebih â†’ endapan?",
            "pilihan": ["Putih murni", "Biru muda", "Biru gelap", "Tidak ada endapan"],
            "jawaban": "Biru gelap",
            "penjelasan": "Cu(OH)â‚‚ membentuk endapan biru yang indah. Warna kompleks tembaga yang ikonik! ðŸ”µ"
        },
        {
            "pertanyaan": "FeÂ³âº + SCNâ» â†’ larutan berwarna?",
            "pilihan": ["Kuning", "Merah darah", "Ungu", "Hijau"],
            "jawaban": "Merah darah",
            "penjelasan": "Kompleks [Fe(SCN)]Â²âº memberikan warna merah darah yang kuat. Sangat sensitif untuk deteksi FeÂ³âº! ðŸ”´"
        }
    ]
    
    # Score Display
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("ðŸ† Skor", st.session_state.skor)
    with col2:
        st.metric("â“ Total", st.session_state.total)
    with col3:
        if st.session_state.total > 0:
            akurasi = (st.session_state.skor / st.session_state.total) * 100
            st.metric("ðŸ“Š Akurasi", f"{akurasi:.0f}%")
    
    st.divider()
    
    # Questions in Tabs
    tabs = st.tabs([f"Soal {i+1}" for i in range(len(soal_list))])
    
    for idx, (tab, soal) in enumerate(zip(tabs, soal_list)):
        with tab:
            st.markdown(f"<h3 style='color:{theme['accent']};'>â“ {soal['pertanyaan']}</h3>", unsafe_allow_html=True)
            
            jawaban_user = st.radio(
                "Pilih jawaban Anda:",
                soal['pilihan'],
                key=f"soal_{idx}",
                label_visibility="collapsed"
            )
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"âœ… Cek Jawaban", key=f"check_{idx}", use_container_width=True):
                    st.session_state.total += 1
                    
                    if jawaban_user == soal['jawaban']:
                        st.session_state.skor += 1
                        st.markdown(f"""
                        <div class='success-box'>
                            ðŸŽ‰ <strong>BENAR!</strong><br>
                            {soal['penjelasan']}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.markdown(f"""
                        <div class='error-box'>
                            âŒ Jawaban Salah<br>
                            <strong>Jawaban Benar:</strong> {soal['jawaban']}<br>
                            {soal['penjelasan']}
                        </div>
                        """, unsafe_allow_html=True)
            
            with col2:
                if st.button("ðŸ’¡ Lihat Penjelasan", key=f"hint_{idx}", use_container_width=True):
                    st.info(soal['penjelasan'])

# =========================
# 3. ANALISIS KESALAHAN
# =========================
elif menu == "ðŸ§  Analisis Kesalahan":
    st.markdown(f"<h1 style='color:{theme['accent']};'>ðŸ§  Analisis Kesalahan Praktikum</h1>", unsafe_allow_html=True)
    st.write("ðŸ” Hadapi masalah saat praktikum? Dapatkan analisis dan solusi terbaik di sini!")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        masalah = st.selectbox(
            "ðŸŽ¯ Pilih masalah yang Anda alami:",
            [
                "Pilih salah satu...",
                "âŒ Larutan tidak berubah warna",
                "âŒ Hasil titrasi sangat berbeda",
                "â±ï¸ End point terlalu cepat",
                "ðŸ§‚ Kristal tidak terbentuk",
                "ðŸ«§ Gas tidak keluar"
            ]
        )
    
    with col2:
        if st.button("ðŸ” Analisis", use_container_width=True):
            st.session_state.analisis = True
    
    st.divider()
    
    if 'analisis' in st.session_state and st.session_state.analisis:
        if masalah == "Pilih salah satu...":
            st.markdown("""
            <div class='error-box'>
                âš ï¸ Silakan pilih masalah terlebih dahulu untuk mendapat analisis
            </div>
            """, unsafe_allow_html=True)
        
        elif masalah == "âŒ Larutan tidak berubah warna":
            st.markdown(f"<h3 style='color:{theme['accent']};'>ðŸ“‹ Analisis Masalah</h3>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                ### ðŸ”´ Kemungkinan Penyebab
                1. *Indikator salah* - Pilih indikator yang tepat
                2. *Reagen sudah kedaluarsa* - Cek tanggal kadaluarsa
                3. *pH tidak sesuai* - Larutan terlalu asam/basa
                4. *Konsentrasi terlalu rendah* - Tambah konsentrasi
                """)
            
            with col2:
                st.markdown(f"""
                ### ðŸŸ¡ Solusi Praktis
                1. *Verifikasi indikator* - Gunakan indikator yang benar
                2. *Ganti reagen* - Ambil dari botol baru
                3. *Atur pH* - Gunakan buffer atau buffer solution
                4. *Periksa reagen* - Pastikan kualitas bahan baik
                5. *Uji pendahuluan* - Lakukan uji sebelum titrasi
                """)
            
            with col3:
                st.markdown(f"""
                ### ðŸŸ¢ Pencegahan Ke Depan
                âœ… Catat tanggal kadaluarsa reagen
                
                âœ… Simpan di tempat gelap & sejuk
                
                âœ… Gunakan wadah tertutup rapat
                
                âœ… Baca SOP dengan teliti
                
                âœ… Lakukan titrasi minimal 3x
                """)
        
        elif masalah == "âŒ Hasil titrasi sangat berbeda":
            st.markdown(f"<h3 style='color:{theme['accent']};'>ðŸ“‹ Analisis Masalah</h3>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                ### ðŸ”´ Kemungkinan Penyebab
                1. *Kesalahan pembacaan* - Baca meniskus salah
                2. *Larutan tidak homogen* - Belum tercampur rata
                3. *Teknik pipet salah* - Pegang pipet tidak vertikal
                4. *Buret tidak dikalibrasi* - Presisi alat kurang
                5. *Pengocokan berlebihan* - Terlalu cepat
                """)
            
            with col2:
                st.markdown(f"""
                ### ðŸŸ¡ Solusi Praktis
                1. *Baca dengan hati-hati* - Mata sejajar dengan meniskus
                2. *Aduk perlahan* - Gunakan pengaduk sampai homogen
                3. *Pegang pipet vertikal* - Jangan miring
                4. *Kalibrasikan alat* - Periksa keakuratan buret
                5. *Ambil rata-rata* - Gunakan 3 hasil yang dekat
                """)
            
            with col3:
                st.markdown(f"""
                ### ðŸŸ¢ Pencegahan Ke Depan
                âœ… Latih pembacaan meniskus
                
                âœ… Gunakan lampu untuk pembacaan
                
                âœ… Cuci alat hingga bersih
                
                âœ… Kalibrasi alat berkala
                
                âœ… Lakukan warming up practice
                """)

# =========================
# 4. PANDUAN LENGKAP
# =========================
elif menu == "ðŸ“š Panduan Lengkap":
    st.markdown(f"<h1 style='color:{theme['accent']};'>ðŸ“š Panduan & Referensi Lengkap</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["ðŸ“– Teori", "ðŸ§ª Teknik Praktikum", "âš—ï¸ Tabel Reaksi", "ðŸ’¡ Tips & Trik"])
    
    with tab1:
        st.subheader("ðŸ“– Teori Dasar Pengenceran & Titrasi")
        st.markdown("""
        ### 1ï¸âƒ£ Pengenceran Larutan (Dilution)
        *Definisi*: Proses menambahkan pelarut untuk menurunkan konsentrasi larutan
        
        *Prinsip Penting*:
        - âœ… Mol zat terlarut tetap sama
        - âœ… Volume larutan bertambah
        - âœ… Konsentrasi berkurang
        - âœ… Energi diberikan saat pencampuran
        
        *Rumus*: Câ‚Vâ‚ = Câ‚‚Vâ‚‚
        
        ### 2ï¸âƒ£ Titrasi (Titration)
        *Definisi*: Teknik analisis untuk menentukan konsentrasi larutan
        
        *Jenis Titrasi*:
        - Titrasi Asam-Basa
        - Titrasi Redoks
        - Titrasi Kompleksometri
        - Titrasi Presipitasi
        
        *Syarat End Point*:
        - âœ… Perubahan warna indikator yang jelas
        - âœ… Perubahan warna tidak kembali saat diaduk
        - âœ… Dilakukan minimal 3 kali
        """)
    
    with tab2:
        st.subheader("ðŸ§ª Teknik Praktikum yang Benar")
        st.markdown("""
        ### âœï¸ Sebelum Praktikum
        - ðŸ“‹ Baca SOP dengan teliti dan lengkap
        - ðŸ” Pahami teori reaksi yang akan dilakukan
        - ðŸ“ Siapkan format pengisian data
        - ðŸ§¤ Siapkan APD lengkap (jas lab, sarung tangan, kacamata, sepatu tertutup)
        
        ### âš—ï¸ Saat Praktikum
        - ðŸ‘€ Amati setiap perubahan dengan cermat
        - ðŸ“ Catat data secara real-time (jangan mengandalkan ingatan)
        - ðŸ§¼ Cuci alat setelah digunakan
        - â±ï¸ Catat waktu jika diperlukan
        - ðŸš¨ Minta bantuan jika ada yang tidak jelas
        
        ### ðŸ“Š Setelah Praktikum
        - ðŸ”¢ Analisis data dengan statistik yang tepat
        - ðŸ“š Bandingkan hasil dengan literatur
        - ðŸ“‹ Tulis laporan yang jelas dan terstruktur
        - ðŸ¤” Diskusikan kesalahan dan perbaikan
        """)
    
    with tab3:
        st.subheader("âš—ï¸ Tabel Reaksi Kimia & Warnanya")
        
        data_reaksi = {
            "Reaksi": [
                "KMnOâ‚„ (aq) + FeÂ²âº",
                "Agâº + Clâ»",
                "Iâ‚‚ dalam Hâ‚‚O",
                "CuSOâ‚„ + NaOH (berlebih)",
                "FeÂ³âº + SCNâ»",
                "Kâ‚„[Fe(CN)â‚†] + FeÂ³âº",
                "CuÂ²âº + NHâ‚ƒ",
                "BaÂ²âº + SOâ‚„Â²â»"
            ],
            "Warna Produk": [
                "Tak berwarna (ungu â†’ hilang)",
                "Putih (endapan)",
                "Coklat gelap",
                "Biru tua (endapan)",
                "Merah darah",
                "Biru Prusia",
                "Biru terang",
                "Putih (endapan)"
            ],
            "Tipe Reaksi": [
                "Redoks",
                "Presipitasi",
                "Fisika",
                "Presipitasi",
                "Kompleksasi",
                "Kompleksasi",
                "Kompleksasi",
                "Presipitasi"
            ],
            "Keterangan": [
                "Reduksi permanganat",
                "AgCl tidak larut",
                "Iâ‚‚ berwarna",
                "Cu(OH)â‚‚ biru",
                "Kompleks Fe-tiosenat",
                "Kompleks besi sianida",
                "Kompleks ammin Cu",
                "BaSOâ‚„ tidak larut"
            ]
        }
        
        df = pd.DataFrame(data_reaksi)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    with tab4:
        st.subheader("ðŸ’¡ Tips & Trik Sukses Praktikum")
        st.markdown(f"""
        ### ðŸ† Tips Umum
        âœ… *Persiapan matang* = 80% kesuksesan praktikum
        
        âœ… *Teliti saat pembacaan* = Hasil akurat terjamin
        
        âœ… *Catat semua data* = Bahan analisis yang lengkap
        
        ### ðŸŽ¯ Tips Spesifik Titrasi
        1. *Warming Up*: Lakukan 1-2 titrasi pendahuluan
        2. *Blank Correction*: Catat volume awal buret dengan teliti
        3. *Konsistensi*: Gunakan teknik yang sama untuk semua titrasi
        4. *Penghitungan*: Gunakan data yang konsisten (RSD < 5%)
        
        ### ðŸ”¬ Tips Pembacaan Alat
        - *Meniskus*: Baca bagian bawah untuk cairan bening
        - *Mata Sejajar*: Posisi mata harus sejajar dengan garis skala
        - *Pencahayaan*: Gunakan lampu yang cukup
        - *Stabilitas*: Tunggu hingga meniskus stabil sebelum membaca
        
        ### âš¡ Troubleshooting Cepat
        | Masalah | Solusi |
        |---------|--------|
        | Warna tidak muncul | Ubah indikator atau pH |
        | Hasil sangat berbeda | Ulangi dengan teknik lebih hati-hati |
        | End point susah dilihat | Gunakan cahaya lebih baik |
        | Konsentrasi tidak akurat | Kalibrasi ulang larutan standar |
        """)

st.divider()

# =========================
# FOOTER
# =========================
st.markdown(f"""
<div style='text-align:center;padding:2rem;opacity:0.8;border-top:1px solid {theme['primary']};margin-top:2rem;'>
    <p style='font-size:1.1rem;color:{theme['accent']};'>ðŸ§ª <strong>ChemLab Mini Tools v3.0</strong> ðŸ§ª</p>
    <p style='margin-top:0.5rem;'>âœ¨ Belajar Kimia Lebih Seru dan Interaktif âœ¨</p>
    <p style='margin-top:1rem;font-size:0.9rem;opacity:0.7;'>
        Tema Aktif: <strong>{st.session_state.theme.upper()}</strong> | 
        Â© 2026 | Platform Pembelajaran Kimia Interaktif
    </p>
    <p style='font-size:0.85rem;opacity:0.6;margin-top:0.5rem;'>
        ðŸ’¡ Tips: Gunakan aplikasi ini sebagai pendamping belajar, bukan pengganti guru!
    </p>
</div>
""", unsafe_allow_html=True)
