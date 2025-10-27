import streamlit as st
import json
import re

# 🔹 Load slang dictionary
def load_slang_dict(path="data/slang_dict.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("⚠️ slang_dict.json not found. Please add it in /data folder.")
        return {}

# 🔹 Core translation logic
def translate_text(text, slang_dict):
    words = re.findall(r"\b\w+\b", text.lower())
    translated_words = []

    for word in words:
        translated_words.append(slang_dict.get(word, word))
    
    return " ".join(translated_words)

# 🔹 Streamlit UI
def main():
    st.set_page_config(page_title="AI Slang Translator", page_icon="🧠")

    st.title("🧠 AI Slang Translator")
    st.write("Convert regional or internet slang into clear, standard English using NLP text normalization.")

    slang_dict = load_slang_dict()

    user_input = st.text_area("Enter a slang sentence:", "brb gonna grab some grub")

    if st.button("Translate"):
        result = translate_text(user_input, slang_dict)
        st.success(result)

    st.markdown("---")
    st.caption("Built with ❤️ using Python + Streamlit")

if __name__ == "__main__":
    main()
