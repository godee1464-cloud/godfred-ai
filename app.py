import streamlit as st
from groq import Groq

# Get API Key
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except:
    GROQ_API_KEY = ""

st.set_page_config(
    page_title="GODFRED AI GH",
    page_icon="🇬🇭",
    layout="centered"
)

# ========== BEAUTIFUL GHANA THEME ==========
st.markdown("""
<style>
    /* Background - Light Gold */
   .stApp {
        background: linear-gradient(135deg, #FFFDF0 0%, #FFEB99 50%, #FFD700 100%);
    }

    /* ALL TEXT COLORS - BLACK & READABLE */
   .stMarkdown, p, label, div, span,.stText {
        color: #000000!important;
    }

    /* Title - Ghana Red */
    h1 {
        color: #CE1126!important;
        text-align: center!important;
        font-weight: 900!important;
        font-size: 42px!important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    /* Subtitle - Ghana Green */
    h3 {
        color: #006B3F!important;
        text-align: center!important;
        font-weight: 700!important;
    }

    /* Input Labels - Black Bold */
   .stTextInput label,.stTextArea label {
        color: #000000!important;
        font-weight: bold!important;
        font-size: 18px!important;
    }

    /* Input Boxes - White with border */
   .stTextInput input,.stTextArea textarea {
        background-color: #FFFFFF!important;
        color: #000000!important;
        border: 2.5px solid #006B3F!important;
        border-radius: 15px!important;
        font-size: 16px!important;
        font-weight: 500!important;
    }

    /* Button - Ghana Flag Gradient */
   .stButton > button {
        background: linear-gradient(90deg, #CE1126 0%, #FFD700 50%, #006B3F 100%)!important;
        color: #FFFFFF!important;
        font-weight: bold!important;
        font-size: 20px!important;
        border-radius: 30px!important;
        border: 3px solid #000000!important;
        padding: 15px 30px!important;
        width: 100%!important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
   .stButton > button:hover {
        transform: scale(1.02);
    }

    /* Answer Box - White Card */
   .stSuccess,.stAlert, div[data-testid="stNotification"] {
        background-color: #FFFFFF!important;
        color: #000000!important;
        border-radius: 20px!important;
        border-left: 6px solid #006B3F!important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        font-size: 16px!important;
        line-height: 1.6!important;
    }

    /* Spinner text */
   .stSpinner > div {
        color: #CE1126!important;
    }
</style>
""", unsafe_allow_html=True)

# ========== APP CONTENT ==========
st.markdown("<h1>🇬🇭 GODFRED AI GH 🇬🇭</h1>", unsafe_allow_html=True)
st.markdown("<h3>Built by Godfred - Your WASSCE Helper!</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #333333; font-weight: 600;'>📚 Science • Math • English • Social Studies • Ask Anything!</p>", unsafe_allow_html=True)

st.write("")

# Inputs
name = st.text_input("👤 Your Name:", "Godfred")
question = st.text_area("❓ Ask ANY WASSCE Question:", "What is photosynthesis? Explain like I'm preparing for WASSCE.", height=130)

st.write("")

# Button
if st.button("🚀 Ask Godfred AI"):
    if not question.strip():
        st.warning("⚠️ Please type a question first!")
    elif not GROQ_API_KEY:
        st.error("⚠️ Admin: Add GROQ_API_KEY in Secrets!")
    else:
        try:
            with st.spinner("🤔 Godfred AI is thinking..."):
                client = Groq(api_key=GROQ_API_KEY)
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": f"You are GODFRED AI GH, a friendly expert WASSCE tutor built by Godfred from Ghana. Help {name} with clear, simple explanations for WASSCE. Use Ghana examples, be encouraging, and explain step-by-step. Keep language simple."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )
                st.markdown("### ✅ Answer:")
                st.success(response.choices[0].message.content)
                st.balloons()

        except Exception as e:
            st.error(f"❌ Error: {e}")

st.markdown("---")
st.markdown("""
<div style='text-align: center; background: white; padding: 15px; border-radius: 15px; border: 2px solid #FFD700;'>
    <p style='color: #006B3F!important; font-weight: bold; margin: 0; font-size: 16px;'>
        © 2026 Godfred AI - Made with ❤️ in Ghana 🇬🇭<br>
        <span style='color: #CE1126!important;'>Built by Godfred - For Ghanaian Students</span>
    </p>
</div>
""", unsafe_allow_html=True)
