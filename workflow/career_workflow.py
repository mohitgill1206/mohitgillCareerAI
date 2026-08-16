from agent.planner_agent import planner_agent
from agent.skill_agent import skill_agent
from agent.resume_agent import resume_agent
from agent.roadmap_agent import roadmap_agent


def run_career_workflow(user_input):

    print("Running Planner Agent...")
    planner_output = planner_agent(user_input)

    print("Running Skill Agent...")
    skill_output = skill_agent(user_input)

    print("Running Resume Agent...")
    resume_output = resume_agent(user_input)

    print("Running Roadmap Agent...")
    roadmap_output = roadmap_agent(user_input)

    final_report = f"""
==================================================
          CAREERPILOT AI FINAL REPORT
==================================================

📌 PLANNER ANALYSIS
{planner_output}


==================================================

🛠 SKILL ANALYSIS
{skill_output}


==================================================

📄 RESUME ANALYSIS
{resume_output}


==================================================

🗺 AI/ML ROADMAP
{roadmap_output}

==================================================
"""

    return final_report