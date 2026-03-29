import streamlit as st
import google.generativeai as genai

# --- 🎨 SİBER TASARIM ---
st.set_page_config(page_title="Şahin Sistem v6.4", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .header-box { text-align: center; padding: 25px; border: 2px solid #d4af37; border-radius: 15px; background: #0a0a0a; margin-bottom: 30px; }
    .stTextInput>div>div>input { background-color: #050505 !important; color: #00ff41 !important; border: 2px solid #d4af37 !important; text-align: center; font-size: 20px; }
    .response-area { background: #0a0a0a; border: 2px solid #00ff41; padding: 25px; border-radius: 15px; margin-top: 30px; }
    </style>
""", unsafe_allow_html=True)

# --- 🦅 ÜST PANEL ---
st.markdown('<div class="header-box"><h1 style="color: white; margin:0;">🦅 ŞAHİN SİSTEM v6.4</h1><p style="color: #00ff41; font-weight: bold;">SİSTEM DURUMU: [AKTİF]</p><p style="color: #d4af37; font-size: 14px;">YUSUF EFE ŞAHİN | 7/D</p></div>', unsafe_allow_html=True)

# --- 🧠 SİSTEM MOTORU (BOŞLUKLARI DÜZELTİLMİŞ) ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        key = st.secrets["GEMINI_API_KEY"]
    else:
        st.error("⚠️ Secrets kısmına GEMINI_API_KEY eklenmemiş!")
        st.stop()

    genai.configure(api_key=key)
    
    # DİKKAT: Buradaki boşluklar Python için hayati önem taşır!
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    talimat = "Sen Şahin Sistem'sin. Yusuf Efe Şahin seni kodladı. 7. sınıf uzmanısın."

    st.markdown("<h3 style='color:#d4af37; text-align:center;'>💬 ANALİZ TERMİNALİ</h3>", unsafe_allow_html=True)
    soru = st.text_input("", placeholder="Sorunuzu yazın...")

    if soru:
        with st.spinner("Analiz ediliyor..."):
            response = model.generate_content(f"{talimat}\nSoru: {soru}")
            st.markdown(f"<div class='response-area'><b style='color:#00ff41;'>⚡ SONUÇ:</b><br><br>{response.text}</div>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"⚠️ MOTOR HATASI: {e}")

# --- 🌟 İMZA ---
st.markdown("<div style='text-align:center; color:#ff00ff; font-size:45px; font-weight:bold; margin-top:100px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
