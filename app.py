import streamlit as st
import requests

st.set_page_config(page_title="GH GODFRED AI", page_icon="🇬🇭", layout="centered")

st.title("🇬🇭 GH GODFRED AI")
st.markdown("### Built by Godfred - Your WASSCE Helper!")
st.markdown("❤️ **Made with LOVE from Ghana** ❤️")
st.divider()

name = st.text_input("Your Name:", value="Godfred")
question = st.text_area("❓ Ask ANY WASSCE Question:", placeholder="E.g. What is photosynthesis? Explain like I'm preparing for WASSCE.", height=120)

# Get key safely
if "GROQ_KEY" not in st.secrets:
    st.error("Add GROQ_KEY in Secrets!")
    st.stop()

GROQ_KEY = st.secrets["GROQ_KEY"]

if st.button("🚀 Ask AI", type="primary", use_container_width=True):
    if not question:
        st.warning("Please type a question first!")
    else:
        with st.spinner(f"Thinking for you {name}... 🤔"):
            try:
                url = "https://api.groq.com/openai/v1/chat/completions"
                headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
                data = {
                    "model": "llama-3.3-70b-versatile",
                    "messages": [
                        {"role": "system", "content": "You are GH GODFRED AI, a brilliant WASSCE tutor for Ghanaian students. Format answers BEAUTIFULLY with: # Headings, **bold** for key terms, bullet lists, emojis, examples, and a summary. Explain simply for WASSCE."},
                        {"role": "user", "content": question}
                    ],
                    "temperature": 0.7
                }
                response = requests.post(url, headers=headers, json=data, timeout=30)

                if response.status_code == 200:
                    answer = response.json()["choices"][0]["message"]["content"]
                    st.success(f"Here you go {name}! 👇")
                    st.markdown(answer)
                    st.balloons()
                else:
                    st.error(f"Groq Error: {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")

st.divider()
st.caption("Powered by Groq + Streamlit | For Ghanaian Students 🇬🇭")
