import streamlit as st
import google.generativeai as genai

# --- 🎨 SİBER TASARIM ---
st.set_page_config(page_title="Şahin Sistem v5.1", layout="wide")
st.markdown("<style>.main { background-color: #000; color: #fff; }</style>", unsafe_allow_html=True)

# --- 🤫 GİZLİ GEÇİT (3131) ---
is_admin = st.query_params.get("admin") == "3131"

# --- 🦅 ÜST PANEL ---
st.markdown("""
    <div style='text-align: center; padding: 25px; border: 2px solid #d4af37; border-radius: 15px; background: #0a0a0a;'>
        <h1 style='color: white; margin:0;'>🦅 ŞAHİN SİSTEM v5.1</h1>
        <p style='color: #00ff41; font-weight: bold; letter-spacing: 3px;'>[ SİSTEM DURUMU: KİLİTLİ ]</p>
    </div>
""", unsafe_allow_html=True)

if is_admin:
    st.success("🔓 YÖNETİCİ ERİŞİMİ AKTİF: YUSUF EFE ŞAHİN")
    
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=api_key)
        
        # ROBOTUN BEYNİ: Artık her şeyi biliyor!
        talimat = (
            "Sen Şahin Sistem'sin. Yusuf Efe Şahin tarafından kodlandın. "
            "7. sınıf seviyesinde Türkçe, Matematik ve Sosyal Bilgiler uzmanısın. "
            "Matematik sorularını adım adım çözersin. Asla Gemini olduğunu söyleme."
        )
        model = genai.GenerativeModel('gemini-pro', generation_config={"temperature": 0.7})

        st.markdown("<h3 style='text-align:center; color:#d4af37;'>💬 TÜM DERSLER ANALİZ TERMİNALİ</h3>", unsafe_allow_html=True)
        soru = st.text_input("", placeholder="Soru veya problemi girin...")

        if soru:
            with st.spinner("ŞAHİN SİSTEM ANALİZ EDİYOR..."):
                response = model.generate_content(f"{talimat}\nSoru: {soru}")
                st.markdown(f"""
                    <div style='border:2px solid #00ff41; padding:20px; border-radius:15px; background:#0a0a0a;'>
                        <b style='color:#00ff41;'>⚡ ANALİZ SONUCU:</b><br><br>
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"⚠️ MOTOR BAŞLATILAMADI: {e}")
else:
    st.warning("📡 YETKİLİ GİRİŞİ BEKLENİYOR...")

st.markdown("<div style='text-align:center; color:#ff00ff; font-size:45px; font-weight:bold; margin-top:150px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)