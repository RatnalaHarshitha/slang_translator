# 🧩 Case Study: AI-Driven Local Slang Translator

### 👩‍💻 Author: Harshitha Ratnala  
**Repo:** [github.com/RatnalaHarshitha/slang_translator](https://github.com/RatnalaHarshitha/slang_translator)

---

## 1. Context

Everyday chat messages, especially on social media or WhatsApp, are full of local slang and abbreviations.  
Standard NLP tools and chatbots fail to interpret these correctly — causing poor sentiment analysis and misunderstanding.

---

## 2. Problem

Most NLP pipelines are trained on formal English datasets.  
They fail to recognize slang like:

| Slang | Meaning |
|--------|----------|
| “lit” | amazing, exciting |
| “no cap” | seriously, not lying |
| “savage” | bold or unapologetic |

Goal: **Build an AI tool that converts such informal phrases into standard English automatically.**

---

## 3. Approach

### 🔹 Tools & Libraries
- **Python**
- **NLTK** (tokenization, text preprocessing)
- **JSON** dataset (custom slang dictionary)

### 🔹 System Design
1. **Input** — user enters text containing slang.  
2. **Tokenizer** — NLTK splits text into words/tokens.  
3. **Translator** — replaces slang using `slang_dict.json`.  
4. **Output** — clean English version.

```text
User: That party was lit no cap!
→ Output: That party was amazing seriously!
