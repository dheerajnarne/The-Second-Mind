from huggingface_hub import login


from .memory_agent import MemoryAgent
from .generation_agent import GenerationAgent
from .ranking_agent import RankingAgent
from .evolution_agent import EvolutionAgent
from .proximity_agent import ProximityAgent
from .metareview_agent import MetaReviewAgent
from .reflection_agent import ReflectionAgent
class SupervisorAgent:
    def __init__(self):
        """Initialize the supervisor agent"""
        self.memory_agent = MemoryAgent()
        self.generation_agent = GenerationAgent()
        self.ranking_agent = RankingAgent()
        self.evolution_agent = EvolutionAgent()
        self.reflection_agent = ReflectionAgent()
        self.proximity_agent = ProximityAgent(self.memory_agent)
        self.meta_review_agent = MetaReviewAgent()
        self.reflections = []  # Stores reflections
        self.process_log = []  # Logs the process steps

    def fetch_web_data(self, query):
        """Fetch web data based on the query"""
        return fetch_web_data(query)

    def interact(self, query):
        """Interact with the environment by generating ideas, reflecting, and planning"""
        # Fetch web data
        web_data = self.fetch_web_data(query)
        self.process_log.append(f"Fetched web data for query: {query}")
        
        # Generate initial idea
        idea = self.generation_agent.generate_idea(query, web_data)
        self.process_log.append(f"Generated idea: {idea}")
        
        # Reflect on the idea
        reflection = self.reflection_agent.reflect(idea, web_data)
        self.process_log.append(f"Reflection: {reflection}")
        
        # Rank the idea
        ranking_feedback = self.ranking_agent.rank(idea, web_data)
        self.process_log.append(f"Ranking feedback: {ranking_feedback}")
        
        # Evolve the idea based on ranking feedback
        refined_idea = self.evolution_agent.evolve(idea, ranking_feedback, web_data)
        self.process_log.append(f"Evolved idea: {refined_idea}")
        
        # Link to past interactions
        proximity_feedback = self.proximity_agent.link_to_past(query, refined_idea)
        self.process_log.append(f"Proximity feedback: {proximity_feedback}")
        
        # Add to memory
        self.memory_agent.add_to_memory(query, refined_idea)
        self.process_log.append(f"Added to memory: {refined_idea}")
        
        # Meta-review the process
        meta_review = self.meta_review_agent.review_process("\n".join(self.process_log))
        self.process_log.append(f"Meta-review: {meta_review}")
        
        return {
            "idea": refined_idea,
            "ranking_feedback": ranking_feedback,
            "reflection": reflection,
            "proximity_feedback": proximity_feedback,
            "meta_review": meta_review,
            "web_data": web_data
        }