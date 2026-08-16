import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerPilot AI")
st.subheader("Your AI Career Mentor")

st.write("Fill your profile and get a personalized AI career report.")

user = st.text_area(
    "Enter Your Profile",
    height=250,
    placeholder="""
Name: Mohit
Branch: CSE AIML
Year: 2nd
Interested in AI/ML
Knows Python Basics
"""
)

if st.button("Generate Career Report"):
    if user.strip() == "":
        st.warning("Please enter your profile.")
    else:
        with st.spinner("CareerPilot AI is thinking..."):
            report = run_career_workflow(user)

        st.success("Report Generated Successfully!")

        st.markdown(report)

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="career_report.txt",
            mime="text/plain"
        )
