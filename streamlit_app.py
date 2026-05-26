import streamlit as st

st.title("🧪 ChemLab Mini Tools")

menu = st.sidebar.selectbox("Pilih Fitur", [
    "Kalkulator Pengenceran",
    "Tebak Warna Reaksi",
    "Kenapa Gagal?"
])

# =========================
# 1. Kalkulator Pengenceran
# =========================
if menu == "Kalkulator Pengenceran":
    st.header("📊 Kalkulator Pengenceran")

    M1 = st.number_input("Konsentrasi Awal (M1)", min_value=0.0)
    V1 = st.number_input("Volume Awal (V1)", min_value=0.0)
    M2 = st.number_input("Konsentrasi Akhir (M2)", min_value=0.0)

    if st.button("Hitung V2"):
        if M2 != 0:
            V2 = (M1 * V1) / M2
            st.success(f"Volume akhir (V2) = {V2:.2f} mL")
        else:
            st.error("M2 tidak boleh nol!")
