import streamlit as st
from groq import Groq

# PUT YOUR NEW KEY HERE INSIDE QUOTES
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

st.set_page_config(page_title="GODFRED AI", page_icon="📚", layout="centered")
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    }
    h1 {
        color: #FFD700 !important;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(90deg, #CE1126, #FCD116, #006B3F) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        width: 100% !important;
        height: 50px !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("GODFRED AI 📚")
st.markdown("### Built by Godfred - Ghana GH 🇬🇭")

KNOWLEDGE = {
    "photosynthesis": "**PHOTOSYNTHESIS** is when green plants make food using sunlight.",
    "osmosis": "**OSMOSIS:** Water moves from low to high concentration.",
    "mitosis": "**MITOSIS:** Cell division for growth. Makes 2 identical cells.",
    "newton": "**NEWTON LAWS:** 1) Inertia 2) F=ma 3) Action=Reaction",
    "democracy": "**DEMOCRACY:** Gov't of the people, by the people, for the people."
}

client = Groq(api_key=GROQ_API_KEY)

st.title("GODFRED AI 📚")
st.markdown("### Built by Godfred - Ghana GH")
st.write("Your WASSCE Helper!")

name = st.text_input("Your Name:", "Godfred")
question = st.text_area("Ask ANY question:", placeholder="e.g. What is electrolysis?")

if st.button("Ask GODFRED AI"):
    if not question:
        st.warning("Type a question!")
    else:
        with st.spinner(f"Thinking for {name}..."):
            try:
                chat = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": "You are GODFRED AI, built by Godfred from Ghana. Help Ghanaian students pass WASSCE. Explain simply."},
                        {"role": "user", "content": question}
                    ]
                )
                st.success(f"Great question, {name}!")
                st.write(chat.choices[0].message.content)
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")