from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class GenerationAgent:
    def __init__(self, model_name="EleutherAI/pythia-2.8b"):
        """Initialize the generation agent with Pythia 2.8B"""
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name)  # Load model on GPU

    def generate_idea(self, query):
        """Use Pythia 2.8B to generate a novel research hypothesis"""
        prompt = f"""Generate one innovative and feasible research idea related to {query}. 
        The idea should:
        1. Address a pressing urban challenge.
        2. Leverage renewable energy technologies.
        3. Be feasible to implement in the next 5 years.
        4. Have a clear potential impact on urban sustainability.
        
        Provide a brief explanation of how the idea works and its potential benefits."""
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")  # Move inputs to GPU
        outputs = self.model.generate(**inputs, max_new_tokens=200)
        new_idea = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return new_idea