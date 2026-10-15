import streamlit as st
from groq import Groq

# Get key safely
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = ""

st.set_page_config(page_title="GODFRED AI - WASSCE Helper", page_icon="🇬🇭")
st.markdown("<h1 style='text-align: center; color: gold;'>GODFRED AI 🇬🇭</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Built by Godfred - Ghana GH</h3>", unsafe_allow_html=True)
st.write("Your WASSCE Helper!")

name = st.text_input("Your Name:", "Godfred")
question = st.text_area("Ask ANY question:", "What is photosynthesis?")

if st.button("Ask Godfred AI"):
    if not GROQ_API_KEY:
        st.error("⚠️ Admin: Please add GROQ_API_KEY in Streamlit Secrets!")
        st.info("Go to Manage app -> Settings -> Secrets and add: GROQ_API_KEY = \"gsk_...\"")
    else:
        try:
            client = Groq(api_key=GROQ_API_KEY)
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": question}]
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown("© 2025 Godfred AI - Made in Ghana 🇬🇭")
