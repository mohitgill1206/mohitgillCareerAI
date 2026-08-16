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
    placeholder="""Name: Mohit
Branch: CSE AIML
Year: 2nd
Interested in AI/ML
Knows Python Basics"""
)

if st.button("Generate Career Report"):
    if not user.strip():
        st.warning("Please enter your profile.")
    else:
        with st.spinner("CareerPilot AI is thinking..."):

            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=st.secrets["GOOGLE_API_KEY"]
            )

            prompt = f"""
You are an AI career mentor.

Analyze this student's profile:

{user}

Create a personalized career report containing:

1. Current skill assessment
2. Recommended career paths
3. Skills to learn
4. Recommended projects
5. A 6-month learning roadmap
6. Internship preparation advice
"""

            response = llm.invoke(prompt)
            report = response.content

        st.success("Report Generated Successfully!")

        st.markdown(report)

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="career_report.txt",
            mime="text/plain"
        )
