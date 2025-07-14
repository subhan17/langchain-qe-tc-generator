import streamlit as st
from app.pdf_utils import extract_text_from_pdf
from app.generator import generate_bdd

st.set_page_config(page_title="AI Test Case Generator", layout="centered")
st.title("🧠 AI-Powered BDD Test Case Generator")

mode = st.radio("Select Input Mode", ["Paste Text", "Upload PDF"])

user_input = ""

if mode == "Paste Text":
    user_input = st.text_area("Paste your requirement or user story:")

elif mode == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file:
        user_input = extract_text_from_pdf(uploaded_file)
        st.success("PDF uploaded and text extracted!")

if st.button("Generate BDD Test Cases"):
    if user_input.strip():
        with st.spinner("Generating test cases..."):
            result = generate_bdd(user_input)
            st.markdown("### ✅ Generated BDD Test Cases:")
            st.code(result, language="gherkin")
    else:
        st.warning("Please enter or upload some content first.")