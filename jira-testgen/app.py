import streamlit as st
from utils import generate_test_cases, save_to_markdown
from datetime import datetime
import os

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Test Case Generator",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# Header and Description
# ---------------------------------------------------
st.title("🧪 AI Test Case Generator from Jira Tickets")
st.markdown("""
This tool leverages **OpenAI GPT** to read Jira ticket descriptions and produce **QA-ready test cases** in Gherkin or Markdown format.

---

### 📝 Instructions:
1. Paste your Jira ticket description below.
2. Choose your desired **output format**.
3. Click **"Generate Test Cases"**.
4. View, copy, or download the result for QA documentation.
""")

# ---------------------------------------------------
# Sidebar Options
# ---------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    output_format = st.selectbox(
        "Choose Output Format",
        options=["Gherkin", "Markdown", "Plain Text"],
        index=0
    )

    filename_prefix = st.text_input("Optional Filename Prefix", value="test_cases")

    st.markdown("---")
    st.info("Powered by OpenAI's GPT API")

# ---------------------------------------------------
# Main Input Area
# ---------------------------------------------------
description = st.text_area(
    "📥 Jira Ticket Description",
    height=300,
    placeholder="Example: As a user, I want to reset my password via email verification...",
)

# ---------------------------------------------------
# Generate Button
# ---------------------------------------------------
if st.button("🚀 Generate Test Cases"):

    if not description.strip():
        st.warning("⚠️ Please enter a Jira ticket description before proceeding.")
        st.stop()

    with st.spinner("🤖 Thinking... Generating QA test cases..."):
        # Call the OpenAI function
        result = generate_test_cases(description)

        if result.startswith("❌ Error:"):
            st.error(result)
            st.stop()

        # Timestamped file for uniqueness
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file_name = f"{filename_prefix}_{timestamp}.md"

        # Save markdown version
        save_to_markdown(result, output_file_name)

    # ---------------------------------------------------
    # Display Output
    # ---------------------------------------------------
    st.success("✅ Test cases generated successfully!")
    st.markdown("### 📋 Output Test Cases:")

    if output_format == "Gherkin":
        st.code(result, language="gherkin")
    elif output_format == "Plain Text":
        st.text(result)
    else:
        st.markdown(result)

    # ---------------------------------------------------
    # Download File
    # ---------------------------------------------------
    with open(f"output/{output_file_name}", "r", encoding="utf-8") as f:
        st.download_button(
            label="📥 Download Markdown File",
            data=f.read(),
            file_name=output_file_name,
            mime="text/markdown"
        )

    # ---------------------------------------------------
    # File Info
    # ---------------------------------------------------
    st.markdown(f"🗂️ Saved locally at: `output/{output_file_name}`")

    # Option to clear
    if st.button("🔄 Start New"):
        st.experimental_rerun()

# ---------------------------------------------------
# Footer / Credits
# ---------------------------------------------------
st.markdown("---")
st.markdown("""
👨‍💻 Developed by [Your Name or Team]  

Have feedback? Contact us!
""")
# 🔗 Powered by [OpenAI](https://platform.openai.com) · Built with [Streamlit](https://streamlit.io)
