from AGENTS import continuity_agent, motion_agent, review_agent, storyboard_agent, visual_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "storyboard": storyboard_agent.run(case),
        "visual": visual_agent.run(case),
        "motion": motion_agent.run(case),
        "continuity": continuity_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
