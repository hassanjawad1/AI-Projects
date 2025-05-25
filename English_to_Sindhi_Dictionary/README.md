# 🌍 English-to-Sindhi Neural Translator 🇬🇧➡️🇸🇳

**A Natural Language Processing project that bridges English and Sindhi using Deep Learning and Rule-Based NLP techniques.**

This project enables seamless translation between English and Sindhi — focusing on accuracy, accessibility, and preserving regional languages through modern AI.

---

## 📌 Features

- ✅ Rule-based Sindhi ➡️ English translation (dictionary lookup)
- 🤖 English ➡️ Sindhi neural machine translation using HuggingFace’s MarianMT
- 📚 Custom parallel dataset (English ↔️ Sindhi)
- 🧠 Fine-tuned Transformer model for low-resource translation
- 💬 Potential for speech and TTS integration

---

## 🧠 Model Architecture

- **Model:** MarianMT (`Helsinki-NLP/opus-mt-en-ROMANCE`)
- **Frameworks:** Hugging Face Transformers, PyTorch
- **Dataset:** 10,000+ paired English↔Sindhi sentences from `s1.csv`
- **Approach:**
  - Preprocessing with tokenization
  - Fine-tuning with `Seq2SeqTrainer`
  - Evaluated on accuracy of translation and sentence structure

---

## 📁 Dataset

- Built from local resources and parallel sentence collections
- Format: CSV with columns `English`, `Sindhi`
- Preprocessed using Hugging Face’s `datasets` module

---

## 🛠️ How to Run

### ⚙️ Requirements

```bash
pip install transformers datasets pandas torch
```

### 🚀 Translate English to Sindhi

```python
from transformers import MarianTokenizer, MarianMTModel

model_name = "Helsinki-NLP/opus-mt-en-ROMANCE"  # or your fine-tuned version
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_en_to_sd(text):
    tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

print(translate_en_to_sd("How are you today?"))
```

---

## 🧪 Rule-Based Sindhi ➡️ English Translator

```python
sindhi_to_english = {
    'مان': 'I',
    'توھان': 'you',
    'هو': 'he',
    'آهي': 'is',
    # Add more dictionary entries here
}

def rule_based_translate(sindhi_sentence):
    words = sindhi_sentence.split()
    return ' '.join(sindhi_to_english.get(w, f"[{w}]") for w in words)

print(rule_based_translate("سائين مان اسڪول وڃان"))
# Output: sir I school go
```

---

## 📊 Performance & Limitations

- BLEU Score: _(to be added if calculated)_
- Good for basic sentence structure
- May struggle with:
  - Complex grammar
  - Slang and idioms
  - Named entity preservation
- Future improvements:
  - Roman ↔ Arabic Sindhi script conversion
  - Add speech input/output
  - Improve accuracy with larger corpus

---

## 📸 Project Screenshot
```
## 📸 Translation App Screenshots

## 📸 Project Screenshots

![UI Preview](images/1.png)
*Main user interface showing English to Sindhi translation*

![Example 1](images/2.png)
*Model translating simple English sentence*

![Example 2](images/3.png)
*Fine-tuned transformer results*

![Example 3](images/4.png)
*Rule-based Sindhi to English output preview*

---

## ✍️ Author

**Jawad Ahmed Jamali**  
_“Preserving language through code.”_  
🔗 [GitHub](#) • 💬 [LinkedIn](#) • 📧 [Email](#)

> _(Add your actual links above if you want them clickable)_

---

## 🏁 License

**MIT License** — use it, remix it, improve it, share it.


---

## ✍️ Author

**Jawad Ahmed Jamali**  
_“Preserving language through code.”_  
🔗 GitHub | 💬 LinkedIn | 📧 Email

---

## 🏁 License

MIT — use it, remix it, build on it.
