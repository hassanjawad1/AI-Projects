import streamlit as st
import tempfile
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text

st.set_page_config(page_title="AI Paper Summarizer", layout="centered")
st.title("🧠 AI-Made Research Paper Summarizer")

uploaded_file = st.file_uploader("📄 Upload a scientific paper (PDF)", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    raw_text = extract_text_from_pdf(pdf_path)

    # Crude section parsing (improve later with regex)
    abstract = ""
    intro = ""
    conclusion = ""

    if "abstract" in raw_text.lower():
        abstract_start = raw_text.lower().find("abstract")
        intro_start = raw_text.lower().find("introduction")
        conclusion_start = raw_text.lower().find("conclusion")

        abstract = raw_text[abstract_start:intro_start] if intro_start > -1 else raw_text[abstract_start:]
        intro = raw_text[intro_start:conclusion_start] if conclusion_start > -1 else raw_text[intro_start:]
        conclusion = raw_text[conclusion_start:] if conclusion_start > -1 else ""

    with st.spinner("🔍 Summarizing abstract..."):
        abstract_summary = summarize_text(abstract, "abstract")
    with st.spinner("📘 Summarizing introduction..."):
        intro_summary = summarize_text(intro, "introduction")
    with st.spinner("📦 Summarizing conclusion..."):
        conclusion_summary = summarize_text(conclusion, "conclusion")

    st.subheader("🔍 Abstract Summary")
    st.write(abstract_summary)

    st.subheader("📘 Introduction Summary")
    st.write(intro_summary)

    st.subheader("📦 Conclusion Summary")
    st.write(conclusion_summary)
