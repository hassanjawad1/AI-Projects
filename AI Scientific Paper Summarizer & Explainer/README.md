# 🤖 AI Scientific Paper Summarizer & Explainer

This is a Streamlit-powered web app that takes scientific papers (PDFs), extracts key sections like **Abstract**, **Introduction**, and **Conclusion**, and summarizes them using state-of-the-art HuggingFace Transformers (Facebook's `bart-large-cnn`).

Perfect for:
-  Researchers trying to save time
- 📚 Students prepping for exams
- 📈 Analysts reviewing papers quickly
- 💻 Devs showcasing GenAI use-cases

---

## 🔧 Features

- 📄 Upload any scientific research paper in PDF format
- 🔍 Auto-detects **Abstract**, **Introduction**, and **Conclusion**
- 🧠 Summarizes each section using a HuggingFace summarization model
- 💬 Handles long sections via intelligent chunking
- 🚫 Gracefully handles API errors like busy model or bad response

---

## 🖼️ Demo

![Demo Screenshot](E:\Gen AI Projects\AI Scientific Paper Summarizer & Explainer\Ui image.JPG) <!-- Add your own screenshot here -->

---

## 🚀 Tech Stack

- [Streamlit](https://streamlit.io/) – For the web UI
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) – PDF parsing
- [Hugging Face Transformers](https://huggingface.co/models/facebook/bart-large-cnn) – Text summarization
- [NLTK](https://www.nltk.org/) – Sentence tokenization

---

📌 To-Do (Future Upgrades)
- ✅ Advanced section detection (Regex / ML parsing)

- 🧠 GPT-style section explainers

- 📊 Citation and keyword extraction

- 🌍 Deploy on Hugging Face Spaces or Streamlit Cloud

- 🗃️ Save and compare multiple summaries

- 📎 Upload multiple PDFs in one session

--- 
🧑‍💻 Author
- Built with ❤️ by Hassan Jawad
- If you like this project, don't forget to ⭐ the repo and follow me on GitHub 🙌

- github.com/hassanjawad1

