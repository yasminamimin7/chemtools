# ChemLab Mini Tools v4.0 (Revisi)
# Catatan:
# Ini adalah kerangka revisi untuk menggantikan beberapa bagian yang bermasalah:
# - number_input tanpa value=None
# - quiz anti-spam skor
# - history dibatasi
# - reset analisis
# - CSS lebih aman

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="ChemLab Mini Tools v4.0",
    layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

if "skor" not in st.session_state:
    st.session_state.skor = 0

if "total" not in st.session_state:
    st.session_state.total = 0

if "jawaban_tercek" not in st.session_state:
    st.session_state.jawaban_tercek = {}

st.title("ðŸ§ª ChemLab Mini Tools v4.0")

menu = st.sidebar.selectbox(
    "Menu",
    ["Kalkulator Pengenceran", "Quiz Reaksi"]
)

if menu == "Kalkulator Pengenceran":
    st.subheader("Câ‚Vâ‚ = Câ‚‚Vâ‚‚")

    c1 = st.number_input("Câ‚", min_value=0.0, step=0.1)
    v1 = st.number_input("Vâ‚", min_value=0.0, step=0.1)
    c2 = st.number_input("Câ‚‚", min_value=0.0, step=0.1)

    if st.button("Hitung Vâ‚‚"):
        if c2 == 0:
            st.error("Câ‚‚ tidak boleh nol")
        else:
            v2 = (c1 * v1) / c2
            st.success(f"Vâ‚‚ = {v2:.3f}")

            st.session_state.history.append({
                "waktu": datetime.now().strftime("%H:%M:%S"),
                "hasil": f"Vâ‚‚ = {v2:.3f}"
            })

            if len(st.session_state.history) > 50:
                st.session_state.history.pop(0)

    if st.session_state.history:
        st.dataframe(pd.DataFrame(st.session_state.history))

elif menu == "Quiz Reaksi":
    soal = {
        "pertanyaan": "Agâº + Clâ» menghasilkan endapan berwarna?",
        "pilihan": ["Putih", "Merah", "Biru"],
        "jawaban": "Putih"
    }

    st.write(soal["pertanyaan"])

    jawab = st.radio(
        "Pilih",
        soal["pilihan"]
    )

    if st.button("Cek Jawaban"):
        idx = 0

        if idx not in st.session_state.jawaban_tercek:
            st.session_state.total += 1

            if jawab == soal["jawaban"]:
                st.session_state.skor += 1
                st.success("Benar")
            else:
                st.error("Salah")

            st.session_state.jawaban_tercek[idx] = True
        else:
            st.warning("Soal ini sudah dinilai")

    st.metric("Skor", st.session_state.skor)
    st.metric("Total", st.session_state.total)
