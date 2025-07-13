import streamlit as st
from utils import run_flake8, run_black, run_radon

st.set_page_config(page_title="AI Code Reviewer", layout="wide")
st.title("AI Code Reviewer")
st.markdown("""
#### Analyze Python Code using Flake8, Black, and Radon
Paste your code or upload a file to see linting, formatting, and complexity analysis.
""")

code_input = st.text_area("Paste your Python code here:", height=300)

uploaded_file = st.file_uploader("Or upload a Python (.py) file", type=["py"])
if uploaded_file:
    code_input = uploaded_file.read().decode("utf-8")

if code_input:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Formatted Code (black)")
        formatted_code = run_black(code_input)
        st.code(formatted_code, language="python")
        st.download_button("Download formatted code", data=formatted_code, file_name="formatted.py", mime="text/x-python")

    with col2:
        st.subheader("Linting (flake8)")
        lint_result = run_flake8(code_input)
        st.code(lint_result, language="text")

    st.subheader("Complexity Report (radon)")
    complexity = run_radon(code_input)
    st.code(complexity, language="text")