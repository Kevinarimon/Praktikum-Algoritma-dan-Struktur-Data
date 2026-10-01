import streamlit as st
import pandas as pd

# --- Title ---
st.title("🏠 Pengeluaran Anak Kos 71251208")

# --- Input Uang Bulanan ---
st.subheader("Uang Bulanan")
duitAwal = st.number_input("Uang sebulanan:", value=0, placeholder="Masukkan uang bulanan....")


# --- Input Pengeluaran ---
st.subheader("Pengeluaran Bulanan")
mkn = st.number_input("Pengeluaran Beli Makan:", value=0, placeholder="Masukkan pengeluaran makan....") 
kos = st.number_input("Bayar Kos:", value=0, placeholder="Harga sewa kos....") 
trans = st.number_input("Pengeluaran Transport:", value=0, placeholder="Harga bensin and servis....") 
internet = st.number_input("Langganan Internet:", value=0, placeholder="Harga Internet....") 
ml = st.number_input("Duit Have Fun:", value=0, placeholder="Pengeluaran Have fun....") 

# --- Tombol Ngitung Pengeluaran ---
if st.button("Ngitung!", type = "primary"): # if jangan dihapus, cuman nambahin tombol disini :

    # --- Ngitung Total Pengeluaran ---
    total = int( mkn + kos + trans + internet + ml )
    sisa = int(duitAwal - total)

    # --- Ngitung Sisa Uang ---
    


    # --- Menampilkan Hasil Perhitungan ---
    st.subheader("Ringkasan Keuangan")
    kolom1, kolom2, kolom3 = st.columns(3)
    with kolom1:
        st.metric(
            # Tampilin uang bulanan di sini
            "Uang bulanan",
            st.write(duitAwal)
        )
    with kolom2:
        st.metric(
            # Tampilin total pengeluaran di sini
            "Total pengeluaran",
            st.write(total)
        )
    with kolom3:
        st.metric(
            # Tampilin sisa uang di sini
            "Sisa duit",
            st.write(sisa)
        )


    # --- Kondisi Keuangan ---
    st.subheader("Kondisi Keuangan")

    # Kondisi 1
    if sisa > 0:
        st.success("Keuanganmu masih aman bulan ini!") 

    # Kondisi 2
    elif sisa == 0:
        st.warning("Uangmu habis..") 


    # Kondisi 3
    else:
        st.eror("Pengeluaranmu melebihi uang bulanan!")


    # --- Data Pengeluaran ---
    # Ini gausah diubah! 
    # Udah kubantu bikinin, tinggal dipake aja
    data_pengeluaran = {
        "Kategori": [
            "Makanan",
            "Kos",
            "Transportasi",
            "Internet/Pulsa",
            "Hiburan"
        ],
        "Pengeluaran": [
            mkn,
            kos,
            trans,
            internet,
            ml
        ]
    }

    df_pengeluaran = pd.DataFrame(data_pengeluaran)

    # --- Pengeluaran Terbesar ---
    terbesar = max(mkn, kos, trans, internet, ml)

    st.subheader("Pengeluaran Terbesar")
    st.write("Pengeluaran terbesar kamu adalah:") # Tampilin pengeluaran terbesar di sini
    st.write(terbesar)
    st.write("Rp", terbesar)

    # --- Grafik Pengeluaran ---
    st.subheader("Grafik Pengeluaran")
    st.bar_chart(df_pengeluaran.set_index("Kategori")) # Tampilin grafik pengeluaran di sini