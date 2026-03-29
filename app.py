import streamlit as st
import google.generativeai as genai

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN & NEON) ---
st.set_page_config(page_title="Şahin Sistem v6.2", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .header-box { text-align: center; padding: 25px; border: 2px solid #d4af37; border-radius: 15px; background: #0a0a0a; margin-bottom: 30px; box-shadow: 0 0 15px rgba(212, 175, 55, 0.3); }
    .stTextInput>div>div>input { background-color: #050505 !important; color: #00ff41 !important; border: 2px solid #d4af37 !important; text-align: center; font-size: 20px; border-radius: 10px; }
    .response-area { background: #0a0a0a; border: 2px solid #00ff41; padding: 25px; border-radius: 15px; margin-top: 30px; box-shadow: 0 0 20px rgba(0, 255, 65, 0.2); line-height: 1.6; }
    </style>
""", unsafe_allow_html=True)

# --- 🦅 ÜST PANEL ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: white; margin:0; font-family: 'Courier New', Courier, monospace;">🦅 ŞAHİN SİSTEM v6.2</h1>
        <p style="color: #00ff41; font-weight: bold; letter-spacing: 3px; margin-top:10px;">SİSTEM DURUMU: [AKTİF - TAM YETKİ]</p>
        <p style="color: #d4af37; font-size: 14px;">YUSUF EFE ŞAHİN | 7/D SINIFI UZMANI</p>
    </div>
""", unsafe_allow_html=True)

# --- 🧠 SİSTEM MOTORU (GÜNCEL FLASH MODEL) ---
try:
    # Secrets kontrolü
    if "GEMINI_API_KEY" in st.secrets:
        key = st.secrets["GEMINI_API_KEY"]
    else:
        st.error("⚠️ HATA: Secrets kısmına GEMINI_API_KEY eklenmemiş!")
        st.stop()

    genai.configure(api_key=key)
    
    # En yeni ve hızlı model: gemini-1.5-flash
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    talimat = (
        "Sen Şahin Sistem'sin. Yusuf Efe Şahin seni 7/D sınıfı için özel olarak kodladı. "
        "Türkçe, Matematik ve Sosyal Bilgiler konularında bir dahisin. "
        "Cevaplarını samimi ama profesyonel bir asistan gibi ver."
    )

    # --- ⌨️ ANALİZ TERMİNALİ ---
    st.markdown("<h3 style='color:#d4af37; text-align:center;'>💬 DERS ANALİZ TERMİNALİ</h3>", unsafe_allow_html=True)
    soru = st.text_input("", placeholder="Hemen bir soru sor (Örn: Rasyonel sayılarda bölme nasıl yapılır?)...")

    if soru:
        with st.spinner("🚀 Şahin Sistem Verileri İşliyor..."):
            response = model.generate_content(f"{talimat}\nSoru: {soru}")
            st.markdown(f"""
                <div class="response-area">
                    <b style="color:#00ff41; font-size:18px;">⚡ ANALİZ SONUCU:</b><br><br>
                    {response.text}
                </div>
            """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"⚠️ KRİTİK HATA: {e}")

# --- 🌟 NEON İMZA ---
st.markdown(f"<div style='text-align:center; color:#ff00ff; font-size:45px; font-weight:bold; text-shadow:0 0 20px #ff00ff; margin-top:100px; font-family: Arial;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
