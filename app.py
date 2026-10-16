import streamlit as st

st.title("GH GODFRED AI")

# This will NOT crash anymore
if "GROQ_KEY" not in st.secrets:
    st.error("GROQ_KEY missing! Add it in Manage app > Settings > Secrets")
    st.stop()

st.success("✅ GROQ_KEY found! Your app is fixed!")
st.write("Now we can add AI back")

key = st.secrets["GROQ_KEY"]
st.write(f"Key starts with: {key[:10]}... Good!")
