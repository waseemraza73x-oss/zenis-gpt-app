import streamlit as st
from groq import Groq

# ऐप का डिज़ाइन
st.set_page_config(page_title="Zenis GPT", page_icon="🧠", layout="centered")

st.title("🧠 Zenis GPT")
st.write("⚡ Boundless intelligence. Instant answers. Your personal 🧠Zenis GPT.")

# 🔑 यहाँ अपनी Groq API Key डालें जो gsk_ से शुरू होती है
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

user_input = st.text_input("Ask anything to Zenis AI", placeholder="Ask your questions here...")

if st.button("Find answer"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                # Groq AI को कनेक्ट करना
                client = Groq(api_key=GROQ_API_KEY)
                completion = client.chat.completions.create(
                    model="openai/gpt-oss-20b",  # यह Groq का सबसे तेज और स्टेबल मॉडल है
                    messages=[{"role": "user", "content": user_input}]
                )
                st.success("Answer")
                st.write(completion.choices[0].message.content)
            except Exception as e:
                st.error(f"something else: {e}")
    else:
        st.warning("Please type here any question!")
