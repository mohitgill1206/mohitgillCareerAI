from llm.gemini_client import ask_llm
from prompts.resume_prompt import RESUME_PROMPT


def resume_agent(user_input):
    """
    Suggests projects and resume improvements
    based on the student's profile.
    """

    prompt = f"""
{RESUME_PROMPT}

Student Profile:
{user_input}
"""

    response = ask_llm(prompt)

    return response