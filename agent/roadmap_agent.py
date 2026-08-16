from llm.gemini_client import ask_llm
from prompts.roadmap_prompt import ROADMAP_PROMPT


def roadmap_agent(user_input):
    """
    Generates a personalized AI/ML roadmap for the student.
    """

    prompt = f"""
{ROADMAP_PROMPT}

Student Profile:
{user_input}

Create a detailed learning roadmap with:
1. Beginner Phase
2. Intermediate Phase
3. Advanced Phase
4. Projects to build
5. Recommended Resources
6. Timeline
7. Final Career Goal
"""

    return ask_llm(prompt)