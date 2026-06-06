import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AnKim Hub",
    page_icon="🧪",
    layout="wide"
)

# =========================
# DATABASE CHEMSCAN
# =========================

chemicals = {
    "HCl": {
        "Nama": "Hydrochloric Acid",
        "Rumus": "HCl",
        "Mr": "36.46",
        "Bahaya": "Korosif, iritasi pernapasan",
        "APD": "Sarung tangan, kacamata, jas lab",
        "Penyimpanan": "Jauh dari basa kuat",
        "Reaktivitas": "Bereaksi dengan basa dan logam tertentu"
    },
    "NaOH": {
        "Nama": "Sodium Hydroxide",
        "Rumus": "NaOH",
        "Mr": "40.00",
        "Bahaya": "Korosif kuat",
        "APD": "Sarung tangan, kacamata, jas lab",
        "Penyimpanan": "Tempat kering dan tertutup",
        "Reaktivitas": "Bereaksi dengan asam dan aluminium"
    },
    "KMnO4": {
        "Nama": "Potassium Permanganate",
        "Rumus": "KMnO₄",
        "Mr": "158.03",
        "Bahaya": "Oksidator kuat",
        "APD": "Sarung tangan dan kacamata",
        "Penyimpanan": "Jauh dari bahan organik",
        "Reaktivitas": "Bereaksi dengan reduktor"
    },
    "AgNO3": {
        "Nama": "Silver Nitrate",
        "Rumus": "AgNO₃",
        "Mr": "169.87",
        "Bahaya": "Korosif dan oksidator",
        "APD": "Sarung tangan dan kacamata",
        "Penyimpanan": "Botol gelap",
        "Reaktivitas": "Bereaksi dengan ion klorida"
    }
}

# =========================
# SIDEBAR
# =========================

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Dashboard",
        "Kalkulator Pengenceran",
        "ChemScan",
        "Quiz Center"
    ]
)

# =========================
# DASHBOARD
# =========================

if menu == "Dashboard":

    st.title("🧪 AnKim Hub")
    st.subheader("One Platform for Analytical Chemistry Students")

    col1,col2,col3 = st.columns(3)

    col1.metric("Database Bahan", len(chemicals))
    col2.metric("Quiz Aktif", 5)
    col3.metric("Tools", 3)

    st.info(
        "Selamat datang di AnKim Hub. Platform mahasiswa Analis Kimia."
    )

# =========================
# PENGENCERAN
# =========================

elif menu == "Kalkulator Pengenceran":

    st.title("🧪 Kalkulator Pengenceran")

    st.latex(r"C_1V_1=C_2V_2")

    c1 = st.number_input(
        "Konsentrasi Awal (C1)",
        min_value=0.0
    )

    c2 = st.number_input(
        "Konsentrasi Akhir (C2)",
        min_value=0.0
    )

    v2 = st.number_input(
        "Volume Akhir mL (V2)",
        min_value=0.0
    )

    if st.button("Hitung"):

        if c1 > 0 and c2 > 0:

            v1 = (c2 * v2) / c1

            st.success(
                f"Volume stok yang diambil = {v1:.2f} mL"
            )

            st.info(
                f"Tambahkan pelarut hingga volume {v2:.2f} mL"
            )

# =========================
# CHEMSCAN
# =========================

elif menu == "ChemScan":

    st.title("🔬 ChemScan")

    pilihan = st.selectbox(
        "Pilih Bahan Kimia",
        list(chemicals.keys())
    )

    data = chemicals[pilihan]

    st.subheader(data["Nama"])

    st.write("**Rumus Kimia:**", data["Rumus"])
    st.write("**Mr:**", data["Mr"])
    st.write("**Bahaya:**", data["Bahaya"])
    st.write("**APD:**", data["APD"])
    st.write("**Penyimpanan:**", data["Penyimpanan"])
    st.write("**Reaktivitas:**", data["Reaktivitas"])

# =========================
# QUIZ
# =========================

elif menu == "Quiz Center":

    st.title("📝 Quiz Kimia")

    soal = "Larutan standar primer yang sering digunakan untuk standarisasi NaOH adalah..."

    jawaban = st.radio(
        soal,
        [
            "NaCl",
            "KHP",
            "NH4OH",
            "H2SO4"
        ]
    )

    if st.button("Cek Jawaban"):

        if jawaban == "KHP":
            st.success("Benar! ✅")
        else:
            st.error("Salah ❌")

    st.divider()

    soal2 = "Alat yang digunakan untuk mengukur pH adalah..."

    jawaban2 = st.radio(
        soal2,
        [
            "Buret",
            "pH Meter",
            "Piknometer",
            "Neraca"
        ],
        key="soal2"
    )

    if st.button("Cek Soal 2"):

        if jawaban2 == "pH Meter":
            st.success("Benar! ✅")
        else:
            st.error("Salah ❌")
            
