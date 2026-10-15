import streamlit as st
from groq import Groq

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = ""

st.set_page_config(page_title="GODFRED AI GH", page_icon="🇬🇭", layout="centered")

# BEAUTIFUL GHANA THEME CSS
st.markdown("""
<style>
   .stApp {
        background: linear-gradient(135deg, #FFF8DC 0%, #FFD700 100%);
    }
    h1 {
        color: #CE1126!important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    h3 {
        color: #006B3F!important;
    }
   .stTextInput>div>div>input,.stTextArea>div>div>textarea {
        background-color: white!important;
        color: black!important;
        border: 2px solid #FFD700!important;
        border-radius: 15px!important;
    }
   .stButton>button {
        background: linear-gradient(90deg, #CE1126 0%, #FFD700 50%, #006B3F 100%);
        color: white!important;
        font-weight: bold;
        font-size: 18px;
        border-radius: 25px;
        border: none;
        padding: 12px 30px;
        width: 100%;
    }
   .stSuccess {
        background-color: white!important;
        border-radius: 15px;
        border-left: 5px solid #006B3F;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🇬🇭 GODFRED AI GH 🇬🇭</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Built by Godfred - Your WASSCE Helper!</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333;'>Ask me anything - Science, Math, English, Social Studies!</p>", unsafe_allow_html=True)

st.write("")

name = st.text_input("Your Name:", "Godfred")
question = st.text_area("Ask ANY question:", "What is photosynthesis?", height=120)

if st.button("🚀 Ask Godfred AI"):
    if not question:
        st.warning("Please type a question!")
    else:
        try:
            with st.spinner("Godfred AI is thinking... 🤔"):
                client = Groq(api_key=GROQ_API_KEY)
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": f"You are GODFRED AI, a friendly WASSCE tutor built by Godfred from Ghana. Help {name} in simple clear English. Use Ghana examples."},
                        {"role": "user", "content": question}
                    ]
                )
                st.success(response.choices[0].message.content)
                st.balloons()
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #006B3F; font-weight: bold;'>© 2026 Godfred AI - Made with ❤️ in Ghana 🇬🇭</p>", unsafe_allow_html=True)
