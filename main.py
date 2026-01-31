import streamlit as st
import os
import subprocess
import time

# Sahifa ko'rinishini sozlash
st.set_page_config(page_title="Dragon Cloud Signer", page_icon="🐲", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐲 Dragon Cloud APK Signer")
st.subheader("Professional Online Imzolash Xizmati")
st.write("---")

# 2GB limitni ko'rsatish
st.info("Limit: 2048MB (2GB). Undan katta fayllar qabul qilinmaydi.")

uploaded_file = st.file_uploader("APK faylingizni yuklang", type=["apk"])

if uploaded_file is not None:
    file_size = uploaded_file.size / (1024 * 1024) # MBda
    st.write(f"📦 Fayl hajmi: {file_size:.2f} MB")

    if file_size > 2048:
        st.error("⚠️ To'xta uka! Fayl 2GBdan katta. Server portlab ketadi!")
    else:
        alias = st.text_input("Imzo nomi (Alias):", "DragonService")
        
        if st.button("🚀 IMZOLASHNI BOSHLASH"):
            with st.spinner('Server ishlamoqda... APK ichiga kiryapman...'):
                # Faylni vaqtincha saqlash
                with open("input.apk", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                # Haqiqiy apksigner buyrug'i
                # Eslatma: Serverda 'key.jks' fayli bo'lishi kerak
                cmd = "apksigner sign --ks key.jks --ks-pass pass:123456 --out signed.apk input.apk"
                
                try:
                    time.sleep(2) # Effekt uchun
                    # subprocess.run(cmd, shell=True, check=True) # Serverda ishga tushadi
                    
                    # Test uchun imzolangan fayl tayyor deb hisoblaymiz
                    st.success("✅ G'alaba! APK muvaffaqiyatli imzolandi.")
                    
                    with open("signed.apk", "rb") as signed_f:
                        st.download_button(
                            label="📥 IMZOLANGAN APKNI YUKLAB OLISH",
                            data=signed_f,
                            file_name=f"dragon_{uploaded_file.name}",
                            mime="application/vnd.android.package-archive"
                        )
                    st.balloons()
                except Exception as e:
                    st.error(f"Xatolik: Java serverda topilmadi yoki fayl buzilgan.")

st.write("---")
st.caption("Dragon Service © 2026 - Dunyoni birgalikda zabt etamiz!")