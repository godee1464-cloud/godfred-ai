import streamlit as st
import requests

st.set_page_config(page_title="GODFRED AI - WASSCE Helper", layout="centered")

# --- CLEAN UI ---
st.markdown("""
<style>
   .stTextArea textarea {border-radius: 12px!important; border: 2px solid #f59e0b!important;}
   .stButton button {background-color: #f59e0b; color: black; font-weight: bold; border-radius: 20px; width: 100%;}
   .answer-box {background: #fffbeb; padding: 20px; border-radius: 15px; border-left: 5px solid #f59e0b; color: #1f2937; line-height: 1.7;}
</style>
<h1 style='text-align:center; color:#92400e;'>GH GODFRED AI GH GH</h1>
<p style='text-align:center;font-weight:bold;'>Built by Godfred - Your WASSCE Helper!</p>
<p style='text-align:center;'>❤️ Made with LOVE from Ghana ❤️</p>
""", unsafe_allow_html=True)

name = st.text_input("👤 Your Name:", value="Godfred")
question = st.text_area("❓ Ask ANY WASSCE Question:", height=120, placeholder="What is photosynthesis? Explain like I'm preparing for WASSCE.")

# PUT YOUR REAL GROQ KEY HERE
GROQ_KEY = st.secrets["GROQ_KEY"]

if st.button("🚀 Ask Godfred AI"):
    if not question:
        st.warning("Please type a question!")
    else:
        with st.spinner("Godfred AI is thinking..."):
            try:
                headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "llama-3.1-8b-instant",
                    "messages": [
                        {"role": "system", "content": f"You are GODFRED AI, built by Godfred in Ghana. You help WASSCE students. User is {name}. RULES: Always use clean paragraphs, leave empty line between points, use numbered lists 1. 2. 3. with line breaks. Make it easy to read for WASSCE."},
                        {"role": "user", "content": question}
                    ],
                    "temperature": 0.7
                }
                res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=30)
                result = res.json()

                if "choices" in result:
                    answer = result['choices'][0]['message']['content']
                    st.divider()
                    st.markdown(f"### ✅ Answer for {name}:")
                    # THIS IS THE FIX - st.markdown renders the layout correctly
                    st.markdown(answer)
                else:
                    st.error(f"API Error: {result}")

            except Exception as e:
                st.error(f"Error: {e}")
