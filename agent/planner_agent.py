from llm.gemini_client import ask_llm
from prompts.planner_prompt import PLANNER_PROMPT


def planner_agent(user_input):
    """
    Generates a career roadmap based on the user's profile.
    """

    prompt = f"""
{PLANNER_PROMPT}

User Details:
{user_input}
"""

    response = ask_llm(prompt)

    return response