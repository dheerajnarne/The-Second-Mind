class ProximityAgent:
    def __init__(self, memory_agent):
        """Initialize the proximity agent with a memory agent"""
        self.memory_agent = memory_agent

    def link_to_past(self, query, idea):
        """Link the idea to past interactions"""
        similar_ideas = self.memory_agent.retrieve_similar_ideas(query)
        if similar_ideas:
            past_context = "\n".join([f"- {q}: {i}" for q, i in similar_ideas])
            return f"""The idea "{idea}" is related to the following past interactions:
            {past_context}"""
        else:
            return "No similar past interactions found."