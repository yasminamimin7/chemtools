import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="SPEKTRA - Kalkulator Pengenceran",
    page_icon="🧪",
    layout="wide"
)

st.markdown("""
<style>
    .calculator-container {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    
    .result-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .info-box {
        background: #e6f2ff;
        border-left: 4px solid #667eea;
        padding: 15px;
        border-radius: 8px;
        margin: 15px 0;
    }
    
    .formula {
        background: #f5f5f5;
        padding: 15px;
        border-radius: 8px;
        font-family: monospace;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧪 Kalkulator Pengenceran")
st.markdown("Hitung pengenceran larutan menggunakan rumus M1V1 = M2V2")

st.markdown("---")

# Pilihan metode perhitungan
st.subheader("📐 Pilih Metode Perhitungan")

method = st.radio(
    "Apa yang ingin Anda hitung?",
    ["Hitung Volume Akhir (V2)", "Hitung Konsentrasi Akhir (M2)", "Hitung Konsentrasi Awal (M1)", "Hitung Volume Awal (V1)"],
    horizontal=True
)

st.markdown("---")

st.subheader("📊 Masukkan Data")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='info-box'><strong>ℹ️ Rumus Pengenceran:</strong><br>M1 × V1 = M2 × V2</div>", unsafe_allow_html=True)
    st.markdown("""
    **Keterangan:**
    - **M1** = Konsentrasi awal (mol/L)
    - **V1** = Volume awal (mL)
    - **M2** = Konsentrasi akhir (mol/L)
    - **V2** = Volume akhir (mL)
    """)

with col2:
    st.markdown("<div class='info-box'><strong>💡 Tips Penggunaan:</strong></div>", unsafe_allow_html=True)
    st.markdown("""
    1. Pastikan satuan konsentrasi konsisten
    2. Masukkan semua nilai yang diketahui
    3. Biarkan kolom yang ingin dicari kosong
    4. Klik tombol Hitung untuk mendapatkan hasil
    """)

st.markdown("---")

# Input berdasarkan metode yang dipilih
st.subheader("🔢 Input Data")

if method == "Hitung Volume Akhir (V2)":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        m1 = st.number_input("M1 - Konsentrasi Awal (mol/L)", min_value=0.0, value=1.0, step=0.1)
    
    with col2:
        v1 = st.number_input("V1 - Volume Awal (mL)", min_value=0.0, value=100.0, step=10.0)
    
    with col3:
        m2 = st.number_input("M2 - Konsentrasi Akhir (mol/L)", min_value=0.0, value=0.5, step=0.1)
    
    if st.button("🔍 Hitung V2", use_container_width=True):
        if m2 == 0:
            st.error("❌ Konsentrasi akhir (M2) tidak boleh 0!")
        else:
            v2 = (m1 * v1) / m2
            
            st.markdown(f"""
            <div class='result-box'>
                <h3>✅ Hasil Perhitungan</h3>
                <p><strong>Volume Akhir (V2) = {v2:.2f} mL</strong></p>
                <hr>
                <p><strong>Cara Kerja:</strong></p>
                <p>V2 = (M1 × V1) / M2</p>
                <p>V2 = ({m1} × {v1}) / {m2}</p>
                <p>V2 = {m1 * v1} / {m2}</p>
                <p>V2 = {v2:.2f} mL</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Rekomendasi
            st.markdown("<div class='info-box'><strong>💧 Rekomendasi Pengenceran:</strong></div>", unsafe_allow_html=True)
            volume_pelarut = v2 - v1
            st.markdown(f"""
            1. **Ambil {v1:.2f} mL** larutan dengan konsentrasi {m1} mol/L
            2. **Masukkan ke dalam labu ukur** yang sesuai
            3. **Tambahkan pelarut sebanyak {volume_pelarut:.2f} mL** hingga mencapai tanda batas
            4. **Tutup dan campur dengan baik**
            5. **Hasil akhir: {v2:.2f} mL** larutan dengan konsentrasi {m2} mol/L
            """)

elif method == "Hitung Konsentrasi Akhir (M2)":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        m1 = st.number_input("M1 - Konsentrasi Awal (mol/L)", min_value=0.0, value=1.0, step=0.1)
    
    with col2:
        v1 = st.number_input("V1 - Volume Awal (mL)", min_value=0.0, value=100.0, step=10.0)
    
    with col3:
        v2 = st.number_input("V2 - Volume Akhir (mL)", min_value=0.0, value=500.0, step=10.0)
    
    if st.button("🔍 Hitung M2", use_container_width=True):
        if v2 == 0:
            st.error("❌ Volume akhir (V2) tidak boleh 0!")
        else:
            m2 = (m1 * v1) / v2
            
            st.markdown(f"""
            <div class='result-box'>
                <h3>✅ Hasil Perhitungan</h3>
                <p><strong>Konsentrasi Akhir (M2) = {m2:.4f} mol/L</strong></p>
                <hr>
                <p><strong>Cara Kerja:</strong></p>
                <p>M2 = (M1 × V1) / V2</p>
                <p>M2 = ({m1} × {v1}) / {v2}</p>
                <p>M2 = {m1 * v1} / {v2}</p>
                <p>M2 = {m2:.4f} mol/L</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Faktor pengenceran
            faktor = v2 / v1
            st.markdown(f"""
            <div class='info-box'>
            <strong>📌 Faktor Pengenceran:</strong><br>
            Faktor pengenceran = V2 / V1 = {v2} / {v1} = {faktor:.1f}x
            </div>
            """, unsafe_allow_html=True)

elif method == "Hitung Konsentrasi Awal (M1)":
    col1, col2, col3 = st.columns(3)
    
    with col1:
        v1 = st.number_input("V1 - Volume Awal (mL)", min_value=0.0, value=100.0, step=10.0)
    
    with col2:
        m2 = st.number_input("M2 - Konsentrasi Akhir (mol/L)", min_value=0.0, value=0.5, step=0.1)
    
    with col3:
        v2 = st.number_input("V2 - Volume Akhir (mL)", min_value=0.0, value=500.0, step=10.0)
    
    if st.button("🔍 Hitung M1", use_container_width=True):
        if v1 == 0:
            st.error("❌ Volume awal (V1) tidak boleh 0!")
        else:
            m1 = (m2 * v2) / v1
            
            st.markdown(f"""
            <div class='result-box'>
                <h3>✅ Hasil Perhitungan</h3>
                <p><strong>Konsentrasi Awal (M1) = {m1:.4f} mol/L</strong></p>
                <hr>
                <p><strong>Cara Kerja:</strong></p>
                <p>M1 = (M2 × V2) / V1</p>
                <p>M1 = ({m2} × {v2}) / {v1}</p>
                <p>M1 = {m2 * v2} / {v1}</p>
                <p>M1 = {m1:.4f} mol/L</p>
            </div>
            """, unsafe_allow_html=True)

else:  # Hitung Volume Awal (V1)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        m1 = st.number_input("M1 - Konsentrasi Awal (mol/L)", min_value=0.0, value=1.0, step=0.1)
    
    with col2:
        m2 = st.number_input("M2 - Konsentrasi Akhir (mol/L)", min_value=0.0, value=0.5, step=0.1)
    
    with col3:
        v2 = st.number_input("V2 - Volume Akhir (mL)", min_value=0.0, value=500.0, step=10.0)
    
    if st.button("🔍 Hitung V1", use_container_width=True):
        if m1 == 0:
            st.error("❌ Konsentrasi awal (M1) tidak boleh 0!")
        else:
            v1 = (m2 * v2) / m1
            
            st.markdown(f"""
            <div class='result-box'>
                <h3>✅ Hasil Perhitungan</h3>
                <p><strong>Volume Awal (V1) = {v1:.2f} mL</strong></p>
                <hr>
                <p><strong>Cara Kerja:</strong></p>
                <p>V1 = (M2 × V2) / M1</p>
                <p>V1 = ({m2} × {v2}) / {m1}</p>
                <p>V1 = {m2 * v2} / {m1}</p>
                <p>V1 = {v1:.2f} mL</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# Contoh perhitungan
st.subheader("📚 Contoh Perhitungan")

with st.expander("📖 Lihat Contoh"):
    st.markdown("""
    ### Contoh 1: Hitung Volume Akhir
    **Soal:** Anda memiliki 100 mL larutan HCl dengan konsentrasi 2 mol/L. Berapa volume akhir jika ingin membuat larutan dengan konsentrasi 0.5 mol/L?
    
    **Penyelesaian:**
    - M1 = 2 mol/L
    - V1 = 100 mL
    - M2 = 0.5 mol/L
    - V2 = ?
    
    V2 = (M1 × V1) / M2 = (2 × 100) / 0.5 = 200 / 0.5 = **400 mL**
    
    ---
    
    ### Contoh 2: Hitung Konsentrasi Akhir
    **Soal:** 50 mL larutan NaOH 2 mol/L diencerkan menjadi 250 mL. Berapa konsentrasi akhirnya?
    
    **Penyelesaian:**
    - M1 = 2 mol/L
    - V1 = 50 mL
    - V2 = 250 mL
    - M2 = ?
    
    M2 = (M1 × V1) / V2 = (2 × 50) / 250 = 100 / 250 = **0.4 mol/L**
    """)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px; margin-top: 30px;">
    <p>💡 Kalkulator Pengenceran SPEKTRA | Dibuat dengan ❤️ untuk kemajuan pendidikan kimia</p>
</div>
""", unsafe_allow_html=True)

