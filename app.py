import streamlit as st
import google.generativeai as genai

# --- 🎨 ŞAHİN TASARIM ---
st.set_page_config(page_title="Şahin Sistem v7.0", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .header-box { text-align: center; padding: 20px; border: 2px solid #d4af37; border-radius: 15px; background: #0a0a0a; }
    .stTextInput>div>div>input { background-color: #050505 !important; color: #00ff41 !important; border: 2px solid #d4af37 !important; font-size: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header-box"><h1 style="color: white; margin:0;">🦅 ŞAHİN SİSTEM v7.0</h1><p style="color: #d4af37;">YUSUF EFE ŞAHİN | 7/D</p></div>', unsafe_allow_html=True)

# --- 🧠 MOTOR KONTROL ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # EN GARANTİ MODEL ÇAĞIRMA YÖNTEMİ
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        st.markdown("<h3 style='color:#d4af37; text-align:center;'>💬 ANALİZ TERMİNALİ</h3>", unsafe_allow_html=True)
        soru = st.text_input("", placeholder="Sorunuzu buraya yazın...")

        if soru:
            with st.spinner("Şahin Sistem Düşünüyor..."):
                response = model.generate_content(f"Sen Yusuf Efe Şahin'in kodladığı Şahin Sistem'sin. 7. sınıf derslerinde uzmansın. Soru: {soru}")
                st.info(response.text)
    else:
        st.error("⚠️ Secrets ayarlarında GEMINI_API_KEY bulunamadı!")

except Exception as e:
    # Eğer model ismi yine hata verirse, sisteme otomatik alternatif sunuyoruz
    st.warning("⚠️ Sistem güncelleniyor, lütfen 10 saniye bekleyip tekrar deneyin.")
    st.write(f"Hata detayı: {e}")

st.markdown("<div style='text-align:center; color:#ff00ff; font-size:40px; font-weight:bold; margin-top:50px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
