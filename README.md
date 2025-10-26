# 🧠 AI-Driven Local Slang Translator  
> Bridging the gap between informal slang and formal English using NLP. 

---

### 💬 Overview

Languages evolve fast — and so does slang. This project is my attempt to make AI understand the *real* way people talk.

I built an **AI-powered chatbot** that can detect local or casual slang and translate it into **clear, standard English**, using **Python** and **Natural Language Toolkit (NLTK)**.

It’s lightweight, smart, and surprisingly fun to chat with 😄  

---

### 🎯 Problem Statement

Traditional NLP models struggle with slang because:
- Slang changes quickly across regions
- Words often have different contextual meanings
- Datasets rarely include informal text

**Goal:** Train a model (or rule-based system) that learns slang-to-standard mappings and applies context-aware replacements.

---

### ⚙️ How It Works

1. **Tokenization** → Sentence split using NLTK  
2. **Slang Mapping** → Detect slang words from a custom slang dictionary  
3. **Replacement Engine** → Replace slang with standard phrases  
4. **Chat Interface** → Simple terminal chatbot loop for interaction  

---

### 🧩 Tech Stack

| Tool | Purpose |
|------|----------|
| 🐍 Python | Core language |
| 📚 NLTK | Text preprocessing & tokenization |
| ☁️ Flask (optional) | Web chat interface |
| 🧠 Custom Dataset | Slang dictionary for regional terms |

---

### 🚀 Quick Start

```bash
# Clone this repository
git clone https://github.com/RatnalaHarshitha/slang_translator.git
cd slang_translator

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
python slang_translator.py
