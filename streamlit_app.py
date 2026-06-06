import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="SmartLab C",
    page_icon="🧪",
    layout="wide"
)

# ==========================
# CSS
# ==========================
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.metric-box {
    padding:15px;
    border-radius:15px;
    background:white;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
    text-align:center;
}

h1 {
    color:#0f172a;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# SESSION STATE
# ==========================
if "alat" not in st.session_state:
    st.session_state.alat = pd.DataFrame({
        "Nama Alat":[
            "Neraca Analitik",
            "pH Meter",
            "Spektrofotometer UV-Vis"
        ],
        "Status":[
            "Baik",
            "Baik",
            "Rusak Ringan"
        ],
        "Kalibrasi":[
            "2026-06-10",
            "2026-07-15",
            "2026-06-25"
        ]
    })

# ==========================
# HEADER
# ==========================
st.title("🧪 SmartLab C")
st.subheader("Sistem Monitoring Alat Laboratorium")

# ==========================
# METRIC
# ==========================
df = st.session_state.alat

total = len(df)
baik = len(df[df["Status"]=="Baik"])
rusak_ringan = len(df[df["Status"]=="Rusak Ringan"])
rusak_berat = len(df[df["Status"]=="Rusak Berat"])

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Alat", total)
col2.metric("Baik", baik)
col3.metric("Rusak Ringan", rusak_ringan)
col4.metric("Rusak Berat", rusak_berat)

st.divider()

# ==========================
# INPUT DATA
# ==========================
st.header("➕ Tambah Data Alat")

with st.form("form_alat"):

    nama = st.text_input("Nama Alat")

    status = st.selectbox(
        "Status",
        ["Baik","Rusak Ringan","Rusak Berat"]
    )

    kalibrasi = st.date_input(
        "Tanggal Kalibrasi"
    )

    submit = st.form_submit_button("Simpan")

    if submit:

        data_baru = pd.DataFrame({
            "Nama Alat":[nama],
            "Status":[status],
            "Kalibrasi":[kalibrasi]
        })

        st.session_state.alat = pd.concat(
            [st.session_state.alat,data_baru],
            ignore_index=True
        )

        st.success("Data berhasil ditambahkan!")

# ==========================
# TABEL
# ==========================
st.header("📋 Data Alat")

st.dataframe(
    st.session_state.alat,
    use_container_width=True
)

# ==========================
# DOWNLOAD
# ==========================
csv = st.session_state.alat.to_csv(index=False)

st.download_button(
    "⬇ Download CSV",
    csv,
    "data_alat.csv",
    "text/csv"
)

# ==========================
# GRAFIK
# ==========================
st.header("📊 Statistik Status Alat")

chart = (
    st.session_state.alat["Status"]
    .value_counts()
)

st.bar_chart(chart)
