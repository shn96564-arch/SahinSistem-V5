import streamlit as st
import google.generativeai as genai

# --- 🎨 ŞAHİN TASARIM (SİYAH & ALTIN & NEON) ---
st.set_page_config(page_title="Şahin Sistem v7.2", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .header-box { text-align: center; padding: 25px; border: 2px dotted #d4af37; border-radius: 15px; background: #0a0a0a; margin-bottom: 30px; }
    .stTextInput>div>div>input { background-color: #050505 !important; color: #00ff41 !important; border: 2px solid #d4af37 !important; text-align: center; font-size: 20px; border-radius: 10px; }
    .stInfo { background-color: #0a0a0a !important; border: 1px solid #00ff41 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# --- 🦅 ÜST PANEL ---
st.markdown('<div class="header-box"><h1 style="color: white; margin:0; font-family:monospace;">🦅 ŞAHİN SİSTEM v7.2</h1><p style="color: #00ff41; font-weight: bold; letter-spacing: 2px;">[ SİSTEM DURUMU: AKTİF ]</p><p style="color: #d4af37; font-size: 14px;">YUSUF EFE ŞAHİN | 7/D SINIFI ÖZEL SÜRÜM</p></div>', unsafe_allow_html=True)

# --- 🧠 SİSTEM MOTORU (ÇİFT KATMANLI KONTROL) ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # HATA ALMAMAK İÇİN EN GARANTİ LİSTE
        # Sırayla bunları deneyecek:
        model_names = ['gemini-1.5-flash', 'gemini-pro', 'models/gemini-1.5-flash']
        
        # Modeli seçmeye çalışalım
        model = None
        for name in model_names:
            try:
                model = genai.GenerativeModel(name)
                # Küçük bir test yapalım (boş değilse çalışıyordur)
                if model: break
            except:
                continue
        
        if model:
            st.markdown("<h3 style='color:#d4af37; text-align:center;'>💬 ANALİZ TERMİNALİ</h3>", unsafe_allow_html=True)
            soru = st.text_input("", placeholder="Sorunuzu buraya yazın (Örn: Zarflar nedir?)...")

            if soru:
                with st.spinner("🚀 Şahin Sistem Verileri İşliyor..."):
                    # Yusuf Efe Şahin imzalı talimat
                    response = model.generate_content(f"Sen Yusuf Efe Şahin'in 7/D sınıfı için kodladığı Şahin Sistem'sin. Uzmansın. Soru: {soru}")
                    st.info(response.text)
        else:
            st.error("⚠️ KRİTİK HATA: Uygun model bulunamadı!")
            
    else:
        st.error("⚠️ Secrets ayarlarında GEMINI_API_KEY bulunamadı!")

except Exception as e:
    st.error(f"⚠️ SİSTEM DURDURULDU: {e}")

# --- 🌟 NEON İMZA ---
st.markdown("<div style='text-align:center; color:#ff00ff; font-size:45px; font-weight:bold; text-shadow:0 0 20px #ff00ff; margin-top:100px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
