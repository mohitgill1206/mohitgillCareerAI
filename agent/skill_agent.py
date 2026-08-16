from llm.gemini_client import ask_llm
from prompts.skill_prompt import SKILL_PROMPT


def skill_agent(user_input):
    """
    Analyzes the user's skills and recommends what to learn.
    """

    prompt = f"""
{SKILL_PROMPT}

User Profile:
{user_input}
"""

    response = ask_llm(prompt)

    return response