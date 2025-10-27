import json
import re

# 🔹 Load slang dictionary
def load_slang_dict(path="data/slang_dict.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ slang_dict.json not found. Using empty dictionary.")
        return {}

# 🔹 Core translation logic
def translate_text(text, slang_dict):
    # Split sentence into words
    words = re.findall(r"\b\w+\b", text.lower())
    translated_words = []

    for word in words:
        # Replace if slang found
        if word in slang_dict:
            translated_words.append(slang_dict[word])
        else:
            translated_words.append(word)
    
    # Join back into a sentence
    return " ".join(translated_words)

# 🔹 Demo usage
if __name__ == "__main__":
    slang_dict = load_slang_dict()
    print("\n🧠 AI Slang Translator\n")
    user_input = input("Enter slang sentence: ")

    result = translate_text(user_input, slang_dict)
    print("\n💬 Normalized Text:", result)
