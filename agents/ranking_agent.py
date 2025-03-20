from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class RankingAgent:
    def __init__(self, model_name="EleutherAI/pythia-2.8b"):
        """Initialize the ranking agent with Pythia 2.8B"""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name)
    def rank(self, idea):
        """Rank the idea based on predefined criteria"""
        prompt = f"""Evaluate the following research idea based on the following criteria:
        1. Feasibility (1-10): How feasible is the idea to implement?
        2. Innovation (1-10): How innovative is the idea?
        3. Impact (1-10): What is the potential impact of the idea?
        
        Idea: {idea}
        
        Provide a score for each criterion and a brief explanation for the scores."""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")  # Move inputs to GPU
        outputs = self.model.generate(**inputs, max_new_tokens=200)
        ranking = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return ranking