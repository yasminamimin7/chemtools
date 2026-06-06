import streamlit as st
import os
from pathlib import Path

# ==========================
# PAGE CONFIG
# ==========================
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
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .stApp {
        background: #f0f2f6;
    }
    
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .header-container h1 {
        font-size: 2.5em;
        margin-bottom: 10px;
    }
    
    .header-container p {
        font-size: 1.1em;
        opacity: 0.9;
    }
    
    .feature-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 15px 0;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    .metric-box {
        padding: 20px;
        border-radius: 12px;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 4px solid #667eea;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin: 10px 5px;
    }
    
    .divider {
        margin: 30px 0;
        border-top: 2px solid #667eea;
    }
    
    h1, h2, h3 {
        color: #2d3748;
    }
    
    .info-box {
        background: #e6f2ff;
        border-left: 4px solid #667eea;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================
st.markdown("""
<div class="header-container">
    <h1>🧪 SPEKTRA</h1>
    <p>Smart Platform for Chemical Analysis and Laboratory Tools</p>
    <p style="font-size: 0.9em; margin-top: 10px;">Platform terintegrasi untuk analisis kimia, manajemen laboratorium, dan pembelajaran interaktif</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# MAIN CONTENT
# ==========================
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🧪 Kalkulator Pengenceran</h3>
        <p>Hitung pengenceran larutan dengan mudah menggunakan rumus M1V1 = M2V2. Fitur ini membantu Anda menentukan volume dan konsentrasi yang tepat untuk pengenceran larutan.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📝 Quiz Center</h3>
        <p>Uji pemahaman Anda tentang kimia melalui quiz interaktif. Bank soal lengkap dengan pembahasan untuk meningkatkan pengetahuan Anda.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🔬 ChemScan</h3>
        <p>Database lengkap bahan kimia dengan informasi detail: sifat, bahaya, APD, penyimpanan, reaktivitas, dan tindakan darurat darurat.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📚 Materi Kuliah</h3>
        <p>Akses materi pembelajaran kimia yang komprehensif dengan penjelasan detail, rumus, dan contoh soal untuk berbagai topik.</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# STATISTICS
# ==========================
st.markdown("---")
st.header("📊 Platform Statistics")

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.markdown("""
    <div class="metric-box">
        <h3>500+</h3>
        <p>Bahan Kimia</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col2:
    st.markdown("""
    <div class="metric-box">
        <h3>50+</h3>
        <p>Quiz Soal</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col3:
    st.markdown("""
    <div class="metric-box">
        <h3>100+</h3>
        <p>Materi Pembelajaran</p>
    </div>
    """, unsafe_allow_html=True)

with stat_col4:
    st.markdown("""
    <div class="metric-box">
        <h3>24/7</h3>
        <p>Akses Penuh</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# FOOTER
# ==========================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>SPEKTRA © 2026 | Smart Platform for Chemical Analysis and Laboratory Tools</p>
    <p style="font-size: 0.9em;">Dikembangkan dengan ❤️ untuk kemajuan pendidikan kimia</p>
</div>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR INFO
# ==========================
with st.sidebar:
    st.markdown("### 📋 Menu Navigasi")
    st.markdown("""
    - 🧪 **Kalkulator Pengenceran** - Hitung pengenceran larutan
    - 🔬 **ChemScan** - Database bahan kimia
    - 📝 **Quiz Center** - Uji pemahaman
    - 📚 **Materi Kuliah** - Pelajari kimia
    """)
    
    st.divider()
    
    st.markdown("### ℹ️ Tentang SPEKTRA")
    st.markdown("""
    **Versi:** 1.0.0  
    **Platform:** Streamlit  
    **Lisensi:** Apache 2.0  
    
    Hubungi kami untuk saran dan masukan!
    """)
