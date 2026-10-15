import streamlit as st
from groq import Groq

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = ""

st.set_page_config(page_title="GODFRED AI GH", page_icon="🇬🇭")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #FFFDF0 0%, #FFEB99 50%, #FFD700 100%); }
.stMarkdown, p, label, div, span { color: #000000!important; }
    h1 { color: #CE1126!important; text-align: center!important; font-weight: 900!important; }
    h3 { color: #006B3F!important; text-align: center!important; }
.stTextInput label,.stTextArea label { color: #000000!important; font-weight: bold!important; font-size: 18px!important; }
.stTextInput input,.stTextArea textarea {
        background-color: #FFFFFF!important; color: #000000!important;
        border: 2.5px solid #006B3F!important; border-radius: 15px!important;
    }
.stButton > button {
        background: linear-gradient(90deg, #CE1126 0%, #FFD700 50%, #006B3F 100%)!important;
        color: white!important; font-weight: bold!important; font-size: 20px!important;
        border-radius: 30px!important; border: 3px solid black!important; width: 100%!important;
    }
.stSuccess { background-color: white!important; color: black!important; border-radius: 20px!important; border-left: 6px solid #006B3F!important; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🇬🇭 GODFRED AI GH 🇬🇭</h1>", unsafe_allow_html=True)
st.markdown("<h3>Built by Godfred - Your WASSCE Helper!</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-weight: 700;'>❤️ Made with LOVE from Ghana ❤️</p>", unsafe_allow_html=True)

name = st.text_input("👤 Your Name:", "Godfred")
question = st.text_area("❓ Ask ANY WASSCE Question:", "What is photosynthesis? Explain like I'm preparing for WASSCE.", height=130)

if st.button("🚀 Ask Godfred AI"):
    try:
        with st.spinner("🤔 Thinking..."):
            client = Groq(api_key=GROQ_API_KEY)
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[
                    {"role": "system", "content": f"You are GODFRED AI GH, built with love from Fiapre-Sunyani, Ghana by Godfred. Help {name} for WASSCE."},
                    {"role": "user", "content": question}
                ]
            )
            st.success(response.choices[0].message.content)
            st.balloons()
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.markdown("""
<div style='text-align: center; background: white; padding: 20px; border-radius: 20px; border: 3px solid #FFD700;'>
    <p style='color: #CE1126!important; font-weight: 900!important; margin: 0; font-size: 18px;'>
        ❤️ Made with LOVE in Ghana 🇬🇭 ❤️<br>
        Fiapre - Sunyani
    </p>
    <p style='color: #000000!important; font-weight: bold; margin: 8px 0; font-size: 16px;'>
        © 2026 Godfred AI - Made with ❤️ in Ghana 🇬🇭<br>
        Fiapre - Sunyani, Bono Region
    </p>
    <p style='color: #006B3F!important; font-weight: 800!important; margin: 5px 0; font-size: 17px;'>
        Built by Godfred - For Ghanaian Students<br>
        From Fiapre-Sunyani to the World! 🌍
    </p>
</div>
""", unsafe_allow_html=True)
