import streamlit as st
from app.pdf_utils import extract_text_from_pdf
from app.generator import generate_bdd
from app.test_generator import convert_gherkin_to_pytest, save_pytest_file
import base64

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
    if not user_input.strip():
        st.warning("Please provide requirement text first.")
    else:
        with st.spinner("Contacting GPT‑4 and building tests …"):
            bdd = generate_bdd(user_input)
            st.subheader("✅ Generated BDD Scenarios")
            st.code(bdd, language="gherkin")

            test_code = convert_gherkin_to_pytest(bdd)
            file_path = save_pytest_file(test_code)

            st.subheader("🧪 Playwright + Pytest Stub")
            st.code(test_code, language="python")

            st.download_button(
                label="📥 Download .py file",
                data=test_code,
                file_name="test_generated.py",
                mime="text/x-python",
            )
            st.success(f"Saved server‑side copy at {file_path}")

