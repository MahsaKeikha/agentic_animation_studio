from AGENTS import storyboard_agent,visual_agent,motion_agent,continuity_agent,review_agent
def run(c): return {'storyboard':storyboard_agent.run(c),'visual':visual_agent.run(c),'motion':motion_agent.run(c),'continuity':continuity_agent.run(c),'review':review_agent.run(c)}
