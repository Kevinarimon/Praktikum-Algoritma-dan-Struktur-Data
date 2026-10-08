import streamlit as st
from user import user_data_by_username

# CEK APAKAH SUDAH LOGIN
if "logged_in" not in st.session_state or not st.session_state.logged_in == True:
    st.switch_page("app.py")
user = user_data_by_username()

# hint untuk mematikan text input ada di -> https://docs.streamlit.io/develop/api-reference/widgets/st.text_input
# BUAT 2 INPUT TEXT 1 Username 1 Password namun disable/matikan field Username dan yang password harus tipe password

# Silahkan kalau mau baca baca ini hehe ga wajib ya-> https://discuss.streamlit.io/t/buttons-alignment/51929
col1, space, col2 = st.columns([1,3,1])
with col1:
    # Buat tombol logout st.button("logout", type="primary") keluar ke app.py
    st.write('mau logout??')
    if st.button("Log Out"):
        st.session_state['logged_in'] = False
            
with col2:
    ganti_usrnm = st.write("Ganti Username")
    ganti_pass =  st.write("Ganti Password")
    # Ini untuk ubah password st.button("Ganti Data", type="secondary", width=400)
    if st.button("Ganti Data", type="secondary", width=400):
        if ganti_usrnm == user[username]:
            st.error("Username tidak boleh sama")
        elif ganti_pass == user["password"]:
            st.error("Password tidak boleh sama")
        else:
            user.update({Username:ganti_usrnm})
            user.update({"password":ganti_pass})
            st.success("Berhasil")

    # Kondisi -> Password baru dan lama ga boleh sama 
    # Jika sama -> st.error("ga boleh sama wok")
    # jika beda ubah melalui variabel 'user' lalu tampilkan st.success("Berhasil")
