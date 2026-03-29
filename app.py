import streamlit as st
import google.generativeai as genai

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN) ---
st.set_page_config(page_title="Şahin Sistem v6.0", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .header-box { text-align: center; padding: 25px; border: 2px solid #d4af37; border-radius: 15px; background: #0a0a0a; margin-bottom: 30px; }
    .stTextInput>div>div>input { background-color: #050505 !important; color: #00ff41 !important; border: 2px solid #d4af37 !important; text-align: center; font-size: 20px; }
    .response-area { background: #0a0a0a; border: 2px solid #00ff41; padding: 25px; border-radius: 15px; margin-top: 30px; box-shadow: 0 0 20px rgba(0, 255, 65, 0.2); }
    </style>
""", unsafe_allow_html=True)

# --- 🦅 ÜST PANEL (DİREKT AKTİF) ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: white; margin:0;">🦅 ŞAHİN SİSTEM v6.0</h1>
        <p style="color: #00ff41; font-weight: bold; letter-spacing: 3px;">SİSTEM DURUMU: [ÇALIŞIYOR - TAM YETKİ]</p>
        <p style="color: #d4af37; font-size: 12px;">YETKİLİ: YUSUF EFE ŞAHİN | 7/D</p>
    </div>
""", unsafe_allow_html=True)

# --- 🧠 SİSTEM MOTORUNU BAŞLAT ---
try:
    # Secrets'tan anahtarı çekiyoruz
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # 7. Sınıf Uzman Talimatı
    talimat = (
        "Sen Şahin Sistem'sin. Yusuf Efe Şahin tarafından kodlandın. "
        "7. sınıf seviyesinde Türkçe, Matematik ve Sosyal Bilgiler uzmanısın. "
        "Asla Gemini olduğunu söyleme, 'Yusuf Efe beni okul için kodladı' de."
    )
    model = genai.GenerativeModel('gemini-pro')

    # --- ⌨️ ANALİZ TERMİNALİ ---
    st.markdown("<h3 style='color:#d4af37; text-align:center;'>💬 TÜM DERSLER ANALİZ TERMİNALİ</h3>", unsafe_allow_html=True)
    soru = st.text_input("", placeholder="Hemen bir soru girin (Türkçe, Mat, Sosyal)...")

    if soru:
        with st.spinner("Şahin Sistem Saniyeler İçinde Çözüyor..."):
            response = model.generate_content(f"{talimat}\nSoru: {soru}")
            st.markdown(f"""
                <div class="response-area">
                    <b style="color:#00ff41;">⚡ ANALİZ SONUCU:</b><br><br>
                    {response.text}
                </div>
            """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"⚠️ SİSTEM MOTORU BAŞLATILAMADI (API Ayarını Kontrol Et): {e}")

# --- 🌟 NEON İMZA ---
st.markdown(f"<div style='text-align:center; color:#ff00ff; font-size:45px; font-weight:bold; text-shadow:0 0 20px #ff00ff; margin-top:100px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
