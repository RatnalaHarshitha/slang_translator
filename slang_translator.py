# Slang words and their meanings
slang_dict = {
    "yaar": "friend",
    "chill": "relax",
    "bro": "brother",
    "gonna": "going to",
    "what's up": "how are you"
}
def translate_slang(sentence):
    words = sentence.lower().split()  # Convert sentence to lowercase and split into words
    translated_words = []  # This will store the translated sentence
    
    for word in words:
        if word in slang_dict:
            translated_words.append(slang_dict[word])  # Replace slang
        else:
            translated_words.append(word)  # Keep the original word if not slang

    return ' '.join(translated_words)  # Join words back to form a sentence
print("Welcome to the Local Slang Translator!")  # Greeting message
sentence = input("Enter a sentence with slang: ")  # Take input from user
translated = translate_slang(sentence)  # Call the function
print(f"Standard Translation: {translated}")  # Show the result
