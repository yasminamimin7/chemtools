import streamlit as st

st.set_page_config(
    page_title="SPEKTRA",
    page_icon="🧪",
    layout="wide"
)

st.sidebar.title("SPEKTRA")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Kalkulator Pengenceran",
        "ChemScan",
        "Reaksi Titrasi",
        "Quiz"
    ]
)

# =====================
# DASHBOARD
# =====================

if menu == "Dashboard":

    st.title("🧪 SPEKTRA")
    st.subheader(
        "Smart Platform for Chemical Analysis and Laboratory Tools"
    )

    st.success(
        "Platform pembelajaran dan alat bantu mahasiswa Analis Kimia."
    )

# =====================
# PENGENCERAN
# =====================

elif menu == "Kalkulator Pengenceran":

    st.title("🧪 Kalkulator Pengenceran")

    st.latex("C_1V_1=C_2V_2")

    c1 = st.number_input("C1", min_value=0.0)
    c2 = st.number_input("C2", min_value=0.0)
    v2 = st.number_input("V2 (mL)", min_value=0.0)

    if st.button("Hitung"):

        if c1 > 0:

            v1 = (c2 * v2) / c1

            st.success(
                f"Volume stok yang diambil = {v1:.2f} mL"
            )

# =====================
# CHEMSCAN
# =====================

elif menu == "ChemScan":

    data = {

        "HCl": {
            "Bahaya":"Korosif",
            "Penyimpanan":"Lemari asam"
        },

        "NaOH":{
            "Bahaya":"Korosif kuat",
            "Penyimpanan":"Tempat kering"
        },

        "KMnO4":{
            "Bahaya":"Oksidator kuat",
            "Penyimpanan":"Botol gelap"
        }

    }

    bahan = st.selectbox(
        "Pilih Bahan",
        list(data.keys())
    )

    st.write(
        "Bahaya:",
        data[bahan]["Bahaya"]
    )

    st.write(
        "Penyimpanan:",
        data[bahan]["Penyimpanan"]
    )

# =====================
# REAKSI TITRASI
# =====================

elif menu == "Reaksi Titrasi":

    jenis = st.selectbox(
        "Jenis Titrasi",
        [
            "Asam Basa",
            "Permanganometri",
            "Argentometri",
            "Kompleksometri"
        ]
    )

    if jenis == "Asam Basa":
        st.latex(
            "HCl + NaOH \\rightarrow NaCl + H_2O"
        )

    elif jenis == "Permanganometri":
        st.latex(
            "MnO_4^- + Fe^{2+} \\rightarrow Fe^{3+}"
        )

    elif jenis == "Argentometri":
        st.latex(
            "AgNO_3 + Cl^- \\rightarrow AgCl \\downarrow"
        )

    elif jenis == "Kompleksometri":
        st.latex(
            "Ca^{2+} + EDTA \\rightarrow Ca-EDTA"
        )

# =====================
# QUIZ
# =====================

elif menu == "Quiz":

    st.title("Quiz Kimia")

    soal = st.radio(
        "Larutan standar primer untuk standarisasi NaOH?",
        [
            "NaCl",
            "KHP",
            "NH4OH",
            "HCl"
        ]
    )

    if st.button("Periksa"):

        if soal == "KHP":
            st.success("Benar")
        else:
            st.error("Salah")
